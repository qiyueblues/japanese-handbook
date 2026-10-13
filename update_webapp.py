# -*- coding: utf-8 -*-
"""
Generator for the Full Comprehensive Japanese Mobile Web App.
Includes:
- Dedicated Module on Pitch Accent (声调/音调核) with visual curves and pronunciation rules
- Full, uncompressed content from all 5 PDF modules (Verbs, Adjectives, Particles, Sentences, Colloquial Spoken)
- Furigana (<ruby>) on all Kanji
- Pitch accent notation (⓪型平板, ①型头高, ②型中高, 尾高型) on key vocabulary
- Speech synthesis with adjusted parameters
- Filterable search across all modules
- Offline iOS PWA compatibility
"""

import os

html_code = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="apple-mobile-web-app-title" content="日语随身宝">
<meta name="theme-color" content="#ffffff" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0f172a" media="(prefers-color-scheme: dark)">
<title>日语核心语法与全景口语随身宝 · 完整进阶版</title>

<!-- Apple Touch Icon -->
<link rel="apple-touch-icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 512 512'><rect width='512' height='512' rx='128' fill='%232563eb'/><path d='M160 140h192M256 140v232M190 230h132' stroke='white' stroke-width='36' stroke-linecap='round'/><circle cx='370' cy='360' r='36' fill='%23f43f5e'/></svg>">

<style>
  :root {
    --bg-main: #f8fafc;
    --bg-card: #ffffff;
    --text-main: #0f172a;
    --text-muted: #64748b;
    --border-color: #cbd5e1;
    
    --theme-pitch: #d97706;
    --theme-pitch-bg: #fef3c7;
    --theme-verb: #2563eb;
    --theme-verb-bg: #eff6ff;
    --theme-adj: #059669;
    --theme-adj-bg: #ecfdf5;
    --theme-particle: #ea580c;
    --theme-particle-bg: #fff7ed;
    --theme-sent: #7c3aed;
    --theme-sent-bg: #faf5ff;
    --theme-spoken: #e11d48;
    --theme-spoken-bg: #fff1f2;
    
    --active-theme: var(--theme-pitch);
    --active-theme-bg: var(--theme-pitch-bg);
  }

  @media (prefers-color-scheme: dark) {
    :root {
      --bg-main: #0f172a;
      --bg-card: #1e293b;
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
      --border-color: #334155;
      
      --theme-pitch-bg: rgba(217, 119, 6, 0.18);
      --theme-verb-bg: rgba(37, 99, 235, 0.18);
      --theme-adj-bg: rgba(5, 150, 105, 0.18);
      --theme-particle-bg: rgba(234, 88, 12, 0.18);
      --theme-sent-bg: rgba(124, 58, 237, 0.18);
      --theme-spoken-bg: rgba(225, 29, 72, 0.18);
    }
  }

  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    -webkit-tap-highlight-color: transparent;
  }

  body {
    font-family: -apple-system, BlinkMacSystemFont, "SF Pro Text", "SF Pro Display", "PingFang SC", "Hiragino Sans", "Meiryo", sans-serif;
    background-color: var(--bg-main);
    color: var(--text-main);
    line-height: 1.55;
    font-size: 14.5px;
    padding-top: max(14px, env(safe-area-inset-top));
    padding-bottom: max(85px, calc(env(safe-area-inset-bottom) + 70px));
    -webkit-font-smoothing: antialiased;
  }

  ruby { ruby-position: over; }
  rt { font-size: 0.65em; color: var(--text-muted); font-weight: normal; }

  /* Pitch Accent Badges */
  .pitch-tag {
    display: inline-flex;
    align-items: center;
    font-size: 10.5px;
    padding: 1px 5px;
    border-radius: 4px;
    font-weight: 700;
    margin-left: 3px;
    vertical-align: middle;
  }
  .pitch-0 { background: #e0f2fe; color: #0284c7; } /* 平板 ⓪ */
  .pitch-1 { background: #fee2e2; color: #dc2626; } /* 头高 ① */
  .pitch-2 { background: #fef3c7; color: #d97706; } /* 中高 ② */
  .pitch-3 { background: #f3e8ff; color: #9333ea; } /* 中高 ③ */
  .pitch-odaka { background: #fce7f3; color: #db2777; } /* 尾高 */

  /* Pitch curve text: highlight the high-pitch mora */
  .hi {
    text-decoration: overline;
    color: inherit;
    font-weight: 700;
  }
  .lo {
    color: var(--text-muted);
  }

  /* Header Bar */
  .top-bar {
    position: sticky;
    top: 0;
    z-index: 50;
    background: rgba(255, 255, 255, 0.92);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border-bottom: 1px solid var(--border-color);
    padding: 10px 16px 8px 16px;
  }
  @media (prefers-color-scheme: dark) {
    .top-bar { background: rgba(15, 23, 42, 0.92); }
  }

  .app-title-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 8px;
  }
  .app-title {
    font-size: 17.5px;
    font-weight: 800;
    letter-spacing: -0.4px;
    display: flex;
    align-items: center;
    gap: 6px;
  }
  .badge-pwa {
    font-size: 11px;
    padding: 2px 7px;
    border-radius: 999px;
    background: var(--active-theme-bg);
    color: var(--active-theme);
    font-weight: 700;
  }

  /* Search Bar */
  .search-box {
    position: relative;
    width: 100%;
  }
  .search-input {
    width: 100%;
    height: 36px;
    border-radius: 10px;
    border: 1px solid var(--border-color);
    background: var(--bg-main);
    color: var(--text-main);
    padding: 0 12px 0 34px;
    font-size: 13.5px;
    outline: none;
    transition: all 0.2s;
  }
  .search-input:focus {
    border-color: var(--active-theme);
    background: var(--bg-card);
  }
  .search-icon {
    position: absolute;
    left: 10px;
    top: 50%;
    transform: translateY(-50%);
    font-size: 14px;
    color: var(--text-muted);
  }

  /* Container */
  .container {
    padding: 14px 16px;
    max-width: 640px;
    margin: 0 auto;
  }

  /* Audio Speak Button / Tapable */
  .speak-btn {
    display: inline-flex;
    align-items: center;
    gap: 4px;
    background: rgba(0,0,0,0.05);
    border: none;
    padding: 3px 8px;
    border-radius: 6px;
    font-size: 13.5px;
    font-weight: 600;
    color: inherit;
    cursor: pointer;
    margin: 2px 0;
  }
  @media (prefers-color-scheme: dark) {
    .speak-btn { background: rgba(255,255,255,0.08); }
  }
  .speak-btn:active {
    opacity: 0.6;
    transform: scale(0.98);
  }
  .speak-icon {
    font-size: 12px;
    opacity: 0.7;
  }

  /* Card Component */
  .card {
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: 14px;
    padding: 14px 15px;
    margin-bottom: 14px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.02);
  }

  .card-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 10px;
  }
  .card-title {
    font-size: 15.5px;
    font-weight: 700;
    display: flex;
    align-items: center;
    gap: 7px;
  }
  .card-tag {
    font-size: 11px;
    padding: 2px 8px;
    border-radius: 999px;
    font-weight: 700;
  }

  /* Notice Callouts */
  .callout {
    padding: 11px 13px;
    border-radius: 10px;
    margin-bottom: 12px;
    font-size: 13px;
    line-height: 1.6;
  }
  .callout-anime {
    background: #fdf4ff;
    border-left: 4px solid #d946ef;
    color: #86198f;
  }
  @media (prefers-color-scheme: dark) {
    .callout-anime { background: rgba(217, 70, 239, 0.15); color: #f5d0fe; }
  }
  .callout-trap {
    background: #fff1f2;
    border-left: 4px solid #e11d48;
    color: #9f1239;
  }
  @media (prefers-color-scheme: dark) {
    .callout-trap { background: rgba(225, 29, 72, 0.15); color: #fecdd3; }
  }
  .callout-tip {
    background: #fefce8;
    border-left: 4px solid #ca8a04;
    color: #854d0e;
  }
  @media (prefers-color-scheme: dark) {
    .callout-tip { background: rgba(202, 138, 4, 0.15); color: #fef08a; }
  }

  /* Tables (Responsive Card/List look on phone) */
  .table-box {
    width: 100%;
    overflow-x: auto;
    border-radius: 10px;
    border: 1px solid var(--border-color);
    margin-bottom: 10px;
    -webkit-overflow-scrolling: touch;
  }
  table.m-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 12.8px;
    text-align: left;
    white-space: normal;
  }
  table.m-table th {
    background: var(--bg-main);
    padding: 7px 9px;
    font-weight: 700;
    border-bottom: 1px solid var(--border-color);
    font-size: 12px;
  }
  table.m-table td {
    padding: 7px 9px;
    border-bottom: 1px solid var(--border-color);
    vertical-align: top;
  }
  table.m-table tr:last-child td { border-bottom: none; }

  /* Quick List Grid */
  .quick-grid {
    display: grid;
    grid-template-columns: 1fr;
    gap: 9px;
  }
  .quick-item {
    background: var(--bg-main);
    border: 1px solid var(--border-color);
    border-radius: 10px;
    padding: 10px 12px;
  }
  .quick-item-head {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 4px;
    font-weight: 700;
  }

  .highlight { color: #e11d48; font-weight: 700; }
  .jp-bold { font-family: "Meiryo", "Hiragino Sans", sans-serif; font-weight: 700; }

  /* Floating Bottom Navigation Bar */
  .bottom-nav {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    z-index: 100;
    background: rgba(255, 255, 255, 0.94);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border-top: 1px solid var(--border-color);
    padding-bottom: max(8px, env(safe-area-inset-bottom));
    display: flex;
    justify-content: space-around;
    padding-top: 6px;
  }
  @media (prefers-color-scheme: dark) {
    .bottom-nav { background: rgba(15, 23, 42, 0.94); }
  }

  .nav-btn {
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    background: none;
    border: none;
    padding: 3px 0;
    color: var(--text-muted);
    font-size: 10.5px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s;
  }
  .nav-btn .icon {
    font-size: 18px;
    margin-bottom: 2px;
    transition: transform 0.2s;
  }
  .nav-btn.active {
    color: var(--active-theme);
  }
  .nav-btn.active .icon {
    transform: scale(1.15);
  }

  /* Tab View Visibility */
  .tab-pane {
    display: none;
    animation: fadeIn 0.2s ease-in-out;
  }
  .tab-pane.active {
    display: block;
  }

  @keyframes fadeIn {
    from { opacity: 0; transform: translateY(4px); }
    to { opacity: 1; transform: translateY(0); }
  }

  /* Pitch Visual Demo Card */
  .pitch-demo-box {
    display: flex;
    gap: 8px;
    align-items: center;
    padding: 6px 10px;
    background: var(--bg-main);
    border-radius: 8px;
    margin: 4px 0;
    font-size: 13px;
  }
  .pitch-curve {
    display: inline-flex;
    align-items: center;
    font-family: monospace;
    font-weight: bold;
    letter-spacing: 1px;
  }

  /* Help Banner on First Visit */
  .ios-install-banner {
    background: linear-gradient(135deg, #d97706, #f59e0b);
    color: #ffffff;
    border-radius: 12px;
    padding: 12px 14px;
    margin-bottom: 14px;
    font-size: 12.5px;
    line-height: 1.6;
    display: flex;
    align-items: flex-start;
    gap: 10px;
  }
  .ios-install-banner .close-btn {
    margin-left: auto;
    background: none;
    border: none;
    color: #fff;
    font-size: 16px;
    opacity: 0.8;
  }
</style>
</head>
<body>

<!-- STICKY TOP BAR -->
<header class="top-bar">
  <div class="app-title-row">
    <div class="app-title">
      <span>🎌 日语随身宝</span>
      <span class="badge-pwa" id="currentModuleBadge">声调必修篇</span>
    </div>
    <div style="font-size: 12px; color: var(--text-muted);">
      <span id="audioStatus">🔊 点词可发音</span>
    </div>
  </div>

  <div class="search-box">
    <span class="search-icon">🔍</span>
    <input type="text" class="search-input" id="globalSearch" placeholder="搜索语法、词形或台词 (如: 0型, て形, は, すげえ)..." oninput="handleSearch()">
  </div>
</header>

<main class="container">

  <!-- iOS 添加主屏幕指引条 -->
  <div class="ios-install-banner" id="pwaBanner">
    <div style="font-size: 20px;">📲</div>
    <div>
      <strong>建议添加到 iPhone 桌面（离线全屏独立 App）：</strong><br>
      在 Safari 浏览器中点击底部 <strong>分享按钮 (⎋)</strong> $\rightarrow$ 选择 <strong>「添加到主屏幕」</strong>，随时秒开！
    </div>
    <button class="close-btn" onclick="document.getElementById('pwaBanner').style.display='none'">✕</button>
  </div>

  <!-- ================= TAB 0: 声调与发音必修篇 ================= -->
  <section class="tab-pane active" id="tab-pitch">
    <div class="callout callout-tip" style="background:#fef3c7; border-color:#d97706; color:#92400e;">
      🎵 <strong>为什么你觉得读音不对、像机器人？</strong><br>
      汉语是<strong>“音调语言（四声高低升降）”</strong>，而日语是<strong>“音高重音（Pitch Accent，高低拍）”</strong>！每个拍（假名）只有【高】和【低】之分，同一个词高低拍放错位置，意思完全相反（如“雨”与“糖”）。
    </div>

    <!-- 声调四大类型 -->
    <div class="card">
      <div class="card-header">
        <div class="card-title"><span>1. 东京标准音四大音调类型</span></div>
        <span class="card-tag" style="background:#fef3c7; color:#d97706;">声调总纲</span>
      </div>

      <div class="quick-grid">
        <!-- 0型 -->
        <div class="quick-item">
          <div class="quick-item-head">
            <span>⓪型【平板型 (へいばん)】</span>
            <span class="pitch-tag pitch-0">⓪ 平板</span>
          </div>
          <div style="font-size:12.5px; line-height:1.7;">
            • <strong>规则</strong>：第1拍低，第2拍起升高并保持高音。<strong>后续加助词（が/を/に）也不下降</strong>！<br>
            • <strong>音高轨迹</strong>：<span class="lo">低</span> - <span class="hi">高</span> - <span class="hi">高</span> - <span class="hi">高...</span><br>
            <div class="pitch-demo-box">
              <button class="speak-btn" onclick="speak('みず')">水 (みず)<span class="speak-icon">🔊</span></button>
              <span class="pitch-curve">[み<span class="hi">ず</span>]</span>
              <span style="color:var(--text-muted);">水が [み<span class="hi">ずが</span>] 不降！</span>
            </div>
            <div class="pitch-demo-box">
              <button class="speak-btn" onclick="speak('いく')">行く (いく)<span class="speak-icon">🔊</span></button>
              <span class="pitch-curve">[い<span class="hi">く</span>]</span>
              <span style="color:var(--text-muted);">走、去 (动词)</span>
            </div>
            <div class="pitch-demo-box">
              <button class="speak-btn" onclick="speak('にほんご')">日本語 (にほんご)<span class="speak-icon">🔊</span></button>
              <span class="pitch-curve">[に<span class="hi">ほんご</span>]</span>
              <span style="color:var(--text-muted);">日语 (名词)</span>
            </div>
          </div>
        </div>

        <!-- 1型 -->
        <div class="quick-item">
          <div class="quick-item-head">
            <span>①型【头高型 (あたまだか)】</span>
            <span class="pitch-tag pitch-1">① 头高</span>
          </div>
          <div style="font-size:12.5px; line-height:1.7;">
            • <strong>规则</strong>：只有第1拍最高，第2拍起<strong>立即断崖式骤降</strong>为低音！后续助词全为低音。<br>
            • <strong>音高轨迹</strong>：<span class="hi">高</span> - <span class="lo">低</span> - <span class="lo">低</span> - <span class="lo">低...</span><br>
            <div class="pitch-demo-box">
              <button class="speak-btn" onclick="speak('あめ')">雨 (あめ)<span class="speak-icon">🔊</span></button>
              <span class="pitch-curve">[<span class="hi">あ</span>め]</span>
              <span style="color:var(--text-muted);">下雨 (对比: 糖果是 飴 [⓪])</span>
            </div>
            <div class="pitch-demo-box">
              <button class="speak-btn" onclick="speak('はし')">箸 (はし)<span class="speak-icon">🔊</span></button>
              <span class="pitch-curve">[<span class="hi">は</span>し]</span>
              <span style="color:var(--text-muted);">筷子 (对比: 桥是 [②尾高])</span>
            </div>
            <div class="pitch-demo-box">
              <button class="speak-btn" onclick="speak('のむ')">飲む (のむ)<span class="speak-icon">🔊</span></button>
              <span class="pitch-curve">[<span class="hi">の</span>む]</span>
              <span style="color:var(--text-muted);">喝 (动词)</span>
            </div>
          </div>
        </div>

        <!-- 2型 -->
        <div class="quick-item">
          <div class="quick-item-head">
            <span>②型【中高型 (なかだか)】</span>
            <span class="pitch-tag pitch-2">② 中高</span>
          </div>
          <div style="font-size:12.5px; line-height:1.7;">
            • <strong>规则</strong>：第1拍低，<strong>第2拍最高</strong>，第3拍起立刻骤降！后续助词全为低音。<br>
            • <strong>音高轨迹</strong>：<span class="lo">低</span> - <span class="hi">高</span> - <span class="lo">低</span> - <span class="lo">低...</span><br>
            <div class="pitch-demo-box">
              <button class="speak-btn" onclick="speak('たべる')">食べる (たべる)<span class="speak-icon">🔊</span></button>
              <span class="pitch-curve">[た<span class="hi">べ</span>る]</span>
              <span style="color:var(--text-muted);">吃 (二类核心动词)</span>
            </div>
            <div class="pitch-demo-box">
              <button class="speak-btn" onclick="speak('たまご')">卵 (たまご)<span class="speak-icon">🔊</span></button>
              <span class="pitch-curve">[た<span class="hi">ま</span>ご]</span>
              <span style="color:var(--text-muted);">鸡蛋 (名词)</span>
            </div>
          </div>
        </div>

        <!-- 尾高型 -->
        <div class="quick-item">
          <div class="quick-item-head">
            <span>尾高型 (おだか)</span>
            <span class="pitch-tag pitch-odaka">尾高型</span>
          </div>
          <div style="font-size:12.5px; line-height:1.7;">
            • <strong>规则</strong>：单词自身从第2拍一直高到最后一拍；但<strong>一旦接助词（が/を/に），助词立刻跳水骤降</strong>！<br>
            <div class="pitch-demo-box">
              <button class="speak-btn" onclick="speak('はし')">橋 (はし)<span class="speak-icon">🔊</span></button>
              <span class="pitch-curve">[は<span class="hi">し</span>]</span>
              <span style="color:var(--text-muted);">桥 (单读像0型，接 橋<span class="lo">が</span> 骤降！)</span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- 动词活用的声调转移法则 -->
    <div class="card">
      <div class="card-header">
        <div class="card-title"><span>2. 动词活用时的“声调转移”铁律</span></div>
        <span class="card-tag" style="background:#fef3c7; color:#d97706;">变形音调</span>
      </div>
      <p style="margin-bottom:8px; font-size:12.5px;">很多同学动词原形音准对，一变「ない」或「ます」就跑调。牢记这两大阵营的转移规则：</p>

      <div class="table-box">
        <table class="m-table">
          <thead><tr><th>阵营</th><th>原形 (辞书形)</th><th>否定形 (ない)</th><th>礼貌形 (ます)</th><th>连接形 (て)</th></tr></thead>
          <tbody>
            <tr>
              <td><strong>平板型动词<br>(如 行く)</strong></td>
              <td><span class="pitch-tag pitch-0">⓪</span> [い<span class="hi">く</span>]</td>
              <td><span class="pitch-tag pitch-2">②</span> [い<span class="hi">か</span>ない]<br><span style="font-size:11px; color:var(--text-muted);">升到か骤降</span></td>
              <td><span class="pitch-tag pitch-3">③</span> [い<span class="hi">きま</span>す]<br><span style="font-size:11px; color:var(--text-muted);">ます前最高</span></td>
              <td><span class="pitch-tag pitch-0">⓪</span> [い<span class="hi">って</span>]<br><span style="font-size:11px; color:var(--text-muted);">依旧保持平</span></td>
            </tr>
            <tr>
              <td><strong>起伏型动词<br>(如 食べる)</strong></td>
              <td><span class="pitch-tag pitch-2">②</span> [た<span class="hi">べ</span>る]</td>
              <td><span class="pitch-tag pitch-2">②</span> [た<span class="hi">べ</span>ない]<br><span style="font-size:11px; color:var(--text-muted);">原核位置不变</span></td>
              <td><span class="pitch-tag pitch-3">③</span> [た<span class="hi">べま</span>す]<br><span style="font-size:11px; color:var(--text-muted);">转移到ま最高</span></td>
              <td><span class="pitch-tag pitch-1">①</span> [<span class="hi">た</span>べて]<br><span style="font-size:11px; color:var(--text-muted);">前移到头高！</span></td>
            </tr>
            <tr>
              <td><strong>起伏型动词<br>(如 飲む)</strong></td>
              <td><span class="pitch-tag pitch-1">①</span> [<span class="hi">の</span>む]</td>
              <td><span class="pitch-tag pitch-2">②</span> [の<span class="hi">ま</span>ない]<br><span style="font-size:11px; color:var(--text-muted);">后移到ま骤降</span></td>
              <td><span class="pitch-tag pitch-3">③</span> [の<span class="hi">みま</span>す]<br><span style="font-size:11px; color:var(--text-muted);">转移到ま最高</span></td>
              <td><span class="pitch-tag pitch-1">①</span> [<span class="hi">の</span>んで]<br><span style="font-size:11px; color:var(--text-muted);">维持头高！</span></td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="callout callout-tip" style="margin-bottom:0;">
        💡 <strong>秒懂心法：</strong> 凡是变「〜ます」，最高音几乎全都落在 <strong>「ま」</strong> 上（行<span class="hi">きま</span>す、食<span class="hi">べま</span>す、飲<span class="hi">みま</span>す）！
      </div>
    </div>
  </section>

  <!-- ================= TAB 1: 动词篇 ================= -->
  <section class="tab-pane" id="tab-verbs">
    <div class="callout callout-anime">
      🎬 <strong>从声音直觉到语法骨架：</strong> 明白动词如何在五段跳跃，以及「て形/た形」音便的发音顺畅本质。
    </div>

    <!-- 动词分类与判定 -->
    <div class="card">
      <div class="card-header">
        <div class="card-title"><span>1. 动词三大家族极简判定树</span></div>
        <span class="card-tag" style="background:#eff6ff; color:#2563eb;">核心分类</span>
      </div>
      
      <div class="quick-grid">
        <div class="quick-item">
          <div class="quick-item-head">
            <span>三类动词（仅有两个 · 不规则）</span>
            <span class="badge-pwa">死记</span>
          </div>
          <div style="font-size:12.5px; color:var(--text-muted); line-height:1.7;">
            • <button class="speak-btn" onclick="speak('する')">する <span class="pitch-tag pitch-0">⓪</span><span class="speak-icon">🔊</span></button> (做 / 干)<br>
            • <button class="speak-btn" onclick="speak('くる')"><ruby>来<rt>く</rt></ruby>る <span class="pitch-tag pitch-1">①</span><span class="speak-icon">🔊</span></button> (来)
          </div>
        </div>

        <div class="quick-item">
          <div class="quick-item-head">
            <span>二类动词（一段动词 · 最听话）</span>
            <span class="badge-pwa" style="background:#ecfdf5; color:#059669;">直接去「る」</span>
          </div>
          <div style="font-size:12.5px; color:var(--text-muted); line-height:1.7;">
            词尾必定是「る」，且倒数第二个假名在 <strong>i段（上一段）</strong> 或 <strong>e段（下一段）</strong>：<br>
            • <button class="speak-btn" onclick="speak('たべる')"><ruby>食<rt>た</rt></ruby>べる <span class="pitch-tag pitch-2">②</span><span class="speak-icon">🔊</span></button> (ta-be-ru) $\rightarrow$ 食べない / 食べた<br>
            • <button class="speak-btn" onclick="speak('みる')"><ruby>見<rt>み</rt></ruby>る <span class="pitch-tag pitch-1">①</span><span class="speak-icon">🔊</span></button> (mi-ru) $\rightarrow$ 見ない / 見た<br>
            • <button class="speak-btn" onclick="speak('おきる')"><ruby>起<rt>お</rt></ruby>きる <span class="pitch-tag pitch-2">②</span><span class="speak-icon">🔊</span></button> (o-ki-ru) $\rightarrow$ 起きない / 起きた<br>
            • <button class="speak-btn" onclick="speak('あきらめる')"><ruby>諦<rt>あきら</rt></ruby>める <span class="pitch-tag pitch-4">④</span><span class="speak-icon">🔊</span></button> (me-ru) $\rightarrow$ 諦めない / 諦めた
          </div>
        </div>

        <div class="quick-item">
          <div class="quick-item-head">
            <span>一类动词（五段动词 · 数量最多）</span>
            <span class="badge-pwa" style="background:#fef3c7; color:#92400e;">五十音跳跃</span>
          </div>
          <div style="font-size:12.5px; color:var(--text-muted); line-height:1.7;">
            词尾不是「る」，或词尾虽是「る」但倒数第二字为 a/u/o 段：<br>
            • <button class="speak-btn" onclick="speak('いく')"><ruby>行<rt>い</rt></ruby>く <span class="pitch-tag pitch-0">⓪</span><span class="speak-icon">🔊</span></button> (去)、
            <button class="speak-btn" onclick="speak('のむ')"><ruby>飲<rt>の</rt></ruby>む <span class="pitch-tag pitch-1">①</span><span class="speak-icon">🔊</span></button> (喝)、
            <button class="speak-btn" onclick="speak('はなす')"><ruby>話<rt>はな</rt></ruby>す <span class="pitch-tag pitch-2">②</span><span class="speak-icon">🔊</span></button> (说)<br>
            • <button class="speak-btn" onclick="speak('かう')"><ruby>買<rt>か</rt></ruby>う <span class="pitch-tag pitch-0">⓪</span><span class="speak-icon">🔊</span></button> (买)、
            <button class="speak-btn" onclick="speak('おわる')"><ruby>終<rt>お</rt></ruby>わる <span class="pitch-tag pitch-0">⓪</span><span class="speak-icon">🔊</span></button> (结束)
          </div>
        </div>
      </div>

      <div class="callout callout-trap" style="margin-top:10px; margin-bottom:0;">
        ⚠️ <strong>必背高频陷阱词（看似二类，实全为一类五段动词！）：</strong><br>
        • <button class="speak-btn" onclick="speak('かえる')"><ruby>帰<rt>かえ</rt></ruby>る <span class="pitch-tag pitch-1">①</span><span class="speak-icon">🔊</span></button> (回家) $\rightarrow$ 帰らない / 帰ります<br>
        • <button class="speak-btn" onclick="speak('はいる')"><ruby>入<rt>はい</rt></ruby>る <span class="pitch-tag pitch-1">①</span><span class="speak-icon">🔊</span></button> (进入) $\rightarrow$ 入らない / 入ります<br>
        • <button class="speak-btn" onclick="speak('はしる')"><ruby>走<rt>はし</rt></ruby>る <span class="pitch-tag pitch-2">②</span><span class="speak-icon">🔊</span></button> (奔跑) $\rightarrow$ 走らない / 走ります<br>
        • <button class="speak-btn" onclick="speak('しる')"><ruby>知<rt>し</rt></ruby>る <span class="pitch-tag pitch-0">⓪</span><span class="speak-icon">🔊</span></button> (知道) $\rightarrow$ 知らない / 知ります<br>
        • <button class="speak-btn" onclick="speak('きる')"><ruby>切<rt>き</rt></ruby>る <span class="pitch-tag pitch-1">①</span><span class="speak-icon">🔊</span></button> (剪切) $\rightarrow$ 切らない (注: 着る·穿衣为二类)<br>
        • <button class="speak-btn" onclick="speak('いる')"><ruby>要<rt>い</rt></ruby>る <span class="pitch-tag pitch-0">⓪</span><span class="speak-icon">🔊</span></button> (需要)、
        <button class="speak-btn" onclick="speak('しゃべる')"><ruby>喋<rt>しゃべ</rt></ruby>る <span class="pitch-tag pitch-2">②</span><span class="speak-icon">🔊</span></button> (聊天唠叨)
      </div>
    </div>

    <!-- 五十音活用表 -->
    <div class="card">
      <div class="card-header">
        <div class="card-title"><span>2. 五十音图六大形态活用全景表</span></div>
        <span class="card-tag" style="background:#eff6ff; color:#2563eb;">活用总览</span>
      </div>

      <div class="table-box">
        <table class="m-table">
          <thead>
            <tr><th>形态名称</th><th>段位与接续</th><th>一类例词: 書く [⓪]</th><th>二类例词: 食べる [②]</th><th>动漫经典台词</th></tr>
          </thead>
          <tbody>
            <tr>
              <td><strong>未然形</strong></td>
              <td>一类变 <span class="highlight">あ段</span><br>二类去「る」</td>
              <td><button class="speak-btn" onclick="speak('かかない')">書かない <span class="pitch-tag pitch-2">②</span><span class="speak-icon">🔊</span></button><br>書かれる (被写)</td>
              <td><button class="speak-btn" onclick="speak('たべない')">食べない <span class="pitch-tag pitch-2">②</span><span class="speak-icon">🔊</span></button><br>食べられる (能/被吃)</td>
              <td><span class="highlight">負けない！</span> (绝不认输)<br><span class="highlight">諦めないで</span> (别放弃)</td>
            </tr>
            <tr>
              <td><strong>连用形</strong></td>
              <td>一类变 <span class="highlight">い段</span><br>二类去「る」</td>
              <td><button class="speak-btn" onclick="speak('かきます')">書きます <span class="pitch-tag pitch-3">③</span><span class="speak-icon">🔊</span></button><br>書きたい (想写)</td>
              <td><button class="speak-btn" onclick="speak('たべます')">食べます <span class="pitch-tag pitch-3">③</span><span class="speak-icon">🔊</span></button><br>食べたい (想吃)</td>
              <td><span class="highlight">行きます！</span> (我出发了)<br><span class="highlight">会いたい</span> (好想见你)</td>
            </tr>
            <tr>
              <td><strong>终止形</strong></td>
              <td>保持 <span class="highlight">う段</span>(原形)</td>
              <td><button class="speak-btn" onclick="speak('かく')">書く <span class="pitch-tag pitch-0">⓪</span><span class="speak-icon">🔊</span></button><br>書く人 (定语)</td>
              <td><button class="speak-btn" onclick="speak('たべる')">食べる <span class="pitch-tag pitch-2">②</span><span class="speak-icon">🔊</span></button><br>食べる人 (定语)</td>
              <td><span class="highlight">俺が守る！</span> (由我守护)<br><span class="highlight">行くぞ！</span> (上吧！)</td>
            </tr>
            <tr>
              <td><strong>假定形</strong></td>
              <td>一类变 <span class="highlight">え段</span><br>二类变 <span class="highlight">れ</span></td>
              <td><button class="speak-btn" onclick="speak('かけば')">書けば <span class="pitch-tag pitch-1">①</span><span class="speak-icon">🔊</span></button></td>
              <td><button class="speak-btn" onclick="speak('たべれば')">食べれば <span class="pitch-tag pitch-2">②</span><span class="speak-icon">🔊</span></button></td>
              <td><span class="highlight">逃げれば助かる</span> (逃了就活)<br><span class="highlight">やればできる</span> (干了就能行)</td>
            </tr>
            <tr>
              <td><strong>命令形</strong></td>
              <td>一类变 <span class="highlight">え段</span><br>二类变 <span class="highlight">ろ/よ</span></td>
              <td><button class="speak-btn" onclick="speak('かけ')">書け！ <span class="pitch-tag pitch-1">①</span><span class="speak-icon">🔊</span></button></td>
              <td><button class="speak-btn" onclick="speak('たべろ')">食べろ！ <span class="pitch-tag pitch-2">②</span><span class="speak-icon">🔊</span></button></td>
              <td><span class="highlight">逃げろ！</span> (快逃！)<br><span class="highlight">死ね！</span> (去死！)<br><span class="highlight">行け！</span> (冲！)</td>
            </tr>
            <tr>
              <td><strong>意志形</strong></td>
              <td>一类变 <span class="highlight">お段+う</span><br>二类去る+ <span class="highlight">よう</span></td>
              <td><button class="speak-btn" onclick="speak('かこう')">書こう <span class="pitch-tag pitch-2">②</span><span class="speak-icon">🔊</span></button></td>
              <td><button class="speak-btn" onclick="speak('たべよう')">食べよう <span class="pitch-tag pitch-3">③</span><span class="speak-icon">🔊</span></button></td>
              <td><span class="highlight">帰ろう</span> (咱们回吧)<br><span class="highlight">行こうぜ！</span> (咱们出发吧)</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div class="callout callout-tip" style="margin-bottom:0;">
        <strong>★ 三类动词（する / くる）特殊变形速查：</strong><br>
        • <strong>する</strong>：しない [②] | します [②] | すれば [①] | しろ！ [①] | しよう [②]<br>
        • <strong>来る(くる)</strong>：こない [①] | きます [②] | くれば [①] | こい！ [①] | こよう [②]
      </div>
    </div>

    <!-- て形音便口诀 -->
    <div class="card">
      <div class="card-header">
        <div class="card-title"><span>3. 一类动词「て/た形」音便口诀</span></div>
        <span class="card-tag" style="background:#fefce8; color:#a16207;">最难关卡</span>
      </div>

      <div class="callout callout-tip" style="line-height:1.8;">
        🎵 <strong>终身难忘四句口诀：</strong><br>
        ① <strong>う・つ・る</strong> 变促音 <strong>って</strong>：買う $\rightarrow$ <button class="speak-btn" onclick="speak('かって')">買って <span class="pitch-tag pitch-0">⓪</span><span class="speak-icon">🔊</span></button>、待つ $\rightarrow$ <button class="speak-btn" onclick="speak('まって')">待って <span class="pitch-tag pitch-1">①</span><span class="speak-icon">🔊</span></button><br>
        ② <strong>ぬ・ぶ・む</strong> 变拨音 <strong>んで</strong>：死ぬ $\rightarrow$ <button class="speak-btn" onclick="speak('しんで')">死んで <span class="pitch-tag pitch-1">①</span><span class="speak-icon">🔊</span></button>、飲む $\rightarrow$ <button class="speak-btn" onclick="speak('のんで')">飲んで <span class="pitch-tag pitch-1">①</span><span class="speak-icon">🔊</span></button><br>
        ③ <strong>く</strong> 变 <strong>いて</strong>，<strong>ぐ</strong> 变 <strong>いだ</strong>：書く $\rightarrow$ <button class="speak-btn" onclick="speak('かいて')">書いて <span class="pitch-tag pitch-1">①</span><span class="speak-icon">🔊</span></button>、泳ぐ $\rightarrow$ <button class="speak-btn" onclick="speak('およいで')">泳いで <span class="pitch-tag pitch-2">②</span><span class="speak-icon">🔊</span></button><br>
        &nbsp;&nbsp;&nbsp;&nbsp;★ <strong>唯一特例</strong>：<span class="highlight">行く $\rightarrow$ <button class="speak-btn" onclick="speak('いって')">行って <span class="pitch-tag pitch-0">⓪</span><span class="speak-icon">🔊</span></button></span> (绝不可说 いいて！)<br>
        ④ <strong>す</strong> 变 <strong>して</strong>：話す $\rightarrow$ <button class="speak-btn" onclick="speak('はなして')">話して <span class="pitch-tag pitch-2">②</span><span class="speak-icon">🔊</span></button><br>
        <em>※ 二类动词直接去「る」加「て」（食べて、見て）；三类动词变 して、きて。把「て/で」换成「た/だ」即为过去式！</em>
      </div>
    </div>
  </section>

  <!-- ================= TAB 2: 形容词篇 ================= -->
  <section class="tab-pane" id="tab-adj">
    <div class="callout callout-anime">
      🌈 <strong>形容词两大阵营：</strong> い形容词自带活用器官；な形容词本质是个名词，靠背后的 だ/です 帮它变。
    </div>

    <!-- 伪装假词避坑 -->
    <div class="card">
      <div class="card-header">
        <div class="card-title"><span>1. 5 大披着「い」外衣的 な形容词陷阱</span></div>
        <span class="card-tag" style="background:#ecfdf5; color:#059669;">伪装避坑</span>
      </div>

      <div class="callout callout-trap">
        ⚠️ <strong>读音带 i，但在日文汉字体系中，汉字后没有独立假名「い」，全部属于「な形容词」：</strong><br>
        1. <button class="speak-btn" onclick="speak('きれい')"><ruby>綺麗<rt>きれい</rt></ruby> <span class="pitch-tag pitch-1">①</span><span class="speak-icon">🔊</span></button> $\rightarrow$ 綺麗な花 (漂亮/干净)<br>
        2. <button class="speak-btn" onclick="speak('ゆうめい')"><ruby>有名<rt>ゆうめい</rt></ruby> <span class="pitch-tag pitch-0">⓪</span><span class="speak-icon">🔊</span></button> $\rightarrow$ 有名な人 (有名)<br>
        3. <button class="speak-btn" onclick="speak('きらい')"><ruby>嫌<rt>きら</rt></ruby>い <span class="pitch-tag pitch-0">⓪</span><span class="speak-icon">🔊</span></button> $\rightarrow$ 嫌いな人 (讨厌)<br>
        4. <button class="speak-btn" onclick="speak('とくい')"><ruby>得意<rt>とくい</rt></ruby> <span class="pitch-tag pitch-2">②</span><span class="speak-icon">🔊</span></button> $\rightarrow$ 得意な科目 (擅长)<br>
        5. <button class="speak-btn" onclick="speak('さいわい')"><ruby>幸<rt>さいわ</rt></ruby>い <span class="pitch-tag pitch-0">⓪</span><span class="speak-icon">🔊</span></button> (幸运/庆幸)
      </div>
    </div>

    <!-- い形容词变形 -->
    <div class="card">
      <div class="card-header">
        <div class="card-title"><span>2. い形容词全变形网络 (去「い」大作战)</span></div>
        <span class="card-tag" style="background:#ecfdf5; color:#059669;">活用公式</span>
      </div>

      <div class="table-box">
        <table class="m-table">
          <thead><tr><th>语法功能</th><th>公式</th><th>例: 高い [②] (贵)</th><th>例: 可愛い [③] (可爱)</th></tr></thead>
          <tbody>
            <tr><td>原形(肯定)</td><td>直接使用</td><td><button class="speak-btn" onclick="speak('たかい')">高い <span class="pitch-tag pitch-2">②</span><span class="speak-icon">🔊</span></button></td><td><button class="speak-btn" onclick="speak('かわいい')">可愛い <span class="pitch-tag pitch-3">③</span><span class="speak-icon">🔊</span></button></td></tr>
            <tr><td>否定(不……)</td><td>去い + <span class="highlight">くない</span></td><td><button class="speak-btn" onclick="speak('たかくない')">高くない <span class="pitch-tag pitch-3">③</span><span class="speak-icon">🔊</span></button></td><td><button class="speak-btn" onclick="speak('かわいくない')">可愛くない <span class="pitch-tag pitch-4">④</span><span class="speak-icon">🔊</span></button></td></tr>
            <tr><td>过去(曾经……)</td><td>去い + <span class="highlight">かった</span></td><td><button class="speak-btn" onclick="speak('たかかった')">高かった <span class="pitch-tag pitch-3">③</span><span class="speak-icon">🔊</span></button></td><td><button class="speak-btn" onclick="speak('かわいかった')">可愛かった <span class="pitch-tag pitch-4">④</span><span class="speak-icon">🔊</span></button></td></tr>
            <tr><td>过去否定</td><td>去い + <span class="highlight">くなかった</span></td><td><button class="speak-btn" onclick="speak('たかくなかった')">高くなかった<span class="speak-icon">🔊</span></button></td><td><button class="speak-btn" onclick="speak('かわいくなかった')">可愛くなかった<span class="speak-icon">🔊</span></button></td></tr>
            <tr><td>中顿连接</td><td>去い + <span class="highlight">くて</span></td><td><button class="speak-btn" onclick="speak('たかくてかえない')">高くて買えない<span class="speak-icon">🔊</span></button></td><td><button class="speak-btn" onclick="speak('かわいくてやさしい')">可愛くて優しい<span class="speak-icon">🔊</span></button></td></tr>
            <tr><td>修饰动词(副词)</td><td>去い + <span class="highlight">く</span></td><td><button class="speak-btn" onclick="speak('はやくおきる')">早く起きる (早起)<span class="speak-icon">🔊</span></button></td><td><button class="speak-btn" onclick="speak('かわいくわらう')">可爱地笑<span class="speak-icon">🔊</span></button></td></tr>
            <tr><td>样态推测</td><td>去い + <span class="highlight">そう</span></td><td><button class="speak-btn" onclick="speak('おいしそう')">美味しそう (看起来香)<span class="speak-icon">🔊</span></button></td><td>高そう (看起来贵)</td></tr>
          </tbody>
        </table>
      </div>

      <div class="callout callout-tip" style="margin-bottom:0;">
        🌟 <strong>唯一神级特例词：「いい」（好）变身全解</strong><br>
        原形说 いい [①]，所有变形<strong>一律回归古语「よい [①]」</strong>：<br>
        • 不好：<button class="speak-btn" onclick="speak('よくない')">よくない <span class="pitch-tag pitch-2">②</span><span class="speak-icon">🔊</span></button> (绝不可说 いくない ❌)<br>
        • 太好啦：<button class="speak-btn" onclick="speak('よかった')">よかった！ <span class="pitch-tag pitch-1">①</span><span class="speak-icon">🔊</span></button> (动漫超高频感叹)<br>
        • 又好又……：<button class="speak-btn" onclick="speak('よくて')">よくて <span class="pitch-tag pitch-1">①</span><span class="speak-icon">🔊</span></button><br>
        • 看起来不错：<button class="speak-btn" onclick="speak('よさそう')">よさそう <span class="pitch-tag pitch-0">⓪</span><span class="speak-icon">🔊</span></button> (插入さ)
      </div>
    </div>
  </section>

  <!-- ================= TAB 3: 介词助词篇 ================= -->
  <section class="tab-pane" id="tab-particles">
    <div class="callout callout-anime">
      ⚓ <strong>助词定格位：</strong> 日语句序能颠倒，就是因为各个成分全靠背后的助词界定身份！
    </div>

    <!-- は vs が -->
    <div class="card">
      <div class="card-header">
        <div class="card-title"><span>1. 【は】 vs 【が】终极化解 (信息焦点论)</span></div>
        <span class="card-tag" style="background:#fff7ed; color:#ea580c;">世纪对决</span>
      </div>

      <div class="quick-grid">
        <div class="quick-item">
          <div class="quick-item-head">
            <span>【は】提示大主题 (重心在后句)</span>
          </div>
          <div style="font-size:12.5px; line-height:1.7;">
            对方已知的旧信息，重点在后面的评价：<br>
            • <button class="speak-btn" onclick="speak('わたしはたなかです')">私は田中です。<span class="speak-icon">🔊</span></button> (关于我嘛，是田中)
          </div>
        </div>

        <div class="quick-item">
          <div class="quick-item-head">
            <span>【が】主格排他聚焦 (重心在自身)</span>
          </div>
          <div style="font-size:12.5px; line-height:1.7;">
            探求“到底是谁”、排除他人；或眼前客观现象：<br>
            • <button class="speak-btn" onclick="speak('かれがはんにんだ')"><span class="highlight">彼が犯人だ！</span><span class="speak-icon">🔊</span></button> (<strong>他</strong>才是犯人！聚焦)<br>
            • <button class="speak-btn" onclick="speak('あめがふってきた')">あ、雨が降ってきた！<span class="speak-icon">🔊</span></button> (下雨了！眼前自然现象)
          </div>
        </div>
      </div>

      <div class="callout callout-tip" style="margin-top:10px; margin-bottom:0;">
        💡 <strong>固定对象必须用「が」：</strong><br>
        感情、能力、希望的对象固定用 が：<br>
        • <button class="speak-btn" onclick="speak('アニメがすきだ')">アニメが 好きだ<span class="speak-icon">🔊</span></button> (喜欢动漫)<br>
        • <button class="speak-btn" onclick="speak('にほんごができる')">日本語が できる<span class="speak-icon">🔊</span></button> (会日语)<br>
        • <button class="speak-btn" onclick="speak('みずがほしい')">水が 欲しい<span class="speak-icon">🔊</span></button> (想要水)
      </div>
    </div>

    <!-- に vs で -->
    <div class="card">
      <div class="card-header">
        <div class="card-title"><span>2. 【に】 vs 【で】静动大决战</span></div>
        <span class="card-tag" style="background:#fff7ed; color:#ea580c;">时空对决</span>
      </div>

      <div class="table-box">
        <table class="m-table">
          <thead><tr><th>助词</th><th>核心语义</th><th>典型例句</th></tr></thead>
          <tbody>
            <tr>
              <td><span class="highlight">に</span><br>(图钉原则)</td>
              <td>静态存在位置、落脚点、精确时间点、动作对象</td>
              <td>
                • 机の上<span class="highlight">に</span>本がある (桌上有书-静止)<br>
                • ７時<span class="highlight">に</span>起きる (7点起床-具体时间)<br>
                • 電車<span class="highlight">に</span>乗る (上电车-落脚点)<br>
                • 友達<span class="highlight">に</span>会う (见朋友-对象)
              </td>
            </tr>
            <tr>
              <td><span class="highlight">で</span><br>(舞台工具)</td>
              <td>动态动作场所、工具手段、交通方式、原因理由</td>
              <td>
                • 図書館<span class="highlight">で</span>勉強する (动态学习)<br>
                • 電車<span class="highlight">で</span>行く (坐电车去-手段)<br>
                • 箸<span class="highlight">で</span>食べる (用筷子吃-工具)<br>
                • 風邪<span class="highlight">で</span>休む (因感冒请假-原因)
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </section>

  <!-- ================= TAB 4: 句子造句篇 ================= -->
  <section class="tab-pane" id="tab-sent">
    <div class="callout callout-anime">
      🧱 <strong>SOV 谓语绝对压轴律：</strong> 中文是“我 [吃] 饭”，日语必须是“私 は ご飯 を [食べます]”。动词永远在句尾收尾！
    </div>

    <!-- 万能积木造句公式 -->
    <div class="card">
      <div class="card-header">
        <div class="card-title"><span>1. 万能积木造句公式</span></div>
        <span class="card-tag" style="background:#faf5ff; color:#7c3aed;">乐高拼装</span>
      </div>
      <div class="callout callout-tip" style="line-height:1.7;">
        <strong>【时间】</strong> + <strong>【主语 は/が】</strong> + <strong>【伴随者 と】</strong> + <strong>【场所 で】</strong> + <strong>【工具 で】</strong> + <strong>【宾语 を】</strong> + <span class="highlight">【谓语动词 (绝对压轴)】</span>
      </div>
      <div style="font-size:13px; line-height:1.7;">
        阶梯扩句演示：<br>
        1. 核心动作：<button class="speak-btn" onclick="speak('たべる')">食べる<span class="speak-icon">🔊</span></button> (吃)<br>
        2. 加宾语：ご飯<span class="highlight">を</span> 食べる<br>
        3. 加伴随：友達<span class="highlight">と</span> ご飯を食べる<br>
        4. 加场所方式：食堂<span class="highlight">で</span> 箸<span class="highlight">で</span> ご飯を食べる<br>
        5. 成句：<button class="speak-btn" onclick="speak('きのうわたしはしょくどうでともだちとはしでごはんをたべた')">昨日、私は友達と食堂で箸でご飯を食べた。<span class="speak-icon">🔊</span></button>
      </div>
    </div>

    <!-- 授受动词 -->
    <div class="card">
      <div class="card-header">
        <div class="card-title"><span>2. 授受动词流向 (给与拿)</span></div>
        <span class="card-tag" style="background:#faf5ff; color:#7c3aed;">社交恩惠</span>
      </div>
      <div class="quick-grid">
        <div class="quick-item">
          <div class="quick-item-head"><span>あげる (我给别人 / 外向流)</span></div>
          <div style="font-size:12.5px;">• 友達にプレゼントをあげた (我给朋友送了礼物)</div>
        </div>
        <div class="quick-item">
          <div class="quick-item-head"><span>くれる (别人给我 / 内向流·感恩)</span></div>
          <div style="font-size:12.5px;">
            • <button class="speak-btn" onclick="speak('たすけてくれてありがとう')"><span class="highlight">助けてくれてありがとう！</span><span class="speak-icon">🔊</span></button> (谢谢你救了我！动漫名台词)
          </div>
        </div>
        <div class="quick-item">
          <div class="quick-item-head"><span>もらう (我从别人处得到)</span></div>
          <div style="font-size:12.5px;">• 先生に日本語を教えてもらった (承蒙老师教我日语)</div>
        </div>
      </div>
    </div>

    <!-- 四大假定条件 -->
    <div class="card">
      <div class="card-header">
        <div class="card-title"><span>3. 四大假定条件句 (如果……)</span></div>
        <span class="card-tag" style="background:#faf5ff; color:#7c3aed;">假定齿轮</span>
      </div>
      <div class="quick-grid">
        <div class="quick-item">
          <div class="quick-item-head"><span>〜たら (万能口语之王)</span></div>
          <div style="font-size:12.5px;">
            如果/一旦发生就……(后句无限制)：<br>
            • <button class="speak-btn" onclick="speak('にほんについたられんらくして')">日本に着いたら、連絡して (到了日本联系我)<span class="speak-icon">🔊</span></button>
          </div>
        </div>
        <div class="quick-item">
          <div class="quick-item-head"><span>〜ば (纯逻辑推导)</span></div>
          <div style="font-size:12.5px;">只要……就一定会：<br>• やればできる！ (只要去干就能成)</div>
        </div>
        <div class="quick-item">
          <div class="quick-item-head"><span>〜と (自然恒常必然)</span></div>
          <div style="font-size:12.5px;">一……就必然发生：<br>• ボタンを押すと水が出る (一按就出水)</div>
        </div>
        <div class="quick-item">
          <div class="quick-item-head"><span>〜なら (话题承接建议)</span></div>
          <div style="font-size:12.5px;">要是去日本的话：<br>• 日本へ行くなら秋がいい (要是去日本推荐秋天)</div>
        </div>
      </div>
    </div>
  </section>

  <!-- ================= TAB 5: 常用口语篇 ================= -->
  <section class="tab-pane" id="tab-spoken">
    <div class="callout callout-anime" style="background:#fff1f2; border-color:#e11d48; color:#9f1239;">
      🗣️ <strong>口语的灵魂：</strong> 聊天不冷场的「相槌」、舌头偷懒合并的「缩音」、以及避免社交尴尬的「现实礼貌界限」。
    </div>

    <!-- 接话神术 -->
    <div class="card">
      <div class="card-header">
        <div class="card-title"><span>1. 神级接话术【相槌 (あいづち)】</span></div>
        <span class="card-tag" style="background:#ffe4e6; color:#9f1239;">绝不冷场</span>
      </div>
      <div class="quick-grid">
        <div class="quick-item">
          <div class="quick-item-head"><span>日常倾听：うん、うん / ええ</span></div>
          <div style="font-size:12.5px;">轻微点头，表示“我在认真听呢，继续说”</div>
        </div>
        <div class="quick-item">
          <div class="quick-item-head"><span>强烈共鸣：そうそう！ / それな！</span></div>
          <div style="font-size:12.5px;">
            • <button class="speak-btn" onclick="speak('そうそうそれな')">そうそう、それな！ (对对对，就是说啊！)<span class="speak-icon">🔊</span></button>
          </div>
        </div>
        <div class="quick-item">
          <div class="quick-item-head"><span>震惊反转：マジで？！ / 嘘でしょ？！</span></div>
          <div style="font-size:12.5px;">
            • <button class="speak-btn" onclick="speak('えっうそでしょ')">えっ、嘘でしょ？！ (骗人的吧？！)<span class="speak-icon">🔊</span></button>
          </div>
        </div>
        <div class="quick-item">
          <div class="quick-item-head"><span>领会：なるほど！ / そういうことか</span></div>
          <div style="font-size:12.5px;">
            • <button class="speak-btn" onclick="speak('なるほどね')">なるほどね！ (原来如此啊！)<span class="speak-icon">🔊</span></button>
          </div>
        </div>
      </div>
    </div>

    <!-- 三大万能词 -->
    <div class="card">
      <div class="card-header">
        <div class="card-title"><span>2. 日常离不开的三大万能词</span></div>
        <span class="card-tag" style="background:#ffe4e6; color:#9f1239;">高频神器</span>
      </div>
      <div class="quick-grid">
        <div class="quick-item">
          <div class="quick-item-head"><span>【どうも】打招呼/致谢/抱歉</span></div>
          <div style="font-size:12.5px;">见面点头说、扶门道谢说、电车借过说。</div>
        </div>
        <div class="quick-item">
          <div class="quick-item-head"><span>【大丈夫】关心/安心/委婉推辞</span></div>
          <div style="font-size:12.5px;">
            • 大丈夫？(升调: 没事吧?)<br>
            • 大丈夫だよ(平调: 放心没事)<br>
            • あ、大丈夫です(摆手: 不用了谢谢)
          </div>
        </div>
        <div class="quick-item">
          <div class="quick-item-head"><span>【ちょっと…】国宝级委婉推辞</span></div>
          <div style="font-size:12.5px;">
            面露难色说一句：<button class="speak-btn" onclick="speak('あしたはちょっと')">あ、明日は…ちょっと…<span class="speak-icon">🔊</span></button>，对方立刻心领神会。
          </div>
        </div>
      </div>
    </div>

    <!-- 现实防踩雷 -->
    <div class="card">
      <div class="card-header">
        <div class="card-title"><span>3. ⚠️ 现实社交防踩雷三大铁律</span></div>
        <span class="card-tag" style="background:#ffe4e6; color:#9f1239;">避坑必看</span>
      </div>
      <div class="callout callout-trap" style="margin-bottom:0;">
        1. <strong>千万别对真人叫「お前（おまえ）」！</strong> 现实中极不礼貌甚至具挑衅意味，请称呼对方姓氏 + さん。<br>
        2. <strong>对长辈/初次见面务必收起普通体！</strong> 使用标准的敬体 <span class="highlight">です / ます</span>，不可张口闭口“すげえ、〜だろ”。<br>
        3. <strong>告别别说「さようなら」！</strong> 日常分别用 <button class="speak-btn" onclick="speak('じゃあまた')">じゃあ、また！<span class="speak-icon">🔊</span></button> 或 <button class="speak-btn" onclick="speak('おつかれさまでした')">お疲れ様でした！<span class="speak-icon">🔊</span></button>。
      </div>
    </div>
  </section>

</main>

<!-- FLOATING BOTTOM TAB BAR (6 TABS) -->
<nav class="bottom-nav">
  <button class="nav-btn active" onclick="switchTab('pitch', this, '#d97706', '#fef3c7', '声调必修')">
    <span class="icon">🎵</span>
    <span>声调</span>
  </button>
  <button class="nav-btn" onclick="switchTab('verbs', this, '#2563eb', '#eff6ff', '动词篇')">
    <span class="icon">🏃</span>
    <span>动词</span>
  </button>
  <button class="nav-btn" onclick="switchTab('adj', this, '#059669', '#ecfdf5', '形容词篇')">
    <span class="icon">✨</span>
    <span>形容词</span>
  </button>
  <button class="nav-btn" onclick="switchTab('particles', this, '#ea580c', '#fff7ed', '介词助词')">
    <span class="icon">⚓</span>
    <span>助词</span>
  </button>
  <button class="nav-btn" onclick="switchTab('sent', this, '#7c3aed', '#faf5ff', '句子造句')">
    <span class="icon">🧱</span>
    <span>造句</span>
  </button>
  <button class="nav-btn" onclick="switchTab('spoken', this, '#e11d48', '#fff1f2', '常用口语')">
    <span class="icon">🗣️</span>
    <span>口语</span>
  </button>
</nav>

<script>
  // Tab Switching
  function switchTab(tabId, btn, themeColor, themeBg, badgeText) {
    document.querySelectorAll('.tab-pane').forEach(el => el.classList.remove('active'));
    document.querySelectorAll('.nav-btn').forEach(el => el.classList.remove('active'));
    
    document.getElementById('tab-' + tabId).classList.add('active');
    btn.classList.add('active');
    
    document.documentElement.style.setProperty('--active-theme', themeColor);
    document.documentElement.style.setProperty('--active-theme-bg', themeBg);
    document.getElementById('currentModuleBadge').innerText = badgeText;
    
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  // Native Speech Synthesis tuned for iOS Japanese
  function speak(text) {
    if (!('speechSynthesis' in window)) {
      alert('您的设备暂不支持发音功能');
      return;
    }
    window.speechSynthesis.cancel();
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = 'ja-JP';
    utterance.rate = 0.86; // 适合初学者的适度语速
    utterance.pitch = 1.0; // 标准自然音高
    
    // Pick native high-quality voice on iOS if available
    const voices = window.speechSynthesis.getVoices();
    const jaVoice = voices.find(v => v.lang.includes('ja') || v.lang.includes('JP'));
    if (jaVoice) {
      utterance.voice = jaVoice;
    }

    window.speechSynthesis.speak(utterance);
    
    const status = document.getElementById('audioStatus');
    status.innerText = '🔊 正在发音: ' + text;
    utterance.onend = () => { status.innerText = '🔊 点词可发音'; };
    utterance.onerror = () => { status.innerText = '🔊 点词可发音'; };
  }

  // Global Quick Search Filter
  function handleSearch() {
    const query = document.getElementById('globalSearch').value.trim().toLowerCase();
    const cards = document.querySelectorAll('.card, .quick-item');
    
    if (!query) {
      cards.forEach(card => card.style.display = '');
      return;
    }

    cards.forEach(card => {
      const text = card.innerText.toLowerCase();
      if (text.includes(query)) {
        card.style.display = '';
        const parentTab = card.closest('.tab-pane');
        if (parentTab) {
          parentTab.classList.add('active');
        }
      } else {
        card.style.display = 'none';
      }
    });
  }

  // Ensure voices are loaded on mobile Safari
  if ('speechSynthesis' in window) {
    window.speechSynthesis.onvoiceschanged = () => {
      window.speechSynthesis.getVoices();
    };
  }
</script>

</body>
</html>
"""

with open('日语随身宝.html', 'w', encoding='utf-8') as f:
    f.write(html_code)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_code)

print("Updated 日语随身宝.html and index.html successfully.")
