# Image Resizer

* 画像のリサイズをする. 
* 画像の中心から正方形に画像切り出し、指定サイズの正方形に切り出す

## Require

```
- Python
- OpenCV (python ver.)
- numpy
```

## Usage

```
$ python resize_images.py {options}
 [option]
   --size : resized image size (integer, default=96)
   --raw_dir : Raw Image directory (string)
   --out_dir : Output Image directory (string)
e.g.
$ python resized_images.py --size=100 --raw_dir=./images_raw --out_dir=./images
```

リサイズの関数を別のコードにimportすることもできる.
```
from resize_images import resize_images_square

...

img_orig = cv2.imread(fname_image_raw)
img_resized = resize_images_square(img_orig, size)

...

```


