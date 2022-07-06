import shutil
import json
import os
from PIL import Image
size = 400, 400
dirlist = os.listdir('insta')
f = open('arch/accs.txt', 'w+')
f_arch = open('arch/arch.txt', 'w+')
f.write("\n".join(dirlist))
f.close()
arch = {"accs": []}

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
    dir_mat_files = [i for i in [filenames for dirpath, dirnames, filenames in os.walk(f'arch/{directory}')][0] if all(x not in i for x in ['thumb', 'json', 'txt', 'cover', 'profile'])]
    dir_mat_files.sort()
    for file in dir_mat_files:
        if file.count('_') == 3:
            filename = '_'.join(file.split('_')[:-1])
            print(file, filename)
            if filename in post_feed['files'][-1]:
                post_feed['files'].append({"file": file, "thumbnail": f'thumb_{file}.jpg'})
                if f'{filename}.json' in dir_all_files:
                    post_feed['json_data'] = f'{filename}.json'
                if f'{filename}.txt' in dir_all_files:
                    post_feed['description'] = f'{filename}.txt'
                if f'{filename}_comments.json' in dir_all_files:
                    post_feed['comments'] = f'{filename}_comments.json'
                if f'{filename}_location.txt' in dir_all_files:
                    post_feed['geolocation'] = f'{filename}_location.txt'
