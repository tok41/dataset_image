# -*- coding: utf-8 -*-

import sys, os
import cv2

from face_trimmer import FaceTrimmer

raw_path = "./images_raw/image_sample"
out_path = "./images/face_sample"
output_prfx = "anime_face"
trimmer = FaceTrimmer("lbpcascade_animeface.xml")
files = os.listdir(raw_path)
cnt = 0
for f in files:
    file_path = "%s/%s"%(raw_path, f)
    print file_path
    face_list = trimmer.face_trimmer(file_path)
    print len(face_list)
    for image in face_list:
        cv2.imwrite("%s/%s_%07d.png"%(out_path, output_prfx, cnt), image)
        cnt+=1
