# -*- coding: utf-8 -*-
import os, av

VID = r"C:\Users\CT\Desktop\新建文件夹 (2)\视频功能介绍.mp4"
OUT = r"C:\Users\CT\Doubao\chats\2026-09-22\new-chat-1\baoxiaohe-clone\_verify\video_frames"
os.makedirs(OUT, exist_ok=True)

container = av.open(VID)
stream = container.streams.video[0]
print("duration(s):", float(stream.duration * stream.time_base), " fps:", stream.average_rate, " size:", stream.width, "x", stream.height)

# key time points following the transcript segments
points = [3, 8, 14, 20, 26, 31, 36, 41, 46, 52, 58, 64, 70, 76, 82, 88, 94, 100, 106, 112, 116]

import av
def extract(sec):
    container.seek(int(sec / stream.time_base), stream=stream, backward=True)
    for frame in container.decode(stream):
        if frame.time * 1.0 >= sec - 0.1:
            img = frame.to_image()
            img.save(os.path.join(OUT, f"t{sec:03d}.jpg"), quality=88)
            print("saved", sec)
            break

for p in points:
    try:
        extract(p)
    except Exception as e:
        print("fail", p, e)
print("DONE")
