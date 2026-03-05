import os
import csv
import cv2
import numpy as np
import torch
from deep_sort_realtime.deepsort_tracker import DeepSort
from ultralytics import YOLO

# Load YOLOv8 model (Ensure you have YOLOv8 installed and trained for vehicles)
model = YOLO("vehicles.pt")  # Use a fine-tuned model if available

# Initialize DeepSORT tracker
tracker = DeepSort(max_age=30, n_init=3)

# Define lane boundaries (To be adjusted for your setup)
NO_OVERTAKE_ZONE = [(200, 400), (1000, 400)]  # Example lane points

# Function to check if a vehicle is overtaking
def check_overtaking(vehicle_tracks, no_overtake_zone):
    overtaking_vehicles = []
    
    for track_id, history in vehicle_tracks.items():
        if len(history) < 2:
            continue
        
        prev_x, prev_y = history[-2]
        curr_x, curr_y = history[-1]
        
        # Check if vehicle moved past another in a no-overtaking zone
        if (prev_x < no_overtake_zone[0][0] and curr_x > no_overtake_zone[1][0]):
            overtaking_vehicles.append(track_id)
    
    return overtaking_vehicles

# Open video feed
cap = cv2.VideoCapture(os.path.join('.', 'road_clips', '1l.mp4'))  # Replace with 0 for live camera

vehicle_tracks = {}

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Run YOLO object detection
    results = model(frame)
    detections = []
    
    for result in results:
        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = box.conf[0].item()
            cls = int(box.cls[0].item())
            
            if cls in [2, 3, 5, 7]:  # Car, truck, bus, motorcycle (YOLO class IDs)
                detections.append(([x1, y1, x2 - x1, y2 - y1], conf, cls))
    
    # Track vehicles
    tracks = tracker.update_tracks(detections, frame=frame)
    
    for track in tracks:
        if not track.is_confirmed():
            continue
        
        track_id = track.track_id
        bbox = track.to_ltrb()
        x1, y1, x2, y2 = map(int, bbox)
        center_x = (x1 + x2) // 2
        center_y = (y1 + y2) // 2
        
        # Store vehicle position history
        if track_id not in vehicle_tracks:
            vehicle_tracks[track_id] = []
        vehicle_tracks[track_id].append((center_x, center_y))
        
        # Draw bounding boxes
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, f"{track_id}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    # Check for overtaking violations
    overtakers = check_overtaking(vehicle_tracks, NO_OVERTAKE_ZONE)
    
    for overtaker in overtakers:
        cv2.putText(frame, f"Overtaking! ID: {overtaker}", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
    
    # Show frame
    cv2.imshow("Traffic Monitoring", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
