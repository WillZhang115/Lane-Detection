from lane_detection import pipeline
import cv2
import matplotlib.pyplot as plt

image = cv2.imread("../test_images/sample.jpg")
result = pipeline(image)
plt.imshow(result)
plt.show()