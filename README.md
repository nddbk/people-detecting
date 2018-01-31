# people-detecting
Detect people from video/camera using OpenCV


## What

Download `yolo.weights` or `tiny-yolo-voc.weights` from [YOLO site](https://pjreddie.com/darknet/yolo/) first:



```
export YOLO_PATH=/ABSOLUTE/PATH/TO/YOLO/WEIGHTS/FILE

git clone --recursive https://github.com/ndaidong/people-detecting.git
cd people-detecting
git checkout YOLO

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

python start.py
```

## How

- In this branch, we try to use [YOLO](https://pjreddie.com/darknet/yolo/) with [darknet](https://pjreddie.com/darknet/) for TensorFlow via [a fork](https://github.com/bendidi/darkflow) of [darkflow](https://github.com/thtrieu/darkflow).


## Think

This is exactly what we need. The accuracy is incredible! Everything is ready to deal with GPU.
