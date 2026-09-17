import cv2
import numpy as np


def calculate_mse(original, segmented):
    """
    Calculate Mean Squared Error between two images.
    """
    original = original.astype(np.float32)
    segmented = segmented.astype(np.float32)

    mse = np.mean((original - segmented) ** 2)

    return round(float(mse), 2)


def calculate_psnr(original, segmented):
    """
    Calculate Peak Signal-to-Noise Ratio.
    """
    mse = calculate_mse(original, segmented)

    if mse == 0:
        return float("inf")

    psnr = 10 * np.log10((255 ** 2) / mse)

    return round(float(psnr), 2)


def detect_edges(image):
    """
    Detect edges using the Canny edge detector.
    """
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(gray, 100, 200)

    return edges


def calculate_edge_count(image):
    """
    Count the number of detected edge pixels.
    """
    edges = detect_edges(image)

    return int(np.count_nonzero(edges))


def analyze_regions(image):
    """
    Analyze connected regions in the image.
    """
    edges = detect_edges(image)

    # Convert edges into a binary image
    binary = cv2.threshold(
        edges,
        0,
        255,
        cv2.THRESH_BINARY
    )[1]

    # Find connected components
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(
        binary,
        connectivity=8
    )

    # Ignore the background
    region_count = max(0, num_labels - 1)

    return region_count


def analyze_segmentation(original, segmented):
    """
    Generate segmentation performance metrics.
    """
    mse = calculate_mse(original, segmented)
    psnr = calculate_psnr(original, segmented)
    edge_count = calculate_edge_count(segmented)
    region_count = analyze_regions(segmented)

    return {
        "MSE": mse,
        "PSNR": psnr,
        "Edge Count": edge_count,
        "Region Count": region_count
    }