# YOLOv7-Based Threat Detection System

## 1. Overview

This project implements a computer vision-based threat detection system using the YOLOv7 object detection framework. The system is designed to identify potentially dangerous objects such as firearms and weapons in images, videos, or real-time webcam input. The objective is to demonstrate how deep learning can be applied to automate surveillance and improve safety monitoring.


## 2. Problem Statement

Monitoring surveillance systems manually is time-consuming and prone to human error. There is a need for automated systems that can detect potential threats in real-time and assist in improving response time and situational awareness.


## 3. Objective

The primary objective of this project is to build a system capable of detecting multiple types of weapons using a trained YOLOv7 model and to demonstrate its effectiveness in real-time object detection scenarios.


## 4. Model Details

* Model Architecture: YOLOv7
* Input Resolution: 416 × 416
* Number of Classes: 9

### Detected Classes

* Automatic Rifle
* Bazooka
* Handgun
* Knife
* Grenade Launcher
* Shotgun
* SMG
* Sniper
* Sword


## 5. Methodology

The system follows a standard object detection pipeline:

1. Input image or video frame is provided to the model
2. The frame is preprocessed and resized
3. YOLOv7 performs object detection using convolutional neural networks
4. Bounding boxes and class labels are generated
5. Relevant objects (weapons) are highlighted in the output


## 6. Installation

Install the required dependencies using:

pip install -r requirements.txt


## 7. Usage

Run the following command to perform detection:

python detect.py --weights best.pt --conf 0.25 --img-size 640 --source path/to/input --data data.yaml

Where:

* `--source` can be an image file, video file, or `0` for webcam
* `--conf` specifies the confidence threshold


## 8. Project Structure

project/
|── detect.py
│── app.py
│── data.yaml
│── requirements.txt
│── best.pt (model weights)
│── sample_output/


## 9. Results

The system is able to detect multiple weapon categories in real-time and highlight them using bounding boxes. Performance is generally reliable under standard lighting and clear visibility conditions.


## 10. Limitations

* The model performance depends on the quality and diversity of the training dataset
* False positives may occur in complex environments
* Detection accuracy may decrease in low-light or occluded conditions
* Large model size affects portability


## 11. Future Scope

* Train on a larger and more diverse custom dataset
* Integrate an alert or notification system
* Deploy as a web or mobile application
* Optimize the model for faster inference


## 12. Learnings

* Understanding of object detection using YOLOv7
* Experience with pretrained deep learning models
* Handling real-time video processing
* Application of computer vision in security systems


## 13. Note on Model Weights

Due to file size considerations, the trained model file (`best.pt`) may not be included in the repository. If not present, it should be downloaded separately and placed in the project directory before running the system.

## 14. Conclusion

This project demonstrates the practical application of deep learning in building an automated threat detection system. It highlights the effectiveness of YOLOv7 for real-time object detection and its potential use in surveillance and security domains.

