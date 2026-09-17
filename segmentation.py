import cv2
import numpy as np


def kmeans_segmentation(image, k=3):
    """
    Segment an image using K-Means clustering.

    Parameters:
        image: Input BGR image.
        k: Number of clusters.

    Returns:
        Segmented BGR image.
    """
    # Convert image pixels into a 2D array
    pixels = image.reshape((-1, 3))
    pixels = np.float32(pixels)

    # K-Means termination criteria
    criteria = (
        cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,
        100,
        0.2
    )

    # Apply K-Means
    _, labels, centers = cv2.kmeans(
        pixels,
        k,
        None,
        criteria,
        10,
        cv2.KMEANS_RANDOM_CENTERS
    )

    # Convert centers back to uint8
    centers = np.uint8(centers)

    # Replace each pixel with its cluster center
    segmented_pixels = centers[labels.flatten()]

    # Restore original image dimensions
    segmented_image = segmented_pixels.reshape(image.shape)

    return segmented_image


def mean_shift_segmentation(image):
    """
    Segment an image using Mean Shift filtering.
    """
    segmented_image = cv2.pyrMeanShiftFiltering(
        image,
        sp=20,
        sr=30
    )

    return segmented_image


def get_segmented_regions(image, method="K-Means", k=3):
    """
    Select the segmentation method.
    """
    if method == "K-Means":
        return kmeans_segmentation(image, k)

    elif method == "Mean Shift":
        return mean_shift_segmentation(image)

    else:
        raise ValueError("Invalid segmentation method selected.")