# Virtual Mouse with Hand Gestures

This project uses a webcam and hand gesture recognition to control your computer's mouse. Move the cursor using your index finger and perform click actions using simple pinch gestures — all without touching your mouse!

---

## Features

- Control the mouse with your index finger
- Click by pinching index and middle fingers together
- Move only within a defined frame region to avoid noise
- Smoothing applied to cursor movement for better control
- FPS counter overlay for performance tracking

---

## Tech Stack

- **Python**
- **OpenCV**
- **NumPy**
- **AutoPy** – for controlling mouse operations
- **MediaPipe** (inside `handDetection.py`) – for real-time hand tracking

---

## Project Structure
```bash
VirtualMouse/
├── handDetection.py # Custom hand tracking module
├── virtualMouse.py # Main script
├── images/ # (Optional) screenshots or demo GIFs
└── README.md
```
## Controls

| Gesture                        | Action                  |
|--------------------------------|--------------------------|
| ☝️ Index Finger Up             | Move the mouse cursor   |
| ✌️ Index + Middle Fingers Up   | Enter click-ready mode  |
| 🤏 Pinch (fingers touch)       | Perform a left click    |
| `d` key                        | Exit the application    |


