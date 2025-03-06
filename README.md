"""
Jarvis 2.0 - Emotion Detection System
====================================

## Overview
Jarvis 2.0 is an AI-powered assistant that detects facial expressions using OpenCV's deep learning module and provides voice feedback based on detected emotions.

## Installation
Before running the script, ensure you have installed the required dependencies:
```sh
pip install opencv-python numpy pyttsx3
```

## How It Works
1. The script uses OpenCV's Deep Neural Network (DNN) module to load a pre-trained Caffe model for facial expression detection.
2. The webcam captures a live video stream.
3. The captured frame is processed and passed through the model to determine the most dominant emotion.
4. The detected emotion is displayed on the screen.
5. If an emotion is detected, the system provides voice feedback using `pyttsx3`.
6. The loop continues until the user presses 'q' to exit.

## Code Explanation
- **Imports:**
  - `cv2`: OpenCV for image processing.
  - `numpy`: Numerical operations.
  - `pyttsx3`: Text-to-speech conversion.
- **Loading Model:**
  - The Caffe model (`res10_300x300_ssd_iter_140000.caffemodel`) and its configuration (`deploy.prototxt.txt`) are loaded.
- **Processing Video:**
  - Frames are captured and resized.
  - The frames are passed into the model for emotion classification.
- **Voice Feedback:**
  - If an emotion is detected, the system announces it.

## Running the Script
Run the script using:
```sh
python script_name.py
```
Replace `script_name.py` with the actual filename.

## Exiting the Program
Press 'q' to close the window and terminate the script.

"""
