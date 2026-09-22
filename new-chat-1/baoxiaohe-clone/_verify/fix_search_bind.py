# -*- coding: utf-8 -*-
import io

P = r"C:\Users\CT\Doubao\chats\2026-09-22\new-chat-1\baoxiaohe-clone\包小盒同款功能模板.html"
with io.open(P, "r", encoding="utf-8") as f:
    html = f.read()

# 1) remove rfSearch binding from bindKnife (element not yet rendered at startup)
old_line = """  el('rfSearch').addEventListener('input', ()=>applyRfFilter());
}"""
assert old_line in html, "rfSearch line"
html = html.replace(old_line, "}", 1)

# 2) bind rfSearch inside bindRfFilters (runs after panel renders)
old_bf = """  [u,i,c].forEach(x=>x.addEventListener('change', applyRfFilter));"""
assert old_bf in html, "bf anchor"
new_bf = """  const q=el('rfSearch'); if(q) q.addEventListener('input', applyRfFilter);
  [u,i,c].forEach(x=>x.addEventListener('change', applyRfFilter));"""
html = html.replace(old_bf, new_bf, 1)

with io.open(P, "w", encoding="utf-8") as f:
    f.write(html)
print("OK fix, size:", len(html))
