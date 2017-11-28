#!/usr/bin/env python

# --------------------------------------------------------
# Faster R-CNN
# Copyright (c) 2015 Microsoft
# Licensed under The MIT License [see LICENSE for details]
# Written by Ross Girshick
#########not good enough##############
# --------------------------------------------------------

"""
Demo script showing detections in sample images.

See README.md for installation instructions before running.
"""

import _init_paths
from fast_rcnn.config import cfg
from fast_rcnn.test import im_detect
from fast_rcnn.nms_wrapper import nms
from utils.timer import Timer
import matplotlib.pyplot as plt
import numpy as np
import scipy.io as sio
import caffe, os, sys, cv2
import argparse

CLASSES = ('__background__', # always index 0
           'headshoulder', 'ignore')

NETS = {'vgg16': ('VGG16',
                  'VGG16_alt_opt_ignore-difficult0.caffemodel'),
        'zf': ('ZF',
                  'ZF_faster_rcnn_final.caffemodel')}

while True:
    demo_video(net,cv2.VideoCapture(videoFilePath))
def demo_video(net, videoFile):
    global frameRate
    # Load the demo image
    ret, im = videoFile.read()
    # Detect all object classes and regress object bounds
    timer = Timer()
    timer.tic()
    scores, boxes = im_detect(net, im)
    timer.toc()
    print ('Detection took {:.3f}s for '
        '{:d} object proposals').format(timer.total_time, boxes.shape[0])
    frameRate = 1.0/timer.total_time
    print "fps: " + str(frameRate)
    # Visualize detections for each class
    CONF_THRESH = 0.65
    NMS_THRESH = 0.2
    for cls_ind, cls in enumerate(CLASSES[1:]):
        cls_ind += 1 # because we skipped background
        cls_boxes = boxes[:, 4*cls_ind:4*(cls_ind + 1)]
        cls_scores = scores[:, cls_ind]
        dets = np.hstack((cls_boxes,
                          cls_scores[:, np.newaxis])).astype(np.float32)
        keep = nms(dets, NMS_THRESH)
        dets = dets[keep, :]
        im=vis_detections_video(im, cls, dets, thresh=CONF_THRESH)
    cv2.putText(im,'{:s} {:.2f}'.format("FPS:", frameRate(1750,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255))
    cv2.imshow(videoFilePath.split('/')[len(videoFilePath.split('/'))-1],im)
    cv2.waitKey(20)
