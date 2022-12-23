import os
import cv2 as cv
from conf import config


photos_path = os.path.join(config.RESOURCE_PATH, 'Photos')


def basic_read():
    img1 = cv.imread(os.path.join(photos_path, 'cat_large.jpg'))
    cv.imshow('cat', img1)
    cv.waitKey(0)  # keyboard interaction
