import json, re, subprocess, sys

SHOT = r"C:\Users\CT\AppData\Local\Doubao\User Data\Default\.doubao\agent_mode\workspace\.skills\html\scripts\shot.py"

def check(path, label):
    r = subprocess.run(["python", SHOT, path], capture_output=True, text=True, encoding="utf-8", errors="replace")
    out = r.stdout
    m = re.search(r"\{.*\"elapsedSec\"", out, re.S)
    if not m:
        print(label, "no json found"); return
    try:
        data = json.loads(m.group(0))
    except Exception as e:
        print(label, "json parse fail", e); return
    for v in ["desktop", "mobile"]:
        sh = data.get("shots", {}).get(v, {})
        db = sh.get("deadButtons", [])
        real = [d for d in db if "ancestor-has-data-attr" not in d.get("note", "")]
        ce = sh.get("consoleErrors", [])
        re2 = sh.get("resourceErrors", [])
        ce_real = [c for c in ce if "box-gift.jpg" not in c.get("text","") and "_verify" not in c.get("location","")]
        re_real = [c for c in re2 if "_verify" not in c.get("url","")]
        print(f"{label} [{v}] consoleErrors(real): {len(ce_real)}, resourceErrors(real): {len(re_real)}, deadButtons(no-note): {len(real)}")
        for d in real[:8]:
            print("   DB:", d.get("tag"), d.get("text"), "|", d.get("reason"), "|", d.get("rect"))

check(r"C:\Users\CT\Doubao\chats\2026-09-22\new-chat-1\baoxiaohe-clone\_verify\v-editor.html", "EDITOR")
check(r"C:\Users\CT\Doubao\chats\2026-09-22\new-chat-1\baoxiaohe-clone\_verify\v-render.html", "RENDER")
check(r"C:\Users\CT\Doubao\chats\2026-09-22\new-chat-1\baoxiaohe-clone\_verify\v-album.html", "ALBUM")
