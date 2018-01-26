# people-detecting
Detect people from video/camera using OpenCV


## What


```
git clone https://github.com/ndaidong/people-detecting.git
cd people-detecting
git checkout Pedestrian

virtualenv --python=python3 --system-site-packages venv
source venv/bin/activate
pip install -r requirements.txt

python start.py
```

## How

- Approach by Fede as he described here "[People Counter with OpenCV Python](https://www.femb.com.mx/people-counter/people-counter-with-opencv-python/)". This is almost standard process for implementing a People Counter system, including background substraction, filtering, finding contours, and the most important step is following the movement.


## Think

The result is quite accurate, easy to scale up, with an acceptable performance.
