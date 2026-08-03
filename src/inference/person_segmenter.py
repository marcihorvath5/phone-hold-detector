"""Phase 1: pretrained person segmentation wrapper — person masks + boxes (track IDs arrive in Phase 2)."""
from ultralytics import YOLO




class PersonSegmenter:
    def __init__(self, weights_path):
        self.model = YOLO(weights_path)

    def get_persons(self, image, conf=0.5):
        result = self.model.predict(image, conf=conf, classes=[0],verbose=False,retina_masks=True,device='mps')[0]

        if result.masks is None:
            return []
        return list(result.masks)