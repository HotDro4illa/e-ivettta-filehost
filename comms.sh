#!/bin/bash
termux-wake-lock
cd /sdcard/arch/insta
instaloader --login=hot_dro4illa228 landy2006 e_ivettta bettty.i poqri polyaqurilo alyona.filatova02 --stories --highlights --tagged --igtv --no-metadata-json --no-video-thumbnails --comments --no-pictures --no-videos


cd ..
python merge.py insta
python copier.py
git add -A
git commit -m "update"
git pull
git push
pkill termux



















