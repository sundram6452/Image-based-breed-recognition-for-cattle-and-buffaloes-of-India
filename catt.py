from ultralytics import YOLO
import numpy as np

# Load your trained model
model = YOLO("runs/classify/train20/weights/best.pt")

# Define your custom class names (same order as dataset folders)
class_names = {
    0: "Aryshire",
    1: "Brown",
    2: "Dane",
    3: "Friesian",
    4: "Jersey"
}
url="https://cdn.britannica.com/53/157153-050-E5582B5A/Holstein-cow.jpg"

# Predict on a single image
results = model.predict(url)

for r in results:
    probs = r.probs.data.cpu().numpy()
    top_indices = probs.argsort()[::-1]  # sort by confidence descending

    print("\nTop Predictions:")
    for idx in top_indices[:]:  # show top-3
        print(f"{class_names[idx]}: {probs[idx]*100:.2f}%")
