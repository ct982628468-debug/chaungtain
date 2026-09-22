# -*- coding: utf-8 -*-
import io

P = r"C:\Users\CT\Doubao\chats\2026-09-22\new-chat-1\baoxiaohe-clone\包小盒同款功能模板.html"

with io.open(P, "r", encoding="utf-8") as f:
    html = f.read()

card = """            <div class="svc" data-demo="小批量印刷（印刷下单演示）"><div class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M7 8V5a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2v3"/><rect x="3" y="8" width="18" height="10" rx="2"/><path d="M7 14h.01M17 14h.01"/></svg></div><h3>小批量印刷</h3><p>设计稿直达印刷生产</p></div>
"""
assert card in html, "print card not found"
html = html.replace(card, "")

with io.open(P, "w", encoding="utf-8") as f:
    f.write(html)
print("OK, removed 小批量印刷 card, size:", len(html))
