# Training workflow (Phase 3)

The loop this directory exists for:

1. Collect varied phone images (multiple rooms, lighting, hands, angles — generalization is the point).
2. Label phone bounding boxes in Roboflow; generate a dataset version with a train/val split.
3. Train in Google Colab (or locally on the Mac); watch loss curves and mAP — expect to meet overfitting.
4. Download the trained weights and copy them to `../models/` (the app loads them via `PHONE_MODEL_PATH`).

`data/` holds raw images and exported datasets — gitignored, never committed.
Colab notebooks / training scripts land here as they come to exist.