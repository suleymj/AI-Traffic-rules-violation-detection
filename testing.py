from ultralytics import YOLO
import os
import cv2

#load yolov8 model
#model = YOLO('vehicles.pt')
model = YOLO('vehicles.pt')


#load image
image =cv2.imread(os.path.join('.', 'vehicles_p', '2mat.jpg'))

#detect objects
results = model(image)

results[0].show()

#cv2.imshow('image', image)
#cv2.waitKey(0)