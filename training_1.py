from ultralytics import YOLO

# Load the pre-trained YOLOv8 COCO model
model = YOLO("yolov8s.pt")

# Train only on the vehicle classes (car, motorcycle, bus, truck)
model.train(data="coco128.yaml", epochs=30, imgsz=640, batch=16, classes=[2, 3, 5, 7])

# Save the fine-tuned model
model.export(format="pt", path="vehicle_detector.pt")

print("🚀 Training complete! Your vehicle-only model is saved as vehicle_detector.pt")
