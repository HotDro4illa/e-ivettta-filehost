:c
instaloader --login=hot_dro4illa228 --fast-update --latest-stamps profile e_ivettta bettty.i --stories --highlights --tagged --igtv --no-captions --no-metadata-json --no-video-thumbnails
python loader.py e_ivettta
python merge.py e_ivettta
python merge.py bettty.i
python thumb.py
python copier.py

git add -A
git commit -m "update"
git push

timeout /t 21600
goto c