#!/bin/bash
termux-wake-lock
while :
do
pip install instaloader --upgrade
cd ~/storage/external-1/Instaloader/insta
instaloader --fast-update --login=hot_dro4illa228 landy2006 e_ivettta bettty.i poqri polyaqurilo alyona.filatova02 --stories --highlights --tagged --igtv --no-video-thumbnails --comments --no-compress-json --geotags --sanitize-paths

cd ..
python copier.py
git add -A
git commit -m "update"
git push
echo "Done"
sleep 43200
done
