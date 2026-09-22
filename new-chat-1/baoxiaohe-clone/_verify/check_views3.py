# -*- coding: utf-8 -*-
import os, io, subprocess, re

SRC = r"C:\Users\CT\Doubao\chats\2026-09-22\new-chat-1\baoxiaohe-clone\包小盒同款功能模板.html"
SHOT = r"C:\Users\CT\AppData\Local\Doubao\User Data\Default\.doubao\agent_mode\workspace\.skills\html\scripts\shot.py"

def grab(text, key):
    m = re.search(r'"%s":\s*(\[[^\]]*\])' % key, text)
    if not m:
        # array may span; find from key to next top-level field
        m = re.search(r'"%s":\s*(\[)' % key, text)
        if not m: return "?"
        start = m.start(1)
        depth = 0
        for i in range(start, len(text)):
            if text[i] == '[': depth += 1
            elif text[i] == ']':
                depth -= 1
                if depth == 0:
                    return text[start:i+1]
        return "?"
    return m.group(1)

with io.open(SRC, "r", encoding="utf-8") as f:
    html = f.read()

for view in ["knife", "render"]:
    out = os.path.join(r"C:\Users\CT\Doubao\chats\2026-09-22\new-chat-1\baoxiaohe-clone", f"_v-{view}.html")
    injected = html.replace("<body>", '<body><script>location.hash="#/' + view + '";</script>', 1)
    with io.open(out, "w", encoding="utf-8") as f:
        f.write(injected)
    r = subprocess.run(["python", SHOT, out], capture_output=True, text=True, encoding="utf-8", errors="replace")
    txt = r.stdout
    print("===", view)
    print("   consoleErrors:", grab(txt, "consoleErrors")[:300])
    print("   resourceErrors:", grab(txt, "resourceErrors")[:300])
    print("   horizontalOverflow:", grab(txt, "horizontalOverflow")[:200])
print("DONE")
