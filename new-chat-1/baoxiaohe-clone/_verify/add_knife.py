# -*- coding: utf-8 -*-
import io, re

P = r"C:\Users\CT\Doubao\chats\2026-09-22\new-chat-1\baoxiaohe-clone\包小盒同款功能模板.html"
with io.open(P, "r", encoding="utf-8") as f:
    html = f.read()

# ---------- 1) CSS: knife converter styles ----------
anchor_css = "/* ===== 设计编辑器 ===== */"
assert html.count(anchor_css) == 1, "css anchor"
knife_css = """/* ===== 私有刀版3D转换器 ===== */
.knife-shell{display:flex;flex-direction:column;background:#fff;border:1px solid var(--line);border-radius:12px;overflow:hidden;min-height:calc(100vh - 140px)}
.knife-top{display:flex;align-items:center;gap:10px;border-bottom:1px solid var(--line);padding:8px 14px;background:#fff;flex-wrap:wrap}
.knife-top .tool-name{color:var(--accent);font-weight:700;font-size:14px;margin-right:4px}
.knife-top .file-chip{display:inline-flex;align-items:center;gap:6px;background:var(--bg);border:1px solid var(--line);border-radius:7px;padding:5px 12px;font-size:13px;color:var(--ink-2);cursor:pointer}
.knife-top .file-chip svg{width:14px;height:14px;color:var(--muted)}
.knife-body{display:flex;flex:1;min-height:0}
.knife-preview{width:210px;border-right:1px solid var(--line);padding:14px;background:#F7F8FA;display:flex;flex-direction:column;gap:10px}
.knife-preview .pv{background:#fff;border:1px solid var(--line);border-radius:10px;padding:10px;text-align:center}
.knife-preview .pv img{width:100%;display:block;border-radius:6px}
.knife-preview .pv .cap{font-size:12px;color:var(--muted);margin-top:6px}
.knife-stage{flex:1;background:#F3F4F6;display:flex;align-items:center;justify-content:center;position:relative;overflow:hidden;min-height:420px}
.knife-sheet{background:#fff;box-shadow:0 6px 28px rgba(20,24,35,.14);border-radius:8px;max-width:min(52vh,430px);width:100%;position:relative;transition:transform .3s}
.knife-sheet img{display:block;width:100%;border-radius:8px}
.knife-bend{position:absolute;width:18px;height:18px;border-radius:50%;background:#FF4D3E;color:#fff;font-size:9px;display:flex;align-items:center;justify-content:center;font-weight:700;border:2px solid #fff;box-shadow:0 2px 6px rgba(0,0,0,.3);cursor:pointer;transform:translate(-50%,-50%)}
.knife-bend .val{position:absolute;left:50%;top:-22px;transform:translateX(-50%);background:#2A2E37;color:#fff;font-size:10px;padding:2px 6px;border-radius:4px;white-space:nowrap}
.knife-right{width:262px;border-left:1px solid var(--line);overflow-y:auto;background:#fff}
.knife-right .sec{padding:12px 14px;border-bottom:1px solid var(--line)}
.knife-right .sec h4{font-size:13px;font-weight:700;margin-bottom:8px;display:flex;align-items:center;justify-content:space-between}
.knife-right .sec h4 .tog{font-size:12px;color:var(--accent);cursor:pointer;font-weight:500}
.fold-row{display:flex;align-items:center;justify-content:space-between;font-size:12px;color:var(--ink-2);padding:5px 6px;border-radius:6px;margin:2px 0;cursor:pointer}
.fold-row:hover{background:var(--bg)}
.fold-row.on{background:var(--accent-soft);color:var(--accent);font-weight:600}
.fold-row select{height:26px;border:1px solid var(--line);border-radius:6px;font-size:12px;padding:0 4px;background:#fff;color:var(--ink);cursor:pointer}
.knife-foot{display:flex;align-items:center;gap:16px;border-top:1px solid var(--line);padding:10px 14px;background:#fff;flex-wrap:wrap}
.knife-foot .kf-label{font-size:12px;color:var(--muted);display:flex;align-items:center;gap:6px;white-space:nowrap}
.knife-foot input[type=range]{accent-color:var(--accent);width:170px}
.knife-foot .kf-btn{background:var(--accent);color:#fff;font-weight:700;padding:8px 18px;border-radius:8px;font-size:13px;cursor:pointer}
.knife-foot .kf-btn.ghost{background:var(--bg);color:var(--ink-2);border:1px solid var(--line)}
.knife-hint{font-size:11px;color:var(--muted)}
@media (max-width:860px){
  .knife-preview{display:none}
  .knife-right{width:210px}
}
""" + anchor_css
html = html.replace(anchor_css, knife_css, 1)

# ---------- 2) HTML: view-knife section ----------
anchor_view = "      <!-- ===== 视图：设计编辑器（复刻 3D云设计编辑器） ===== -->"
assert html.count(anchor_view) == 1, "view anchor"
knife_view = """      <!-- ===== 视图：私有刀版3D转换器（复刻） ===== -->
      <section class="view" id="view-knife">
        <div class="knife-shell">
          <div class="knife-top">
            <span class="tool-name">私有刀版3D转换器</span>
            <span class="file-chip" id="knifeImport"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v12m0 0 4-4m-4 4-4-4"/><path d="M4 17v2a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2v-2"/></svg>导入DXF文件</span>
            <span class="file-chip" style="cursor:default">展示盒刀模.dxf</span>
          </div>
          <div class="knife-body">
            <div class="knife-preview">
              <div class="pv"><img src="assets/knife-diecut.jpg" id="knife3d" alt="3D 预览"><div class="cap">3D 模型预览</div></div>
              <div class="pv"><img src="assets/box-gift.jpg" alt="成品预览"><div class="cap">折叠后效果</div></div>
            </div>
            <div class="knife-stage">
              <div class="knife-sheet" id="knifeSheet">
                <img src="assets/knife-diecut.jpg" alt="刀版展开图" id="knifeSheetImg">
                <div class="knife-bend" data-b="0" style="left:30%;top:22%"><span class="val">90°</span>折</div>
                <div class="knife-bend" data-b="1" style="left:70%;top:22%"><span class="val">90°</span>折</div>
                <div class="knife-bend" data-b="2" style="left:30%;top:45%"><span class="val">90°</span>折</div>
                <div class="knife-bend" data-b="3" style="left:70%;top:45%"><span class="val">90°</span>折</div>
                <div class="knife-bend" data-b="4" style="left:30%;top:72%"><span class="val">90°</span>折</div>
                <div class="knife-bend" data-b="5" style="left:70%;top:72%"><span class="val">90°</span>折</div>
              </div>
            </div>
            <div class="knife-right">
              <div class="sec"><h4>设置</h4></div>
              <div class="sec"><h4>基础参数</h4>
                <div class="frow"><span>材质</span><select id="knifeMat" style="height:28px;border:1px solid var(--line);border-radius:6px;font-size:12px;padding:0 6px"><option>自定义材质</option><option>白卡纸</option><option>瓦楞纸</option><option>铜版纸</option></select></div>
                <div class="frow"><span>厚度(0.1~15mm)</span><b id="knifeThick">3.0mm</b></div>
                <div class="frow"><input type="range" id="knifeThickRange" min="0.1" max="15" step="0.1" value="3"></div>
                <div class="frow"><span>动画</span><div class="switch on" id="knifeAnim"></div></div>
              </div>
              <div class="sec"><h4>折线角度 <span class="tog" id="knifeSelAll">全选折线</span></h4>
                <div id="knifeFolds"></div>
                <div class="knife-hint" style="margin-top:6px">按住 shift 可多选 / 取消折线；0° 为平铺，90° 为标准折叠</div>
              </div>
            </div>
          </div>
          <div class="knife-foot">
            <span class="kf-label">展开</span>
            <input type="range" id="knifeOpen" min="0" max="100" value="60">
            <span class="kf-label">闭合 <b id="knifeOpenVal">60%</b></span>
            <button class="kf-btn" data-goto="editor">创建设计</button>
            <button class="kf-btn ghost" data-demo="保存定制的刀版（演示）">保存定制的刀版</button>
          </div>
        </div>
      </section>

""" + anchor_view
html = html.replace(anchor_view, knife_view, 1)

# ---------- 3) NAV: add 刀版3D转换器 ----------
anchor_nav = "    {id:'editor', label:'设计编辑器', icon:IC.design},"
assert html.count(anchor_nav) == 1, "nav anchor"
html = html.replace(anchor_nav, "    {id:'knife', label:'刀版3D转换器', icon:IC.box},\n" + anchor_nav, 1)

# ---------- 4) VIEWS map ----------
old_views = "const VIEWS = {home:'view-home', designs:'view-designs', renders:'view-renders', favorites:'view-favorites', templates:'view-templates', models:'view-models', scenes:'view-scenes', editor:'view-editor', render:'view-render', album:'view-album'};"
assert html.count(old_views) == 1, "views anchor"
html = html.replace(old_views, "const VIEWS = {home:'view-home', designs:'view-designs', renders:'view-renders', favorites:'view-favorites', templates:'view-templates', models:'view-models', scenes:'view-scenes', knife:'view-knife', editor:'view-editor', render:'view-render', album:'view-album'};", 1)

# ---------- 5) route dispatch ----------
old_grid = "{designs:renderDesigns, renders:renderRenders, favorites:renderFavs, templates:renderTpls, models:renderBoxes, scenes:renderScenes, home:renderHome, editor:renderEditor, render:renderRender, album:renderAlbum}[view]"
assert html.count(old_grid) == 1, "grid anchor"
html = html.replace(old_grid, "{designs:renderDesigns, renders:renderRenders, favorites:renderFavs, templates:renderTpls, models:renderBoxes, scenes:renderScenes, home:renderHome, knife:renderKnife, editor:renderEditor, render:renderRender, album:renderAlbum}[view]", 1)

with io.open(P, "w", encoding="utf-8") as f:
    f.write(html)
print("OK part1, size:", len(html))
