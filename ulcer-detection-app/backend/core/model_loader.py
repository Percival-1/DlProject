from ultralytics import YOLO
from pathlib import Path

MODEL_PATH = Path('../../models/trained/weights.pt')

model = None

def get_model():
    global model
    if model is None:
        model = YOLO(MODEL_PATH)

    return model
