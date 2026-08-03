"""Orchestrator: owns the frame loop, wiring capture → inference → logic → rendering → output."""
import time

from src.capture.webcam import Webcam
from src.inference.person_segmenter import PersonSegmenter
from src.output.display import Display
from src.rendering.overlay import draw_fps, draw_masks


def run(camera_source, seg_model_path):
    segmenter = PersonSegmenter(seg_model_path)
    display = Display()
    camera = Webcam(camera_source)
    fps = 0.0
    prev = time.perf_counter()
    try:
        while True:
            frame = camera.get_frame()
            persons = segmenter.get_persons(frame)
            frame = draw_masks(frame, persons)
            now = time.perf_counter()
            fps = 0.9 * fps + 0.1 / (now - prev)
            prev = now
            frame = draw_fps(frame, fps)
            if not display.show(frame):
                break
    finally:
        camera.close()
        display.close()