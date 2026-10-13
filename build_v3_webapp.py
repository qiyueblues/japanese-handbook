# -*- coding: utf-8 -*-
"""
Builder for V3 Japanese Mobile Web App.
Features:
- Fixed Light & Dark theme color contrast bugs (table text, headers, bottom nav)
- Explicit "What is this form for?" annotations for verb conjugations
- Horizontal Swipeable Page Carousel (4 sub-pages per module)
- Removed 'view all' mode, clean modular layout
- Touch swipe + top pills + bottom step buttons
- 100% full content preserved, zero audio
"""

import os
import re

modules_config = [
    {
        "id": "verb",
        "file": "01_日语核心语法精讲_动词篇.html",
        "title": "动词篇",
        "icon": "🏃",
        "primary": "#1e40af",
        "primary_light": "#eff6ff",
        "accent": "#2563eb",
        "th_bg": "#1e3a8a",
        "pills": ["1. 分类判定", "2. 六大活用", "3. 音便口诀", "4. 派生句型"]
    },
    {
        "id": "adj",
        "file": "02_日语核心语法精讲_形容词篇.html",
        "title": "形容词",
        "icon": "✨",
        "primary": "#065f46",
        "primary_light": "#ecfdf5",
        "accent": "#059669",
        "th_bg": "#064e3b",
        "pills": ["1. 两派假词", "2. い形变形", "3. な形与PK", "4. 派生变音"]
    },
    {
        "id": "particle",
        "file": "03_日语核心语法精讲_介词助词篇.html",
        "title": "助词篇",
        "icon": "⚓",
        "primary": "#9a3412",
        "primary_light": "#fff7ed",
        "accent": "#ea580c",
        "th_bg": "#7c2d12",
        "pills": ["1. はvsが", "2. 核心格助词", "3. 并列与副助", "4. 终助词人设"]
    },
    {
        "id": "sent",
        "file": "04_日语核心语法精讲_句子造句篇.html",
        "title": "造句篇",
        "icon": "🧱",
        "primary": "#581c87",
        "primary_light": "#faf5ff",
        "accent": "#7c3aed",
        "th_bg": "#4c1d95",
        "pills": ["1. 积木公式", "2. 复句齿轮", "3. 授受动词", "4. 常用句型"]
    },
    {
        "id": "spoken",
        "file": "05_日语核心语法精讲_常用口语篇.html",
        "title": "口语篇",
        "icon": "🗣️",
        "primary": "#9f1239",
        "primary_light": "#fff1f2",
        "accent": "#e11d48",
        "th_bg": "#881337",
        "pills": ["1. 相槌万能词", "2. 7大缩约音", "3. 情境短句", "4. 现实防踩雷"]
    }
]

# Process and load modules
modules_data = []

for mod in modules_config:
    with open(mod["file"], "r", encoding="utf-8") as f:
        raw_html = f.read()

    # Extract body content
    match = re.search(r"<body[^>]*>(.*?)</body>", raw_html, re.DOTALL | re.IGNORECASE)
    if not match:
        raise ValueError(f"Body not found in {mod['file']}")
    body = match.group(1).strip()

    # Split into 4 pages
    pages = re.split(r"<div class=[\x27\x22]page-break[\x27\x22]></div>", body)
    if len(pages) != 4:
        raise ValueError(f"Expected 4 pages in {mod['file']}, found {len(pages)}")

    cleaned_pages = []
    for p_idx, page in enumerate(pages):
        p_content = page.strip()

        # Wrap all custom-tables in horizontal scroll containers
        p_content = re.sub(
            r"(<table\s+class=[\x27\x22]custom-table[\x27\x22][^>]*>.*?</table>)",
            r'<div class="table-container"><div class="table-scroll-hint">↔️ 可横向滑动查看完整列</div>\1</div>',
            p_content,
            flags=re.DOTALL
        )

        # Enhance Verb Module Page 2 (Conjugation table)
        if mod["id"] == "verb" and p_idx == 1:
            # 1. Add intuitive explanation callout above table
            callout = """
<div class="card form-explainer-card">
  <div class="form-explainer-title">
    🎯【动词六大形态到底是干嘛的？—— 一分钟大白话破译】
  </div>
  <div class="form-explainer-body">
    初学最容易被“未然、连用、终止”这些晦涩称呼搞懵。其实记住它们的人话真正用途即可：<br>
    • <strong>未然形</strong>：事情还没发生呢 ➔ 变【否定·不干】(ない)、【被动·挨打】(れる)、【使役·让别人干】(せる)<br>
    • <strong>连用形</strong>：连接后面的零件 ➔ 变【礼貌·敬体】(ます)、【想做·愿望】(たい)、或连句中顿<br>
    • <strong>终止形/连体形</strong>：原原本本的原形 ➔ 句尾【直接结句】或直接挂在名词前【充当定语】(如: 食べる人)<br>
    • <strong>假定形</strong>：假设条件 ➔ 接「ば」表示【如果……就……】(如: やればできる 只要去干就能成)<br>
    • <strong>命令形</strong>：长官命令手下 ➔ 强硬命令【快去！】(如: 逃げろ 快逃！ 行け 冲！)<br>
    • <strong>意志形</strong>：表达决心与邀请 ➔ 【我要…… / 咱们一起……吧】(如: 帰ろう 咱们回吧！ 行こうぜ 出发！)
  </div>
</div>
"""
            p_content = callout + p_content

            # 2. Enrich the first column of the 6 rows in the conjugation table
            p_content = p_content.replace(
                "<td><strong>未然形</strong></td>",
                """<td>
                  <div class="form-tag-badge" style="background:#fee2e2; color:#b91c1c;">未然形</div>
                  <div class="form-purpose-text" style="color:#b91c1c;">【表否定 / 被动】</div>
                  <div class="form-detail-desc">事情未发生，用来接「ない」(不……)或接「れる」(被动/可能)</div>
                </td>"""
            )
            p_content = p_content.replace(
                "<td><strong>连用形</strong></td>",
                """<td>
                  <div class="form-tag-badge" style="background:#dbeafe; color:#1d4ed8;">连用形</div>
                  <div class="form-purpose-text" style="color:#1d4ed8;">【表礼貌 / 想要】</div>
                  <div class="form-detail-desc">连接用言，接「ます」变礼貌敬体，或接「たい」表想做愿望、动名词与中顿</div>
                </td>"""
            )
            p_content = p_content.replace(
                "<td><strong>终止形/连体形</strong></td>",
                """<td>
                  <div class="form-tag-badge" style="background:#dcfce7; color:#15803d;">终止形 / 连体形</div>
                  <div class="form-purpose-text" style="color:#15803d;">【原形结句 / 修饰名词】</div>
                  <div class="form-detail-desc">字典原形，句尾直接打句号，或直接放在名词前面充当修饰语(如: 食べる人)</div>
                </td>"""
            )
            p_content = p_content.replace(
                "<td><strong>假定形</strong></td>",
                """<td>
                  <div class="form-tag-badge" style="background:#fef3c7; color:#b45309;">假定形</div>
                  <div class="form-purpose-text" style="color:#b45309;">【表如果……条件】</div>
                  <div class="form-detail-desc">假设条件，后接「ば」表示“如果……就……”、“只要……就能……”</div>
                </td>"""
            )
            p_content = p_content.replace(
                "<td><strong>命令形</strong></td>",
                """<td>
                  <div class="form-tag-badge" style="background:#ffe4e6; color:#be123c;">命令形</div>
                  <div class="form-purpose-text" style="color:#be123c;">【强硬命令 / 热血喊话】</div>
                  <div class="form-detail-desc">直接结句，命令对方去做，热血动漫高频台词（快逃！冲！去死！）</div>
                </td>"""
            )
            p_content = p_content.replace(
                "<td><strong>意志形</strong></td>",
                """<td>
                  <div class="form-tag-badge" style="background:#f3e8ff; color:#7e22ce;">意志形</div>
                  <div class="form-purpose-text" style="color:#7e22ce;">【自身意愿 / 提议邀请】</div>
                  <div class="form-detail-desc">表达自己的主观决心（“我要……”）或向同伴发出邀请（“咱们……吧！”）</div>
                </td>"""
            )

        cleaned_pages.append(p_content)

    modules_data.append({
        "info": mod,
        "pages": cleaned_pages
    })

print(f"Successfully processed {len(modules_data)} modules with 4 pages each.")
