from ultralytics import YOLO

# Load a pre-trained YOLOv8 model (for general object detection)
model = YOLO('yolov8n.pt')  # You can replace 'yolov8n.pt' with a different variant (e.g., yolov8s.pt for a faster model)

# Run inference on an image
results = model('i6.jpg')

# Display the results
results.show()  # This will display the image with the detections

# Optionally, save the results
results.save()  # Saves the image with detections to the 'runs/detect/exp' folder
