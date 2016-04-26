# -*- coding: utf-8 -*-

import sys, os

from face_trimmer import face_trimmer

if len(sys.argv) != 2:
    sys.stderr.write("usage: anime_face.py <raw_image_directory>\n")
    sys.exit(-1)

#raw_path = "./raw_images"
raw_path = sys.argv[1]
out_path = "./face_imgs"
print(raw_path)

cnt = 0
files = os.listdir(raw_path)
for f in files:
    file_path = "%s/%s"%(raw_path, f)
    print file_path
    cnt = face_trimmer(file_path, counter=cnt, path=out_path)
