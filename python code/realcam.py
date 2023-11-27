
from ultralytics import YOLO
from ultralytics.yolo.v8.detect.predict import DetectionPredictor
import cv2

model = YOLO("C:/Users/c1257/Desktop/ultralytics-main/ultralytics-main/runs/detect/best/weights/best.pt")

results = model.predict(source="0", show=True)

print(results)