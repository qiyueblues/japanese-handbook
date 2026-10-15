# -*- coding: utf-8 -*-
"""
Builder V5:
1. Adds dedicated Page 5 to Verb Module: "常见高频动词全套变形实战大典 (加深记忆)"
   - 涵盖：三类不规则动词(する/くる)、二类一段动词(食べる/見る/起きる/忘れる/教える/諦める)、
     一类五段动词全词尾(買う/行く/書く/泳ぐ/話す/待つ/死ぬ/遊ぶ/飲む/終わる)、
     必背高频陷阱词(帰る/入る/知る/走る/要る/切る)。
   - 展现每词原形、否定、敬体、て形、た形、假定、命令、意志、可能、动漫名台词。
2. Adds dedicated Page 5 to Adjective Module: "常见高频形容词全套变形实战大典 (加深记忆)"
   - 涵盖：神级特例词(いい/良い)、高频い形容词(高い/美味しい/楽しい/早い/忙しい/優しい/難しい/面白い/可愛い/痛い/怖い/すごい/やばい)、
     高频な形容词(綺麗/有名/嫌い/得意/好き/静か/便利/大丈夫/暇/大切)。
   - 展现每词肯定、否定、过去、过去否定、中顿、副词、样态、动漫口语变音(うめえ/すげえ/やべえ)。
3. Synchronizes horizontal swiper:
   - Dynamic total page count (5 pages for Verb & Adj, 4 pages for Particles, Sentences, Spoken).
   - Dynamic header pills and step indicator ("第 X / 5 章").
4. Strict Light/Dark mode contrast, PWA Service Worker v2, zero audio, 100% full original content preserved.
"""

import os
import re

# ================= 1. DEFINE EXTRA PAGE 5 FOR VERB MODULE =================
verb_page_5_html = """
<!-- PAGE 5: 常见高频动词全套变形实战大典 -->
<div class="doc-header" style="background: linear-gradient(135deg, #1e3a8a 0%, #2563eb 100%);">
  <h1>第五章 · 常见高频动词全套变形实战大典</h1>
  <div class="subtitle">针对动漫与日常交流最高频的 18 个核心动词 —— 涵盖各类音便与陷阱词，彻底打通变形反射弧</div>
  <div class="tags">
    <span class="tag">三类不规则 (2词)</span>
    <span class="tag">二类一段高频 (6词)</span>
    <span class="tag">一类各音便代表 (5词)</span>
    <span class="tag">必背陷阱词 (5词)</span>
  </div>
</div>

<div class="card form-explainer-card">
  <div class="form-explainer-title">
    💡【如何使用本章加深肌肉记忆？】
  </div>
  <div class="form-explainer-body">
    变形不需要每次在脑子里推算五段图，而是要把<strong>“原形 ➔ 否定 ➔ 敬体 ➔ て形 ➔ た形”</strong>读成一段连贯的声音。
    请重点观察下表中动词词尾在 <span class="highlight">あ/い/う/え/お</span> 上的跳跃，以及二类动词去「る」的爽快感！
  </div>
</div>

<div class="card" style="background: linear-gradient(135deg, rgba(37,99,235,0.12), rgba(139,92,246,0.12)); border: 2px dashed #3b82f6; border-radius: 14px; padding: 18px 20px; margin-bottom: 20px; text-align: center;">
  <div style="font-size: 1.15rem; font-weight: 800; color: var(--text-main); margin-bottom: 6px;">🎮 动词变形光看不练容易忘？来做网页闯关实战！</div>
  <div style="font-size: 0.88rem; color: var(--text-muted); line-height: 1.6; margin-bottom: 14px;">涵盖 58+ 精选变形考题：音便专场、外观一段实五段致命陷阱词、键盘快捷键作答、连击评分与错题本！</div>
  <a href="动词变形特训.html" style="display: inline-flex; align-items: center; gap: 8px; background: linear-gradient(135deg, #2563eb, #7c3aed); color: #fff; padding: 11px 24px; border-radius: 12px; font-weight: 700; text-decoration: none; box-shadow: 0 4px 14px rgba(37,99,235,0.4); font-size: 0.95rem;">
    <span>🚀 立即打开【动词变形实战特训器】做题</span>
  </a>
</div>

<!-- Category 1: 三类动词 (不规则神词) -->
<div class="section avoid-break">
  <div class="section-title"><span class="num">1</span> 三类动词（不规则变形 · 数量仅两个 · 必须死记）</div>
  
  <div class="conj-card" style="border-left: 4px solid #8b5cf6;">
    <div class="conj-card-header">
      <div class="conj-card-title-group">
        <span class="conj-badge" style="background:#f3e8ff; color:#7e22ce;">する (做 / 干)</span>
        <span class="conj-purpose-badge" style="background:#faf5ff; color:#6b21a8;">三类サ变动词 · 万能动作核心</span>
      </div>
    </div>
    <div class="table-container" style="margin-top:6px; margin-bottom:6px;">
      <table class="custom-table" style="min-width:620px;">
        <thead><tr><th>否定(未然)</th><th>敬体(ます)</th><th>连接(て形)</th><th>过去(た形)</th><th>假定(ば)</th><th>命令</th><th>意志(邀请)</th><th>可能/被动</th></tr></thead>
        <tbody>
          <tr>
            <td><strong class="highlight">しない</strong> (不做)</td>
            <td><strong>します</strong> (做-敬)</td>
            <td><strong>して</strong> (做了/请做)</td>
            <td><strong>した</strong> (做了)</td>
            <td><strong>すれば</strong> (如果做)</td>
            <td><span class="highlight">しろ！</span> / せよ</td>
            <td><strong>しよう</strong> (做吧)</td>
            <td>できる (能做) / される</td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="conj-anime-quote">
      🎬 <strong>动漫台词：</strong>どう<strong>する</strong>？ (怎么办？) / 約束<strong>して</strong>！ (拉钩发誓/答应我！) / 覚悟<strong>しろ</strong>！ (做好觉悟吧！)
    </div>
  </div>

  <div class="conj-card" style="border-left: 4px solid #8b5cf6;">
    <div class="conj-card-header">
      <div class="conj-card-title-group">
        <span class="conj-badge" style="background:#f3e8ff; color:#7e22ce;">来る (くる · 来)</span>
        <span class="conj-purpose-badge" style="background:#faf5ff; color:#6b21a8;">三类カ变动词 · 汉字读音跟随形态大变身</span>
      </div>
    </div>
    <div class="table-container" style="margin-top:6px; margin-bottom:6px;">
      <table class="custom-table" style="min-width:620px;">
        <thead><tr><th>否定(未然)</th><th>敬体(ます)</th><th>连接(て形)</th><th>过去(た形)</th><th>假定(ば)</th><th>命令</th><th>意志(邀请)</th><th>可能/被动</th></tr></thead>
        <tbody>
          <tr>
            <td><strong class="highlight">こない</strong> (来ない)</td>
            <td><strong class="highlight">きます</strong> (来ます)</td>
            <td><strong class="highlight">きて</strong> (来て)</td>
            <td><strong class="highlight">きた</strong> (来た)</td>
            <td><strong class="highlight">くれば</strong> (来れば)</td>
            <td><strong class="highlight">こい！</strong> (来い)</td>
            <td><strong>こよう</strong> (来よう)</td>
            <td>こられる (能来/被来)</td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="conj-anime-quote">
      🎬 <strong>动漫台词：</strong>奴が<strong>来た</strong>！ (那家伙来了！) / こっちへ<strong>来い</strong>！ (到这儿来！) / 助けに<strong>来て</strong>！ (快来救我！)
    </div>
  </div>
</div>

<!-- Category 2: 二类一段动词 (日常最常用代表) -->
<div class="section avoid-break">
  <div class="section-title"><span class="num">2</span> 二类动词（一段动词 · 最听话 · 直接丢「る」接零件）</div>
  
  <div class="table-container">
    <div class="table-scroll-hint">↔️ 左右滑动查看全套变形（一目了然：词尾一律丢「る」！）</div>
    <table class="custom-table" style="min-width:760px;">
      <thead>
        <tr>
          <th style="min-width:120px;">辞书原形 (释义)</th>
          <th style="min-width:90px;">否定(ない)</th>
          <th style="min-width:95px;">敬体(ます)</th>
          <th style="min-width:90px;">连接(て形)</th>
          <th style="min-width:85px;">过去(た形)</th>
          <th style="min-width:85px;">假定(ば)</th>
          <th style="min-width:85px;">命令(ろ)</th>
          <th style="min-width:90px;">意志(よう)</th>
          <th style="min-width:130px;">高频台词搭配</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>食べる</strong> (たべる·吃)</td>
          <td>食べ-ない</td>
          <td>食べ-ます</td>
          <td>食べ-て</td>
          <td>食べ-た</td>
          <td>食べれ-ば</td>
          <td>食べ-ろ</td>
          <td>食べ-よう</td>
          <td>全部<strong>食べた</strong> (全吃光了)</td>
        </tr>
        <tr>
          <td><strong>見る</strong> (みる·看)</td>
          <td>見-ない</td>
          <td>見-ます</td>
          <td>見-て</td>
          <td>見-た</td>
          <td>見れ-ば</td>
          <td>見-ろ</td>
          <td>見-よう</td>
          <td><strong>見て！</strong> (你看！) / 見たぞ！</td>
        </tr>
        <tr>
          <td><strong>起きる</strong> (おきる·起床)</td>
          <td>起き-ない</td>
          <td>起き-ます</td>
          <td>起き-て</td>
          <td>起き-た</td>
          <td>起きれ-ば</td>
          <td>起き-ろ</td>
          <td>起き-よう</td>
          <td>早く<strong>起きろ！</strong> (快起床！)</td>
        </tr>
        <tr>
          <td><strong>忘れる</strong> (わすれる·忘记)</td>
          <td>忘れ-ない</td>
          <td>忘れ-ます</td>
          <td>忘れ-て</td>
          <td>忘れ-た</td>
          <td>忘れれ-ば</td>
          <td>忘れ-ろ</td>
          <td>忘れ-よう</td>
          <td><strong>忘れないで</strong> (请别忘记我)</td>
        </tr>
        <tr>
          <td><strong>教える</strong> (おしえる·教/告知)</td>
          <td>教え-ない</td>
          <td>教え-ます</td>
          <td>教え-て</td>
          <td>教え-た</td>
          <td>教えれ-ば</td>
          <td>教え-ろ</td>
          <td>教え-よう</td>
          <td><strong>教えてくれ</strong> (告诉我吧！)</td>
        </tr>
        <tr>
          <td><strong>諦める</strong> (あきらめる·放弃)</td>
          <td>諦め-ない</td>
          <td>諦め-ます</td>
          <td>諦め-て</td>
          <td>諦め-た</td>
          <td>諦めれ-ば</td>
          <td>諦め-ろ</td>
          <td>諦め-よう</td>
          <td><span class="highlight">諦めない！</span> (绝不轻言放弃！)</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<!-- Category 3: 一类五段动词 (按词尾各音便代表) -->
<div class="section avoid-break">
  <div class="section-title"><span class="num">3</span> 一类动词（五段动词 · 各词尾行音便全代表词）</div>
  
  <div class="table-container">
    <div class="table-scroll-hint">↔️ 左右滑动查看全套变形（注意音便：促音便 って / 拨音便 んで / い音便 いて）</div>
    <table class="custom-table" style="min-width:820px;">
      <thead>
        <tr>
          <th style="min-width:130px;">原形 [尾字行]</th>
          <th style="min-width:95px;">否定(あ段+ない)</th>
          <th style="min-width:95px;">敬体(い段+ます)</th>
          <th style="min-width:105px;">连接(て形音便)</th>
          <th style="min-width:95px;">过去(た形音便)</th>
          <th style="min-width:85px;">假定(え段+ば)</th>
          <th style="min-width:80px;">命令(え段)</th>
          <th style="min-width:90px;">意志(お段+う)</th>
          <th style="min-width:130px;">音便类别与台词</th>
        </tr>
      </thead>
      <tbody>
        <tr style="background:rgba(219,234,254,0.3);">
          <td><strong>行く</strong> (いく·去) <span class="badge badge-rose">特例!</span></td>
          <td>行か-ない</td>
          <td>行き-ます</td>
          <td><strong class="highlight">行っ-て</strong></td>
          <td><strong class="highlight">行っ-た</strong></td>
          <td>行け-ば</td>
          <td>行け！</td>
          <td>行こう</td>
          <td>促音特例！ <strong>行け！</strong> (冲啊！)</td>
        </tr>
        <tr>
          <td><strong>買う</strong> (かう·买) [う行]</td>
          <td>買<span class="highlight">わ</span>-ない</td>
          <td>買い-ます</td>
          <td><strong class="highlight">買っ-て</strong></td>
          <td>買っ-た</td>
          <td>買え-ば</td>
          <td>買え</td>
          <td>買おう</td>
          <td>促音便 (买给我: 買ってくれ)</td>
        </tr>
        <tr>
          <td><strong>待つ</strong> (まつ·等) [つ行]</td>
          <td>待た-ない</td>
          <td>待ち-ます</td>
          <td><strong class="highlight">待っ-て</strong></td>
          <td>待っ-た</td>
          <td>待て-ば</td>
          <td>待て！</td>
          <td>待とう</td>
          <td>促音便 <strong>ちょっと待って！</strong></td>
        </tr>
        <tr>
          <td><strong>書く</strong> (かく·写) [く行]</td>
          <td>書か-ない</td>
          <td>書き-ます</td>
          <td><strong class="highlight">書い-て</strong></td>
          <td>書い-た</td>
          <td>書け-ば</td>
          <td>書け</td>
          <td>書こう</td>
          <td>い音便 (く ➔ いて)</td>
        </tr>
        <tr>
          <td><strong>泳ぐ</strong> (およぐ·游) [ぐ行]</td>
          <td>泳が-ない</td>
          <td>泳ぎ-ます</td>
          <td><strong class="highlight">泳い-で</strong></td>
          <td>泳い-だ</td>
          <td>泳げ-ば</td>
          <td>泳げ</td>
          <td>泳ごう</td>
          <td>い音便 (ぐ ➔ 浊化 いで)</td>
        </tr>
        <tr>
          <td><strong>話す</strong> (はなす·说) [す行]</td>
          <td>話さ-ない</td>
          <td>話し-ます</td>
          <td><strong class="highlight">話し-て</strong></td>
          <td>話し-た</td>
          <td>話せ-ば</td>
          <td>話せ</td>
          <td>話そう</td>
          <td>常规变 (す ➔ して，不音便)</td>
        </tr>
        <tr>
          <td><strong>死ぬ</strong> (しぬ·死) [ぬ行]</td>
          <td>死な-ない</td>
          <td>死に-ます</td>
          <td><strong class="highlight">死ん-で</strong></td>
          <td>死ん-だ</td>
          <td>死ね-ば</td>
          <td>死ね！</td>
          <td>死のう</td>
          <td>拨音便 <strong>死んじゃダメ！</strong></td>
        </tr>
        <tr>
          <td><strong>飲む</strong> (のむ·喝) [む行]</td>
          <td>飲ま-ない</td>
          <td>飲み-ます</td>
          <td><strong class="highlight">飲ん-で</strong></td>
          <td>饮ん-だ</td>
          <td>飲め-ば</td>
          <td>飲め</td>
          <td>飲もう</td>
          <td>拨音便 (のむ ➔ のんで)</td>
        </tr>
        <tr>
          <td><strong>遊ぶ</strong> (あそぶ·玩) [ぶ行]</td>
          <td>遊ば-ない</td>
          <td>遊び-ます</td>
          <td><strong class="highlight">遊ん-で</strong></td>
          <td>遊ん-だ</td>
          <td>遊べ-ば</td>
          <td>遊べ</td>
          <td>遊ぼう</td>
          <td>拨音便 (遊ぼうぜ 咱们玩吧)</td>
        </tr>
        <tr>
          <td><strong>終わる</strong> (おわる·结束) [る行]</td>
          <td>終わら-ない</td>
          <td>終わり-ます</td>
          <td><strong class="highlight">終わっ-て</strong></td>
          <td>終わっ-た</td>
          <td>終われば</td>
          <td>终われ</td>
          <td>終わろう</td>
          <td>促音便 <strong>終わった…</strong> (全完了)</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<!-- Category 4: 必背高频陷阱词 (外表二类，实全为一类五段！) -->
<div class="section avoid-break">
  <div class="section-title"><span class="num">4</span> ⚠️ 必背高频陷阱词变形对照（披着二类皮的一类动词）</div>
  
  <div class="trap-box">
    <div class="title">🔥 铁律：绝不可直接去「る」！它们必须老老实实按五段跳跃！</div>
    <div style="font-size:12px; line-height:1.6;">
      下面的动词倒数第二个假名全是 i 或 e，但<strong>全是一类五段动词</strong>！否定必须是 <strong>〜らない</strong>，连接必须是 <strong>〜って</strong>！
    </div>
  </div>

  <div class="table-container">
    <table class="custom-table" style="min-width:760px;">
      <thead>
        <tr>
          <th style="min-width:130px;">陷阱词 (释义)</th>
          <th style="min-width:105px;">正确否定 (一类)</th>
          <th style="min-width:95px;">绝对错误 ❌</th>
          <th style="min-width:95px;">敬体(ます)</th>
          <th style="min-width:95px;">て形(促音便)</th>
          <th style="min-width:95px;">た形(过去)</th>
          <th style="min-width:120px;">动漫常听台词</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>帰る</strong> (かえる·回家)</td>
          <td><strong class="highlight">帰ら-ない</strong></td>
          <td><span style="color:#94a3b8; text-decoration:line-through;">かえない</span></td>
          <td>帰ります</td>
          <td>帰っ-て</td>
          <td>帰っ-た</td>
          <td><strong>お帰り！</strong> / もう帰ろう</td>
        </tr>
        <tr>
          <td><strong>入る</strong> (はいる·进入)</td>
          <td><strong class="highlight">入ら-ない</strong></td>
          <td><span style="color:#94a3b8; text-decoration:line-through;">はいない</span></td>
          <td>入ります</td>
          <td>入っ-て</td>
          <td>入っ-た</td>
          <td><strong>入っていい？</strong> (能进吗?)</td>
        </tr>
        <tr>
          <td><strong>知る</strong> (しる·知道)</td>
          <td><strong class="highlight">知ら-ない</strong></td>
          <td><span style="color:#94a3b8; text-decoration:line-through;">しない</span></td>
          <td>知ります</td>
          <td>知っ-て</td>
          <td>知っ-た</td>
          <td><span class="highlight">知らない！</span> (我不知道/才不管!)</td>
        </tr>
        <tr>
          <td><strong>走る</strong> (はしる·奔跑)</td>
          <td><strong class="highlight">走ら-ない</strong></td>
          <td><span style="color:#94a3b8; text-decoration:line-through;">はしない</span></td>
          <td>走ります</td>
          <td>走っ-て</td>
          <td>走っ-た</td>
          <td><strong>走れ！</strong> (快跑！)</td>
        </tr>
        <tr>
          <td><strong>要る</strong> (いる·需要)</td>
          <td><strong class="highlight">要ら-ない</strong></td>
          <td><span style="color:#94a3b8; text-decoration:line-through;">いない</span></td>
          <td>要ります</td>
          <td>要っ-て</td>
          <td>要っ-た</td>
          <td><strong>要らないよ</strong> (我不要/用不着)</td>
        </tr>
        <tr>
          <td><strong>切る</strong> (きる·切/挂断)</td>
          <td><strong class="highlight">切ら-ない</strong></td>
          <td><span style="color:#94a3b8; text-decoration:line-through;">きない</span></td>
          <td>切ります</td>
          <td>切っ-て</td>
          <td>切っ-た</td>
          <td>電話を<strong>切った</strong> (把电话挂了)</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
"""

# ================= 2. DEFINE EXTRA PAGE 5 FOR ADJECTIVE MODULE =================
adj_page_5_html = """
<!-- PAGE 5: 常见高频形容词全套变形实战大典 -->
<div class="doc-header" style="background: linear-gradient(135deg, #064e3b 0%, #059669 100%);">
  <h1>第五章 · 常见高频形容词全套变形实战大典</h1>
  <div class="subtitle">精选 20 个日常交流与动漫最核心形容词 —— 一网打尽い形容词与な形容词所有形态</div>
  <div class="tags">
    <span class="tag">神级特例 (いい)</span>
    <span class="tag">高频い形容词 (11词)</span>
    <span class="tag">伪装假词避坑 (4词)</span>
    <span class="tag">高频な形容词 (5词)</span>
  </div>
</div>

<div class="card form-explainer-card" style="border-left-color: #059669;">
  <div class="form-explainer-title" style="color: #059669;">
    💡【形容词变形秒懂心法】
  </div>
  <div class="form-explainer-body">
    • <strong>い形容词</strong>：本体自带变形器官，变形一律<strong>扔掉词尾「い」</strong>，换上 <span class="highlight">くない(不) / かった(曾) / くて(又) / く(修饰动词)</span>。<br>
    • <strong>な形容词</strong>：本质是个名词，词尾是汉字，靠背后的助动词 <strong>だ / です / じゃない / だった / で / に</strong> 帮它变！
  </div>
</div>

<!-- Section 1: 神级特例词 いい -->
<div class="section avoid-break">
  <div class="section-title" style="color:#065f46; border-bottom-color:#065f46;"><span class="num" style="background:#065f46;">1</span> 唯一神级特例词：「いい (良い)」全变形速查（绝不可说 いくない！）</div>
  
  <div class="conj-card" style="border-left: 4px solid #10b981;">
    <div class="conj-card-header">
      <div class="conj-card-title-group">
        <span class="conj-badge" style="background:#dcfce7; color:#15803d;">いい (好)</span>
        <span class="conj-purpose-badge" style="background:#ecfdf5; color:#065f46;">原形说 いい，所有变形一律回到古语「よい」！</span>
      </div>
    </div>
    <div class="table-container" style="margin-top:6px; margin-bottom:6px;">
      <table class="custom-table" style="min-width:660px;">
        <thead><tr><th>原形(好)</th><th>否定(不好)</th><th>过去(太好啦)</th><th>过去否定</th><th>中顿连接</th><th>修饰动词</th><th>样态推测</th></tr></thead>
        <tbody>
          <tr>
            <td><strong>いい</strong></td>
            <td><strong class="highlight">よくない</strong></td>
            <td><strong class="highlight">よかった！</strong></td>
            <td><strong>よくなかった</strong></td>
            <td><strong>よくて</strong></td>
            <td><strong>よく</strong> (よくやった!)</td>
            <td><strong>よさそう</strong> (插さ)</td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="conj-anime-quote">
      🎬 <strong>动漫台词：</strong>本当に<strong>よかった…</strong> (太好啦/谢天谢地…) / 仲が<strong>いい</strong> (关系好) / <strong>よく</strong>頑張ったね (干得漂亮)
    </div>
  </div>
</div>

<!-- Section 2: 高频い形容词变形总览 -->
<div class="section avoid-break">
  <div class="section-title" style="color:#065f46; border-bottom-color:#065f46;"><span class="num" style="background:#065f46;">2</span> 高频 い形容词全变形大对照（全部“去い”换零件）</div>
  
  <div class="table-container">
    <div class="table-scroll-hint">↔️ 左右滑动查看全套变形（含副词形式与动漫男系变音）</div>
    <table class="custom-table" style="min-width:800px;">
      <thead>
        <tr>
          <th style="min-width:110px;">原形 (释义)</th>
          <th style="min-width:95px;">否定 (くない)</th>
          <th style="min-width:95px;">过去 (かった)</th>
          <th style="min-width:90px;">中顿 (くて)</th>
          <th style="min-width:90px;">修饰动词(く)</th>
          <th style="min-width:90px;">推测(そう)</th>
          <th style="min-width:95px;">男系口语变音</th>
          <th style="min-width:130px;">高频名句搭配</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>美味しい</strong> (好吃)</td>
          <td>美味しくない</td>
          <td>美味しかった</td>
          <td>美味しくて</td>
          <td>美味しく食べる</td>
          <td>美味しそう</td>
          <td><span class="highlight">うめえ！</span> (うまい)</td>
          <td>美味しそう！ (看着真香)</td>
        </tr>
        <tr>
          <td><strong>高い</strong> (贵/高)</td>
          <td>高くない</td>
          <td>高かった</td>
          <td>高くて</td>
          <td>高く飞ぶ</td>
          <td>高そう</td>
          <td>たけえ</td>
          <td>高くて買えない (太贵买不起)</td>
        </tr>
        <tr>
          <td><strong>楽しい</strong> (开心)</td>
          <td>楽しくない</td>
          <td>楽しかった</td>
          <td>楽しくて</td>
          <td>楽しく過ごす</td>
          <td>楽しそう</td>
          <td>たのしゅう</td>
          <td>楽しかった！ (玩得很开心)</td>
        </tr>
        <tr>
          <td><strong>早い</strong> (早/快)</td>
          <td>早くない</td>
          <td>早かった</td>
          <td>早くて</td>
          <td><strong class="highlight">早く！</strong> (副词)</td>
          <td>早そう</td>
          <td>はええ</td>
          <td><span class="highlight">早くして！</span> (快点/抓紧!)</td>
        </tr>
        <tr>
          <td><strong>優しい</strong> (温柔)</td>
          <td>優しくない</td>
          <td>優しかった</td>
          <td>優しくて</td>
          <td>優しく微笑む</td>
          <td>優しそう</td>
          <td>—</td>
          <td>優しくて強い (又温柔又坚强)</td>
        </tr>
        <tr>
          <td><strong>難しい</strong> (难)</td>
          <td>難しくない</td>
          <td>難しかった</td>
          <td>難しくて</td>
          <td>難しく考える</td>
          <td>難しそう</td>
          <td>むずい (俗语)</td>
          <td>難しすぎる (太难了)</td>
        </tr>
        <tr>
          <td><strong>面白い</strong> (有趣)</td>
          <td>面白くない</td>
          <td>面白かった</td>
          <td>白くて</td>
          <td>面白く話す</td>
          <td>面白そう</td>
          <td>おもしれえ</td>
          <td><span class="highlight">おもしれー女</span> (有意思的女人)</td>
        </tr>
        <tr>
          <td><strong>可愛い</strong> (可爱)</td>
          <td>可愛くない</td>
          <td>可愛かった</td>
          <td>可愛くて</td>
          <td>可愛く笑う</td>
          <td>可哀想 (注:可怜)</td>
          <td>かわええ</td>
          <td>可愛すぎる！ (萌化了)</td>
        </tr>
        <tr>
          <td><strong>痛い</strong> (疼)</td>
          <td>痛くない</td>
          <td>痛かった</td>
          <td>痛くて</td>
          <td>痛くする</td>
          <td>痛そう</td>
          <td><span class="highlight">いてえ！</span></td>
          <td>痛くも痒くもない (不痛不痒)</td>
        </tr>
        <tr>
          <td><strong>怖い</strong> (害怕)</td>
          <td>怖くない</td>
          <td>怖かった</td>
          <td>怖くて</td>
          <td>怖く思う</td>
          <td>怖そう</td>
          <td><span class="highlight">こええ！</span></td>
          <td>何も怖くない (无所畏惧)</td>
        </tr>
        <tr>
          <td><strong>すごい</strong> (厉害)</td>
          <td>すごくない</td>
          <td>すごかった</td>
          <td>すごくて</td>
          <td><strong class="highlight">すごく</strong> (非常)</td>
          <td>すごそう</td>
          <td><span class="highlight">すげえ！</span></td>
          <td>すげええ！ (牛逼/太猛了)</td>
        </tr>
        <tr>
          <td><strong>やばい</strong> (糟/绝了)</td>
          <td>やばくない</td>
          <td>やばかった</td>
          <td>やばくて</td>
          <td>やばく感じる</td>
          <td>やばそう</td>
          <td><span class="highlight">やべえ！</span></td>
          <td>マジでやばい (真的绝了/要挂)</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>

<!-- Section 3: 高频な形容词变形总览 (含伪装避坑) -->
<div class="section avoid-break">
  <div class="section-title" style="color:#065f46; border-bottom-color:#065f46;"><span class="num" style="background:#065f46;">3</span> 高频 な形容词全变形大对照（修饰名词加「な」，变形全靠「だ/です」）</div>
  
  <div class="table-container">
    <div class="table-scroll-hint">↔️ 左右滑动查看全套变形（前4个为读音带 i 的高频伪装词！）</div>
    <table class="custom-table" style="min-width:780px;">
      <thead>
        <tr>
          <th style="min-width:130px;">原形 (属性)</th>
          <th style="min-width:100px;">修饰名词 (+な)</th>
          <th style="min-width:95px;">现在结句 (+だ)</th>
          <th style="min-width:115px;">否定 (+じゃない)</th>
          <th style="min-width:105px;">过去 (+だった)</th>
          <th style="min-width:90px;">中顿 (+で)</th>
          <th style="min-width:90px;">修饰动词(+に)</th>
          <th style="min-width:130px;">经典实用短语</th>
        </tr>
      </thead>
      <tbody>
        <tr style="background:rgba(254,242,242,0.5);">
          <td><strong>綺麗</strong> (漂亮/干净) <span class="badge badge-rose">伪装假词!</span></td>
          <td>綺麗<strong class="highlight">な</strong>人</td>
          <td>綺麗だ</td>
          <td>綺麗じゃない</td>
          <td>綺麗だった</td>
          <td>綺麗で</td>
          <td>綺麗<strong class="highlight">に</strong>掃除</td>
          <td>手紙が綺麗だ (字迹工整)</td>
        </tr>
        <tr style="background:rgba(254,242,242,0.5);">
          <td><strong>有名</strong> (有名) <span class="badge badge-rose">伪装假词!</span></td>
          <td>有名<strong class="highlight">な</strong>人</td>
          <td>有名だ</td>
          <td>有名じゃない</td>
          <td>有名だった</td>
          <td>有名で</td>
          <td>有名になる</td>
          <td>世界で有名な (享誉世界)</td>
        </tr>
        <tr style="background:rgba(254,242,242,0.5);">
          <td><strong>嫌い</strong> (讨厌) <span class="badge badge-rose">伪装假词!</span></td>
          <td>嫌い<strong class="highlight">な</strong>奴</td>
          <td>嫌いだ</td>
          <td>嫌いじゃない</td>
          <td>嫌いだった</td>
          <td>嫌いで</td>
          <td>嫌いになる</td>
          <td>嘘つきが大嫌いだ (最厌骗子)</td>
        </tr>
        <tr style="background:rgba(254,242,242,0.5);">
          <td><strong>得意</strong> (擅长) <span class="badge badge-rose">伪装假词!</span></td>
          <td>得意<strong class="highlight">な</strong>科目</td>
          <td>得意だ</td>
          <td>得意じゃない</td>
          <td>得意だった</td>
          <td>得意で</td>
          <td>得意そうに</td>
          <td>料理が得意だ (擅长料理)</td>
        </tr>
        <tr>
          <td><strong>好き</strong> (喜欢)</td>
          <td>好き<strong class="highlight">な</strong>人</td>
          <td>好きだ</td>
          <td>好きじゃない</td>
          <td>好きだった</td>
          <td>好きで</td>
          <td>好き<strong class="highlight">に</strong>する</td>
          <td><span class="highlight">好きにして</span> (随你便吧)</td>
        </tr>
        <tr>
          <td><strong>静か</strong> (安静)</td>
          <td>静か<strong class="highlight">な</strong>部屋</td>
          <td>静かだ</td>
          <td>静かじゃない</td>
          <td>静かだった</td>
          <td>静かで</td>
          <td>静か<strong class="highlight">に</strong>する</td>
          <td><span class="highlight">静かにしろ！</span> (安静/闭嘴!)</td>
        </tr>
        <tr>
          <td><strong>便利</strong> (方便)</td>
          <td>便利<strong class="highlight">な</strong>町</td>
          <td>便利だ</td>
          <td>便利じゃない</td>
          <td>便利だった</td>
          <td>便利で</td>
          <td>便利に使う</td>
          <td>とても便利だ (极其方便)</td>
        </tr>
        <tr>
          <td><strong>大丈夫</strong> (没事)</td>
          <td>大丈夫<strong class="highlight">な</strong>事</td>
          <td>大丈夫だ</td>
          <td>大丈夫じゃない</td>
          <td>大丈夫だった</td>
          <td>大丈夫で</td>
          <td>—</td>
          <td><strong>もう大丈夫だ</strong> (已经没事了)</td>
        </tr>
        <tr>
          <td><strong>暇</strong> (空闲)</td>
          <td>暇<strong class="highlight">な</strong>時</td>
          <td>暇だ</td>
          <td>暇じゃない</td>
          <td>暇だった</td>
          <td>暇で</td>
          <td>暇そうに</td>
          <td>今、暇？ (现在有空吗?)</td>
        </tr>
        <tr>
          <td><strong>大切</strong> (重要/珍贵)</td>
          <td>大切<strong class="highlight">な</strong>仲間</td>
          <td>大切だ</td>
          <td>大切じゃない</td>
          <td>大切だった</td>
          <td>大切で</td>
          <td>大切<strong class="highlight">に</strong>する</td>
          <td><span class="highlight">大切にする</span> (好生珍惜)</td>
        </tr>
      </tbody>
    </table>
  </div>
</div>
"""

# Read original builder script
with open("build_v4_webapp.py", "r", encoding="utf-8") as f:
    orig_code = f.read()

# Let's inspect where modules_config and pages appending happen
# Update modules_config to have 5 pills for Verb and Adj
orig_code = orig_code.replace(
    '"pills": ["1. 分类判定", "2. 六大活用", "3. 音便口诀", "4. 派生句型"]',
    '"pills": ["1. 分类判定", "2. 六大活用", "3. 音便口诀", "4. 派生句型", "5. 常用词变形"]'
)

orig_code = orig_code.replace(
    '"pills": ["1. 两派假词", "2. い形变形", "3. な形与PK", "4. 派生变音"]',
    '"pills": ["1. 两派假词", "2. い形变形", "3. な形与PK", "4. 派生变音", "5. 常用词变形"]'
)

# In JS modulePillsData, also update Verb & Adj to 5 pills
orig_code = orig_code.replace(
    'verb: ["1. 分类判定", "2. 六大活用", "3. 音便口诀", "4. 派生句型"],',
    'verb: ["1. 分类判定", "2. 六大活用", "3. 音便口诀", "4. 派生句型", "5. 常用词变形"],'
)

orig_code = orig_code.replace(
    'adj: ["1. 两派假词", "2. い形变形", "3. な形与PK", "4. 派生变音"],',
    'adj: ["1. 两派假词", "2. い形变形", "3. な形与PK", "4. 派生变音", "5. 常用词变形"],'
)

# In renderHeaderPills: update step indicator to dynamic total
orig_code = orig_code.replace(
    'ind.innerText = `第 ${activeIdx + 1} / 4 章 (左右轻滑翻页)`;',
    'ind.innerText = `第 ${activeIdx + 1} / ${pills.length} 章 (左右轻滑翻页)`;'
)

# In nextSlide: update maxIdx check to dynamic total
orig_code = orig_code.replace(
    'if (currentPageIdx < 3) {',
    'const maxIdx = (modulePillsData[modId] || []).length - 1;\n    if (currentPageIdx < maxIdx) {'
)

# In top-header: add link to 动词变形特训.html
old_theme_btn = """    <button class="theme-toggle-btn" id="themeToggleBtn" onclick="toggleTheme()">
      <span id="themeIcon">☀️</span>
      <span id="themeText">浅色</span>
    </button>"""

new_theme_btn = """    <div style="display:flex; align-items:center; gap:8px;">
      <a href="动词变形特训.html" style="text-decoration:none; display:inline-flex; align-items:center; gap:4px; background:linear-gradient(135deg, #3b82f6, #8b5cf6); color:#fff; font-size:0.75rem; font-weight:700; padding:6px 12px; border-radius:20px; box-shadow:0 2px 8px rgba(59,130,246,0.35);" title="打开动词变形实战闯关题库">
        <span>🎮 变形闯关</span>
      </a>
      <button class="theme-toggle-btn" id="themeToggleBtn" onclick="toggleTheme()">
        <span id="themeIcon">☀️</span>
        <span id="themeText">浅色</span>
      </button>
    </div>"""

orig_code = orig_code.replace(old_theme_btn, new_theme_btn)

# Now, append Page 5 to Verb and Adj in cleaned_pages
append_logic = """
        cleaned_pages.append(p_content)

    # Append custom Page 5 for verb and adj modules
    if mod["id"] == "verb":
        cleaned_pages.append(verb_page_5_html)
    elif mod["id"] == "adj":
        cleaned_pages.append(adj_page_5_html)

    modules_data.append({
"""

orig_code = orig_code.replace(
    '        cleaned_pages.append(p_content)\n\n    modules_data.append({',
    append_logic
)

# Also update the footer buttons logic for dynamic total pages:
# Originally:
# if s_i == 0: ...
# elif s_i == 3: ... (jump next mod)
# else: ...
old_footer_logic = """        # Footer buttons for this slide
        if s_i == 0:
            foot_btn = f\"\"\"
            <div class="slide-footer-nav">
              <span></span>
              <button class="slide-nav-btn primary" onclick="goToSlide('{mod_id}', 1)">下一章：{mod['pills'][1]} ▶</button>
            </div>
            \"\"\"
        elif s_i == 3:
            next_mod = {
                'verb': ('adj', '下一大类：形容词篇'),
                'adj': ('particle', '下一大类：助词篇'),
                'particle': ('sent', '下一大类：造句篇'),
                'sent': ('spoken', '下一大类：口语篇'),
                'spoken': ('verb', '回到开头：动词篇')
            }[mod_id]
            foot_btn = f\"\"\"
            <div class="slide-footer-nav">
              <button class="slide-nav-btn" onclick="goToSlide('{mod_id}', 2)">◀ 上一章</button>
              <button class="slide-nav-btn primary" onclick="switchModule('{next_mod[0]}', themeMap['{next_mod[0]}'], '{next_mod[1]}')">{next_mod[1]} ▶</button>
            </div>
            \"\"\"
        else:
            foot_btn = f\"\"\"
            <div class="slide-footer-nav">
              <button class="slide-nav-btn" onclick="goToSlide('{mod_id}', {s_i-1})">◀ 上一章：{mod['pills'][s_i-1]}</button>
              <button class="slide-nav-btn primary" onclick="goToSlide('{mod_id}', {s_i+1})">下一章：{mod['pills'][s_i+1]} ▶</button>
            </div>
            \"\"\""""

new_footer_logic = """        # Dynamic footer buttons for this slide
        total_p = len(item["pages"])
        if s_i == 0:
            foot_btn = f\"\"\"
            <div class="slide-footer-nav">
              <span></span>
              <button class="slide-nav-btn primary" onclick="goToSlide('{mod_id}', 1)">下一章：{mod['pills'][1]} ▶</button>
            </div>
            \"\"\"
        elif s_i == total_p - 1:
            next_mod = {
                'verb': ('adj', '下一大类：形容词篇'),
                'adj': ('particle', '下一大类：助词篇'),
                'particle': ('sent', '下一大类：造句篇'),
                'sent': ('spoken', '下一大类：口语篇'),
                'spoken': ('verb', '回到开头：动词篇')
            }[mod_id]
            foot_btn = f\"\"\"
            <div class="slide-footer-nav">
              <button class="slide-nav-btn" onclick="goToSlide('{mod_id}', {s_i-1})">◀ 上一章：{mod['pills'][s_i-1]}</button>
              <button class="slide-nav-btn primary" onclick="switchModule('{next_mod[0]}', themeMap['{next_mod[0]}'], '{next_mod[1]}')">{next_mod[1]} ▶</button>
            </div>
            \"\"\"
        else:
            foot_btn = f\"\"\"
            <div class="slide-footer-nav">
              <button class="slide-nav-btn" onclick="goToSlide('{mod_id}', {s_i-1})">◀ 上一章：{mod['pills'][s_i-1]}</button>
              <button class="slide-nav-btn primary" onclick="goToSlide('{mod_id}', {s_i+1})">下一章：{mod['pills'][s_i+1]} ▶</button>
            </div>
            \"\"\""""

orig_code = orig_code.replace(old_footer_logic, new_footer_logic)

# Put verb_page_5_html and adj_page_5_html right before processing
orig_code = f"verb_page_5_html = r'''{verb_page_5_html}'''\nadj_page_5_html = r'''{adj_page_5_html}'''\n\n" + orig_code

with open("build_v5_webapp.py", "w", encoding="utf-8") as f:
    f.write(orig_code)

print("Generated build_v5_webapp.py script successfully.")
