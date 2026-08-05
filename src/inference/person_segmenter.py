"""Phase 1: pretrained person segmentation wrapper — person masks + boxes (track IDs arrive in Phase 2)."""
from ultralytics import YOLO




class PersonSegmenter:
    def __init__(self, weights_path):
        self.model = YOLO(weights_path)
        print(f"[PersonSegmenter] loaded model: {self.model.model.yaml['yaml_file']}")

    def get_persons(self, image, conf=0.5):
        result = self.model.track(image, conf=conf, classes=[0],verbose=False,retina_masks=True,device='mps',persist=True)[0]

        if result.masks is None or result.boxes.id is None:
            return []
        return list(zip(result.masks, result.boxes.id))