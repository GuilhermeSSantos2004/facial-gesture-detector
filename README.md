# Face Gesture Automation with MediaPipe and Arduino

This repository contains the code for an automation project based on facial position detection using MediaPipe in Python, and LED control via Arduino, reacting to head direction.

---

## 📌 What this project does

- Detects face keypoints in real time using **MediaPipe FaceMesh**
- Sends commands via **serial communication** to an Arduino
- Controls **LEDs** based on face direction (left, center, right)
- Supports **video files** or **live camera input**
- Includes **Python code**, **Arduino (C++) code**, and a **circuit diagram**

---

## Getting Started

1. Clone this repository

2. Create and activate a Python virtual environment:

```bash
py -3.10 -m venv env
env\Scripts\activate  # For Windows
source env/bin/activate  # For Linux/macOS
```

3. Install the required dependencies:

```bash
pip install mediapipe opencv-python pyserial
```

4. Open the Python code in your editor (e.g., VSCode)
5. Run the script and move your head to trigger LEDs connected to the Arduino


## 🛠 Repository Structure
face_direction_detector.py: Main Python script

- arduino_led_control.ino: Arduino code
- circuit_diagram.png: Circuit sketch with LEDs
- video.mp4 (optional): Input video if not using a live camera

## Applications

This project can be used as a base for:

- Human-machine interfaces with facial recognition
- Gesture-based home automation
- Educational projects combining computer vision and Arduino

