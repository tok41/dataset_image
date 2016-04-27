# -*- coding: utf-8 -*-

import cv2
import sys
import os.path

class FaceTrimmer:
    """
    * Trimming Face from image_file
    * square
    """
    def __init__(self, cascade_file):
        # set face_detector
        self.cascade = cv2.CascadeClassifier( cascade_file )

    def face_trimmer(self, filename):
        image = cv2.imread(filename)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.equalizeHist(gray)
        faces = self.cascade.detectMultiScale(gray,
                                         scaleFactor = 1.1,
                                         minNeighbors = 5,
                                         minSize = (24, 24) )
        im_h = image.shape[0]
        im_w = image.shape[1]
        face_imgs = []
        for (x, y, w, h) in faces:
            l = w if w>h else h
            ## 顔の検出位置よりも、ちょっと広めに顔領域を取りたい
            l = l * 1.3
            x1=x-int((l-w)/2.0)
            x1 = x1 if x1>0 else 0
            x2=x+w+int((l-w)/2.0)
            x2 = x2 if x2<im_w else im_w
            y1=y-int((l-h)/2.0)
            y1 = y1 if y1>0 else 0
            y2=y+h+int((l-h)/2.0)
            y2 = y2 if y2<im_h else im_h
            l2 = x2-x1 if x2-x1 < y2-y1 else y2-y1
            img_face = image[y1:y1+l2, x1:x1+l2]
            face_imgs.append(img_face)
        return face_imgs

if __name__ == '__main__':
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
