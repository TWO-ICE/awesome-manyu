#!/usr/bin/env python3
"""
awesome-manyu 每周自动发现 + 入库脚本

渠道：① 姐妹 awesome 清单 diff  ② GitHub 搜索近 60 天新仓库
达标（≥100星 / 年内活跃 / 非 fork / 非 archived）的项目：
  - 默认：输出 markdown 报告（供记录 / 人工查看）
  - --apply：自动归类写入 data/projects.json，去重，追加 CHANGELOG.md

每周由 GitHub Actions 自动执行，达标新项目直接进清单，无需人工挑。
用法: python3 discover.py [--apply] [--token XXX]
"""
import argparse
import json
import os
import re
import subprocess
import sys
import time
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = ROOT / "data" / "projects.json"
CHANGELOG = ROOT / "CHANGELOG.md"

# 渠道 3：监控的姐妹清单
WATCHLISTS = [
    "ken-fs/awesome-ai-micro-drama",
    "UnderleveledBuilder/awesome-short-drama-skills",
    "PAMPAS-Lab/awesome-ai-short-drama",
    "zhaotoday/awesome-ai-video",
]

# 渠道 2：GitHub 搜索关键词（近 60 天创建）
SEARCH_QUERIES = [
    "漫剧", "AI 短剧", "short drama AI", "comic drama", "motion comic",
    "novel to video", "story to video", "seedance skill", "manju",
]

# 明确排除：通用技能库 / 通用 awesome / 明显无关或废弃项目
EXCLUDE_PATTERNS = [
    r"^anthropics/", r"^vercel-labs/", r"^VoltAgent/",
    r"skills?$", r"awesome$", r"\.github$",
    r"virtual.card|usdt|crypto|web3",          # 蹭概念的可疑项目
    r"player$|聚合播放器|多源短剧",            # 聚合播放器，非创作工具
]

# 自动归类关键词：越具体越靠前；命中多个取第一个。
# 宁可漏收也不错收——归不进任何一类的候选只在报告里留档，不入库。
CAT_RULES = [
    ("prompts", ["prompt", "提示词", "提示语"]),
    ("directing", ["storyboard", "分镜", "镜头", "运镜", "director", "导演", "shot list"]),
    ("writing", ["novel", "小说", "网文", "编剧", "screenplay", "剧本", "写作", "writer"]),
    ("skills", ["skill", "技能包", "claude code", "agent skill"]),
    ("translate", ["mangatranslator", "manga", "漫画", "translat", "翻译", "出海", "字幕组", "ocr"]),
    ("audio", ["tts", "voice", "配音", "口型", "lip.sync", "whisper", "speech", "音色",
               "音频", "语音", "音乐", "music", "sovits", "audiocraft", "rhubarb"]),
    ("img", ["image", "生图", "文生图", "character consistency", "角色一致", "flux",
             "ip-adapter", "portrait", "photo", "照片", "画像", "diffusion", "photoMaker"]),
    ("compose", ["ffmpeg", "剪辑", "合成", "video editor", "字幕烧录", "clipper", "caption"]),
    ("video", ["t2v", "i2v", "文生视频", "视频生成", "wan2", "hunyuanvideo", "cogvideo",
               "seedance", "ltx-video", "kling", "veo", "可灵", "即梦", "动画", "anime",
               "video generation", "video model", "liveportrait", "image to video"]),
    ("allinone", ["all-in-one", "all in one", "全流程", "工作台", "production platform",
                  "studio", "一站式", "短剧", "drama", "漫剧", "pipeline", "一条龙"]),
]


def gh(url: str, token: str | None, raw: bool = False):
    headers = {"Accept": "application/vnd.github.raw" if raw else "application/vnd.github+json",
               "User-Agent": "awesome-manyu-discover"}
    if token:
        headers["Authorization"] = "token " + token
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as r:
        b = r.read()
        return b.decode("utf-8", "ignore") if raw else json.loads(b)


def load_data() -> dict:
    return json.loads(DATA_FILE.read_text(encoding="utf-8"))


def our_repos(data: dict) -> set:
    s = set()
    for cat in data["meta"]["categories"]:
        for item in data.get(cat, []):
            s.add(item["repo"].lower())
    return s


def parse_readme_repos(readme: str) -> set:
    found = set()
    for m in re.findall(r"github\.com/([\w.-]+/[\w.-]+)", readme):
        m = m[:-4] if m.endswith(".git") else m
        if any(re.search(p, m, re.I) for p in EXCLUDE_PATTERNS):
            continue
        found.add(m.lower())
    return found


def age_days(s: str) -> int:
    if len(s) == 10:
        s = s + "T00:00:00+00:00"
    elif s.endswith("Z"):
        s = s[:-1] + "+00:00"
    return (datetime.now(timezone.utc) - datetime.fromisoformat(s)).days


def repo_info(repo: str, token) -> dict | None:
    try:
        d = gh("https://api.github.com/repos/" + repo, token)
        desc = (d.get("description") or "")
        # 废弃/迁移声明的项目不收（描述里带 DEPRECATED / 已废弃 / moved to 等）
        if re.search(r"\[?deprecated\]?|已废弃|不再维护|no longer maintained|moved to", desc, re.I):
            return None
        return {
            "repo": d["full_name"], "stars": d["stargazers_count"],
            "license": (d.get("license") or {}).get("spdx_id"),
            "pushed": d["pushed_at"][:10], "age_d": age_days(d["pushed_at"]),
            "fork": d["fork"], "archived": d["archived"],
            "desc": (d.get("description") or "")[:120],
            "url": d["html_url"], "created": d["created_at"][:10],
        }
    except Exception:
        return None


def collect_candidates(token, ours: set) -> tuple[list, list]:
    cand = set()
    for wl in WATCHLISTS:
        try:
            readme = gh(f"https://api.github.com/repos/{wl}/readme", token, raw=True)
            got = parse_readme_repos(readme)
            cand |= got
            print(f"[watchlist] {wl}: {len(got)} 项，累计 {len(cand)}", file=sys.stderr)
        except Exception as e:
            print(f"[watchlist] {wl} 拉取失败: {e}", file=sys.stderr)
        time.sleep(1)

    since = (datetime.now(timezone.utc) - timedelta(days=60)).strftime("%Y-%m-%d")
    for q in SEARCH_QUERIES:
        try:
            qs = urllib.parse.urlencode({"q": f"{q} created:>{since}", "sort": "stars",
                                         "order": "desc", "per_page": 15})
            d = gh("https://api.github.com/search/repositories?" + qs, token)
            for it in d.get("items", []):
                fn = it["full_name"]
                if not any(re.search(p, fn, re.I) for p in EXCLUDE_PATTERNS):
                    cand.add(fn.lower())
            print(f"[search] {q}: 累计 {len(cand)}", file=sys.stderr)
        except Exception as e:
            print(f"[search] {q} 失败: {e}", file=sys.stderr)
        time.sleep(6)  # search API 限速严格

    cand -= ours
    print(f"去重后候选: {len(cand)}", file=sys.stderr)

    strong, watch = [], []
    for repo in sorted(cand):
        info = repo_info(repo, token)
        time.sleep(0.15)
        if not info or info["fork"] or info["archived"]:
            continue
        if info["stars"] >= 100 and info["age_d"] <= 365:
            strong.append(info)
        elif 30 <= info["stars"] < 100 and info["age_d"] <= 90:
            watch.append(info)
    strong.sort(key=lambda x: -x["stars"])
    watch.sort(key=lambda x: -x["stars"])
    return strong, watch


def classify(info: dict) -> str | None:
    text = (info["repo"] + " " + info["desc"]).lower()
    for cat, kws in CAT_RULES:
        if any(k in text for k in kws):
            return cat
    return None


def clean_desc(info: dict) -> str:
    d = re.sub(r"\s+", " ", info["desc"]).strip().rstrip(".")
    if not d:
        d = info["repo"].split("/")[-1].replace("-", " ")
    if len(d) > 64:
        d = d[:62] + "…"
    return d


def apply_changes(strong: list, data: dict) -> tuple[list, list]:
    """达标候选自动归类入库；归类不上的只在报告留档。返回 (added, unclassified)"""
    existing = our_repos(data)
    added, unclassified = [], []
    for info in strong:
        if info["repo"].lower() in existing:
            continue
        cat = classify(info)
        if not cat:
            unclassified.append(info)
            continue
        data[cat].append({"repo": info["repo"], "desc": clean_desc(info)})
        existing.add(info["repo"].lower())
        added.append((cat, info))
    if added:
        DATA_FILE.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        today = datetime.now(timezone(timedelta(hours=8))).strftime("%Y-%m-%d")
        lines = CHANGELOG.read_text(encoding="utf-8").splitlines() if CHANGELOG.exists() else ["# 自动收录记录", ""]
        lines += [f"## {today} · 自动收录 {len(added)} 个项目", ""]
        for cat, info in added:
            lines.append(f"- `{cat}` [{info['repo']}]({info['url']}) ⭐{info['stars']} — {clean_desc(info)}")
        lines.append("")
        CHANGELOG.write_text("\n".join(lines), encoding="utf-8")
    return added, unclassified


def render_report(strong, watch, added, unclassified) -> str:
    today = datetime.now(timezone(timedelta(hours=8))).strftime("%Y-%m-%d")
    lines = [
        f"## 🛰️ 本周自动收录 · {today}",
        "",
        f"扫描 {len(WATCHLISTS)} 份姐妹清单 + {len(SEARCH_QUERIES)} 组搜索词，"
        f"达标 **{len(strong)}** 个（≥100星/年内活跃），"
        f"**本周自动入库 {len(added)} 个**，已直接更新 `data/projects.json` 与 README。",
        "",
    ]
    if added:
        lines += ["### ✅ 本周新增", "", "| 分类 | 项目 | ⭐ | 说明 |", "|---|---|---|---|"]
        for cat, r in added:
            lines.append(f"| {cat} | [{r['repo']}]({r['url']}) | {r['stars']} | {clean_desc(r)} |")
        lines.append("")
    if unclassified:
        lines += [f"### 🔍 达标但未归类（{len(unclassified)}，仅留档未入库）", "",
                  "| 项目 | ⭐ | 说明 |", "|---|---|---|"]
        for r in unclassified[:30]:
            lines.append(f"| [{r['repo']}]({r['url']}) | {r['stars']} | {clean_desc(r)} |")
        lines.append("")
    if watch:
        lines += [f"### 👀 观察名单（{len(watch)}，未达入库门槛）", "",
                  "| 项目 | ⭐ | 最近活跃 |", "|---|---|---|"]
        for r in watch[:20]:
            lines.append(f"| [{r['repo']}]({r['url']}) | {r['stars']} | {r['pushed']} |")
        lines.append("")
    lines += ["---", "达标项目每周自动入库，无需人工处理。详见 [CHANGELOG.md](./CHANGELOG.md)。"]
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--token", default=os.environ.get("GH_TOKEN", ""))
    ap.add_argument("--apply", action="store_true", help="达标项目自动入库（默认只生成报告）")
    args = ap.parse_args()
    token = args.token or None

    data = load_data()
    strong, watch = collect_candidates(token, our_repos(data))
    added, unclassified = ([], strong) if not args.apply else apply_changes(strong, data)
    print(render_report(strong, watch, added, unclassified))


if __name__ == "__main__":
    main()
