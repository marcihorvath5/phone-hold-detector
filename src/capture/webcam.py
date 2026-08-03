"""Phase 1: local webcam FrameSource backend (Mac built-in camera via OpenCV)."""
import cv2

class Webcam:
    def __init__(self, camera_id=0):
        self.camera = cv2.VideoCapture(camera_id)

    def get_frame(self):
        ok, frame = self.camera.read()
        if not ok:
            raise RuntimeError("Error while reading frame")
        return frame

    def close(self):
        self.camera.release()