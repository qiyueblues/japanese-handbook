# -*- coding: utf-8 -*-
"""
Script to integrate and re-typeset all 5 Japanese Grammar HTML modules into a single mobile-optimized web app.
Zero content deletion, zero audio playback, pure responsive mobile typography.
"""

import os
import re

files_info = [
    {
        "id": "verb",
        "file": "01_日语核心语法精讲_动词篇.html",
        "title": "动词篇",
        "icon": "🏃",
        "primary": "#1e40af",
        "primary_light": "#eff6ff",
        "primary_border": "#93c5fd",
        "accent": "#3b82f6",
        "gradient": "linear-gradient(135deg, #1e3a8a 0%, #2563eb 100%)",
        "th_bg": "#1e3a8a"
    },
    {
        "id": "adj",
        "file": "02_日语核心语法精讲_形容词篇.html",
        "title": "形容词篇",
        "icon": "✨",
        "primary": "#065f46",
        "primary_light": "#ecfdf5",
        "primary_border": "#a7f3d0",
        "accent": "#059669",
        "gradient": "linear-gradient(135deg, #064e3b 0%, #059669 100%)",
        "th_bg": "#064e3b"
    },
    {
        "id": "particle",
        "file": "03_日语核心语法精讲_介词助词篇.html",
        "title": "介词助词篇",
        "icon": "⚓",
        "primary": "#9a3412",
        "primary_light": "#fff7ed",
        "primary_border": "#fed7aa",
        "accent": "#ea580c",
        "gradient": "linear-gradient(135deg, #7c2d12 0%, #ea580c 100%)",
        "th_bg": "#7c2d12"
    },
    {
        "id": "sent",
        "file": "04_日语核心语法精讲_句子造句篇.html",
        "title": "句子造句篇",
        "icon": "🧱",
        "primary": "#581c87",
        "primary_light": "#faf5ff",
        "primary_border": "#d8b4fe",
        "accent": "#7c3aed",
        "gradient": "linear-gradient(135deg, #4c1d95 0%, #7c3aed 100%)",
        "th_bg": "#4c1d95"
    },
    {
        "id": "spoken",
        "file": "05_日语核心语法精讲_常用口语篇.html",
        "title": "常用口语篇",
        "icon": "🗣️",
        "primary": "#9f1239",
        "primary_light": "#fff1f2",
        "primary_border": "#fecdd3",
        "accent": "#e11d48",
        "gradient": "linear-gradient(135deg, #881337 0%, #e11d48 100%)",
        "th_bg": "#881337"
    }
]

# Extract body contents from all 5 files
modules_html = []
for mod in files_info:
    filepath = mod["file"]
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Extract inner body content
    match = re.search(r"<body[^>]*>(.*?)</body>", content, re.DOTALL | re.IGNORECASE)
    if not match:
        raise ValueError(f"Body not found in {filepath}")
    
    body = match.group(1).strip()
    
    # Wrap every custom-table in a table-container for smooth mobile scrolling
    # (Without modifying any content inside the table)
    body = re.sub(
        r"(<table\s+class=[\x27\x22]custom-table[\x27\x22][^>]*>.*?</table>)",
        r'<div class="table-container">\1</div>',
        body,
        flags=re.DOTALL
    )
    
    modules_html.append({
        "info": mod,
        "content": body
    })

# Construct the full mobile web application
html_template = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="apple-mobile-web-app-title" content="日语随身宝">
<meta name="format-detection" content="telephone=no">
<meta name="theme-color" content="#ffffff" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0f172a" media="(prefers-color-scheme: dark)">
<title>日语核心语法与全景口语随身宝 · 手机完整版</title>

<!-- Apple Touch Icon (Torii & Sakura SVG) -->
<link rel="apple-touch-icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 512 512'><rect width='512' height='512' rx='128' fill='%231e3a8a'/><path d='M110 160h292M140 140v242M372 140v242M140 210h232' stroke='white' stroke-width='32' stroke-linecap='round'/><circle cx='380' cy='370' r='42' fill='%23e11d48'/></svg>">

<style>
  :root {
    --text-main: #0f172a;
    --text-muted: #475569;
    --border-color: #cbd5e1;
    --bg-page: #f8fafc;
    --bg-card: #ffffff;
    --current-theme: #1e40af;
    --header-bg: rgba(255, 255, 255, 0.94);
    --bottom-bg: rgba(255, 255, 255, 0.95);
  }

  @media (prefers-color-scheme: dark) {
    :root:not([data-theme="light"]) {
      --text-main: #f1f5f9;
      --text-muted: #94a3b8;
      --border-color: #334155;
      --bg-page: #0f172a;
      --bg-card: #1e293b;
      --header-bg: rgba(15, 23, 42, 0.94);
      --bottom-bg: rgba(15, 23, 42, 0.95);
    }
  }

  [data-theme="dark"] {
    --text-main: #f1f5f9;
    --text-muted: #94a3b8;
    --border-color: #334155;
    --bg-page: #0f172a;
    --bg-card: #1e293b;
    --header-bg: rgba(15, 23, 42, 0.94);
    --bottom-bg: rgba(15, 23, 42, 0.95);
  }

  [data-theme="light"] {
    --text-main: #0f172a;
    --text-muted: #475569;
    --border-color: #cbd5e1;
    --bg-page: #f8fafc;
    --bg-card: #ffffff;
    --header-bg: rgba(255, 255, 255, 0.94);
    --bottom-bg: rgba(255, 255, 255, 0.95);
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
    padding-top: max(56px, calc(env(safe-area-inset-top) + 48px));
    padding-bottom: max(80px, calc(env(safe-area-inset-bottom) + 68px));
  }

  /* Sticky Top Header */
  .top-header {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    z-index: 100;
    background: var(--header-bg);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border-bottom: 1px solid var(--border-color);
    padding: max(8px, env(safe-area-inset-top)) 14px 8px 14px;
    transition: background-color 0.2s;
  }
  @media (prefers-color-scheme: dark) {
    .top-header {
      background: rgba(15, 23, 42, 0.94);
    }
  }

  .header-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 6px;
  }

  .app-title-group {
    display: flex;
    align-items: center;
    gap: 8px;
  }
  .app-title {
    font-size: 16px;
    font-weight: 800;
    letter-spacing: -0.3px;
    display: flex;
    align-items: center;
    gap: 5px;
  }
  .module-badge {
    font-size: 11px;
    padding: 2px 8px;
    border-radius: 999px;
    font-weight: 700;
    color: #ffffff;
    background: var(--current-theme);
    transition: background-color 0.2s;
  }

  .header-actions {
    display: flex;
    align-items: center;
    gap: 6px;
  }
  .theme-toggle-btn, .view-toggle-btn {
    font-size: 12px;
    font-weight: 600;
    padding: 4px 9px;
    border-radius: 8px;
    border: 1px solid var(--border-color);
    background: var(--bg-card);
    color: var(--text-main);
    cursor: pointer;
    transition: all 0.2s;
    display: inline-flex;
    align-items: center;
    justify-content: center;
  }
  .theme-toggle-btn {
    padding: 4px 7px;
    font-size: 13px;
  }
  .view-toggle-btn.active {
    background: var(--current-theme);
    color: #ffffff;
    border-color: var(--current-theme);
  }

  /* Search Bar */
  .search-wrapper {
    position: relative;
    width: 100%;
  }
  .search-input {
    width: 100%;
    height: 33px;
    border-radius: 8px;
    border: 1px solid var(--border-color);
    background: var(--bg-page);
    color: var(--text-main);
    padding: 0 10px 0 32px;
    font-size: 13px;
    outline: none;
    transition: all 0.2s;
  }
  .search-input:focus {
    border-color: var(--current-theme);
    background: var(--bg-card);
  }
  .search-icon {
    position: absolute;
    left: 10px;
    top: 50%;
    transform: translateY(-50%);
    font-size: 12px;
    color: var(--text-muted);
    pointer-events: none;
  }

  /* Content Wrapper */
  .content-container {
    max-width: 680px;
    margin: 0 auto;
    padding: 12px 14px;
  }

  /* Mobile Responsive Table Container */
  .table-container {
    width: 100%;
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
    margin-bottom: 12px;
    border-radius: 8px;
    border: 1px solid var(--border-color);
    background: var(--bg-card);
  }
  table.custom-table {
    width: 100%;
    min-width: 520px; /* guarantees columns aren't crushed on mobile */
    border-collapse: collapse;
    margin-bottom: 0;
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
    padding: 6px 9px;
    border-bottom: 1px solid var(--border-color);
    vertical-align: middle;
  }
  table.custom-table tr:nth-child(even) td {
    background-color: rgba(0, 0, 0, 0.02);
  }
  @media (prefers-color-scheme: dark) {
    table.custom-table tr:nth-child(even) td {
      background-color: rgba(255, 255, 255, 0.03);
    }
    table.custom-table td {
      border-bottom-color: var(--border-color);
      color: #e2e8f0;
    }
  }
  table.custom-table tr:last-child td {
    border-bottom: none;
  }

  /* Doc Headers & Badges */
  .doc-header {
    border-radius: 10px;
    padding: 15px 16px;
    margin-bottom: 14px;
    color: #ffffff;
    box-shadow: 0 2px 4px rgba(0,0,0,0.06);
  }
  .doc-header h1 {
    font-size: 19px;
    font-weight: 800;
    margin-bottom: 4px;
    line-height: 1.35;
  }
  .doc-header .subtitle {
    font-size: 12px;
    opacity: 0.94;
    margin-bottom: 8px;
    line-height: 1.45;
  }
  .tags {
    display: flex;
    gap: 6px;
    flex-wrap: wrap;
  }
  .tag {
    background: rgba(255, 255, 255, 0.22);
    border: 1px solid rgba(255, 255, 255, 0.35);
    padding: 2px 8px;
    border-radius: 999px;
    font-size: 11px;
    font-weight: 600;
  }

  /* Section Styles */
  .section { margin-bottom: 16px; }
  .section-title {
    font-size: 15px;
    font-weight: 700;
    margin-bottom: 10px;
    display: flex;
    align-items: center;
    gap: 8px;
    padding-bottom: 4px;
    border-bottom: 2px solid;
  }
  .section-title .num {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 22px;
    height: 22px;
    border-radius: 50%;
    color: #ffffff;
    font-size: 12px;
    font-weight: 700;
    flex-shrink: 0;
  }

  /* Cards & Callout Boxes */
  .card {
    border: 1px solid var(--border-color);
    border-radius: 9px;
    padding: 11px 13px;
    margin-bottom: 12px;
    background-color: var(--bg-card);
    box-shadow: 0 1px 3px rgba(0,0,0,0.02);
  }

  .info-box {
    background-color: var(--bg-card);
    border-left: 4px solid;
    border-radius: 0 8px 8px 0;
    padding: 10px 13px;
    margin-bottom: 12px;
    font-size: 12.8px;
    line-height: 1.6;
    border-top: 1px solid var(--border-color);
    border-right: 1px solid var(--border-color);
    border-bottom: 1px solid var(--border-color);
  }

  .anime-box {
    background-color: #fdf4ff;
    border: 1px solid #f0abfc;
    border-left: 4px solid #d946ef;
    border-radius: 0 8px 8px 0;
    padding: 10px 13px;
    margin-bottom: 12px;
    font-size: 12.8px;
    line-height: 1.6;
  }
  .anime-box .title { font-weight: 700; color: #a21caf; margin-bottom: 3px; }
  @media (prefers-color-scheme: dark) {
    .anime-box { background-color: rgba(217, 70, 239, 0.12); border-color: rgba(217, 70, 239, 0.3); }
    .anime-box .title { color: #f0abfc; }
  }

  .trap-box {
    background-color: #fff1f2;
    border: 1px solid #fecdd3;
    border-left: 4px solid #e11d48;
    border-radius: 0 8px 8px 0;
    padding: 10px 13px;
    margin-bottom: 12px;
    font-size: 12.8px;
    line-height: 1.6;
  }
  .trap-box .title { font-weight: 700; color: #be123c; margin-bottom: 3px; }
  @media (prefers-color-scheme: dark) {
    .trap-box { background-color: rgba(225, 29, 72, 0.12); border-color: rgba(225, 29, 72, 0.3); }
    .trap-box .title { color: #fecdd3; }
  }

  .mnemonic-box {
    background-color: #fefce8;
    border: 1px solid #fef08a;
    border-left: 4px solid #ca8a04;
    border-radius: 0 8px 8px 0;
    padding: 10px 13px;
    margin-bottom: 12px;
    font-size: 12.8px;
    line-height: 1.6;
  }
  .mnemonic-box .title { font-weight: 700; color: #a16207; margin-bottom: 3px; }
  @media (prefers-color-scheme: dark) {
    .mnemonic-box { background-color: rgba(202, 138, 4, 0.12); border-color: rgba(202, 138, 4, 0.3); }
    .mnemonic-box .title { color: #fef08a; }
  }

  .tip-box {
    background-color: #f0fdf4;
    border: 1px solid #bbf7d0;
    border-left: 4px solid #16a34a;
    border-radius: 0 8px 8px 0;
    padding: 10px 13px;
    margin-bottom: 12px;
    font-size: 12.8px;
    line-height: 1.6;
  }
  .tip-box .title { font-weight: 700; color: #15803d; margin-bottom: 3px; }
  @media (prefers-color-scheme: dark) {
    .tip-box { background-color: rgba(22, 163, 74, 0.12); border-color: rgba(22, 163, 74, 0.3); }
    .tip-box .title { color: #bbf7d0; }
  }

  .warn-box {
    background-color: #fff7ed;
    border: 1px solid #fed7aa;
    border-left: 4px solid #ea580c;
    border-radius: 0 8px 8px 0;
    padding: 10px 13px;
    margin-bottom: 12px;
    font-size: 12.8px;
    line-height: 1.6;
  }
  .warn-box .title { font-weight: 700; color: #c2410c; margin-bottom: 3px; }
  @media (prefers-color-scheme: dark) {
    .warn-box { background-color: rgba(234, 88, 12, 0.12); border-color: rgba(234, 88, 12, 0.3); }
    .warn-box .title { color: #fed7aa; }
  }

  /* Responsive Grids on Mobile */
  .grid-2 {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 11px;
    margin-bottom: 12px;
  }
  .grid-3 {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 11px;
    margin-bottom: 12px;
  }
  @media (max-width: 640px) {
    .grid-2, .grid-3 {
      display: flex;
      flex-direction: column;
      gap: 10px;
    }
  }

  /* Badges & Highlights */
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

  /* Footers & Page Breaks */
  .footer-bar {
    text-align: center;
    font-size: 11px;
    color: var(--text-muted);
    margin: 16px 0 10px 0;
    padding-top: 8px;
    border-top: 1px solid var(--border-color);
  }
  .page-break {
    margin: 20px 0;
    border-top: 1px dashed var(--border-color);
  }

  /* ================= MODULE SPECIFIC THEMES ================= */
  #module-verb {
    --primary: #1e40af;
    --primary-light: #eff6ff;
    --primary-border: #93c5fd;
    --accent: #3b82f6;
  }
  #module-verb .doc-header { background: linear-gradient(135deg, #1e3a8a 0%, #2563eb 100%); }
  #module-verb table.custom-table th { background: #1e3a8a; }
  #module-verb .section-title { color: #1e40af; border-bottom-color: #1e40af; }
  #module-verb .section-title .num { background: #1e40af; }
  #module-verb .info-box { border-left-color: #3b82f6; }

  #module-adj {
    --primary: #065f46;
    --primary-light: #ecfdf5;
    --primary-border: #a7f3d0;
    --accent: #059669;
  }
  #module-adj .doc-header { background: linear-gradient(135deg, #064e3b 0%, #059669 100%); }
  #module-adj table.custom-table th { background: #064e3b; }
  #module-adj .section-title { color: #065f46; border-bottom-color: #065f46; }
  #module-adj .section-title .num { background: #065f46; }
  #module-adj .info-box { border-left-color: #059669; }

  #module-particle {
    --primary: #9a3412;
    --primary-light: #fff7ed;
    --primary-border: #fed7aa;
    --accent: #ea580c;
  }
  #module-particle .doc-header { background: linear-gradient(135deg, #7c2d12 0%, #ea580c 100%); }
  #module-particle table.custom-table th { background: #7c2d12; }
  #module-particle .section-title { color: #9a3412; border-bottom-color: #9a3412; }
  #module-particle .section-title .num { background: #9a3412; }
  #module-particle .info-box { border-left-color: #ea580c; }

  #module-sent {
    --primary: #581c87;
    --primary-light: #faf5ff;
    --primary-border: #d8b4fe;
    --accent: #7c3aed;
  }
  #module-sent .doc-header { background: linear-gradient(135deg, #4c1d95 0%, #7c3aed 100%); }
  #module-sent table.custom-table th { background: #4c1d95; }
  #module-sent .section-title { color: #581c87; border-bottom-color: #581c87; }
  #module-sent .section-title .num { background: #581c87; }
  #module-sent .info-box { border-left-color: #7c3aed; }

  #module-spoken {
    --primary: #9f1239;
    --primary-light: #fff1f2;
    --primary-border: #fecdd3;
    --accent: #e11d48;
  }
  #module-spoken .doc-header { background: linear-gradient(135deg, #881337 0%, #e11d48 100%); }
  #module-spoken table.custom-table th { background: #881337; }
  #module-spoken .section-title { color: #9f1239; border-bottom-color: #9f1239; }
  #module-spoken .section-title .num { background: #9f1239; }
  #module-spoken .info-box { border-left-color: #e11d48; }

  /* Tab View Modes */
  .module-pane {
    display: none;
    animation: fadeIn 0.2s ease-in-out;
  }
  .module-pane.active {
    display: block;
  }
  body.view-all-mode .module-pane {
    display: block !important;
    margin-bottom: 30px;
    padding-bottom: 24px;
    border-bottom: 2px solid var(--border-color);
  }
  body.view-all-mode .module-pane:last-child {
    border-bottom: none;
  }

  @keyframes fadeIn {
    from { opacity: 0; transform: translateY(4px); }
    to { opacity: 1; transform: translateY(0); }
  }

  /* Floating Bottom Navigation Bar */
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
    padding: 6px 4px max(8px, env(safe-area-inset-bottom)) 4px;
    display: flex;
    justify-content: space-around;
  }
  @media (prefers-color-scheme: dark) {
    .bottom-nav {
      background: rgba(15, 23, 42, 0.95);
    }
  }

  .nav-tab-btn {
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    background: none;
    border: none;
    padding: 3px 0;
    color: var(--text-muted);
    font-size: 11px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s;
  }
  .nav-tab-btn .tab-icon {
    font-size: 18px;
    margin-bottom: 2px;
    transition: transform 0.2s;
  }
  .nav-tab-btn.active {
    color: var(--current-theme);
  }
  .nav-tab-btn.active .tab-icon {
    transform: scale(1.15);
  }

  /* Floating Back to Top Button */
  .back-top-btn {
    position: fixed;
    right: 14px;
    bottom: max(68px, calc(env(safe-area-inset-bottom) + 60px));
    z-index: 90;
    width: 38px;
    height: 38px;
    border-radius: 50%;
    background: rgba(0, 0, 0, 0.65);
    backdrop-filter: blur(8px);
    -webkit-backdrop-filter: blur(8px);
    color: #ffffff;
    border: none;
    font-size: 17px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    opacity: 0;
    pointer-events: none;
    transition: all 0.25s;
    box-shadow: 0 2px 8px rgba(0,0,0,0.15);
  }
  .back-top-btn.visible {
    opacity: 1;
    pointer-events: auto;
  }
  .back-top-btn:active {
    transform: scale(0.92);
  }

  /* iOS PWA Install Guide Banner */
  .pwa-guide {
    background: var(--bg-card);
    border: 1px solid var(--border-color);
    border-radius: 10px;
    padding: 10px 12px;
    margin-bottom: 12px;
    font-size: 12px;
    display: flex;
    align-items: center;
    gap: 10px;
    color: var(--text-muted);
  }
  .pwa-guide strong { color: var(--text-main); }
  .pwa-close-btn {
    margin-left: auto;
    background: none;
    border: none;
    color: var(--text-muted);
    font-size: 16px;
    cursor: pointer;
  }
</style>
</head>
<body>

<!-- STICKY TOP HEADER -->
<header class="top-header">
  <div class="header-row">
    <div class="app-title-group">
      <span class="app-title">🎌 日语随身宝</span>
      <span class="module-badge" id="moduleBadge">🏃 动词篇</span>
    </div>
    <div class="header-actions">
      <button class="theme-toggle-btn" id="themeToggleBtn" onclick="toggleTheme()" title="切换明亮/暗黑模式">🌙</button>
      <button class="view-toggle-btn" id="viewToggleBtn" onclick="toggleViewMode()">📜 全部展开</button>
    </div>
  </div>

  <div class="search-wrapper">
    <span class="search-icon">🔍</span>
    <input type="text" class="search-input" id="globalSearch" placeholder="搜索语法、词形、台词 (如: 音便, て形, は, すげえ)..." oninput="handleSearch()">
  </div>
</header>

<!-- MAIN CONTENT -->
<main class="content-container">

  <!-- iOS 主屏幕安装提示条 -->
  <div class="pwa-guide" id="pwaGuide">
    <span style="font-size:18px;">📲</span>
    <div>
      <strong>iPhone 随身技巧：</strong>点击 Safari 底部 <strong>分享按钮 (⎋)</strong> $\rightarrow$ 选择 <strong>「添加到主屏幕」</strong>，即享全屏离线独立 App！
    </div>
    <button class="pwa-close-btn" onclick="document.getElementById('pwaGuide').style.display='none'">✕</button>
  </div>

  <!-- MODULE 1: 动词篇 -->
  <div class="module-pane active" id="module-verb">
    {MODULE_VERB}
  </div>

  <!-- MODULE 2: 形容词篇 -->
  <div class="module-pane" id="module-adj">
    {MODULE_ADJ}
  </div>

  <!-- MODULE 3: 介词助词篇 -->
  <div class="module-pane" id="module-particle">
    {MODULE_PARTICLE}
  </div>

  <!-- MODULE 4: 句子造句篇 -->
  <div class="module-pane" id="module-sent">
    {MODULE_SENT}
  </div>

  <!-- MODULE 5: 常用口语篇 -->
  <div class="module-pane" id="module-spoken">
    {MODULE_SPOKEN}
  </div>

</main>

<!-- FLOATING BACK TO TOP BUTTON -->
<button class="back-top-btn" id="backTopBtn" onclick="scrollToTop()">↑</button>

<!-- FLOATING BOTTOM NAVIGATION BAR -->
<nav class="bottom-nav" id="bottomNav">
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
  
  // Theme Switching
  function initTheme() {
    const saved = localStorage.getItem("app_theme_pref");
    if (saved === "light" || saved === "dark") {
      document.documentElement.setAttribute("data-theme", saved);
    }
    updateThemeIcon();
  }

  function toggleTheme() {
    const current = document.documentElement.getAttribute("data-theme");
    const isDark = current === "dark" || (!current && window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches);
    const next = isDark ? "light" : "dark";
    document.documentElement.setAttribute("data-theme", next);
    localStorage.setItem("app_theme_pref", next);
    updateThemeIcon();
  }

  function updateThemeIcon() {
    const current = document.documentElement.getAttribute("data-theme");
    const isDark = current === "dark" || (!current && window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches);
    const btn = document.getElementById("themeToggleBtn");
    if (btn) btn.innerText = isDark ? "☀️" : "🌙";
  }

  initTheme();

  let isViewAll = false;
  let activeModuleId = 'verb';

  // Switch Module Tab
  function switchModule(modId, themeColor, badgeText) {
    if (isViewAll) {
      toggleViewMode(); // Exit view all mode
    }

    activeModuleId = modId;
    document.querySelectorAll('.module-pane').forEach(el => el.classList.remove('active'));
    document.querySelectorAll('.nav-tab-btn').forEach(btn => btn.classList.remove('active'));

    const target = document.getElementById('module-' + modId);
    if (target) target.classList.add('active');

    const activeBtn = document.querySelector(`.nav-tab-btn[data-mod="${modId}"]`);
    if (activeBtn) activeBtn.classList.add('active');

    document.documentElement.style.setProperty('--current-theme', themeColor);
    document.getElementById('moduleBadge').innerText = badgeText;

    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  // Toggle View All Mode
  function toggleViewMode() {
    isViewAll = !isViewAll;
    const body = document.body;
    const btn = document.getElementById('viewToggleBtn');
    const badge = document.getElementById('moduleBadge');

    if (isViewAll) {
      body.classList.add('view-all-mode');
      btn.innerText = '📑 分篇模式';
      btn.classList.add('active');
      badge.innerText = '📖 全部模块展开';
    } else {
      body.classList.remove('view-all-mode');
      btn.innerText = '📜 全部展开';
      btn.classList.remove('active');
      const activeBtn = document.querySelector('.nav-tab-btn.active');
      if (activeBtn) {
        const mod = activeBtn.getAttribute('data-mod');
        const badgeMap = {
          verb: '🏃 动词篇',
          adj: '✨ 形容词',
          particle: '⚓ 助词篇',
          sent: '🧱 造句篇',
          spoken: '🗣️ 口语篇'
        };
        badge.innerText = badgeMap[mod] || '🏃 动词篇';
      }
    }
  }

  // Back to top
  function scrollToTop() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  // Show/Hide back to top button
  window.addEventListener('scroll', () => {
    const btn = document.getElementById('backTopBtn');
    if (window.scrollY > 300) {
      btn.classList.add('visible');
    } else {
      btn.classList.remove('visible');
    }
  }, { passive: true });

  // Real-time Global Search Filter
  function handleSearch() {
    const query = document.getElementById('globalSearch').value.trim().toLowerCase();
    const allSections = document.querySelectorAll('.section, .card, .doc-header, .table-container, .info-box, .anime-box, .trap-box, .mnemonic-box, .tip-box, .warn-box');

    if (!query) {
      allSections.forEach(el => el.style.display = '');
      return;
    }

    // Temporarily ensure content is visible for searching
    document.body.classList.add('view-all-mode');
    document.getElementById('viewToggleBtn').innerText = '📑 分篇模式';
    document.getElementById('viewToggleBtn').classList.add('active');
    document.getElementById('moduleBadge').innerText = '🔍 搜索模式';

    allSections.forEach(el => {
      const text = el.innerText.toLowerCase();
      if (text.includes(query)) {
        el.style.display = '';
      } else {
        // If it contains child matches, don't hide parent
        const hasChildMatch = el.querySelector && el.querySelector('.section, .card') ? true : false;
        if (!hasChildMatch) {
          el.style.display = 'none';
        }
      }
    });
  }
</script>

</body>
</html>
"""

# Replace placeholders
final_html = html_template
final_html = final_html.replace("{MODULE_VERB}", modules_html[0]["content"])
final_html = final_html.replace("{MODULE_ADJ}", modules_html[1]["content"])
final_html = final_html.replace("{MODULE_PARTICLE}", modules_html[2]["content"])
final_html = final_html.replace("{MODULE_SENT}", modules_html[3]["content"])
final_html = final_html.replace("{MODULE_SPOKEN}", modules_html[4]["content"])

# Write out to 日语随身宝.html and index.html
with open('日语随身宝.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(final_html)

print(f"Generated 日语随身宝.html and index.html successfully.")
print(f"Total HTML file size: {len(final_html.encode('utf-8'))} bytes.")
