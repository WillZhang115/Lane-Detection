
import os
import cv2
import numpy as np
from moviepy import VideoFileClip
from moviepy.video.io.ffmpeg_writer import FFMPEG_VideoWriter

def grayscale(img):
    """Convert image to grayscale."""
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def canny(img, low_threshold=100, high_threshold=200):
    """Apply Canny edge detection."""
    return cv2.Canny(img, low_threshold, high_threshold)

def gaussian_blur(img, kernel_size=7):
    """Apply Gaussian Blur to smooth the image."""
    return cv2.GaussianBlur(img, (kernel_size, kernel_size), 0)

def region_of_interest(img, vertices):
    """Apply a mask to keep only the region of interest."""
    mask = np.zeros_like(img)
    ignore_mask_color = 255 if len(img.shape) == 2 else (255,) * img.shape[2]
    cv2.fillPoly(mask, vertices, ignore_mask_color)
    return cv2.bitwise_and(img, mask)

def hough_lines(img, rho=2, theta=np.pi/180, threshold=20, min_line_len=50, max_line_gap=150):
    """Apply Hough Line Transform and return an image with detected lines drawn."""
    lines = cv2.HoughLinesP(img, rho, theta, threshold, np.array([]), minLineLength=min_line_len, maxLineGap=max_line_gap)
    line_img = np.zeros((*img.shape, 3), dtype=np.uint8)
    draw_lines(line_img, lines)
    return line_img

def draw_lines(img, lines, color=[255, 0, 0], thickness=6):
    """Draw lane lines on the image based on detected Hough lines."""
    if lines is None:
        return
    for line in lines:
        for x1, y1, x2, y2 in line:
            if x1 == x2:
                continue  # Avoid division by zero
            cv2.line(img, (x1, y1), (x2, y2), color, thickness)

def weighted_img(img, initial_img, alpha=0.8, beta=1.0, gamma=0.0):
    """Overlay the detected lane lines on the original image."""
    return cv2.addWeighted(initial_img, alpha, img, beta, gamma)

def pipeline(img):
    """Process the input image to detect lane lines."""
    gray = grayscale(img)
    blurred = gaussian_blur(gray)
    edges = canny(blurred)
    
    imshape = img.shape
    vertices = np.array([[(0, imshape[0]-100), (460, 400), (750, 400), (imshape[1], 600)]], dtype=np.int32)
    masked_edges = region_of_interest(edges, vertices)
    
    hough_line_img = hough_lines(masked_edges)
    result = weighted_img(hough_line_img, img)
    return result

def process_video(input_path, output_path, start_time=0, duration=10):
    """Process a video file using effects."""
    clip = VideoFileClip(input_path).subclipped(start_time, start_time + duration)
    
    output_dir = os.path.dirname(output_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    writer = FFMPEG_VideoWriter(output_path, clip.size, fps=clip.fps)
    

    for frame in clip.iter_frames(fps=clip.fps, dtype="uint8"):
        processed_frame = pipeline(frame)
        writer.write_frame(processed_frame)
    writer.close()

# Example Usage
# process_video("./test_videos/solidWhiteRight.mp4", "./test_videos_output/solidWhiteRight.mp4")