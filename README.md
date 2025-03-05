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
│── data/                     # Folder for sample images and videos
│   ├── test_images/          # Sample test images
│   ├── test_videos/          # Sample test videos
│── output/                   # Folder for storing output videos and images
│── src/                      # Source code for the lane detection pipeline
│   ├── lane_detection.py     # Main script containing lane detection functions
│── notebooks/                # Jupyter notebooks for visualization and experimentation
│   ├── lane_detection.ipynb  # Notebook for testing and visualizing lane detection
│── README.md                 # Project documentation
│── .gitignore                # Files to be ignored by Git
```

🚀 Installation

Clone the repository:

git clone https://github.com/WillZhang115/Lane-Detection.git
cd Lane-Detection

🛠 Usage

Running Lane Detection on an Image

from src.lane_detection import pipeline
import cv2
import matplotlib.pyplot as plt

image = cv2.imread("data/test_images/sample.jpg")
result = pipeline(image)
plt.imshow(result)
plt.show()

Processing a Video

from src.lane_detection import process_video
process_video("data/test_videos/input.mp4", "output/output.mp4")

📜 Requirements

Create a requirements.txt file with the following dependencies:

numpy
opencv-python
matplotlib
pillow
moviepy

📝 License

This project is licensed under the MIT License.

🙌 Acknowledgments

Udacity Self-Driving Car Nanodegree materials.

OpenCV documentation and community support.

