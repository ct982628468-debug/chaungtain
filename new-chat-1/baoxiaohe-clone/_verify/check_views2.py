# -*- coding: utf-8 -*-
import os, io, subprocess

SRC = r"C:\Users\CT\Doubao\chats\2026-09-22\new-chat-1\baoxiaohe-clone\包小盒同款功能模板.html"
TMP = r"C:\Users\CT\Doubao\chats\2026-09-22\new-chat-1\baoxiaohe-clone\_verify"
SHOT = r"C:\Users\CT\AppData\Local\Doubao\User Data\Default\.doubao\agent_mode\workspace\.skills\html\scripts\shot.py"

with io.open(SRC, "r", encoding="utf-8") as f:
    html = f.read()

# temp copies need assets access: put copy into the clone dir itself
for view in ["knife", "render", "album"]:
    out = os.path.join(r"C:\Users\CT\Doubao\chats\2026-09-22\new-chat-1\baoxiaohe-clone", f"_v-{view}.html")
    injected = html.replace("<body>", '<body><script>location.hash="#/' + view + '";</script>', 1)
    with io.open(out, "w", encoding="utf-8") as f:
        f.write(injected)
    r = subprocess.run(["python", SHOT, out], capture_output=True, text=True, encoding="utf-8", errors="replace")
    print("===", view, "exit", r.returncode)
    import re, json
    m = re.search(r"\{.*\"elapsedSec\"", r.stdout, re.S)
    if m:
        try:
            d = json.loads(m.group(0))
            sh = d.get("shots", {}).get("desktop", {})
            print("   consoleErrors:", len([c for c in sh.get("consoleErrors", [])]))
            print("   resourceErrors:", len(sh.get("resourceErrors", [])))
            print("   horizontalOverflow:", len(sh.get("horizontalOverflow", [])))
            print("   deadButtons(no-note):", len([x for x in sh.get("deadButtons", []) if "ancestor-has-data-attr" not in x.get("note","")]))
        except Exception as e:
            print("   parse fail", e)
print("DONE")
