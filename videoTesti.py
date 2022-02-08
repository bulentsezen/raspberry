
from picamera import PiCamera
import time

camera = PiCamera()
camera.resolution = (640, 480)

camera.start_preview()
time.sleep(2)

camera.start_recording("video_kayit.h264")
time.sleep(7)

camera.stop_recording()
camera.close()

