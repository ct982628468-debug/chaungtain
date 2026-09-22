# -*- coding: utf-8 -*-
import io

P = r"C:\Users\CT\Doubao\chats\2026-09-22\new-chat-1\baoxiaohe-clone\包小盒同款功能模板.html"
with io.open(P, "r", encoding="utf-8") as f:
    html = f.read()

# ---------- A) knife data + renderKnife ----------
anchor_rc = "/* ================= 云渲染控制台 ================= */"
assert html.count(anchor_rc) == 1, "rc anchor"
knife_js = """/* ================= 私有刀版3D转换器 ================= */
const KNIFE_FOLDS = ['折线1-2','折线1-8','折线11-1','折线22-23','折线19-18','折线0-11'];
const KNIFE_ANGS = ['0°','45°','90°','135°','180°'];
function renderKnife(){
  el('knifeFolds').innerHTML = KNIFE_FOLDS.map((n,i)=>`<div class="fold-row on" data-fi="${i}"><span>${n}</span><select data-fi="${i}">${KNIFE_ANGS.map(a=>`<option ${a==='90°'?'selected':''}>${a}</option>`).join('')}</select></div>`).join('');
  syncKnifeBends();
}
function syncKnifeBends(){
  document.querySelectorAll('#knifeSheet .knife-bend').forEach(b=>{
    const sel = el('knifeFolds').querySelector(`select[data-fi="${b.dataset.b}"]`);
    b.querySelector('.val').textContent = sel ? sel.value : '90°';
    b.style.background = sel && sel.value==='0°' ? '#9AA1AF' : '#FF4D3E';
  });
}
function bindKnife(){
  el('knifeImport').addEventListener('click', ()=>toast('正在解析 DXF 文件：展示盒刀模.dxf（演示）'));
  el('knifeMat').addEventListener('change', e=>toast('材质已切换为「'+e.target.value+'」（演示）'));
  el('knifeThickRange').addEventListener('input', e=>el('knifeThick').textContent=(+e.target.value).toFixed(1)+'mm');
  el('knifeAnim').addEventListener('click', ()=>{el('knifeAnim').classList.toggle('on'); toast('折叠动画已'+(el('knifeAnim').classList.contains('on')?'开启':'关闭')+'（演示）')});
  el('knifeSelAll').addEventListener('click', ()=>{
    const all = el('knifeFolds').querySelectorAll('.fold-row');
    const turnOn = [...all].some(r=>!r.classList.contains('on'));
    all.forEach(r=>r.classList.toggle('on', turnOn));
  });
  el('knifeFolds').addEventListener('click', e=>{
    const r=e.target.closest('.fold-row'); if(!r) return;
    r.classList.toggle('on');
  });
  el('knifeFolds').addEventListener('change', e=>{
    const s=e.target.closest('select'); if(!s) return;
    syncKnifeBends();
    toast('折线 ' + KNIFE_FOLDS[+s.dataset.fi] + ' 角度设为 ' + s.value + '（演示）');
  });
  el('knifeOpen').addEventListener('input', e=>{
    const v=+e.target.value;
    el('knifeOpenVal').textContent=v+'%';
    el('knifeSheet').style.transform = `perspective(900px) rotateX(${(v/100)*70}deg)`;
    el('knifeSheetImg').style.opacity = 0.5 + (v/100)*0.5;
  });
  el('rfSubTabs').addEventListener('click', e=>{
    const b=e.target.closest('button'); if(!b) return;
    el('rfSubTabs').querySelectorAll('button').forEach(x=>x.classList.remove('on')); b.classList.add('on');
    toast(b.textContent+' 属性面板（演示）');
  });
  el('rfBoxShadow').addEventListener('input', e=>{
    el('rfShadow').classList.add('on');
  });
  el('rfBgColor').addEventListener('input', e=>{
    const m=document.querySelector('#view-render .render-main');
    m.style.background = e.target.value;
  });
  el('rfSearch').addEventListener('input', ()=>applyRfFilter());
}

""" + anchor_rc
html = html.replace(anchor_rc, knife_js, 1)

# ---------- B) rfSceneList: search box + PRO badge ----------
old_rf = """function rfSceneList(){
  return `<div class="rl-filters">
      <select id="rfUse"><option value="all">全部用途</option><option>电商运营</option><option>宣传推广</option><option>销售促单</option><option>营销卖货</option><option>社媒运营</option></select>
      <select id="rfInd"><option value="all">全部行业</option><option>食品饮料</option><option>美妆个护</option><option>生活日化</option><option>数码家电</option></select>
      <select id="rfColor"><option value="all">全部颜色</option><option>白</option><option>绿</option><option>暖</option><option>橙</option><option>蓝</option><option>红</option><option>紫</option></select>
    </div>
    <div id="rfSceneGrid">${R_SCENES.map((s,i)=>`<div class="rl-item ${i===RF_STATE.stage?'on':''}" data-stage="${i}"><img src="${s.img}" alt="${s.name}"><div><div class="n">${s.name}</div><div class="s">${s.use} · ${s.ind}</div></div></div>`).join('')}</div>`;
}"""
assert html.count(old_rf) == 1, "rf list anchor"
new_rf = """function rfSceneList(){
  return `<div class="rl-filters">
      <input id="rfSearch" placeholder="请输入您想要的场景" style="height:28px;border-radius:6px;background:#2A2E37;border:1px solid #333846;color:#D6DAE2;font-size:12px;padding:0 8px;outline:none">
      <select id="rfUse"><option value="all">全部用途</option><option>电商运营</option><option>宣传推广</option><option>销售促单</option><option>营销卖货</option><option>社媒运营</option></select>
      <select id="rfInd"><option value="all">全部行业</option><option>食品饮料</option><option>美妆个护</option><option>生活日化</option><option>数码家电</option></select>
      <select id="rfColor"><option value="all">全部颜色</option><option>白</option><option>绿</option><option>暖</option><option>橙</option><option>蓝</option><option>红</option><option>紫</option></select>
    </div>
    <div id="rfSceneGrid">${R_SCENES.map((s,i)=>`<div class="rl-item ${i===RF_STATE.stage?'on':''}" data-stage="${i}"><img src="${s.img}" alt="${s.name}"><div><div class="n">${s.name}${i%4===1?'<span style="font-size:9px;background:#FFB27A;color:#16181D;border-radius:3px;padding:1px 4px;margin-left:4px;font-weight:700">PRO</span>':''}</div><div class="s">${s.use} · ${s.ind}</div></div></div>`).join('')}</div>`;
}"""
html = html.replace(old_rf, new_rf, 1)

# ---------- C) render props: sub tabs + box shadow + bg color ----------
old_props = '              <h4>属性编辑区</h4>'
assert html.count(old_props) == 1, "props anchor"
new_props = """              <h4>属性编辑区</h4>
              <div style="display:flex;gap:4px;background:#2A2E37;border-radius:8px;padding:3px;margin-bottom:10px" id="rfSubTabs"><button class="rb-btn on">场景</button><button class="rb-btn">模型</button><button class="rb-btn">光影</button></div>
              <div class="rp-row"><span>Box 阴影</span><input type="range" min="0" max="100" value="50" id="rfBoxShadow"></div>
              <div class="rp-row"><span>背景颜色</span><input type="color" id="rfBgColor" value="#16181D" style="width:28px;height:24px;border:none;background:none;padding:0"></div>"""
html = html.replace(old_props, new_props, 1)

# ---------- D) bindToolEvents: call bindKnife at end ----------
old_end = """  el('albumSeg').addEventListener('click', e=>{
    const b=e.target.closest('button'); if(!b) return;
    el('albumSeg').querySelectorAll('button').forEach(x=>x.classList.remove('on')); b.classList.add('on');
    S.albumKind=b.dataset.k; renderAlbum();
  });
}"""
assert html.count(old_end) == 1, "bind end anchor"
new_end = """  el('albumSeg').addEventListener('click', e=>{
    const b=e.target.closest('button'); if(!b) return;
    el('albumSeg').querySelectorAll('button').forEach(x=>x.classList.remove('on')); b.classList.add('on');
    S.albumKind=b.dataset.k; renderAlbum();
  });
  bindKnife();
}"""
html = html.replace(old_end, new_end, 1)

# ---------- E) bindRfFilters: support search + expose applyRfFilter ----------
old_apply = """function bindRfFilters(){
  const u=el('rfUse'), i=el('rfInd'), c=el('rfColor');
  if(!u||!i||!c) return;
  const grid=el('rfSceneGrid'); if(!grid) return;
  function apply(){
    let list=R_SCENES;
    if(u.value!=='all') list=list.filter(s=>s.use===u.value);
    if(i.value!=='all') list=list.filter(s=>s.ind===i.value);
    if(c.value!=='all') list=list.filter(s=>s.color===c.value);
    grid.innerHTML=list.map((s,idx)=>`<div class="rl-item" data-stage="${R_SCENES.indexOf(s)}"><img src="${s.img}" alt="${s.name}"><div><div class="n">${s.name}</div><div class="s">${s.use} · ${s.ind}</div></div></div>`).join('');
  }
  [u,i,c].forEach(x=>x.addEventListener('change', apply));
  grid.addEventListener('click', e=>{
    const it=e.target.closest('.rl-item[data-stage]'); if(!it) return;
    RF_STATE.stage=+it.dataset.stage;
    const s=R_SCENES[RF_STATE.stage];
    el('rfStage').src=s.img; el('rfStageName').textContent=s.name;
    grid.querySelectorAll('.rl-item').forEach(x=>x.classList.toggle('on', x===it));
  });
}"""
assert html.count(old_apply) == 1, "apply anchor"
new_apply = """function applyRfFilter(){
  const u=el('rfUse'), i=el('rfInd'), c=el('rfColor'), q=el('rfSearch');
  if(!u||!i||!c) return;
  const grid=el('rfSceneGrid'); if(!grid) return;
  let list=R_SCENES;
  if(u.value!=='all') list=list.filter(s=>s.use===u.value);
  if(i.value!=='all') list=list.filter(s=>s.ind===i.value);
  if(c.value!=='all') list=list.filter(s=>s.color===c.value);
  if(q && q.value.trim()) list=list.filter(s=>s.name.includes(q.value.trim()));
  grid.innerHTML=list.map((s,idx)=>`<div class="rl-item" data-stage="${R_SCENES.indexOf(s)}"><img src="${s.img}" alt="${s.name}"><div><div class="n">${s.name}${R_SCENES.indexOf(s)%4===1?'<span style="font-size:9px;background:#FFB27A;color:#16181D;border-radius:3px;padding:1px 4px;margin-left:4px;font-weight:700">PRO</span>':''}</div><div class="s">${s.use} · ${s.ind}</div></div></div>`).join('');
}
function bindRfFilters(){
  const u=el('rfUse'), i=el('rfInd'), c=el('rfColor');
  if(!u||!i||!c) return;
  const grid=el('rfSceneGrid'); if(!grid) return;
  [u,i,c].forEach(x=>x.addEventListener('change', applyRfFilter));
  grid.addEventListener('click', e=>{
    const it=e.target.closest('.rl-item[data-stage]'); if(!it) return;
    RF_STATE.stage=+it.dataset.stage;
    const s=R_SCENES[RF_STATE.stage];
    el('rfStage').src=s.img; el('rfStageName').textContent=s.name;
    grid.querySelectorAll('.rl-item').forEach(x=>x.classList.toggle('on', x===it));
  });
}"""
html = html.replace(old_apply, new_apply, 1)

with io.open(P, "w", encoding="utf-8") as f:
    f.write(html)
print("OK part2, size:", len(html))
