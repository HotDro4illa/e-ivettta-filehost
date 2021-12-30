#!/bin/bash

cd /sdcard/arch/insta
instaloader --fast-update --login=hot_dro4illa228 e_ivettta bettty.i poqri polyaqurilo miss_nadiass alyona.filatova02 _history_of_loveee_ --stories --highlights --tagged --igtv --no-metadata-json --no-video-thumbnails --comments

instaloader --fast-update --login=katerin__ea polinakyri --stories --highlights --tagged --igtv --no-metadata-json --no-video-thumbnails --comments
cd ..
python merge.py insta
python copier.py
git add -A
git commit -m "update"
git pull
git push
















