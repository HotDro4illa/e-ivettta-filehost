import shutil
import json
import os
from PIL import Image
size = 400, 400
dirlist = os.listdir('insta')
f = open('arch/accs.txt', 'w+')
f.write("\n".join(dirlist))
f.close()

for directory in dirlist:
    files = []
    counter = 0
    try:
        os.mkdir("arch/" + directory)
        print("Dir created: " + directory)
    except:
        pass

    for dirpath, dirnames, filenames in os.walk("insta/" + directory):
        for filename in filenames:
            if not os.path.exists('arch/' + directory + "/" + filename):
                if (filename == 'id') or (filename == 'list.json') or ("cover" in filename):
                    continue
                if "profile_pic" in filename:
                    src = os.path.join(dirpath, filename)
                    dst = 'arch/' + directory + "/profile_pic.jpg"
                    shutil.copy2(src, dst, follow_symlinks=True)
                    print('uploaded:', src)
                    continue
                if not os.path.exists("arch/" + directory + "/thumb_" + filename):
                    if filename[-1] == "g":
                        with Image.open(os.path.join(dirpath, filename)) as im:
                            im.thumbnail(size)
                            im.save('arch/' + directory + "/thumb_" + filename, "JPEG", quality=50, optimize=True)
                            print(filename + " --> thumb_" + filename)
                if not os.path.exists("arch/" + directory + "/thumb_" + filename + ".jpg"):
                    if filename[-1] == "4":
                        os.system("ffmpeg -ss 00:00:01.000 -i " + '"' + os.path.join(dirpath, filename) + '"' + " -loglevel quiet -n -vframes 1 arch/" + directory + "/thumb_" + filename + ".jpg")
                        print(filename + " --> thumb_" + filename + ".jpg")
                src = os.path.join(dirpath, filename)
                dst = 'arch/' + directory + "/" + filename
                shutil.copy2(src, dst, follow_symlinks=True)
                print('uploaded:', src)
            if (filename != 'id') and (filename != 'list.json') and ("cover" not in filename):
                files.append(filename)

    result = {"gallery": {"videos": [], "photos": [], "tiktok": []}}
    files.sort()

    for file in files:
        if "mp4" in file and "tiktok" not in file and "jpg" not in file:
            year = file.split("_")[0].split("-")
            year.reverse()
            year = ".".join(year)
            minute = ":".join(file.split("_")[1].split("-"))
            time = year + "_" + minute
            if file.split(".")[0].split("_")[-1] == "UTC":
                if os.path.exists('arch/' + directory + "/" + file.split(".")[0] + "_comments.json"):
                    comms = json.load(open('arch/' + directory + "/" + file.split(".")[0] + "_comments.json", "r"))
                else:
                    comms = ""
                if os.path.exists('arch/' + directory + "/" + file.split(".")[0] + ".txt"):
                    desc = open('arch/' + directory + "/" + file.split(".")[0] + ".txt", "r").read()
                else:
                    desc = ""
            else:
                if file.split(".")[0].split("_")[-2] == "UTC":
                    if os.path.exists('arch/' + directory + "/" + "_".join(file.split(".")[0].split("_")[0:3]) + "_comments.json"):
                        comms = json.load(open('arch/' + directory + "/" + "_".join(file.split(".")[0].split("_")[0:3]) + "_comments.json", "r"))
                    else:
                        comms = ""
                    if os.path.exists('arch/' + directory + "/" + "_".join(file.split(".")[0].split("_")[0:3]) + ".txt"):
                        desc = open('arch/' + directory + "/" + "_".join(file.split(".")[0].split("_")[0:3]) + ".txt", "r").read()
                    else:
                        desc = ""
            result["gallery"]["videos"].append({"filename": file, "comments": comms, "description": desc, "time": time})
        if "jpg" in file and "thumb" not in file:
            year = file.split("_")[0].split("-")
            year.reverse()
            year = ".".join(year)
            minute = ":".join(file.split("_")[1].split("-"))
            time = year + "_" + minute
            if file.split(".")[0].split("_")[-1] == "UTC":
                if os.path.exists('arch/' + directory + "/" + file.split(".")[0] + "_comments.json"):
                    comms = json.load(open('arch/' + directory + "/" + file.split(".")[0] + "_comments.json", "r"))
                else:
                    comms = ""
                if os.path.exists('arch/' + directory + "/" + file.split(".")[0] + ".txt"):
                    desc = open('arch/' + directory + "/" + file.split(".")[0] + ".txt", "r").read()
                else:
                    desc = ""
            else:
                if file.split(".")[0].split("_")[-2] == "UTC":
                    if os.path.exists('arch/' + directory + "/" + "_".join(file.split(".")[0].split("_")[0:3]) + "_comments.json"):
                        comms = json.load(open('arch/' + directory + "/" + "_".join(file.split(".")[0].split("_")[0:3]) + "_comments.json", "r"))
                    else:
                        comms = ""
                    if os.path.exists('arch/' + directory + "/" + "_".join(file.split(".")[0].split("_")[0:3]) + ".txt"):
                        desc = open('arch/' + directory + "/" + "_".join(file.split(".")[0].split("_")[0:3]) + ".txt", "r").read()
                    else:
                        desc = ""
            result["gallery"]["photos"].append({"filename": file, "comments": comms, "description": desc, "time": time})
        if "tiktok" in file:
            time = ""
            if file.split(".")[0].split("_")[-1] == "UTC":
                if os.path.exists('arch/' + directory + "/" + file.split(".")[0] + "_comments.json"):
                    comms = json.load(open('arch/' + directory + "/" + file.split(".")[0] + "_comments.json", "r"))
                else:
                    comms = ""
                if os.path.exists('arch/' + directory + "/" + file.split(".")[0] + ".txt"):
                    desc = open('arch/' + directory + "/" + file.split(".")[0] + ".txt", "r").read()
                else:
                    desc = ""
            else:
                if file.split(".")[0].split("_")[-2] == "UTC":
                    if os.path.exists('arch/' + directory + "/" + "_".join(file.split(".")[0].split("_")[0:3]) + "_comments.json"):
                        comms = json.load(open('arch/' + directory + "/" + "_".join(file.split(".")[0].split("_")[0:3]) + "_comments.json", "r"))
                    else:
                        comms = ""
                    if os.path.exists('arch/' + directory + "/" + "_".join(file.split(".")[0].split("_")[0:3]) + ".txt"):
                        desc = open('arch/' + directory + "/" + "_".join(file.split(".")[0].split("_")[0:3]) + ".txt", "r").read()
                    else:
                        desc = ""
            result["gallery"]["tiktok"].append({"filename": file, "comments": comms, "description": desc, "time": time})

    with open('arch/' + directory + '/gallery.json', 'w+') as outfile:
        json.dump(result, outfile, indent=4)
    print('arch/' + directory + '/gallery.json изменён')

    result = {"feed": []}

    for file in files:
        if "txt" not in file and "json" not in file:
            if len(file.split("_")) == 4 and file.split("_")[3].split(".")[0].isnumeric() == True:
                if file.split("_")[3].split(".")[0] == "1":
                    if os.path.exists('arch/' + directory + "/" + file.split("_")[0] + "_" + file.split("_")[1] + "_UTC_comments.json"):
                        comms = json.load(open('arch/' + directory + "/" + file.split("_")[0] + "_" + file.split("_")[1] + "_UTC_comments.json", "r"))
                    else:
                        comms = ""
                    if os.path.exists('arch/' + directory + "/" + file.split("_")[0] + "_" + file.split("_")[1] + "_UTC.txt"):
                        desc = open('arch/' + directory + "/" + file.split("_")[0] + "_" + file.split("_")[1] + "_UTC.txt", "r").read()
                    else:
                        desc = ""
                    year = file.split("_")[0].split("-")
                    year.reverse()
                    year = ".".join(year)
                    minute = ":".join(file.split("_")[1].split("-"))
                    time = year + "_" + minute
                    result["feed"].append({"post": [file], "description": desc, "comments": comms, "time": time})
                else:
                    result["feed"][-1]["post"].append(file)
            elif "thumb" not in file:
                if os.path.exists('arch/' + directory + "/" + file.split(".")[0] + "_comments.json"):
                    comms = json.load(open('arch/' + directory + "/" + file.split(".")[0] + "_comments.json", "r"))
                else:
                    comms = ""
                if os.path.exists('arch/' + directory + "/" + file.split(".")[0] + ".txt"):
                    desc = open('arch/' + directory + "/" + file.split(".")[0] + ".txt", "r").read()
                else:
                    desc = ""
                year = file.split("_")[0].split("-")
                year.reverse()
                year = ".".join(year)
                minute = ":".join(file.split("_")[1].split("-"))
                time = year + "_" + minute
                result["feed"].append({"post": [file], "description": desc, "comments": comms, "time": time})

    with open('arch/' + directory + '/feed.json', 'w+') as outfile:
        json.dump(result, outfile, indent=4)
    print('arch/' + directory + '/feed.json изменён')

