from picamera import PiCamera
import time

camera = PiCamera()

camera.start_preview()
time.sleep(2)

camera.capture("test.jpg")

camera.stop_preview()
camera.close()

