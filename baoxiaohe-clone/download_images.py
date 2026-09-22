import urllib.request
import os

BASE = r"C:\Users\CT\Doubao\chats\2026-09-22\new-chat-1\baoxiaohe-clone\assets"
os.makedirs(BASE, exist_ok=True)

imgs = {
    "box-bag.jpg": "https://aka.doubaocdn.com/s/QbjQHP4U21",
    "box-gift.jpg": "https://aka.doubaocdn.com/s/sjE9yf7Xsl",
    "box-flip.jpg": "https://aka.doubaocdn.com/s/sMjefLKRGH",
    "box-bottle.jpg": "https://aka.doubaocdn.com/s/sw4uO1v8Uy",
    "box-carton.jpg": "https://aka.doubaocdn.com/s/8u0XG2wcWX",
    "box-pouch.jpg": "https://aka.doubaocdn.com/s/VixQZ3WM8q",
    "box-can.jpg": "https://aka.doubaocdn.com/s/fAmmFSDTMy",
    "box-display.jpg": "https://aka.doubaocdn.com/s/Z2NTzdhbU3",
    "scene-glass.jpg": "https://aka.doubaocdn.com/s/6DU3ZAlpTN",
    "scene-minimal.jpg": "https://aka.doubaocdn.com/s/Vnqh28hgZd",
    "scene-chinese.jpg": "https://aka.doubaocdn.com/s/euXZaovyNM",
    "scene-ecommerce.jpg": "https://aka.doubaocdn.com/s/5YRA2DHufq",
    "scene-live.jpg": "https://aka.doubaocdn.com/s/QLO54DKZwe",
    "scene-festival.jpg": "https://aka.doubaocdn.com/s/maqN4m6BZU",
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
