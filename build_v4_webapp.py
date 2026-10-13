# -*- coding: utf-8 -*-
"""
Builder V4:
1. Header Architecture Fix: Embed subpage navigation directly into fixed .top-header (eliminating clipped banners and scrolling overlaps).
2. Verb Conjugation Redesign:
   - Provide dual-view toggle: '📱 手机卡片精读 (推荐)' and '📊 完整活用大表'.
   - In Card View: Beautiful mobile cards for each of the 6 forms with purpose tags, rules, examples, and anime lines.
   - In Table View: Fixed column widths (min-width 830px) + nowrap badges, zero squeezing.
3. Clean theme variables for Light and Dark modes.
4. Smooth horizontal swiper with synchronized top pills.
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
        "pills": ["1. はvs将", "2. 核心格助词", "3. 并列与副助", "4. 终助词人设"]
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

# Build Card View HTML for the 6 verb conjugations
verb_cards_html = """
<div id="conjugation-cards-view" class="conjugation-view-block">
  
  <!-- 1. 未然形 -->
  <div class="conj-card" style="border-left: 4px solid #ef4444;">
    <div class="conj-card-header">
      <div class="conj-card-title-group">
        <span class="conj-badge" style="background:#fee2e2; color:#b91c1c;">1. 未然形</span>
        <span class="conj-purpose-badge" style="background:#fff1f2; color:#be123c;">【干嘛的：表否定 / 被动】</span>
      </div>
      <span class="conj-suffix-pill">+ ない / れる</span>
    </div>
    <div class="conj-meaning-row">
      💡 <strong>用途解说：</strong>动作还“未发生”，用来变“不……”(ない)或“被动/可能”(れる/られる)。
    </div>
    <div class="conj-rule-box">
      <strong>📐 变换法则：</strong>一类动词词尾变 <span class="highlight">あ段</span> (kak-u ➔ kak-a) ；二类动词直接丢「る」
    </div>
    <div class="conj-examples-grid">
      <div class="conj-ex-col">
        <div class="conj-ex-type">一类动词 (書く)</div>
        <div class="conj-ex-text">• 書か-ない (不写)<br>• 書か-れる (被写)</div>
      </div>
      <div class="conj-ex-col">
        <div class="conj-ex-type">二类动词 (食べる)</div>
        <div class="conj-ex-text">• 食べ-ない (不吃)<br>• 食べ-られる (能/被吃)</div>
      </div>
    </div>
    <div class="conj-anime-quote">
      🎬 <strong>动漫名台词：</strong><span class="badge badge-purple">負けない！</span> 绝不认输！ / <span class="badge badge-purple">諦めないで</span> 请别放弃
    </div>
  </div>

  <!-- 2. 连用形 -->
  <div class="conj-card" style="border-left: 4px solid #3b82f6;">
    <div class="conj-card-header">
      <div class="conj-card-title-group">
        <span class="conj-badge" style="background:#dbeafe; color:#1d4ed8;">2. 连用形</span>
        <span class="conj-purpose-badge" style="background:#eff6ff; color:#1e40af;">【干嘛的：表礼貌敬体 / 想要】</span>
      </div>
      <span class="conj-suffix-pill">+ ます / たい</span>
    </div>
    <div class="conj-meaning-row">
      💡 <strong>用途解说：</strong>“连接用言”，用来变礼貌敬体(ます)、愿望想做(たい)、动名词或连句中顿。
    </div>
    <div class="conj-rule-box">
      <strong>📐 变换法则：</strong>一类动词词尾变 <span class="highlight">い段</span> (kak-u ➔ kak-i) ；二类动词直接丢「る」
    </div>
    <div class="conj-examples-grid">
      <div class="conj-ex-col">
        <div class="conj-ex-type">一类动词 (書く)</div>
        <div class="conj-ex-text">• 書き-ます (写-礼貌)<br>• 書き-たい (想写)<br>• 書き物 (书写物)</div>
      </div>
      <div class="conj-ex-col">
        <div class="conj-ex-type">二类动词 (食べる)</div>
        <div class="conj-ex-text">• 食べ-ます (吃-礼貌)<br>• 食べ-たい (想吃)<br>• 食べ物 (食物)</div>
      </div>
    </div>
    <div class="conj-anime-quote">
      🎬 <strong>动漫名台词：</strong><span class="badge badge-blue">行きます！</span> 我出发了！ / <span class="badge badge-blue">会いたい</span> 好想见你！
    </div>
  </div>

  <!-- 3. 终止形 / 连体形 -->
  <div class="conj-card" style="border-left: 4px solid #10b981;">
    <div class="conj-card-header">
      <div class="conj-card-title-group">
        <span class="conj-badge" style="background:#dcfce7; color:#15803d;">3. 终止形 / 连体形</span>
        <span class="conj-purpose-badge" style="background:#ecfdf5; color:#065f46;">【干嘛的：原形结句 / 修饰名词】</span>
      </div>
      <span class="conj-suffix-pill">辞书原形 (う段)</span>
    </div>
    <div class="conj-meaning-row">
      💡 <strong>用途解说：</strong>字典原貌。句尾直接打句号结句(终止形)，或直接放在名词前面充当定语(连体形)。
    </div>
    <div class="conj-rule-box">
      <strong>📐 变换法则：</strong>保持词尾 <span class="highlight">う段</span>（辞书形原样不变）
    </div>
    <div class="conj-examples-grid">
      <div class="conj-ex-col">
        <div class="conj-ex-type">一类动词 (書く)</div>
        <div class="conj-ex-text">• 書く (写-结句)<br>• 書く人 (写字的人-定语)</div>
      </div>
      <div class="conj-ex-col">
        <div class="conj-ex-type">二类动词 (食べる)</div>
        <div class="conj-ex-text">• 食べる (吃-结句)<br>• 食べる人 (吃东西的人-定语)</div>
      </div>
    </div>
    <div class="conj-anime-quote">
      🎬 <strong>动漫名台词：</strong><span class="badge badge-green">俺が守る！</span> 由我来守护！ / <span class="badge badge-green">行くぞ！</span> 上吧！
    </div>
  </div>

  <!-- 4. 假定形 -->
  <div class="conj-card" style="border-left: 4px solid #f59e0b;">
    <div class="conj-card-header">
      <div class="conj-card-title-group">
        <span class="conj-badge" style="background:#fef3c7; color:#b45309;">4. 假定形</span>
        <span class="conj-purpose-badge" style="background:#fffbeb; color:#92400e;">【干嘛的：表如果……假设条件】</span>
      </div>
      <span class="conj-suffix-pill">+ ば (如果)</span>
    </div>
    <div class="conj-meaning-row">
      💡 <strong>用途解说：</strong>假设条件，后接「ば」表示“如果……就……”、“只要……就能……”。
    </div>
    <div class="conj-rule-box">
      <strong>📐 变换法则：</strong>一类动词词尾变 <span class="highlight">え段</span> (kak-u ➔ kak-e) ；二类动词变 <span class="highlight">れ</span> (tabe-re)
    </div>
    <div class="conj-examples-grid">
      <div class="conj-ex-col">
        <div class="conj-ex-type">一类动词 (書く)</div>
        <div class="conj-ex-text">• 書け-ば (如果写的话)</div>
      </div>
      <div class="conj-ex-col">
        <div class="conj-ex-type">二类动词 (食べる)</div>
        <div class="conj-ex-text">• 食べれ-ば (如果吃的话)</div>
      </div>
    </div>
    <div class="conj-anime-quote">
      🎬 <strong>动漫名台词：</strong><span class="badge badge-amber">逃げれば助かる</span> 如果逃就能活！ / <span class="badge badge-amber">やればできる</span> 只要去干就能成！
    </div>
  </div>

  <!-- 5. 命令形 -->
  <div class="conj-card" style="border-left: 4px solid #f43f5e;">
    <div class="conj-card-header">
      <div class="conj-card-title-group">
        <span class="conj-badge" style="background:#ffe4e6; color:#be123c;">5. 命令形</span>
        <span class="conj-purpose-badge" style="background:#fff1f2; color:#9f1239;">【干嘛的：强硬命令 / 热血喊话】</span>
      </div>
      <span class="conj-suffix-pill">直接结句！</span>
    </div>
    <div class="conj-meaning-row">
      💡 <strong>用途解说：</strong>长官命令手下、危急时刻或动漫热血战斗中，强硬命令对方立即去做。
    </div>
    <div class="conj-rule-box">
      <strong>📐 变换法则：</strong>一类动词词尾变 <span class="highlight">え段</span> (kak-e) ；二类动词词尾变 <span class="highlight">ろ / よ</span> (tabe-ro / mi-ro)
    </div>
    <div class="conj-examples-grid">
      <div class="conj-ex-col">
        <div class="conj-ex-type">一类动词 (書く)</div>
        <div class="conj-ex-text">• 書け！ (快写！)<br>• 行け！ (冲！)</div>
      </div>
      <div class="conj-ex-col">
        <div class="conj-ex-type">二类动词 (食べる)</div>
        <div class="conj-ex-text">• 食べろ！ (快吃！)<br>• 見ろ！ (看！)</div>
      </div>
    </div>
    <div class="conj-anime-quote">
      🎬 <strong>动漫名台词：</strong><span class="badge badge-rose">逃げろ！</span> 快逃！ / <span class="badge badge-rose">死ね！</span> 去死吧！ / <span class="badge badge-rose">行け！</span> 冲啊！
    </div>
  </div>

  <!-- 6. 意志形 -->
  <div class="conj-card" style="border-left: 4px solid #8b5cf6;">
    <div class="conj-card-header">
      <div class="conj-card-title-group">
        <span class="conj-badge" style="background:#f3e8ff; color:#7e22ce;">6. 意志形</span>
        <span class="conj-purpose-badge" style="background:#faf5ff; color:#6b21a8;">【干嘛的：自身决心 / 提议邀请】</span>
      </div>
      <span class="conj-suffix-pill">お段+う / よう</span>
    </div>
    <div class="conj-meaning-row">
      💡 <strong>用途解说：</strong>表达自己的主观意愿决心（“我要……”），或向伙伴发出邀请提议（“咱们一起……吧！”）。
    </div>
    <div class="conj-rule-box">
      <strong>📐 变换法则：</strong>一类动词变 <span class="highlight">お段+う</span> (kak-o + u ➔ かこう) ；二类动词去る加 <span class="highlight">よう</span> (tabe-you)
    </div>
    <div class="conj-examples-grid">
      <div class="conj-ex-col">
        <div class="conj-ex-type">一类动词 (書く)</div>
        <div class="conj-ex-text">• 書こう (写吧！/我要写)<br>• 行こう (咱们走吧)</div>
      </div>
      <div class="conj-ex-col">
        <div class="conj-ex-type">二类动词 (食べる)</div>
        <div class="conj-ex-text">• 食べよう (吃吧！)<br>• 見よう (看吧！)</div>
      </div>
    </div>
    <div class="conj-anime-quote">
      🎬 <strong>动漫名台词：</strong><span class="badge badge-blue">帰ろう</span> 咱们回去吧 / <span class="badge badge-blue">行こうぜ！</span> 咱们出发吧！
    </div>
  </div>

</div>
"""

# Process all 5 modules
modules_data = []

for mod in modules_config:
    with open(mod["file"], "r", encoding="utf-8") as f:
        raw_html = f.read()

    match = re.search(r"<body[^>]*>(.*?)</body>", raw_html, re.DOTALL | re.IGNORECASE)
    if not match:
        raise ValueError(f"Body not found in {mod['file']}")
    body = match.group(1).strip()

    pages = re.split(r"<div class=[\x27\x22]page-break[\x27\x22]></div>", body)
    if len(pages) != 4:
        raise ValueError(f"Expected 4 pages in {mod['file']}, found {len(pages)}")

    cleaned_pages = []
    for p_idx, page in enumerate(pages):
        p_content = page.strip()

        # Handle Verb Module Page 2 (Conjugation table) specially
        if mod["id"] == "verb" and p_idx == 1:
            # 1. Explainer card placed cleanly inside the content
            explainer_card = """
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
    • <strong>意志形</strong>：表达决心与邀请 ➔ 【我要…… / 咱们一起……吧】(如: 归ろう 咱们回吧！ 行こうぜ 出发！)
  </div>
</div>
"""
            # View toggle buttons
            view_switch_bar = """
<div class="view-switch-bar">
  <button class="view-switch-btn active" id="btn-verb-cards" onclick="setConjugationView('cards')">📱 手机卡片精读 (推荐)</button>
  <button class="view-switch-btn" id="btn-verb-table" onclick="setConjugationView('table')">📊 完整活用大表 (横向对照)</button>
</div>
"""
            # Table wrapper with fixed width columns
            # Modify original table to have conjugation-table class and proper column widths
            def style_verb_table(m):
                tbl = m.group(1)
                tbl = tbl.replace('<table class="custom-table">', '<table class="custom-table conjugation-table">')
                # Modify cells to have nowrap titles
                tbl = tbl.replace("<td><strong>未然形</strong></td>", '<td><div class="table-form-title" style="color:#b91c1c;">未然形</div><div class="table-form-sub">【表否定/被动】</div></td>')
                tbl = tbl.replace("<td><strong>连用形</strong></td>", '<td><div class="table-form-title" style="color:#1d4ed8;">连用形</div><div class="table-form-sub">【表礼貌/想要】</div></td>')
                tbl = tbl.replace("<td><strong>终止形/连体形</strong></td>", '<td><div class="table-form-title" style="color:#15803d;">终止形/连体形</div><div class="table-form-sub">【原形结句/修饰】</div></td>')
                tbl = tbl.replace("<td><strong>假定形</strong></td>", '<td><div class="table-form-title" style="color:#b45309;">假定形</div><div class="table-form-sub">【表如果条件】</div></td>')
                tbl = tbl.replace("<td><strong>命令形</strong></td>", '<td><div class="table-form-title" style="color:#be123c;">命令形</div><div class="table-form-sub">【强硬命令】</div></td>')
                tbl = tbl.replace("<td><strong>意志形</strong></td>", '<td><div class="table-form-title" style="color:#7e22ce;">意志形</div><div class="table-form-sub">【决心/提议】</div></td>')
                return f"""
                {view_switch_bar}
                {verb_cards_html}
                <div id="conjugation-table-view" class="conjugation-view-block" style="display:none;">
                  <div class="table-container">
                    <div class="table-scroll-hint">↔️ 宽表可左右滑动查看完整例词与台词</div>
                    {tbl}
                  </div>
                </div>
                """

            p_content = re.sub(
                r"(<table\s+class=[\x27\x22]custom-table[\x27\x22][^>]*>.*?</table>)",
                style_verb_table,
                p_content,
                count=1,
                flags=re.DOTALL
            )

            # Insert explainer card after <div class="section-title"><span class="num">2</span> 动词活用总览大对照表</div>
            p_content = p_content.replace(
                '<p style="margin-bottom:8px;">把动词原形与你在动漫中听到的各种语气对号入座：</p>',
                f'{explainer_card}<p style="margin-bottom:8px;">把动词原形与你在动漫中听到的各种语气对号入座：</p>'
            )

        else:
            # Wrap standard custom-tables in horizontal scroll containers
            p_content = re.sub(
                r"(<table\s+class=[\x27\x22]custom-table[\x27\x22][^>]*>.*?</table>)",
                r'<div class="table-container"><div class="table-scroll-hint">↔️ 宽表可左右滑动</div>\1</div>',
                p_content,
                flags=re.DOTALL
            )

        cleaned_pages.append(p_content)

    modules_data.append({
        "info": mod,
        "pages": cleaned_pages
    })

# HTML Master Template
html_template = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="apple-mobile-web-app-title" content="日语随身宝">
<meta name="format-detection" content="telephone=no">
<title>日语核心语法与全景口语随身宝 · 手机版</title>

<link rel="manifest" href="./manifest.json">
<link rel="apple-touch-icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 512 512'><rect width='512' height='512' rx='128' fill='%231e3a8a'/><path d='M110 160h292M140 140v242M372 140v242M140 210h232' stroke='white' stroke-width='32' stroke-linecap='round'/><circle cx='380' cy='370' r='42' fill='%23e11d48'/></svg>">

<style>
  /* ================= RIGID THEME PALETTES ================= */
  :root {
    --text-main: #0f172a;
    --text-muted: #475569;
    --border-color: #cbd5e1;
    --bg-page: #f8fafc;
    --bg-card: #ffffff;
    --table-td-color: #0f172a;
    --table-even-bg: #f8fafc;
    --table-odd-bg: #ffffff;
    --top-bg: rgba(255, 255, 255, 0.98);
    --bottom-bg: rgba(255, 255, 255, 0.98);
    --bottom-text: #475569;
    --search-bg: #f1f5f9;
    --search-text: #0f172a;
    --pill-bg: #e2e8f0;
    --pill-text: #334155;
    --current-theme: #1e40af;
  }

  @media (prefers-color-scheme: dark) {
    :root:not([data-theme="light"]) {
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --border-color: #334155;
      --bg-page: #0f172a;
      --bg-card: #1e293b;
      --table-td-color: #f8fafc;
      --table-even-bg: rgba(255, 255, 255, 0.04);
      --table-odd-bg: #1e293b;
      --top-bg: rgba(15, 23, 42, 0.98);
      --bottom-bg: rgba(15, 23, 42, 0.98);
      --bottom-text: #94a3b8;
      --search-bg: #1e293b;
      --search-text: #f8fafc;
      --pill-bg: #334155;
      --pill-text: #cbd5e1;
    }
  }

  :root[data-theme="dark"] {
    --text-main: #f8fafc !important;
    --text-muted: #94a3b8 !important;
    --border-color: #334155 !important;
    --bg-page: #0f172a !important;
    --bg-card: #1e293b !important;
    --table-td-color: #f8fafc !important;
    --table-even-bg: rgba(255, 255, 255, 0.04) !important;
    --table-odd-bg: #1e293b !important;
    --top-bg: rgba(15, 23, 42, 0.98) !important;
    --bottom-bg: rgba(15, 23, 42, 0.98) !important;
    --bottom-text: #94a3b8 !important;
    --search-bg: #1e293b !important;
    --search-text: #f8fafc !important;
    --pill-bg: #334155 !important;
    --pill-text: #cbd5e1 !important;
  }

  :root[data-theme="light"] {
    --text-main: #0f172a !important;
    --text-muted: #475569 !important;
    --border-color: #cbd5e1 !important;
    --bg-page: #f8fafc !important;
    --bg-card: #ffffff !important;
    --table-td-color: #0f172a !important;
    --table-even-bg: #f8fafc !important;
    --table-odd-bg: #ffffff !important;
    --top-bg: rgba(255, 255, 255, 0.98) !important;
    --bottom-bg: rgba(255, 255, 255, 0.98) !important;
    --bottom-text: #475569 !important;
    --search-bg: #f1f5f9 !important;
    --search-text: #0f172a !important;
    --pill-bg: #e2e8f0 !important;
    --pill-text: #334155 !important;
  }

  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    -webkit-tap-highlight-color: transparent;
  }

  body {
    font-family: -apple-system, BlinkMacSystemFont, "SF Pro Text", "SF Pro Display", "Segoe UI", "PingFang SC", "Hiragino Sans", "Meiryo", "Microsoft YaHei", sans-serif;
    color: var(--text-main);
    background-color: var(--bg-page);
    line-height: 1.58;
    font-size: 13.5px;
    -webkit-font-smoothing: antialiased;
    -webkit-text-size-adjust: 100%;
    /* Extra padding-top so content scrolls completely underneath top-header without any gap */
    padding-top: max(142px, calc(env(safe-area-inset-top) + 130px));
    padding-bottom: max(75px, calc(env(safe-area-inset-bottom) + 65px));
  }

  /* ================= UNIFIED TOP HEADER ================= */
  .top-header {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    z-index: 100;
    background: var(--top-bg);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border-bottom: 1px solid var(--border-color);
    padding: max(8px, env(safe-area-inset-top)) 12px 8px 12px;
  }

  .header-main-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 6px;
  }

  .app-title {
    font-size: 16px;
    font-weight: 800;
    display: flex;
    align-items: center;
    gap: 6px;
  }
  .module-badge {
    font-size: 11px;
    padding: 2px 8px;
    border-radius: 999px;
    font-weight: 700;
    color: #ffffff;
    background: var(--current-theme);
  }

  .theme-toggle-btn {
    font-size: 12px;
    font-weight: 700;
    padding: 3px 9px;
    border-radius: 8px;
    border: 1px solid var(--border-color);
    background: var(--bg-card);
    color: var(--text-main);
    cursor: pointer;
    display: inline-flex;
    align-items: center;
    gap: 4px;
  }

  .search-wrapper {
    position: relative;
    width: 100%;
    margin-bottom: 6px;
  }
  .search-input {
    width: 100%;
    height: 32px;
    border-radius: 8px;
    border: 1px solid var(--border-color);
    background: var(--search-bg);
    color: var(--search-text);
    padding: 0 10px 0 30px;
    font-size: 13px;
    outline: none;
  }
  .search-input:focus {
    border-color: var(--current-theme);
  }
  .search-icon {
    position: absolute;
    left: 9px;
    top: 50%;
    transform: translateY(-50%);
    font-size: 12px;
    color: var(--text-muted);
  }

  /* Embedded Subpage Chapter Pills */
  .header-subpage-nav {
    display: flex;
    flex-direction: column;
    gap: 4px;
  }

  .pills-row {
    display: flex;
    gap: 6px;
    overflow-x: auto;
    scrollbar-width: none;
    -webkit-overflow-scrolling: touch;
    padding-bottom: 2px;
  }
  .pills-row::-webkit-scrollbar { display: none; }

  .chap-pill {
    flex: 0 0 auto;
    padding: 4px 10px;
    border-radius: 999px;
    font-size: 11px;
    font-weight: 700;
    border: 1px solid var(--border-color);
    background: var(--pill-bg);
    color: var(--pill-text);
    cursor: pointer;
    transition: all 0.2s;
  }
  .chap-pill.active {
    background: var(--current-theme);
    color: #ffffff;
    border-color: var(--current-theme);
    box-shadow: 0 2px 6px rgba(0,0,0,0.12);
  }

  .subpage-controls {
    display: flex;
    align-items: center;
    justify-content: space-between;
    font-size: 11px;
    padding: 0 2px;
  }
  .step-arrow-btn {
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: 6px;
    padding: 2px 8px;
    font-size: 11px;
    font-weight: 700;
    color: var(--text-main);
    cursor: pointer;
  }
  .step-indicator {
    font-weight: 700;
    color: var(--current-theme);
  }

  /* ================= HORIZONTAL SWIPER SLIDER ================= */
  .module-pane {
    display: none;
  }
  .module-pane.active {
    display: block;
  }

  .swiper-viewport {
    width: 100%;
    overflow-x: auto;
    overflow-y: hidden;
    scroll-snap-type: x mandatory;
    -webkit-overflow-scrolling: touch;
    scroll-behavior: smooth;
    scrollbar-width: none;
    touch-action: pan-y pan-x;
  }
  .swiper-viewport::-webkit-scrollbar { display: none; }

  .swiper-track {
    display: flex;
    width: 100%;
  }

  .swiper-slide {
    flex: 0 0 100%;
    width: 100%;
    min-width: 100%;
    max-width: 100%;
    scroll-snap-align: start;
    scroll-snap-stop: always;
    box-sizing: border-box;
    padding: 4px 12px 24px 12px;
  }

  /* Slide Footer Navigation */
  .slide-footer-nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: 18px;
    padding-top: 12px;
    border-top: 1px solid var(--border-color);
    gap: 10px;
  }
  .slide-nav-btn {
    flex: 1;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 4px;
    padding: 8px 10px;
    border-radius: 8px;
    font-size: 12.5px;
    font-weight: 700;
    border: 1px solid var(--border-color);
    background: var(--bg-card);
    color: var(--text-main);
    cursor: pointer;
    text-align: center;
  }
  .slide-nav-btn.primary {
    background: var(--current-theme);
    color: #ffffff;
    border-color: var(--current-theme);
  }

  /* ================= VIEW SWITCH BAR (CARDS VS TABLE) ================= */
  .view-switch-bar {
    display: flex;
    gap: 8px;
    margin: 10px 0 12px 0;
  }
  .view-switch-btn {
    flex: 1;
    padding: 7px 10px;
    border-radius: 8px;
    border: 1px solid var(--border-color);
    background: var(--bg-card);
    color: var(--text-main);
    font-size: 12px;
    font-weight: 700;
    cursor: pointer;
    transition: all 0.2s;
  }
  .view-switch-btn.active {
    background: var(--current-theme);
    color: #ffffff;
    border-color: var(--current-theme);
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
  }

  /* ================= CONJUGATION MOBILE CARDS STYLING ================= */
  .conj-card {
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: 10px;
    padding: 12px 13px;
    margin-bottom: 12px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.03);
  }
  .conj-card-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 8px;
    flex-wrap: wrap;
    gap: 5px;
  }
  .conj-card-title-group {
    display: flex;
    align-items: center;
    gap: 6px;
    flex-wrap: wrap;
  }
  .conj-badge {
    font-size: 13px;
    font-weight: 800;
    padding: 2px 7px;
    border-radius: 5px;
    white-space: nowrap;
  }
  .conj-purpose-badge {
    font-size: 11.5px;
    font-weight: 800;
    padding: 2px 6px;
    border-radius: 4px;
    white-space: nowrap;
  }
  .conj-suffix-pill {
    font-size: 11px;
    font-weight: 700;
    padding: 2px 7px;
    border-radius: 999px;
    background: var(--pill-bg);
    color: var(--pill-text);
    white-space: nowrap;
  }
  .conj-meaning-row {
    font-size: 12px;
    line-height: 1.5;
    color: var(--text-main);
    margin-bottom: 8px;
  }
  .conj-rule-box {
    background: rgba(0, 0, 0, 0.03);
    border-radius: 6px;
    padding: 6px 9px;
    font-size: 12px;
    margin-bottom: 8px;
    line-height: 1.5;
  }
  :root[data-theme="dark"] .conj-rule-box {
    background: rgba(255, 255, 255, 0.04);
  }
  .conj-examples-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 8px;
    margin-bottom: 8px;
  }
  .conj-ex-col {
    background: var(--bg-page);
    border: 1px solid var(--border-color);
    border-radius: 6px;
    padding: 6px 8px;
  }
  .conj-ex-type {
    font-size: 10.5px;
    font-weight: 700;
    color: var(--text-muted);
    margin-bottom: 3px;
    border-bottom: 1px solid var(--border-color);
    padding-bottom: 2px;
  }
  .conj-ex-text {
    font-size: 11.5px;
    line-height: 1.55;
    font-weight: 600;
  }
  .conj-anime-quote {
    font-size: 11.5px;
    line-height: 1.5;
    padding-top: 5px;
    border-top: 1px dashed var(--border-color);
  }

  /* Verb Explanation Card */
  .form-explainer-card {
    border-left: 4px solid var(--current-theme);
    background: var(--bg-card);
    margin-bottom: 12px;
  }
  .form-explainer-title {
    font-weight: 800;
    font-size: 13.5px;
    color: var(--current-theme);
    margin-bottom: 4px;
  }
  .form-explainer-body {
    font-size: 12px;
    line-height: 1.65;
    color: var(--text-main);
  }

  /* Table Specific Styles */
  .table-container {
    width: 100%;
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
    margin-bottom: 12px;
    border-radius: 8px;
    border: 1px solid var(--border-color);
    background: var(--bg-card);
  }
  .table-scroll-hint {
    font-size: 10.5px;
    color: var(--text-muted);
    padding: 3px 8px;
    background: rgba(0,0,0,0.02);
    border-bottom: 1px solid var(--border-color);
  }

  table.custom-table {
    width: 100%;
    min-width: 680px;
    border-collapse: collapse;
    font-size: 12px;
    border: none;
  }
  table.custom-table th {
    color: #ffffff;
    padding: 7px 9px;
    font-weight: 700;
    text-align: left;
    white-space: nowrap;
  }
  table.custom-table td {
    padding: 7px 9px;
    border-bottom: 1px solid var(--border-color);
    vertical-align: middle;
    color: var(--table-td-color) !important;
  }
  table.custom-table tr:nth-child(even) td {
    background-color: var(--table-even-bg) !important;
  }
  table.custom-table tr:nth-child(odd) td {
    background-color: var(--table-odd-bg) !important;
  }
  table.custom-table tr:last-child td {
    border-bottom: none;
  }

  /* Explicit column widths for the 6-column verb table */
  .conjugation-table {
    min-width: 820px !important;
  }
  .conjugation-table th:nth-child(1),
  .conjugation-table td:nth-child(1) {
    width: 155px;
    min-width: 155px;
    max-width: 155px;
  }
  .conjugation-table th:nth-child(2),
  .conjugation-table td:nth-child(2) {
    width: 110px;
    min-width: 110px;
  }
  .conjugation-table th:nth-child(3),
  .conjugation-table td:nth-child(3) {
    width: 140px;
    min-width: 140px;
  }
  .conjugation-table th:nth-child(4),
  .conjugation-table td:nth-child(4) {
    width: 120px;
    min-width: 120px;
  }
  .conjugation-table th:nth-child(5),
  .conjugation-table td:nth-child(5) {
    width: 120px;
    min-width: 120px;
  }
  .conjugation-table th:nth-child(6),
  .conjugation-table td:nth-child(6) {
    width: 175px;
    min-width: 175px;
  }

  .table-form-title {
    font-size: 13px;
    font-weight: 800;
    white-space: nowrap;
  }
  .table-form-sub {
    font-size: 11px;
    font-weight: 700;
    color: var(--text-muted);
    white-space: nowrap;
    margin-top: 2px;
  }

  /* Document Generic Components */
  .doc-header {
    border-radius: 10px;
    padding: 14px 15px;
    margin-bottom: 12px;
    color: #ffffff;
  }
  .doc-header h1 {
    font-size: 18.5px;
    font-weight: 800;
    margin-bottom: 4px;
    line-height: 1.35;
  }
  .doc-header .subtitle {
    font-size: 12px;
    opacity: 0.94;
    margin-bottom: 7px;
  }
  .tags { display: flex; gap: 5px; flex-wrap: wrap; }
  .tag {
    background: rgba(255, 255, 255, 0.22);
    border: 1px solid rgba(255, 255, 255, 0.35);
    padding: 1px 7px;
    border-radius: 999px;
    font-size: 10.5px;
    font-weight: 600;
  }

  .section { margin-bottom: 14px; }
  .section-title {
    font-size: 14.5px;
    font-weight: 700;
    margin-bottom: 9px;
    display: flex;
    align-items: center;
    gap: 7px;
    padding-bottom: 4px;
    border-bottom: 2px solid;
  }
  .section-title .num {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 21px;
    height: 21px;
    border-radius: 50%;
    color: #ffffff;
    font-size: 11.5px;
    font-weight: 700;
    flex-shrink: 0;
  }

  .card {
    border: 1px solid var(--border-color);
    border-radius: 9px;
    padding: 11px 13px;
    margin-bottom: 11px;
    background-color: var(--bg-card);
    color: var(--text-main);
  }

  .info-box {
    background-color: var(--bg-card);
    border-left: 4px solid;
    border-radius: 0 8px 8px 0;
    padding: 10px 12px;
    margin-bottom: 11px;
    font-size: 12.8px;
    line-height: 1.6;
    border-top: 1px solid var(--border-color);
    border-right: 1px solid var(--border-color);
    border-bottom: 1px solid var(--border-color);
    color: var(--text-main);
  }

  .anime-box {
    background-color: #fdf4ff;
    border: 1px solid #f0abfc;
    border-left: 4px solid #d946ef;
    border-radius: 0 8px 8px 0;
    padding: 10px 12px;
    margin-bottom: 11px;
    font-size: 12.8px;
    line-height: 1.6;
    color: #701a75;
  }
  .anime-box .title { font-weight: 700; color: #a21caf; margin-bottom: 3px; }
  :root[data-theme="dark"] .anime-box { background-color: rgba(217, 70, 239, 0.12); border-color: rgba(217, 70, 239, 0.3); color: #f5d0fe; }
  :root[data-theme="dark"] .anime-box .title { color: #f0abfc; }

  .trap-box {
    background-color: #fff1f2;
    border: 1px solid #fecdd3;
    border-left: 4px solid #e11d48;
    border-radius: 0 8px 8px 0;
    padding: 10px 12px;
    margin-bottom: 11px;
    font-size: 12.8px;
    line-height: 1.6;
    color: #881337;
  }
  .trap-box .title { font-weight: 700; color: #be123c; margin-bottom: 3px; }
  :root[data-theme="dark"] .trap-box { background-color: rgba(225, 29, 72, 0.12); border-color: rgba(225, 29, 72, 0.3); color: #fecdd3; }
  :root[data-theme="dark"] .trap-box .title { color: #fecdd3; }

  .mnemonic-box {
    background-color: #fefce8;
    border: 1px solid #fef08a;
    border-left: 4px solid #ca8a04;
    border-radius: 0 8px 8px 0;
    padding: 10px 12px;
    margin-bottom: 11px;
    font-size: 12.8px;
    line-height: 1.6;
    color: #713f12;
  }
  .mnemonic-box .title { font-weight: 700; color: #a16207; margin-bottom: 3px; }
  :root[data-theme="dark"] .mnemonic-box { background-color: rgba(202, 138, 4, 0.12); border-color: rgba(202, 138, 4, 0.3); color: #fef08a; }
  :root[data-theme="dark"] .mnemonic-box .title { color: #fef08a; }

  .tip-box {
    background-color: #f0fdf4;
    border: 1px solid #bbf7d0;
    border-left: 4px solid #16a34a;
    border-radius: 0 8px 8px 0;
    padding: 10px 12px;
    margin-bottom: 11px;
    font-size: 12.8px;
    line-height: 1.6;
    color: #14532d;
  }
  .tip-box .title { font-weight: 700; color: #15803d; margin-bottom: 3px; }
  :root[data-theme="dark"] .tip-box { background-color: rgba(22, 163, 74, 0.12); border-color: rgba(22, 163, 74, 0.3); color: #bbf7d0; }
  :root[data-theme="dark"] .tip-box .title { color: #bbf7d0; }

  .warn-box {
    background-color: #fff7ed;
    border: 1px solid #fed7aa;
    border-left: 4px solid #ea580c;
    border-radius: 0 8px 8px 0;
    padding: 10px 12px;
    margin-bottom: 11px;
    font-size: 12.8px;
    line-height: 1.6;
    color: #7c2d12;
  }
  .warn-box .title { font-weight: 700; color: #c2410c; margin-bottom: 3px; }
  :root[data-theme="dark"] .warn-box { background-color: rgba(234, 88, 12, 0.12); border-color: rgba(234, 88, 12, 0.3); color: #fed7aa; }
  :root[data-theme="dark"] .warn-box .title { color: #fed7aa; }

  .grid-2, .grid-3 {
    display: flex;
    flex-direction: column;
    gap: 10px;
    margin-bottom: 11px;
  }

  .badge {
    display: inline-block;
    padding: 2px 7px;
    border-radius: 4px;
    font-size: 11px;
    font-weight: 700;
  }
  .badge-blue { background: #dbeafe; color: #1e40af; }
  .badge-green { background: #d1fae5; color: #065f46; }
  .badge-amber { background: #fef3c7; color: #92400e; }
  .badge-purple { background: #ede9fe; color: #5b21b6; }
  .badge-rose { background: #ffe4e6; color: #9f1239; }

  .highlight { color: #dc2626; font-weight: 700; }
  .jp-bold {
    font-family: -apple-system, BlinkMacSystemFont, "Hiragino Sans", "Meiryo", "PingFang SC", sans-serif;
    font-weight: 700;
    color: inherit;
  }

  .footer-bar {
    text-align: center;
    font-size: 11px;
    color: var(--text-muted);
    margin: 14px 0 6px 0;
    padding-top: 6px;
    border-top: 1px solid var(--border-color);
  }

  /* Module Specific Headers */
  #module-verb { --current-theme: #1e40af; }
  #module-verb .doc-header { background: linear-gradient(135deg, #1e3a8a 0%, #2563eb 100%); }
  #module-verb table.custom-table th { background: #1e3a8a; }
  #module-verb .section-title { color: #1e40af; border-bottom-color: #1e40af; }
  #module-verb .section-title .num { background: #1e40af; }
  #module-verb .info-box { border-left-color: #3b82f6; }

  #module-adj { --current-theme: #065f46; }
  #module-adj .doc-header { background: linear-gradient(135deg, #064e3b 0%, #059669 100%); }
  #module-adj table.custom-table th { background: #064e3b; }
  #module-adj .section-title { color: #065f46; border-bottom-color: #065f46; }
  #module-adj .section-title .num { background: #065f46; }
  #module-adj .info-box { border-left-color: #059669; }

  #module-particle { --current-theme: #9a3412; }
  #module-particle .doc-header { background: linear-gradient(135deg, #7c2d12 0%, #ea580c 100%); }
  #module-particle table.custom-table th { background: #7c2d12; }
  #module-particle .section-title { color: #9a3412; border-bottom-color: #9a3412; }
  #module-particle .section-title .num { background: #9a3412; }
  #module-particle .info-box { border-left-color: #ea580c; }

  #module-sent { --current-theme: #581c87; }
  #module-sent .doc-header { background: linear-gradient(135deg, #4c1d95 0%, #7c3aed 100%); }
  #module-sent table.custom-table th { background: #4c1d95; }
  #module-sent .section-title { color: #581c87; border-bottom-color: #581c87; }
  #module-sent .section-title .num { background: #581c87; }
  #module-sent .info-box { border-left-color: #7c3aed; }

  #module-spoken { --current-theme: #9f1239; }
  #module-spoken .doc-header { background: linear-gradient(135deg, #881337 0%, #e11d48 100%); }
  #module-spoken table.custom-table th { background: #881337; }
  #module-spoken .section-title { color: #9f1239; border-bottom-color: #9f1239; }
  #module-spoken .section-title .num { background: #9f1239; }
  #module-spoken .info-box { border-left-color: #e11d48; }

  /* ================= FLOATING BOTTOM NAVIGATION BAR ================= */
  .bottom-nav {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    z-index: 100;
    background: var(--bottom-bg);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border-top: 1px solid var(--border-color);
    padding: 5px 2px max(6px, env(safe-area-inset-bottom)) 2px;
    display: flex;
    justify-content: space-around;
  }

  .nav-tab-btn {
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    background: none;
    border: none;
    padding: 2px 0;
    color: var(--bottom-text);
    font-size: 11px;
    font-weight: 700;
    cursor: pointer;
    transition: all 0.2s;
  }
  .nav-tab-btn .tab-icon {
    font-size: 17px;
    margin-bottom: 1px;
    transition: transform 0.2s;
  }
  .nav-tab-btn.active {
    color: var(--current-theme);
  }
  .nav-tab-btn.active .tab-icon {
    transform: scale(1.15);
  }
</style>
</head>
<body>

<!-- UNIFIED FIXED TOP HEADER -->
<header class="top-header">
  <div class="header-main-row">
    <div class="app-title">
      <span>🎌 日语随身宝</span>
      <span class="module-badge" id="moduleBadge">🏃 动词篇</span>
    </div>
    <button class="theme-toggle-btn" id="themeToggleBtn" onclick="toggleTheme()">
      <span id="themeIcon">☀️</span>
      <span id="themeText">浅色</span>
    </button>
  </div>

  <div class="search-wrapper">
    <span class="search-icon">🔍</span>
    <input type="text" class="search-input" id="globalSearch" placeholder="搜索语法、词形、台词 (如: 未然形, て形, は, すげえ)..." oninput="handleSearch()">
  </div>

  <!-- EMBEDDED SUBPAGE CHAPTER NAV -->
  <div class="header-subpage-nav">
    <div class="pills-row" id="headerPillsRow">
      <!-- Injected dynamically by JS -->
    </div>
    <div class="subpage-controls">
      <button class="step-arrow-btn" onclick="prevSlide(currentModule)">◀ 上一章</button>
      <span class="step-indicator" id="headerStepIndicator">第 1 / 4 章 (左右轻滑翻页)</span>
      <button class="step-arrow-btn" onclick="nextSlide(currentModule)">下一章 ▶</button>
    </div>
  </div>
</header>

<!-- MAIN MODULES CONTAINER -->
<main id="mainContainer">
{MODULES_PLACEHOLDER}
</main>

<!-- FLOATING BOTTOM NAVIGATION BAR (5 BIG MODULES) -->
<nav class="bottom-nav">
  <button class="nav-tab-btn active" data-mod="verb" onclick="switchModule('verb', '#1e40af', '🏃 动词篇')">
    <span class="tab-icon">🏃</span>
    <span>动词篇</span>
  </button>
  <button class="nav-tab-btn" data-mod="adj" onclick="switchModule('adj', '#065f46', '✨ 形容词')">
    <span class="tab-icon">✨</span>
    <span>形容词</span>
  </button>
  <button class="nav-tab-btn" data-mod="particle" onclick="switchModule('particle', '#9a3412', '⚓ 助词篇')">
    <span class="tab-icon">⚓</span>
    <span>助词篇</span>
  </button>
  <button class="nav-tab-btn" data-mod="sent" onclick="switchModule('sent', '#581c87', '🧱 造句篇')">
    <span class="tab-icon">🧱</span>
    <span>造句篇</span>
  </button>
  <button class="nav-tab-btn" data-mod="spoken" onclick="switchModule('spoken', '#9f1239', '🗣️ 口语篇')">
    <span class="tab-icon">🗣️</span>
    <span>口语篇</span>
  </button>
</nav>

<script>
  let currentModule = 'verb';
  let currentPageIdx = 0;

  const modulePillsData = {
    verb: ["1. 分类判定", "2. 六大活用", "3. 音便口诀", "4. 派生句型"],
    adj: ["1. 两派假词", "2. い形变形", "3. な形与PK", "4. 派生变音"],
    particle: ["1. はvsが", "2. 核心格助词", "3. 并列与副助", "4. 终助词人设"],
    sent: ["1. 积木公式", "2. 复句齿轮", "3. 授受动词", "4. 常用句型"],
    spoken: ["1. 相槌万能词", "2. 7大缩约音", "3. 情境短句", "4. 现实防踩雷"]
  };

  const themeMap = {
    verb: '#1e40af',
    adj: '#065f46',
    particle: '#9a3412',
    sent: '#581c87',
    spoken: '#9f1239'
  };

  const nextModuleMap = {
    verb: { id: 'adj', name: '✨ 形容词篇' },
    adj: { id: 'particle', name: '⚓ 助词篇' },
    particle: { id: 'sent', name: '🧱 造句篇' },
    sent: { id: 'spoken', name: '🗣️ 口语篇' },
    spoken: { id: 'verb', name: '🏃 回到动词篇' }
  };

  // Switch Big Module Tab
  function switchModule(modId, color, badgeText) {
    currentModule = modId;
    currentPageIdx = 0;

    document.querySelectorAll('.module-pane').forEach(el => el.classList.remove('active'));
    document.querySelectorAll('.nav-tab-btn').forEach(btn => btn.classList.remove('active'));

    const target = document.getElementById('module-' + modId);
    if (target) target.classList.add('active');

    const activeBtn = document.querySelector(`.nav-tab-btn[data-mod="${modId}"]`);
    if (activeBtn) activeBtn.classList.add('active');

    document.documentElement.style.setProperty('--current-theme', color);
    document.getElementById('moduleBadge').innerText = badgeText;

    renderHeaderPills(modId, 0);
    goToSlide(modId, 0, false);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  // Render Header Chapter Pills for Current Module
  function renderHeaderPills(modId, activeIdx) {
    const pills = modulePillsData[modId] || [];
    const container = document.getElementById('headerPillsRow');
    if (!container) return;

    let html = '';
    pills.forEach((title, idx) => {
      const act = idx === activeIdx ? ' active' : '';
      html += `<button class="chap-pill${act}" onclick="goToSlide('${modId}', ${idx})">${title}</button>`;
    });
    container.innerHTML = html;

    const ind = document.getElementById('headerStepIndicator');
    if (ind) {
      ind.innerText = `第 ${activeIdx + 1} / 4 章 (左右轻滑翻页)`;
    }
  }

  // Go To Specific Subpage Slide
  function goToSlide(modId, pageIdx, smoothScroll = true) {
    currentPageIdx = pageIdx;
    const viewport = document.getElementById('viewport-' + modId);
    if (!viewport) return;

    viewport.scrollTo({
      left: pageIdx * viewport.clientWidth,
      behavior: smoothScroll ? 'smooth' : 'auto'
    });

    renderHeaderPills(modId, pageIdx);
    if (smoothScroll) {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }
  }

  function prevSlide(modId) {
    if (currentPageIdx > 0) {
      goToSlide(modId, currentPageIdx - 1);
    }
  }

  function nextSlide(modId) {
    if (currentPageIdx < 3) {
      goToSlide(modId, currentPageIdx + 1);
    } else {
      const nextMod = nextModuleMap[modId];
      if (nextMod) {
        switchModule(nextMod.id, themeMap[nextMod.id], nextMod.name);
      }
    }
  }

  // Toggle Conjugation View (Cards vs Table)
  function setConjugationView(mode) {
    const cardsView = document.getElementById('conjugation-cards-view');
    const tableView = document.getElementById('conjugation-table-view');
    const btnCards = document.getElementById('btn-verb-cards');
    const btnTable = document.getElementById('btn-verb-table');

    if (mode === 'cards') {
      if (cardsView) cardsView.style.display = 'block';
      if (tableView) tableView.style.display = 'none';
      if (btnCards) btnCards.classList.add('active');
      if (btnTable) btnTable.classList.remove('active');
    } else {
      if (cardsView) cardsView.style.display = 'none';
      if (tableView) tableView.style.display = 'block';
      if (btnCards) btnCards.classList.remove('active');
      if (btnTable) btnTable.classList.add('active');
    }
  }

  // Bind Swiper Scroll Events
  document.addEventListener('DOMContentLoaded', () => {
    ['verb', 'adj', 'particle', 'sent', 'spoken'].forEach(modId => {
      const viewport = document.getElementById('viewport-' + modId);
      if (viewport) {
        let scrollTimeout;
        viewport.addEventListener('scroll', () => {
          clearTimeout(scrollTimeout);
          scrollTimeout = setTimeout(() => {
            const pageIdx = Math.round(viewport.scrollLeft / viewport.clientWidth);
            if (pageIdx !== currentPageIdx) {
              currentPageIdx = pageIdx;
              renderHeaderPills(modId, pageIdx);
            }
          }, 50);
        }, { passive: true });
      }
    });

    renderHeaderPills('verb', 0);

  // Register PWA Service Worker for 100% Offline Caching
  if ("serviceWorker" in navigator) {
    window.addEventListener("load", () => {
      navigator.serviceWorker.register("./sw.js").then(reg => {
        console.log("PWA Service Worker registered:", reg.scope);
      }).catch(err => {
        console.log("PWA Service Worker failed:", err);
      });
    });
  }

    initTheme();
  });

  // ================= THEME SWITCHING (LIGHT / DARK) =================
  function initTheme() {
    const saved = localStorage.getItem('user_theme_pref');
    if (saved === 'dark' || saved === 'light') {
      document.documentElement.setAttribute('data-theme', saved);
    } else {
      const isSysDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
      document.documentElement.setAttribute('data-theme', isSysDark ? 'dark' : 'light');
    }
    updateThemeUI();
  }

  function toggleTheme() {
    const current = document.documentElement.getAttribute('data-theme');
    const next = current === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', next);
    localStorage.setItem('user_theme_pref', next);
    updateThemeUI();
  }

  function updateThemeUI() {
    const current = document.documentElement.getAttribute('data-theme');
    const isDark = current === 'dark';
    const icon = document.getElementById('themeIcon');
    const text = document.getElementById('themeText');
    if (icon && text) {
      icon.innerText = isDark ? '🌙' : '☀️';
      text.innerText = isDark ? '深色' : '浅色';
    }
  }

  // ================= GLOBAL SEARCH FILTER =================
  function handleSearch() {
    const query = document.getElementById('globalSearch').value.trim().toLowerCase();
    const allCards = document.querySelectorAll('.card, .info-box, .anime-box, .trap-box, .mnemonic-box, .tip-box, .warn-box, .section, .conj-card');

    if (!query) {
      allCards.forEach(el => el.style.display = '');
      return;
    }

    allCards.forEach(el => {
      const text = el.innerText.toLowerCase();
      if (text.includes(query)) {
        el.style.display = '';
      } else {
        const hasChildMatch = el.querySelector && el.querySelector('.section, .card, .conj-card') ? true : false;
        if (!hasChildMatch) el.style.display = 'none';
      }
    });
  }
</script>

</body>
</html>
"""

# Render Modules HTML
modules_rendered = []

for mod_idx, item in enumerate(modules_data):
    mod = item["info"]
    mod_id = mod["id"]
    is_active = " active" if mod_idx == 0 else ""

    slides_html = []
    for s_i, page_content in enumerate(item["pages"]):
        # Footer buttons for this slide
        if s_i == 0:
            foot_btn = f"""
            <div class="slide-footer-nav">
              <span></span>
              <button class="slide-nav-btn primary" onclick="goToSlide('{mod_id}', 1)">下一章：{mod['pills'][1]} ▶</button>
            </div>
            """
        elif s_i == 3:
            next_mod = {
                'verb': ('adj', '下一大类：形容词篇'),
                'adj': ('particle', '下一大类：助词篇'),
                'particle': ('sent', '下一大类：造句篇'),
                'sent': ('spoken', '下一大类：口语篇'),
                'spoken': ('verb', '回到开头：动词篇')
            }[mod_id]
            foot_btn = f"""
            <div class="slide-footer-nav">
              <button class="slide-nav-btn" onclick="goToSlide('{mod_id}', 2)">◀ 上一章</button>
              <button class="slide-nav-btn primary" onclick="switchModule('{next_mod[0]}', themeMap['{next_mod[0]}'], '{next_mod[1]}')">{next_mod[1]} ▶</button>
            </div>
            """
        else:
            foot_btn = f"""
            <div class="slide-footer-nav">
              <button class="slide-nav-btn" onclick="goToSlide('{mod_id}', {s_i-1})">◀ 上一章：{mod['pills'][s_i-1]}</button>
              <button class="slide-nav-btn primary" onclick="goToSlide('{mod_id}', {s_i+1})">下一章：{mod['pills'][s_i+1]} ▶</button>
            </div>
            """

        slides_html.append(f"""
        <div class="swiper-slide" id="slide-{mod_id}-{s_i}">
          {page_content}
          {foot_btn}
        </div>
        """)

    slides_row = "\n".join(slides_html)

    module_block = f"""
<div class="module-pane{is_active}" id="module-{mod_id}">
  <!-- HORIZONTAL SWIPER VIEWPORT -->
  <div class="swiper-viewport" id="viewport-{mod_id}">
    <div class="swiper-track">
      {slides_row}
    </div>
  </div>
</div>
"""
    modules_rendered.append(module_block)

final_html = html_template.replace("{MODULES_PLACEHOLDER}", "\n".join(modules_rendered))

# Write out to 日语随身宝.html and index.html
with open('日语随身宝.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print("Generated V4 日语随身宝.html and index.html successfully.")
print(f"File size: {len(final_html.encode('utf-8'))} bytes.")
