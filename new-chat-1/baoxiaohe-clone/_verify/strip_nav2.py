# -*- coding: utf-8 -*-
import io

P = r"C:\Users\CT\Doubao\chats\2026-09-22\new-chat-1\baoxiaohe-clone\包小盒同款功能模板.html"

with io.open(P, "r", encoding="utf-8") as f:
    html = f.read()

# 1) remove topbar action buttons block
old_top = """    <div class="top-actions">
      <button class="ta-btn on" data-demo="会员中心（会员权益演示）">会员中心</button>
      <button class="ta-btn hide-sm" data-demo="小批量印刷（印刷下单演示）">小批量印刷</button>
      <button class="ta-btn hide-sm" data-demo="更多产品（产品矩阵演示）">更多产品</button>
      <button class="ta-btn" data-demo="国际版 Pacdora（出海版演示）">国际版</button>
    </div>
"""
assert old_top in html, "topbar block not found"
html = html.replace(old_top, "")

# 2) remove sidebar 服务 group in NAV (last group, no trailing comma)
grp = """  {label:'服务', children:[
    {id:'service', label:'包装服务台', icon:IC.service, demo:'包装服务台（印刷/报价服务演示）'},
    {id:'team', label:'团队版', icon:IC.team, demo:'团队版（多人协作演示）'}
  ]}
];
"""
assert grp in html, "service group not found"
html = html.replace(grp, "];")

with io.open(P, "w", encoding="utf-8") as f:
    f.write(html)
print("OK, removed topbar buttons + sidebar 服务 group, size:", len(html))
