"""Entry point: load config, build the pipeline, run. Lives at project root so `src.*` imports resolve."""
from src.config import CAMERA_SOURCE,SEG_MODEL_PATH
from src.pipeline import run

if __name__ == "__main__":
    run(CAMERA_SOURCE, SEG_MODEL_PATH)
