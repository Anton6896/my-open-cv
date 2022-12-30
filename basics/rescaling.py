import os
import cv2 as cv
from conf import config

video_path = os.path.join(config.RESOURCE_PATH, 'Videos', 'dog.mp4')
image_path = os.path.join(config.RESOURCE_PATH, 'Photos', 'cat_large.jpg')


def rescale_frame(frame, scale=.5):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimension = (width, height)
    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)


def resize_video():
    capture = cv.VideoCapture(video_path)
    while True:
        _, frame = capture.read()
        resized_frame = rescale_frame(frame)

        cv.imshow('video', resized_frame)
        if cv.waitKey(20) & 0xFF == ord('d'):
            break

    capture.release()
    cv.destroyAllWindows()


def resize_image():
    img1 = cv.imread(image_path)
    resized = rescale_frame(img1)
    cv.imshow('cat', resized)
    cv.waitKey(0)  # keyboard interaction


def do_resize():
    resize_image()
