import torch
import argparse
from pathlib import Path
import sys
import uuid

# Local YOLOv7 folder
YOLOV7_DIR = Path(__file__).resolve().parent
sys.path.append(str(YOLOV7_DIR))

import detect  # your detect.py module

MODEL_PATH = YOLOV7_DIR / 'best.pt'
DATA_PATH = YOLOV7_DIR / 'data/datawd.yaml'
RUNS_DIR = YOLOV7_DIR / 'runs/detect'
from detect import ThreatDetector

def run_detection(image_path):
    run_name = f"webapp_{uuid.uuid4().hex[:6]}"

    # Prepare options as argparse.Namespace for detect.py
    opt = argparse.Namespace(
        weights=str(MODEL_PATH),
        source=str(image_path),
        data=str(DATA_PATH),
        img_size=416,              # Match your training size
        conf_thres=0.25,
        iou_thres=0.45,
        device='',              # Change to '0' or '' if you want CUDA
        save_txt=True,
        save_conf=True,
        project=str(RUNS_DIR),
        name=run_name,
        exist_ok=True,
        nosave=False,
        classes=None,              # Detect all classes (or set to your class IDs list)
        agnostic_nms=False,
        augment=False,
        update=False,
        no_trace=False,
        view_img=False,
        save_img=True,
        line_thickness=2,
        hide_labels=False,
        hide_conf=False,
        half=False,
        dnn=False
    )
    detector = ThreatDetector(opt)   
    output_img_path, class_names, count = detector.detect(str(image_path))
    
   

    # Construct paths to output files
    output_img_path = RUNS_DIR / run_name / image_path.name
    label_path = RUNS_DIR / run_name / 'labels' / image_path.with_suffix('.txt').name

    labels = []
    if label_path.exists():
        with open(label_path, 'r') as f:
            for line in f:
                cls_id = int(line.strip().split()[0])
                labels.append(cls_id)

    # Get class names from detect module or fallback
    names = detect.names if hasattr(detect, 'names') else ['object'] * 100
    class_names = [names[i] for i in labels]

    return output_img_path, class_names, len(class_names)

