"""Phase 1: draws segmentation masks, labels, holding highlights, and FPS onto frames."""
import cv2
import numpy as np

def draw_masks(frame, masks):
    overlay = cv2.fillPoly(frame.copy(), [poly.astype(np.int32) for mask in masks for poly in mask.xy], (0, 255, 0))
    return cv2.addWeighted(overlay, 0.3, frame, 0.7, 0)

def draw_fps(frame, fps):
    cv2.putText(frame, f"{fps:.1f} FPS", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    return frame
