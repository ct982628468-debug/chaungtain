# -*- coding: utf-8 -*-
import io

P = r"C:\Users\CT\Doubao\chats\2026-09-22\new-chat-1\baoxiaohe-clone\包小盒同款功能模板.html"

with io.open(P, "r", encoding="utf-8") as f:
    html = f.read()

# 1) remove topbar buttons: 会员中心 / 小批量印刷 / 更多产品 / 国际版 (keep the .top-tools div)
import re
m = re.search(r'(<div class="top-tools">)(.*?)(</div>\s*<div class="top-cta">)', html, re.S)
assert m, "top-tools block not found"
block = m.group(2)
print("REMOVING top buttons:", re.findall(r'data-demo="([^"]+)"', block))
html = html.replace(m.group(0), m.group(1) + m.group(3), 1)

# 2) remove sidebar 服务 group in NAV
grp = """  {label:'服务', children:[
    {id:'service', label:'包装服务台', icon:IC.service, demo:'包装服务台（印刷/报价服务演示）'},
    {id:'team', label:'团队版', icon:IC.team, demo:'团队版（多人协作演示）'}
  ]},
"""
assert grp in html, "service group not found"
html = html.replace(grp, "")

with io.open(P, "w", encoding="utf-8") as f:
    f.write(html)
print("OK, removed topbar buttons + sidebar 服务 group, size:", len(html))
