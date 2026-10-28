#!/usr/bin/env python3
"""
awesome-manyu 每周发现脚本（渠道 2 + 渠道 3）
1. 拉取监控清单（姐妹 awesome list）的 README，解析出新收录的仓库（diff 我们的 data/projects.json）
2. GitHub Search 搜近 30 天新建/热门的漫剧相关仓库
3. 对候选拉真实数据，按收录标准分层，生成中文报告 markdown
4. GitHub Actions 里用 gh CLI 把报告发到 Issue（含 label: discovery）

用法: python3 discover.py [--token XXX]
输出: 打印报告 markdown 到 stdout；--post ISSUE_NUMBER 时改为评论到指定 Issue
"""
import argparse
import json
import os
import re
import sys
import time
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = ROOT / "data" / "projects.json"

# 渠道 3：监控的姐妹清单（README 里出现的仓库都算候选来源）
WATCHLISTS = [
    "ken-fs/awesome-ai-micro-drama",
    "UnderleveledBuilder/awesome-short-drama-skills",
    "PAMPAS-Lab/awesome-ai-short-drama",
    "zhaotoday/awesome-ai-video",
]

# 渠道 2：GitHub 搜索关键词（近 60 天创建，按星排序）
SEARCH_QUERIES = [
    "漫剧", "AI 短剧", "short drama AI", "comic drama", "motion comic",
    "novel to video", "story to video", "seedance skill", "manju",
]

# 明确排除：通用技能库/通用 awesome（不是漫剧垂直内容）
EXCLUDE_PATTERNS = [
    r"^anthropics/", r"^vercel-labs/", r"^VoltAgent/",
    r"skills?$", r"awesome$", r"\.github$",
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


def our_repos() -> set:
    d = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    s = set()
    for cat in d["meta"]["categories"]:
        for item in d.get(cat, []):
            s.add(item["repo"].lower())
    return s


def parse_readme_repos(readme: str) -> set:
    found = set()
    for m in re.findall(r"github\.com/([\w.-]+/[\w.-]+)", readme):
        m = m.rstrip(".git") if m.endswith(".git") else m
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
        return {
            "repo": d["full_name"], "stars": d["stargazers_count"],
            "license": (d.get("license") or {}).get("spdx_id"),
            "pushed": d["pushed_at"][:10], "age_d": age_days(d["pushed_at"]),
            "fork": d["fork"], "archived": d["archived"],
            "desc": (d.get("description") or "")[:70],
            "url": d["html_url"],
            "created": d["created_at"][:10],
        }
    except Exception:
        return None


def collect_candidates(token) -> tuple[list, list]:
    ours = our_repos()
    cand = set()

    # 渠道 3：姐妹清单 diff
    for wl in WATCHLISTS:
        try:
            readme = gh(f"https://api.github.com/repos/{wl}/readme", token, raw=True)
            cand |= parse_readme_repos(readme)
            print(f"[watchlist] {wl}: +{len(parse_readme_repos(readme))} 累计 {len(cand)}", file=sys.stderr)
        except Exception as e:
            print(f"[watchlist] {wl} 拉取失败: {e}", file=sys.stderr)
        time.sleep(1)

    # 渠道 2：GitHub 搜索
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

    cand = {c for c in cand if c not in ours}
    print(f"候选去重后: {len(cand)}", file=sys.stderr)

    strong, watch = [], []
    for repo in sorted(cand):
        info = repo_info(repo, token)
        time.sleep(0.2)
        if not info or info["fork"] or info["archived"]:
            continue
        if info["stars"] >= 100 and info["age_d"] <= 365:
            strong.append(info)
        elif 30 <= info["stars"] < 100 and info["age_d"] <= 90:
            watch.append(info)
    strong.sort(key=lambda x: -x["stars"])
    watch.sort(key=lambda x: -x["stars"])
    return strong, watch


def render_report(strong, watch) -> str:
    today = datetime.now(timezone(timedelta(hours=8))).strftime("%Y-%m-%d")
    lines = [
        f"## 🛰️ 每周发现报告 · {today}",
        "",
        f"本周扫描 {len(WATCHLISTS)} 份姐妹清单 + {len(SEARCH_QUERIES)} 组搜索词，",
        f"筛出 **{len(strong)} 个硬达标**（≥100星/年内活跃）和 **{len(watch)} 个潜力项目**（30-100星/90天活跃）。",
        "",
    ]
    if strong:
        lines += ["### ✅ 达标候选（建议人工核验后收录）", "",
                  "| 项目 | ⭐ | License | 最近活跃 | 说明 |", "|---|---|---|---|---|"]
        for r in strong:
            lines.append(f"| [{r['repo']}]({r['url']}) | {r['stars']} | {r['license'] or '未声明'} | {r['pushed']} | {r['desc']} |")
        lines.append("")
    if watch:
        lines += ["### 👀 观察名单（未达标，留档观察）", "",
                  "| 项目 | ⭐ | 最近活跃 | 说明 |", "|---|---|---|---|"]
        for r in watch:
            lines.append(f"| [{r['repo']}]({r['url']}) | {r['stars']} | {r['pushed']} | {r['desc']} |")
        lines.append("")
    lines += [
        "---",
        "**处理流程**：从 ✅ 达标候选挑合适的，按 CONTRIBUTING 加进 `data/projects.json` 对应分类，下周一自动刷进 README。",
        "观察名单的项目星数/活跃度下周会重扫，达标会重新出现在候选里。",
    ]
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--token", default=os.environ.get("GH_TOKEN", ""))
    args = ap.parse_args()
    token = args.token or None

    strong, watch = collect_candidates(token)
    report = render_report(strong, watch)
    print(report)


if __name__ == "__main__":
    main()
