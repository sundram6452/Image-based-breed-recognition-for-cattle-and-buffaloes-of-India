from ultralytics import YOLO

# Load a classification model
model = YOLO("yolov8n-cls.pt")

# Train
model.train(
    data="C:/Users/kumar/OneDrive/Desktop/cattles/dataset",  # path to dataset
    epochs=50,
    imgsz=224,
    batch=16,
    patience=20
)
