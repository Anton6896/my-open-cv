import os
import cv2 as cv


photos_path = os.path.join(
    os.path.abspath(os.path.join(os.path.dirname(
        os.path.realpath(__file__)), os.pardir)),
    'resources',
    'Photos')


def basic_read():
    img1 = cv.imread(os.path.join(photos_path, 'cat_large.jpg'))
    cv.imshow('cat', img1)
    cv.waitKey(0)  # keyboard interaction


if __name__ == '__main__':
    basic_read()
