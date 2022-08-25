import os

for dirpath, dirnames, filenames in os.walk("e_ivettta"):
    for filename in filenames:
        src = os.path.join(dirpath, filename)
        print(src) 
