# Raspberry Pi Movement Detection App

## Overview
### Created For Fun
This project is a simple application designed to run on a Raspberry Pi that captures images and detects movement. When movement is detected between consecutive images, the app saves the changed image and provides a notification. I created this project for fun and to explore ways to weaponize my Raspberry Pi with various tools, enhancing its capabilities for practical applications.
Version : 1.0.0
## Features

- Captures multiple images using a camera module.
- Compares consecutive images to detect changes.
- Saves images where movement is detected.
- Simple command-line interface.

## Requirements

- Raspberry Pi with camera module (make sure the camera is enabled in the Raspberry Pi configuration).
- Python 3.x installed on your Raspberry Pi.
- Required libraries:
  - `PIL` (Pillow)
  - `opencv-python`

## Installation

1. **Clone the repository**:
```
git clone https://github.com/Mohammaddvd/PixelWatch
cd PixelWatch
python3 capture.py
```

https://github.com/user-attachments/assets/54e70f7e-7cb4-4bd0-8a46-df16914639f0

