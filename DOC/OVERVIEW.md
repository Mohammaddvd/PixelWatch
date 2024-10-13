## Main Application (main.py)
Captures images and compares them to detect movement.
Saves detected movement images and prints a notification.

## Image Processing Functions (pixel.py)
Functions for capturing images, comparing pixel values, and checking for camera detection.
The compare function checks pixel differences and identifies movement.
Notes
The sensitivity of movement detection can be adjusted by changing the threshold value in the compare function.
Ensure you have proper permissions to access the camera and write files to the directory.
