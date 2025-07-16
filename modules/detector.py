from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO("models/yolov8n.pt")  # path to your YOLOv8 weights

def detect_items(image_path):
    # Run detection
    results = model(image_path)
    boxes = results[0].boxes
    names = results[0].names  # class ID to label mapping

    detected = []
    for box in boxes:
        class_id = int(box.cls[0])
        label = names[class_id]
        detected.append(label)

    return detected
