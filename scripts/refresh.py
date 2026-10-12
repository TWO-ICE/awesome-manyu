#!/usr/bin/env python3
"""
awesome-manyu 数据刷新脚本
读 data/projects.json -> 逐项调 GitHub API -> 重写 README 中 manyu:table 区块。
用法: python3 refresh.py [--token YOUR_TOKEN] [--check]
  --check  只检查不写文件（CI 里用来判断是否有变化时配合 git diff）
"""
import argparse
import json
import os
import sys
import time
import urllib.request
from datetime import datetime, timezone, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = ROOT / "data" / "projects.json"
README = ROOT / "README.md"

STALE_MONTHS = 12  # 超过 N 个月没 push 打 🏢

LICENSE_MAP = {
    "MIT": "✅ MIT",
    "Apache-2.0": "✅ Apache-2.0",
    "BSD-3-Clause": "✅ BSD-3",
    "BSD-2-Clause": "✅ BSD-2",
    "CC0-1.0": "✅ CC0",
    "CC-BY-4.0": "✅ CC-BY-4.0",
    "ISC": "✅ ISC",
    "Unlicense": "✅ Unlicense",
    "GPL-3.0": "📚 GPL-3.0",
    "GPL-2.0": "📚 GPL-2.0",
    "AGPL-3.0": "📚 AGPL-3.0",
    "LGPL-3.0": "📚 LGPL-3.0",
    "MPL-2.0": "📚 MPL-2.0",
    "EPL-2.0": "📚 EPL-2.0",
    "NOASSERTION": None,   # 走 custom_license 或标 ⚠️
    "Other": None,
    "JSON": None,          # GitHub 有时返回奇怪的 spdx
}


def gh_api(url: str, token: str | None) -> dict:
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "awesome-manyu-refresh"}
    if token:
        headers["Authorization"] = "token " + token
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def fetch_repo(repo: str, token: str | None) -> dict:
    d = gh_api(f"https://api.github.com/repos/{repo}", token)
    spdx = (d.get("license") or {}).get("spdx_id")
    return {
        "full_name": d["full_name"],
        "url": d["html_url"],
        "stars": d["stargazers_count"],
        "spdx": spdx,
        "pushed_at": d["pushed_at"],
        "archived": bool(d.get("archived")),
        "missing": False,
    }


def license_badge(item: dict, info: dict) -> tuple[str, str]:
    """返回 (badge, 排序/提示用的原始文本)。badge 会拼进表格 License 列。"""
    override = item.get("license_override")
    if override == "research":
        return "❌ " + item.get("license_note", "仅研究用途"), "research"
    spdx = info["spdx"]
    if item.get("custom_license"):
        name = item["custom_license"]
        # 以 copyleft 协议名开头的按 📚 标，其余自定义一律 ⚠️
        prefix = "📚" if name.upper().startswith(("LGPL", "GPL", "AGPL", "MPL")) else "⚠️"
        return f"{prefix} {name}", "custom"
    badge = LICENSE_MAP.get(spdx)
    if badge:
        return badge, spdx
    if spdx in (None, "NOASSERTION", "Other", "JSON"):
        return "⚠️ 自定义（读原文）", "custom"
    return "⚠️ " + spdx, "custom"


def stale_badge(info: dict) -> str:
    if info["archived"]:
        return " 🏛️已归档"
    try:
        pushed = datetime.fromisoformat(info["pushed_at"].replace("Z", "+00:00"))
        age_days = (datetime.now(timezone.utc) - pushed).days
        if age_days > STALE_MONTHS * 30:
            return " 🏢"
    except Exception:
        pass
    return ""


def render_table(items: list, cat: str, token: str | None) -> str:
    rows = []
    misses = []
    for item in items:
        repo = item["repo"]
        try:
            info = fetch_repo(repo, token)
        except Exception as e:
            print(f"  !! {repo} 拉取失败: {e}", file=sys.stderr)
            misses.append(repo)
            continue
        lic, _ = license_badge(item, info)
        stale = stale_badge(info)
        desc = item["desc"]
        if cat == "video":
            rows.append(
                f"| [{info['full_name'].split('/')[-1]}]({info['url']}) "
                f"| {info['stars']} | {item.get('vram', '—')} | {lic}{stale} | {desc} |"
            )
        else:
            rows.append(
                f"| [{info['full_name'].split('/')[-1]}]({info['url']}) "
                f"| {info['stars']} | {desc} | {lic}{stale} |"
            )
        time.sleep(0.3)
    for m in misses:
        # 拉取失败的项目保留旧行由人工处理，这里只提示
        print(f"  !! 注意: {m} 未更新（API 失败），请人工核查", file=sys.stderr)
    if cat == "video":
        return (
            "| 模型 | ⭐ | 最低显存 | License | 点评 |\n"
            "|---|---|---|---|---|\n" + "\n".join(rows)
        )
    return (
        "| 项目 | ⭐ | 说明 | License |\n"
        "|---|---|---|---|\n" + "\n".join(rows)
    )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--token", default=os.environ.get("GH_TOKEN", ""))
    ap.add_argument("--check", action="store_true", help="只打印统计不写 README")
    args = ap.parse_args()
    token = args.token or None

    data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
    cats = data["meta"]["categories"]

    total = 0
    today = datetime.now(timezone(timedelta(hours=8))).strftime("%Y-%m-%d")
    tables = {}
    for cat in cats:
        items = data.get(cat, [])
        print(f"== {cat} ({len(items)} 项)")
        tables[cat] = render_table(items, cat, token)
        total += len(items)

    print(f"共刷新 {total} 个项目，数据日期 {today}")

    if args.check:
        return 0

    text = README.read_text(encoding="utf-8")
    for cat, table in tables.items():
        start = f"<!-- manyu:table:{cat} -->"
        end = f"<!-- /manyu:table:{cat} -->"
        s = text.find(start)
        e = text.find(end)
        if s == -1 or e == -1:
            print(f"!! README 里找不到 {start} 标记，跳过 {cat}", file=sys.stderr)
            continue
        text = text[: s + len(start)] + "\n" + table + "\n" + text[e:]

    old_meta_s = text.find("<!-- manyu:meta -->")
    old_meta_e = text.find("<!-- /manyu:meta -->")
    if old_meta_s != -1 and old_meta_e != -1:
        meta = f"<!-- manyu:meta -->\n📊 收录 **{total}** 个项目 ｜ 数据更新于 **{today}** ｜ 由 GitHub Actions 每周自动刷新\n"
        text = text[:old_meta_s] + meta + text[old_meta_e:]

    README.write_text(text, encoding="utf-8")
    print("README 已更新")
    return 0


if __name__ == "__main__":
    sys.exit(main())
