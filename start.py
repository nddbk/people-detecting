from os import environ

from darkflow.darkflow.defaults import argHandler
from darkflow.darkflow.net.build import TFNet

FLAGS = argHandler()
FLAGS.setDefaults()

FLAGS.demo = "vtest.avi"  # or "camera"
FLAGS.model = "darkflow/cfg/yolo.cfg"
FLAGS.load = environ.get('YOLO_PATH')
FLAGS.threshold = 0.7
FLAGS.gpu = 0
FLAGS.track = False
FLAGS.trackObj = ["person"]
FLAGS.saveVideo = False
FLAGS.BK_MOG = True
FLAGS.tracker = "sort"
FLAGS.skip = 0
FLAGS.csv = False
FLAGS.display = True

tfnet = TFNet(FLAGS)

tfnet.camera()
exit('Demo stopped, exit.')
