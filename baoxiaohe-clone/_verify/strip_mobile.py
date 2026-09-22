# -*- coding: utf-8 -*-
import io

P = r"C:\Users\CT\Doubao\chats\2026-09-22\new-chat-1\baoxiaohe-clone\包小盒同款功能模板.html"

with io.open(P, "r", encoding="utf-8") as f:
    html = f.read()

m1 = """@media (max-width:640px){
  .render-left{width:170px}
  .editor-left{width:180px}
  .editor-canvas{min-height:300px}
  .canvas-meta{flex-wrap:wrap;font-size:10px;gap:5px;max-width:94%}
  .render-bottom{gap:6px}
  .rb-render{margin-left:0}
}

"""
assert m1 in html, "m1 not found"
html = html.replace(m1, "")

m2 = """@media (max-width:640px){
  .content{padding:14px}
  .card-grid{grid-template-columns:repeat(auto-fill,minmax(160px,1fr));gap:10px}
  .tpl-grid{grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:10px}
  .hero{padding:20px}
  .hero h1{font-size:22px}
  .page-head h1{font-size:18px}
  .f-row{gap:6px}
  .searchbox{display:none}
  .ta-btn:not(.on){display:none}
  .ta-btn{min-height:36px}
  .top-cta .btn{min-width:40px;min-height:40px}
  .card .ops .btn{height:36px;min-height:36px}
  .top-cta .btn span{display:none}
  .top-cta .btn{width:40px}
}
"""
assert m2 in html, "m2 not found"
html = html.replace(m2, "")

# keep one section marker
html = html.replace("/* ===== 响应式 ===== */", "/* ===== 响应式（桌面窗口缩放） ===== */")

with io.open(P, "w", encoding="utf-8") as f:
    f.write(html)

print("OK, removed mobile media queries, size:", len(html))
