# people-detecting
Detect people from video/camera using OpenCV


## What


```
git clone https://github.com/ndaidong/people-detecting.git
cd people-detecting
git checkout Pedestrian

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

python start.py
```

## How

- I got this method at Fede's blog article "[People Counter with OpenCV Python](https://www.femb.com.mx/people-counter/people-counter-with-opencv-python/)". It felt that it's near to a standard process of building People Counter system, including background substraction, filtering, finding contours, and the most important step is following the movements.


## Think

The result is quite accurate, easy to scale up, with an acceptable performance.
