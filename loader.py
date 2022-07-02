from TikTokApi import TikTokApi
import os
import yt_dlp
import shutil
from sys import argv

if len(argv) == 1:
    print("Укажите имя аккаунта!")
    try:
        f = open(".\\latest.txt", "r")
        last = f.read()
        if last != "":
            print("Использовать последний аккаунт? " + last)
        f.close()
    except:
        pass
    name = input()
    if name == "":
        try:
            name = last
        except:
            exit()
else:
    name = argv[1]


last = open(".\\latest.txt", "w")
last.write(name)
last.close()

print("Скачиваю видео пользователя: " + name)

ydl_opts = {
    "format": "best",
    "outtmpl": "video.mp4",
    "overwrites": True,
    "quiet": True}


api = TikTokApi.get_instance(use_test_endpoints=True, generate_static_device_id=True)


eivettta = api.by_username(name, count=30)


os.system("mkdir " + name)

for post in eivettta:
    video_id = post["video"]["id"]
    if not os.path.exists(".\\" + name + "\\" + name + "_" + video_id + "_tiktok.mp4"):
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download(["https://www.tiktok.com/@" + name + "/video/" + video_id])

        shutil.copy2(".\\video.mp4", ".\\" + name + "\\" + name + "_" + video_id + "_tiktok.mp4", follow_symlinks=True)
        os.remove("video.mp4")
        print("Downloaded: " + video_id)
    else:
        print(video_id + " уже скачан")
