#!/bin/bash

cd /sdcard/arch/insta
instaloader --login=hot_dro4illa228 --fast-update e_ivettta bettty.i poqri polyaqurilo --stories --highlights --tagged --igtv --no-captions --no-metadata-json --no-video-thumbnails
cd ..
python loader.py e_ivettta
python copier.py
git add -A
git commit -m "update"
git pull
git push






