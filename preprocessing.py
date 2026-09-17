import cv2
import numpy as np


def resize_image(image, width=600):
    """
    Resize image while maintaining aspect ratio.
    """
    height, original_width = image.shape[:2]

    if original_width == width:
        return image

    ratio = width / original_width
    new_height = int(height * ratio)

    return cv2.resize(image, (width, new_height))


def convert_to_grayscale(image):
    """
    Convert a color image to grayscale.
    """
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def apply_gaussian_blur(image, kernel_size=5):
    """
    Reduce noise using Gaussian filtering.
    """
    return cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)


def enhance_image(image):
    """
    Enhance image contrast using histogram equalization.
    """
    gray = convert_to_grayscale(image)
    enhanced = cv2.equalizeHist(gray)

    return enhanced