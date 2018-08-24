# tensorflow_sample_2
転移学習
[参考](https://book.mynavi.jp/manatee/detail/id=86951)

## 画像ダウンロード
```
python3 download_images.py
```

## 転移学習
```
python3 retrain.py \
 --image_dir=dataset  \
 --how_many_training_steps 500 \
 --bottleneck_dir=retrain/bottlenecks \
 --model_dir=retrain/inception \
 --output_graph=release/model/retrained_graph.pb \
 --output_labels=release/model/retrained_labels.txt
```

## 認識
- recognizer フォルダに使用する学習モデル `model` を置く
- recognizer フォルダにターゲットの画像 `target.jpg` を置く
- `python3 recognizer/app.py` を実行する
