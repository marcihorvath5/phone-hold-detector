"""Phase 1: local display window via cv2.imshow, including quit-key handling."""
import cv2


class Display:
    def __init__(self, window_name="phone-hold-detector"):
        self.window_name = window_name

    def show(self, frame):
        """Render one frame. Returns False when the viewer pressed 'q' (stop the loop)."""
        cv2.imshow(self.window_name, frame)
        return cv2.waitKey(1) & 0xFF != ord("q")

    def close(self):
        cv2.destroyAllWindows()