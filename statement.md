# Project Statement

## Project Title

Image Segmentation & Object Analysis System

## Problem Statement

Digital images often contain complex colors, textures, objects, and boundaries, making it difficult to analyze individual regions directly. Image segmentation is a fundamental computer vision technique used to divide an image into meaningful regions based on visual characteristics.

The objective of this project is to develop a simple computer vision system that allows a user to upload an image and perform image preprocessing, image segmentation, edge detection, and region analysis.

The system applies Gaussian filtering as a preprocessing technique and provides two segmentation approaches: K-Means clustering and Mean Shift segmentation. Canny edge detection is then applied to identify important boundaries, followed by basic region analysis and quantitative evaluation using MSE, PSNR, edge count, and region count.

## Scope of the Project

The project focuses on image-based processing and analysis. The system provides the following capabilities:

1. Upload JPG, JPEG, and PNG images.
2. Resize uploaded images for processing.
3. Apply Gaussian filtering for noise reduction.
4. Perform image segmentation using K-Means clustering.
5. Perform image segmentation using Mean Shift.
6. Detect image boundaries using the Canny edge detector.
7. Analyze connected regions.
8. Calculate MSE and PSNR for result evaluation.
9. Display original, preprocessed, segmented, and edge-detected images.
10. Download the generated segmented image.

The project is designed as an educational computer vision application demonstrating concepts covered in the Digital Image Processing syllabus.

## Target Users

The system is intended for:

- Students studying Digital Image Processing and Computer Vision.
- Faculty members demonstrating image processing concepts.
- Beginners learning image segmentation techniques.
- Users who want to visually compare basic segmentation approaches.

## High-Level Features

### 1. Image Input Module

The user can upload an image in JPG, JPEG, or PNG format through the application interface.

### 2. Image Preprocessing Module

The uploaded image is resized and processed using Gaussian filtering to reduce noise before segmentation.

### 3. Image Segmentation Module

The system provides two segmentation methods:

- K-Means clustering
- Mean Shift segmentation

For K-Means, the user can select the number of clusters.

### 4. Edge Detection Module

The system uses the Canny edge detection algorithm to identify significant boundaries in the segmented image.

### 5. Region Analysis Module

Connected regions are analyzed and the number of detected regions is displayed.

### 6. Performance Analysis Module

The system calculates:

- Mean Squared Error (MSE)
- Peak Signal-to-Noise Ratio (PSNR)
- Edge Count
- Region Count

### 7. Result Export Module

The user can download the generated segmented image for further analysis or documentation.

## Technologies Used

- Python
- OpenCV
- NumPy
- Pillow
- Streamlit

## Expected Outcome

The completed system provides an interactive interface for demonstrating image preprocessing, segmentation, edge detection, and region analysis. It allows users to visually compare processing results and examine basic quantitative metrics.