# -*- coding: utf-8 -*-

import cv2
import sys
import os.path

# 顔検出のための関数
def face_trimmer(filename, output_prfx = "face", counter = 0, path = ".", cascade_file = "lbpcascade_animeface.xml"):
    if not os.path.isfile(cascade_file):
        raise RuntimeError("%s: not found" % cascade_file)
    cascade = cv2.CascadeClassifier(cascade_file)
    image = cv2.imread(filename)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)

    faces = cascade.detectMultiScale(gray,
                                     # detector options
                                     scaleFactor = 1.1,
                                     minNeighbors = 5,
                                     minSize = (24, 24))
    im_h = image.shape[0]
    im_w = image.shape[1]
    #print("w,h = %s, %s"%(im_w, im_h))
    cnt = counter
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
        #print("x1,x2, y1,y2 = %s,%s,  %s,%s"%(x1,x1+l2,y1,y1+l2))
        img_face = image[y1:y1+l2, x1:x1+l2]
        cv2.imwrite("%s/%s_%07d.png"%(path, output_prfx, cnt), img_face)
        cnt += 1

    #cv2.imshow("AnimeFaceDetect", image)
    #cv2.waitKey(0)
    #cv2.imwrite("out.png", image)
    print "detected face_num : %s"%len(faces)
    return cnt

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.stderr.write("usage: detect.py <filename>\n")
        sys.exit(-1)

    face_trimmer(sys.argv[1], counter=10, path="./face_imgs")
