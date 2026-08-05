"""Phase 1: draws segmentation masks, labels, holding highlights, and FPS onto frames."""
import cv2
import numpy as np

def _topmost_point(mask):
    all_points = np.concatenate(mask.xy)
    topmost = all_points[all_points[:, 1].argmin()]
    return int(topmost[0]), int(topmost[1])

def draw_masks(frame, masks):
    overlay = cv2.fillPoly(frame.copy(), [poly.astype(np.int32) for mask,person_id in masks for poly in mask.xy], (0, 255, 0))
    blended = cv2.addWeighted(overlay, 0.3, frame, 0.7, 0)

    for mask, person_id in masks:
        x, y = _topmost_point(mask)
        label_text = str(int(person_id))
        (text_w, text_h), baseline = cv2.getTextSize(label_text, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2)

        box_bottom = max(y - 10, text_h + baseline + 8)
        box_top = box_bottom - text_h - baseline - 8
        box_left, box_right = x, x + text_w + 8

        cv2.rectangle(blended, (box_left, box_top), (box_right, box_bottom), (0, 255, 0), -1)
        cv2.putText(blended, label_text, (box_left + 4, box_bottom - baseline - 4), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)

    return blended

def draw_fps(frame, fps):
    cv2.putText(frame, f"{fps:.1f} FPS", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    return frame
