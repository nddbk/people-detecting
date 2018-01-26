# people-detecting
Detect people from video/camera using OpenCV


# What


```
git clone https://github.com/ndaidong/people-detecting.git
cd people-detecting
git checkout accumulateWeighted

virtualenv --python=python3 --system-site-packages venv
source venv/bin/activate
pip install -r requirements.txt

python start.py
```

# How

- Use [cvtColor](https://docs.opencv.org/3.2.0/d7/d1b/group__imgproc__misc.html#ga397ae87e1288a81d2363b61574eb8cab) & [GaussianBlur](https://docs.opencv.org/3.1.0/d4/d86/group__imgproc__filter.html#gaabe8c836e97159a9193fb0b11ac52cf1) to create gray version of frame.
- Use [accumulateWeighted](https://docs.opencv.org/2.4/modules/imgproc/doc/motion_analysis_and_object_tracking.html#accumulateweighted) to analyze the motions.
- Use [threshold](https://docs.opencv.org/3.1.0/d7/d1b/group__imgproc__misc.html#gae8a4a146d1ca78c626a53577199e9c57) & [dilate](https://docs.opencv.org/3.1.0/d4/d86/group__imgproc__filter.html#ga4ff0f3318642c4f469d0e11f242f3b6c) to filter.
- Use [findContours](https://docs.opencv.org/3.1.0/d3/dc0/group__imgproc__shape.html#ga17ed9f5d79ae97bd4c7cf18403e1689a) to estimate the objects. 



This method is fast, but the accuracy is quite low.
