"""Typed configuration constants loaded from .env / environment — the only module that reads os.environ."""
import os

from dotenv import load_dotenv

load_dotenv()

# Device index ("0" → int 0 for cv2.VideoCapture) or a stream URL (stays a string).
_camera_source = os.getenv("CAMERA_SOURCE", "1")
CAMERA_SOURCE = int(_camera_source) if _camera_source.isdigit() else _camera_source

SEG_MODEL_PATH = os.getenv("SEG_MODEL_PATH", "models/yolo26n-seg.pt")
PHONE_MODEL_PATH = os.getenv("PHONE_MODEL_PATH", "models/phone_detector.pt")