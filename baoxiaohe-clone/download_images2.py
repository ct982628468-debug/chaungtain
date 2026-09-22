import urllib.request
import os

BASE = r"C:\Users\CT\Doubao\chats\2026-09-22\new-chat-1\baoxiaohe-clone\assets"
imgs = {
    "box-glass.jpg": "https://aka.doubaocdn.com/s/p44Z2zUp0W",
    "box-irregular.jpg": "https://aka.doubaocdn.com/s/2vLWw6QAfW",
    "box-insert.jpg": "https://aka.doubaocdn.com/s/iZb1Es99tV",
    "box-cup.jpg": "https://aka.doubaocdn.com/s/4SYtl7wQzb",
}
for name, url in imgs.items():
    path = os.path.join(BASE, name)
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=60) as r, open(path, "wb") as f:
            f.write(r.read())
        print("OK", name, os.path.getsize(path))
    except Exception as e:
        print("FAIL", name, repr(e))
