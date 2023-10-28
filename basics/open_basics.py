import os
import cv2 as cv
from conf import config


def resize_frame(frame, scale: float = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def read_picture():
    photos_path = os.path.join(config.RESOURCE_PATH, 'Photos')
    img1 = cv.imread(os.path.join(photos_path, 'cat_large.jpg'))
    cv.imshow('cat', img1)
    cv.waitKey(0)  # keyboard interaction (allow to see image)


def read_video():
    video_path = os.path.join(config.RESOURCE_PATH, 'Videos', 'dog.mp4')
    video_frames = cv.VideoCapture(video_path)

    while 1:
        have_frame, frame = video_frames.read()
        if not have_frame:
            break
        resized_frame = resize_frame(frame, 0.50)
        cv.imshow('video-1', resized_frame)
        if cv.waitKey(20) & 0xFF == ord('d'):
            break

    video_frames.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    read_video()
