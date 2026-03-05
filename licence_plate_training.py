from ultralytics import YOLO

# Load the YOLO model (replace 'best.pt' with your model if needed)
model = YOLO('best.pt')  # Use 'yolov8s.pt' or your custom model if needed

# Train the model
model.train(
    data='data.yaml',  # Path to data.yaml
    epochs=40, 
    imgsz=640, 
    batch=16, 
    device='cpu'  # Use 'cuda' if you have a GPU
)

