Lane Detection Using Computer Vision

This repository contains a lane detection pipeline using OpenCV and Python. The goal is to detect lane markings in images and videos using edge detection and Hough Transform.

📌 Features

Grayscale conversion and Gaussian blurring for noise reduction.

Canny edge detection to extract lane boundaries.

Region of interest selection to filter unnecessary information.

Hough Line Transform for lane detection.

Weighted overlay of detected lanes on the original image.

📂 Project Structure

```
Lane-Detection/                    
│── test_images/          # Folder for sample test images
│── test_videos/          # Folder for sample test videos
│── output/                   # Folder for storing output videos and images
│── src/                      # Source code for the lane detection pipeline
│   ├── lane_detection.py     # Main script containing lane detection functions
│   ├── usage_image.py
│   ├── usage_video.py 
│── README.md                 # Project documentation
│── .gitignore                # Files to be ignored by Git
```

🚀 Installation

Clone the repository:

git clone https://github.com/WillZhang115/Lane-Detection.git
cd Lane-Detection

🛠 Usage

Running Lane Detection on an Image
```
from lane_detection import pipeline
import cv2
import matplotlib.pyplot as plt

image = cv2.imread("../test_images/sample.jpg")
result = pipeline(image)
plt.imshow(result)
plt.show()
```
Processing a Video
```
from lane_detection import process_video
process_video("../test_videos/input.mp4", "output/output.mp4")
```
📜 Requirements
```
numpy
opencv-python
matplotlib
pillow
moviepy
```
📝 License

This project is licensed under the MIT License.

🙌 Acknowledgments

Udacity Self-Driving Car Nanodegree materials.

OpenCV documentation and community support.

