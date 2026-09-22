# -*- coding: utf-8 -*-
import io

P = r"C:\Users\CT\Doubao\chats\2026-09-22\new-chat-1\baoxiaohe-clone\包小盒同款功能模板.html"
with io.open(P, "r", encoding="utf-8") as f:
    html = f.read()

# ---------- A) CSS: motion panel + banner + badges ----------
anchor_css = ".knife-hint{font-size:11px;color:var(--muted)}"
assert html.count(anchor_css) == 1, "css anchor"
css_add = """@keyframes edFold{0%{transform:rotateX(0)}100%{transform:rotateX(60deg)}}
@keyframes edSpinY{to{transform:rotateY(1turn)}}
@keyframes edSpinX{to{transform:rotateX(1turn)}}
@keyframes edDrop{0%{transform:translateY(-30%) rotate(-10deg);opacity:.2}100%{transform:translateY(0) rotate(0);opacity:1}}
.canvas-paper.mo-fold{animation:edFold 4s ease forwards}
.canvas-paper.mo-spinY{animation:edSpinY 5s linear}
.canvas-paper.mo-spinX{animation:edSpinX 3s linear}
.canvas-paper.mo-drop{animation:edDrop 2s ease}
.ed-motion-panel{position:absolute;right:12px;top:12px;background:#fff;border:1px solid var(--line);border-radius:10px;box-shadow:var(--shadow);padding:10px;width:196px;z-index:5}
.ed-motion-panel h5{font-size:12px;font-weight:700;margin-bottom:6px;color:var(--ink)}
.mo-item{display:flex;justify-content:space-between;align-items:center;padding:7px 8px;border-radius:7px;cursor:pointer;font-size:12px;color:var(--ink-2)}
.mo-item:hover{background:var(--bg)}
.mo-item .t{color:var(--accent);font-size:11px;font-weight:600}
.render-banner{display:flex;align-items:center;justify-content:space-between;background:linear-gradient(90deg,#2A2E37,#333846);color:#E8EBF0;font-size:12px;padding:7px 14px;border-bottom:1px solid #2A2E37}
.render-banner b{color:#FFB27A;font-weight:700}
.render-banner button{background:none;border:none;color:#9AA1AF;font-size:14px;cursor:pointer;line-height:1;padding:2px 6px}
.render-banner button:hover{color:#fff}
.album-card .res-badge{position:absolute;right:8px;top:8px;background:rgba(22,24,29,.72);color:#FFB27A;font-size:10px;padding:2px 7px;border-radius:5px;font-weight:600}
""" + anchor_css
html = html.replace(anchor_css, css_add, 1)

# ---------- B) motion panel HTML in editor canvas ----------
anchor_canvas = """              <div class="canvas-meta"><span>模型ID: 21127734</span><span id="zoomVal">100%</span><button id="zoomOut">-</button><button id="zoomIn">+</button></div>"""
assert html.count(anchor_canvas) == 1, "canvas anchor"
motion_html = """              <div class="ed-motion-panel" id="edMotionPanel" style="display:none">
                <h5>动效</h5>
                <div class="mo-item" data-m="fold">折叠展开<span class="t">4s</span></div>
                <div class="mo-item" data-m="spinY">物体平视自转一圈<span class="t">5s</span></div>
                <div class="mo-item" data-m="spinX">物体俯视自转一周<span class="t">3s</span></div>
                <div class="mo-item" data-m="drop">旋转掉落<span class="t">2s</span></div>
                <div class="mo-item" data-demo="下载 4K 高清图片（演示）">下载4K图片<span class="t">PRO</span></div>
              </div>
              <div class="canvas-meta"><span>模型ID: 21127734</span><span id="zoomVal">100%</span><button id="zoomOut">-</button><button id="zoomIn">+</button></div>"""
html = html.replace(anchor_canvas, motion_html, 1)

# ---------- C) render banner HTML ----------
anchor_rt = """            <div class="rt-saved"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg>22:21 已保存</div>
          </div>"""
assert html.count(anchor_rt) == 1, "rt anchor"
banner_html = """            <div class="rt-saved"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg>23:06 已保存</div>
          </div>
          <div class="render-banner" id="rfBanner"><span><b>V3.0 云渲染全新升级</b> — 所见即所得，创作照片级渲染</span><button id="rfBannerClose">×</button></div>"""
html = html.replace(anchor_rt, banner_html, 1)

# ---------- D) JS: motion + 3d panel toggle + banner close ----------
old_mode = """  el('edMode2d').addEventListener('click', ()=>{ED_STATE.mode='2d'; el('edMode2d').classList.add('on'); el('edMode3d').classList.remove('on'); el('canvasPaper').classList.add('dim2d')});
  el('edMode3d').addEventListener('click', ()=>{ED_STATE.mode='3d'; el('edMode3d').classList.add('on'); el('edMode2d').classList.remove('on'); el('canvasPaper').classList.remove('dim2d')});"""
assert html.count(old_mode) == 1, "mode anchor"
new_mode = """  el('edMode2d').addEventListener('click', ()=>{ED_STATE.mode='2d'; el('edMode2d').classList.add('on'); el('edMode3d').classList.remove('on'); el('canvasPaper').classList.add('dim2d'); el('edMotionPanel').style.display='none'});
  el('edMode3d').addEventListener('click', ()=>{ED_STATE.mode='3d'; el('edMode3d').classList.add('on'); el('edMode2d').classList.remove('on'); el('canvasPaper').classList.remove('dim2d'); el('edMotionPanel').style.display='block'});
  el('edMotionPanel').addEventListener('click', e=>{
    const it=e.target.closest('.mo-item[data-m]'); if(!it) return;
    const p=el('canvasPaper');
    p.classList.remove('mo-fold','mo-spinY','mo-spinX','mo-drop');
    void p.offsetWidth;
    p.classList.add('mo-'+it.dataset.m);
    toast('3D 动效演示：'+it.childNodes[0].textContent.trim()+'（'+it.querySelector('.t').textContent+'）');
    setTimeout(()=>p.classList.remove('mo-fold','mo-spinY','mo-spinX','mo-drop'), 5200);
  });
  el('rfBannerClose').addEventListener('click', ()=>el('rfBanner').style.display='none');"""
html = html.replace(old_mode, new_mode, 1)

# ---------- E) album cards: resolution badge ----------
old_album = '<div class="album-card" data-demo="打开渲染效果图「${a.name}」（演示）">'
assert html.count(old_album) == 1, "album anchor"
new_album = '<div class="album-card" data-demo="打开渲染效果图「${a.name}」（演示）" style="position:relative"><span class="res-badge">2K高清</span>'
html = html.replace(old_album, new_album, 1)

with io.open(P, "w", encoding="utf-8") as f:
    f.write(html)
print("OK, size:", len(html))
