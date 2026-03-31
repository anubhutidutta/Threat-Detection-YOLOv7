# YOLOv7 Threat Detection System

## Overview

This project implements a threat detection system using the YOLOv7 object detection model. It is designed to identify various types of weapons in images or video streams for security applications.

## Model Details

* **Model:** YOLOv7
* **Input Size:** 416 × 416
* **Classes:** 9 (Automatic Rifle, Bazooka, Handgun, Knife, Grenade Launcher, Shotgun, SMG, Sniper, Sword)

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python detect.py --weights best.pt --conf 0.25 --img-size 640 --source path/to/image.jpg --data data.yaml
```

## Features

* Detects multiple weapon types
* Works with images, videos, and webcam
* Real-time object detection

## Note

The model file (best.pt) is large in size and may take time to download. For convenience, it can also be accessed via an external link if required.
