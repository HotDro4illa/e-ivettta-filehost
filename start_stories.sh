#!/bin/bash
termux-wake-lock
cd /sdcard/arch/insta
instaloader --fast-update --login=hot_dro4illa228 landy2006 e_ivettta bettty.i poqri polyaqurilo alyona.filatova02 --stories --highlights --tagged --igtv --no-video-thumbnails --comments --no-compress-json --geotags --max-connection-attempts 1 | tee log.txt


cd ..
python copier.py
git add -A
git commit -m "update"
git pull
git push
pkill termux























