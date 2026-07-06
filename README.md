# phone-hold-detector

Real-time camera pipeline that outlines people with a pretrained segmentation model and
detects whether each person is holding a phone with a detector I train myself — a personal
project for learning ML/computer vision end to end (dataset → labeling → training → inference).

Full project instructions, decisions, and build phases live in [CLAUDE.md](CLAUDE.md).

## Layout

    main.py            entry point (stays at root so `src.*` imports resolve)
    src/
      config.py        .env → typed constants (only module reading the environment)
      pipeline.py      orchestrator: capture → inference → logic → rendering → output
      capture/         frame sources (Mac webcam now, Pi MJPEG stream later)
      inference/       thin model wrappers (pretrained segmentation + trained phone detector)
      logic/           "holding" geometry — pure functions, no cv2/model imports
      rendering/       OpenCV drawing: masks, labels, FPS
      output/          display window now; MJPEG stream + SQLite log later
    models/            weight files (gitignored)
    training/          Phase 3 dataset/training workflow (data gitignored)

## Setup (Phase 0)

    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    cp .env.example .env   # then edit for this machine