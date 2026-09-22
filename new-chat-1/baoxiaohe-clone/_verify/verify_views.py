import re, os, shutil, subprocess

SRC = r"C:\Users\CT\Doubao\chats\2026-09-22\new-chat-1\baoxiaohe-clone\包小盒同款功能模板.html"
TMP = r"C:\Users\CT\Doubao\chats\2026-09-22\new-chat-1\baoxiaohe-clone\_verify"
SHOT = r"C:\Users\CT\AppData\Local\Doubao\User Data\Default\.doubao\agent_mode\workspace\.skills\html\scripts\shot.py"
os.makedirs(TMP, exist_ok=True)

with open(SRC, "r", encoding="utf-8") as f:
    html = f.read()

for view in ["editor", "render", "album"]:
    out = os.path.join(TMP, f"v-{view}.html")
    # inject hash set right after <body> so route() reads it
    injected = html.replace("<body>", '<body><script>location.hash="#/' + view + '";</script>', 1)
    with open(out, "w", encoding="utf-8") as f:
        f.write(injected)
    r = subprocess.run(["python", SHOT, out], capture_output=True, text=True, encoding="utf-8", errors="replace")
    print("=== ", view, " exit:", r.returncode)
    # print key check fields
    for line in r.stdout.splitlines():
        if any(k in line for k in ['"consoleErrors"', '"consoleWarnings"', '"resourceErrors"', '"horizontalOverflow"', 'screenshot"', 'firstH1', '"h1"', 'clippedText', 'overlappingText', 'deadButtons"']):
            print("   ", line.strip()[:120])
print("DONE")
