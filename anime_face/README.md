# Anime Face Trimmer

* アニメ画像から顔画像データを生成する

## Require

```
- Python (2.7で確認)
- OpenCV (2.4.12で確認)
-- 顔検出用のカスケードファイルが必要(https://github.com/nagadomi/lbpcascade_animeface)
```

## Files

* anime_face.py
  * 指定したディレクトリ内の画像（アニメ）の中から顔部分だけを切り出す
* face_trimmer.py
  * アニメ画像の中から顔部分をトリミングするためのクラス定義
* lbpcascade_animeface.xml
  * アニメ顔画像を検出するためのOpenCVのカスケードファイル
  * https://github.com/nagadomi/lbpcascade_animeface


## Usage

* anime_face.py
  * face_trimmer.py でも同じメイン関数が書いてあるので、どっちでも良い

```
$ python anime_face.py
```

