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

- This approach make use of the pre-trained Histogram of Oriented Gradients (HOG) and Linear Support Vector Machine (SVM) model shipped with OpenCV. [Adrian Rosebrock](https://twitter.com/pyimagesearch) had written about this in his article "[Pedestrian Detection OpenCV](https://www.pyimagesearch.com/2015/11/09/pedestrian-detection-opencv/)".


## Think

This method is quite good, can be improved for better result. But it consumes a big amount of CPU and very slow in regular dev environment. It maybe good if we process with GPU.
