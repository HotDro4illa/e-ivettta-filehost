import shutil
import json
import os
from PIL import Image
size = 400, 400
try:
    os.mkdir("arch/")
    print("Arch created")
except:
    pass
dirlist = os.listdir('insta')
f_arch = open('arch/arch.txt', 'w+')
arch = {"accs": [], "dirlist": dirlist}

for directory in dirlist:
    try:
        os.mkdir("arch/" + directory)
        print("Dir created: " + directory)
    except:
        pass

    for dirpath, dirnames, filenames in os.walk(f'insta/{directory}'):
        for filename in filenames:
            src = os.path.join(dirpath, filename)
            if not os.path.exists(f'arch/{directory}/{filename}'):
                if any(x in filename for x in ['id', 'list.json', 'cover', 'thumb']):
                    continue
                if "profile_pic" in filename:
                    dst = f'arch/{directory}/profile_pic.jpg'
                    shutil.copy2(src, dst, follow_symlinks=True)
                    print('uploaded:', src)
                    continue
                if not os.path.exists(f'arch/{directory}/thumb_{filename}.jpg'):
                    if filename[-1] == "g":
                        with Image.open(src) as im:
                            im.thumbnail(size)
                            im.save(f'arch/{directory}/thumb_{filename}.jpg', "JPEG", quality=50, optimize=True)
                            print(f'{filename} --> thumb_{filename}.jpg')
                if not os.path.exists(f'arch/{directory}/thumb_{filename}.jpg'):
                    if filename[-1] == "4":
                        os.system(f'ffmpeg -ss 00:00:01.000 -i "{src}" -loglevel quiet -n -vframes 1 "arch/{directory}/thumb_{filename}.jpg"')
                        print(f'{filename} --> thumb_{filename}.jpg')
                dst = f'arch/{directory}/{filename}'
                shutil.copy2(src, dst, follow_symlinks=True)
                print('uploaded:', src)

    dir_result = {directory: {"feed": [], "gallery": []}}
    post_feed = {"files": [], "json_data": "", "description": "", "comments": "", "geolocation": ""}
    dir_all_files = [i for i in [filenames for dirpath, dirnames, filenames in os.walk(f'arch/{directory}')][0]]
    dir_mat_files = [i for i in [filenames for dirpath, dirnames, filenames in os.walk(f'arch/{directory}')][0] if all(x not in i for x in ['thumb', 'json', 'txt', 'cover', 'profile', 'tiktok'])]
    posts = [[dir_mat_files[0]]]
    for file in dir_mat_files:
        if file.count('_') == 3:
            filename = "_".join(file.split("_")[:-1])
            if filename in posts[-1][-1]:
                posts[-1].append(file)
            else:
                posts.append([file])
        else:
            posts.append([file])

    for post in posts:
        if len(post) > 1:
            post = list(set(post))
            post.sort(key=lambda x: int(x.split('_')[3].split('.')[0]))
            filename = "_".join(post[0].split("_")[:-1])
        else:
            filename = post[0].split(".")[0]
        post_feed = {"files": [], "json_data": "", "description": "", "comments": "", "geolocation": "", "date": {"year": "", "month": "", "day": "", "hour": "", "minute": "", "second": ""}}
        for file in post:
            if "jpg" in file:
                file_type = "image"
            elif "mp4" in file and "tiktok" not in file:
                file_type = "video"
            elif "tiktok" in file:
                file_type = "tiktok"
            else:
                file_type = "other"
            post_feed["files"].append({"file": file, "thumbnail": f'thumb_{file}.jpg', "file_type": file_type})

        year, month, day = filename.split('_')[0].split('-')
        hour, minute, second = filename.split('_')[1].split('-')
        post_feed['date']['year'] = year
        post_feed['date']['month'] = month
        post_feed['date']['day'] = day
        post_feed['date']['hour'] = hour
        post_feed['date']['minute'] = minute
        post_feed['date']['second'] = second
        if f'{filename}.json' in dir_all_files:
            post_feed['json_data'] = f'{filename}.json'
        if f'{filename}.txt' in dir_all_files:
            post_feed['description'] = f'{filename}.txt'
        if f'{filename}_comments.json' in dir_all_files:
            post_feed['comments'] = f'{filename}_comments.json'
        if f'{filename}_location.txt' in dir_all_files:
            post_feed['geolocation'] = f'{filename}_location.txt'
        dir_result[directory]["feed"].append(post_feed)

    videos = [{"file": i, "thumbnail": f'thumb_{i}.jpg', "date": {"year": filename.split('_')[0].split('-')[0], "month":filename.split('_')[0].split('-')[1], "day":filename.split('_')[0].split('-')[2], "hour":filename.split('_')[1].split('-')[0], "minute":filename.split('_')[1].split('-')[1], "second":filename.split('_')[1].split('-')[2]}} for i in dir_mat_files if 'mp4' in i]
    photos = [{"file": i, "thumbnail": f'thumb_{i}.jpg', "date": {"year": filename.split('_')[0].split('-')[0], "month":filename.split('_')[0].split('-')[1], "day":filename.split('_')[0].split('-')[2], "hour":filename.split('_')[1].split('-')[0], "minute":filename.split('_')[1].split('-')[1], "second":filename.split('_')[1].split('-')[2]}} for i in dir_mat_files if 'jpg' in i]
    tiktok = [{"file": i, "thumbnail": f'thumb_{i}.jpg', "date": {"year": filename.split('_')[0].split('-')[0], "month":filename.split('_')[0].split('-')[1], "day":filename.split('_')[0].split('-')[2], "hour":filename.split('_')[1].split('-')[0], "minute":filename.split('_')[1].split('-')[1], "second":filename.split('_')[1].split('-')[2]}} for i in dir_all_files if 'mp4' in i and 'tiktok' in i and "thumb" not in i]
    dir_result[directory]["gallery"].append({"videos": videos, "photos": photos, "tiktok": tiktok})
    arch["accs"].append(dir_result)
json.dump(arch, f_arch, indent=4)
f_arch.close()
