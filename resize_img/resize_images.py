# -*- coding: utf-8 -*-
import sys
import os
import numpy as np
import cv2, cv
import argparse

## set command line arguments
parser = argparse.ArgumentParser(description='option')
parser.add_argument('--raw_dir', '-RD', default='./images_raw/test_images', type=str)
parser.add_argument('--out_dir', '-OD', default='./images/test_images', type=str)
parser.add_argument('--size', '-s', default=96, type=int)
args = parser.parse_args()

##### Resize Images
def resize_images_square(image, length):
    ### measure short edge
    short_edge = np.min( image.shape[:2] ) ## 色部分の次元を除いて短辺を計測
    ### crop image (square lengthxlength)
    cropped_img = image[ int(image.shape[0]/2-short_edge/2):int(image.shape[0]/2+short_edge/2),
                         int(image.shape[1]/2-short_edge/2):int(image.shape[1]/2+short_edge/2) ]
    ### resize
    resized_img = cv2.resize(cropped_img, (length, length), interpolation=cv2.INTER_AREA)
    return resized_img



if __name__ == "__main__":
    size = args.size
    raw_img_dir = args.raw_dir
    res_img_dir = args.out_dir
    
    # create image directory
    try:
        os.mkdir(res_img_dir)
    except Exception as e:
        print str(e)
        print "cannot create directory (image_directory is already exist)  ディレクトリが既に存在. 無視します."

    cnt = 0
    images = os.listdir(raw_img_dir)
    for image in images:
        ## file_name of raw image
        fname_image_raw = "%s/%s"%(raw_img_dir, image)
        ## 修正後の画像ファイル(フルパス) file_name of resized image
        imagepath = ("%s/image%07d.jpg"%(res_img_dir, cnt))
        print "raw_image_name : " + fname_image_raw
        print "mod_image_name : " + imagepath
        # execute resize
        try:
            img_orig = cv2.imread(fname_image_raw)
            img_resized = resize_images_square(img_orig, size)
            # save image
            cv2.imwrite(imagepath, img_resized)
            cnt += 1
        except AttributeError:
            print "AttributeError : %s"%fname_image_raw
    print "finished"


