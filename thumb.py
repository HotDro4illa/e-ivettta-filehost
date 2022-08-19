import os

for dirpath, dirnames, filenames in os.walk("e_ivettta"):
    for filename in filenames:
        if not os.path.exists("e_ivettta/thumbs/thumb_" + filename + ".jpg"):
            if filename[-1] == "4":

                os.system("ffmpeg -ss 00:00:01.000 -i " + '"' + os.path.join(dirpath, filename) + '"' + " -loglevel quiet -n -vframes 1 e_ivettta/thumbs/thumb_" + filename + ".jpg")
                print(filename + " --> thumb_" + filename + ".jpg")

for dirpath, dirnames, filenames in os.walk("bettty.i"):
    for filename in filenames:
        if not os.path.exists("bettty.i/thumbs/thumb_" + filename + ".jpg"):
            if filename[-1] == "4":

                os.system("ffmpeg -ss 00:00:01.000 -i " + '"' + os.path.join(dirpath, filename) + '"' + " -loglevel quiet -n -vframes 1 bettty.i/thumbs/thumb_" + filename + ".jpg")
                print(filename + " --> thumb_" + filename + ".jpg")
