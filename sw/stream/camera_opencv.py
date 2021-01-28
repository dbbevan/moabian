import os
import cv2
from base_camera import BaseCamera


class CameraOpenCV(BaseCamera):
    video_source = 0

    @staticmethod
    def frames():
        camera = cv2.VideoCapture(0)

        w = 384
        h = 288

        d = 256

        x = int((w / 2 - d / 2))
        y = int((h / 2 - d / 2))

        x += -12
        y +=  4

        camera.set(cv2.CAP_PROP_FRAME_WIDTH, w)
        camera.set(cv2.CAP_PROP_FRAME_HEIGHT, h)
        camera.set(cv2.CAP_PROP_FPS, 30)

        if not camera.isOpened():
            raise RuntimeError('Could not start camera.')

        while True:
            # read current frame
            _, img = camera.read()

            crop = img[y:y+d, x:x+d]

            # encode as a jpeg image and return it
            yield cv2.imencode('.jpg', crop)[1].tobytes()
