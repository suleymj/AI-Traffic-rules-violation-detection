# AI-Traffic-rules-violation-detection
1. Overview
This project implements an AI-based traffic monitoring system designed to detect traffic rule violations, specifically overtaking and overlapping violations, using computer vision techniques.
The system processes recorded video footage, detects vehicles, analyzes lane positions, and identifies violations based on rule-based logic.
Note: Real-time deployment was limited by hardware processing constraints, but the system can perform well on recorded video input.
2. Problem Statement
Traffic violations such as illegal overtaking contribute significantly to road accidents. The goal of this project was to design a cost-effective AI-based system capable of automatically detecting such violations and reporting offenders.
3. System Architecture
Input Video → Vehicle Detection → Lane Detection (Canny + Hough) →
Position Analysis → Violation Logic → Licence plate detection → Email Alert + Output Frame
4. Technologies Used
Python
OpenCV
YOLO (Object Detection)
NumPy
SMTP (for email alerts)
Raspberry Pi (target deployment device)
5. Methodology
Vehicle Detection
Vehicles are detected using a YOLO-based object detection model trained for car classification.
Lane Detection
Classical computer vision techniques were applied:
Canny Edge Detection
Hough Line Transform
This allowed estimation of lane boundaries.
Violation Detection Logic
A vehicle is flagged for overtaking/overlapping when:
It crosses predefined lane boundary conditions.
Bounding box centroid shifts into restricted lane region.
Temporal tracking confirms sustained violation across frames.
Reporting
When a violation is detected:
The frame is captured licence plate of vehicle is detected then 
An automated email alert is generated with the evidence image.
6. Performance & Limitations
The system performs accurately on recorded video input.
Real-time processing was limited by:
CPU processing capacity
Lack of dedicated GPU acceleration
Camera latency
7. Future improvements:
Model optimization (YOLO-tiny / quantization)
Multi-threaded processing
Edge AI accelerator integration
8. Sample Results
(Insert screenshots here)
Detected vehicles with bounding boxes
Lane overlay visualization
Violation alert frame
licence plate detection 
Email alert screenshot
10. Future Work
Real-time optimization on edge devices

 
