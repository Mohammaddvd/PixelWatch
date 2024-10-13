# Image Comparison Process
## Initialization:

The application starts by capturing a base image using the camera. This image serves as a reference for future comparisons.
Capturing Images:

The program captures a series of images in a loop. For each iteration, it captures a new image from the camera after the initial base image.
Pixel Comparison:

The core of the movement detection lies in the pixel comparison process. The following steps outline how this works:
a. Image Loading:

The get_p() function loads both the base image (test.png) and the new image (test2.png) using the Pillow library.
The pixel data for both images is accessed through the load() method, which allows for pixel-wise manipulation.
b. Border Calculation:

The get_b(w, h) function generates a list of pixel positions to check. It divides the image into a grid-like structure by creating lists of positions that correspond to specific parts of the image (e.g., every 10% of width and height).
This helps limit the number of pixels that need to be checked, making the comparison process more efficient.
c. Pixel Difference Calculation:

The compare(px, px2, bs) function compares the pixel values from the base image and the new image at the specified positions.
It iterates through the predefined positions (borders) and checks the RGB values of each corresponding pixel in both images.
A threshold is applied to determine whether a pixel has changed. In this case, if the difference in RGB values is within ±15 for each color channel (R, G, B), the pixels are considered unchanged. If the difference exceeds this threshold, the pixel is marked as changed.
d. Change Detection:

A counter (c) keeps track of the number of changed pixels. If the number of changed pixels exceeds a defined threshold (300 in this case), the function concludes that movement has been detected and returns True.
If the number of changes is below this threshold, it returns False, indicating no significant movement.
Movement Notification:

If movement is detected (i.e., get_p() returns True), the new image (test2.png) is saved with a filename indicating that movement has occurred (e.g., 0_movement.png).
