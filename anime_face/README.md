# Anime-Faces

* 顔画像データを生成する

## Require

```
- Python (2.7で確認)
- OpenCV (2.4.12で確認)

```

## Files

* anime_face.py
  * 指定したディレクトリ内の画像（アニメ）の中から顔部分だけを切り出す
* face_trimmer.py
  * アニメ画像の中から顔部分をトリミングするための関数

* lbpcascade_animeface.xml
  * アニメ顔画像を検出するためのOpenCVのカスケードファイル
  * https://github.com/nagadomi/lbpcascade_animeface


## Usage

* anime_face.py

```
$ python anime_face.py ./raw_images
## 第１引数 : 元画像のディレクトリ。このディレクトリ内の画像の中から顔部分を抽出
      出力先はハードコーディングしているので、confとか作った方が幸せかも
```

