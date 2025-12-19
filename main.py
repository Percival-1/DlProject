import torch
from ultralytics import YOLO

print("Torch CUDA available:", torch.cuda.is_available())
print("GPU:", torch.cuda.get_device_name(0))

# Load a small YOLO model
model = YOLO("yolov8n.pt")

# Run a dummy inference (this downloads assets if needed)
results = model.predict(source="https://ultralytics.com/images/bus.jpg", device=0)

print("YOLO inference successful")
