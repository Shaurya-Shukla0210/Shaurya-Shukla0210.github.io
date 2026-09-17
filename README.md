# Image Segmentation & Object Analysis System

## Project Overview

The Image Segmentation & Object Analysis System is a Python-based computer vision application designed to demonstrate important Digital Image Processing concepts.

The system allows users to upload an image and perform preprocessing, image segmentation, edge detection, region analysis, and performance evaluation through an interactive Streamlit interface.

Two segmentation techniques are provided: K-Means Clustering and Mean Shift Segmentation.

The system uses Gaussian filtering for preprocessing and Canny Edge Detection for identifying important image boundaries.

## Objectives

The main objectives of this project are:

- To preprocess digital images using Gaussian filtering.
- To implement K-Means based image segmentation.
- To implement Mean Shift based image segmentation.
- To detect image boundaries using Canny Edge Detection.
- To perform basic connected-region analysis.
- To evaluate segmentation results using MSE and PSNR.
- To provide an interactive interface for image processing.
- To allow users to download the segmented image.

## Features

### Image Upload

Users can upload JPG, JPEG, or PNG images for processing.

### Image Preprocessing

The system resizes the uploaded image and applies Gaussian filtering to reduce noise before segmentation.

### K-Means Segmentation

K-Means clustering groups image pixels into a selected number of clusters. The user can select the number of clusters from the sidebar.

### Mean Shift Segmentation

Mean Shift segmentation groups pixels according to their spatial and color characteristics.

### Canny Edge Detection

Canny Edge Detection is used to identify important boundaries in the segmented image.

### Region Analysis

The system performs connected-region analysis and displays the detected region count.

### Performance Analysis

The system calculates Mean Squared Error (MSE), Peak Signal-to-Noise Ratio (PSNR), Edge Count, and Region Count.

### Result Download

The generated segmented image can be downloaded as a PNG file.

## Processing Pipeline

Image Upload → Image Resizing → Gaussian Filtering → Image Segmentation → Canny Edge Detection → Region Analysis → Performance Evaluation → Result Download

## Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Core programming language |
| OpenCV | Image processing and computer vision |
| NumPy | Numerical operations |
| Pillow | Image loading and conversion |
| Streamlit | Web-based user interface |

## Project Structure

Image-Segmentation-Project/

├── app.py  
├── preprocessing.py  
├── segmentation.py  
├── analysis.py  
├── requirement.txt  
├── README.md  
├── statement.md  
│  
├── Images/  
│   └── Sample input images  
│  
└── Results/  
    └── Generated result screenshots

## File Description

### app.py

Contains the Streamlit application and user interface.

### preprocessing.py

Contains image preprocessing functions such as resizing and Gaussian filtering.

### segmentation.py

Contains K-Means and Mean Shift segmentation functions.

### analysis.py

Contains Canny edge detection, region analysis, MSE, and PSNR calculations.

### requirement.txt

Contains the Python packages required to run the project.

### README.md

Contains the project documentation, features, technologies, installation instructions, usage instructions, testing information, and future enhancements.

### statement.md

Contains the project statement, scope, target users, and high-level features.

### Images/

Contains sample input images used for testing.

### Results/

Contains screenshots and generated results from the segmentation experiments.

## Installation

Make sure Python is installed on your computer.

Open the project folder in the terminal and install the required packages using:

pip install -r requirement.txt

## Running the Application

Run the following command in the terminal:

streamlit run app.py

The application will open in a web browser.

## How to Use

1. Start the Streamlit application.
2. Select a segmentation method from the sidebar.
3. If K-Means is selected, choose the required number of clusters.
4. Upload a JPG, JPEG, or PNG image.
5. View the original image.
6. View the preprocessed image.
7. View the segmented image.
8. View the Canny edge map.
9. Check MSE, PSNR, Edge Count, and Region Count.
10. Download the segmented image.

## Testing

The application was tested using sample images.

The following functions were tested:

| Test Case | Expected Result |
|-----------|-----------------|
| Upload JPG image | Image is accepted |
| Upload PNG image | Image is accepted |
| Select K-Means | K-Means segmentation is performed |
| Change K value | Segmentation result changes |
| Select Mean Shift | Mean Shift segmentation is performed |
| Canny Edge Detection | Edge map is generated |
| Region Analysis | Region count is displayed |
| Performance Analysis | MSE and PSNR are displayed |
| Download Result | Segmented image is downloaded |

## Results

The system successfully produces:

- Original image
- Preprocessed image
- K-Means segmented image
- Mean Shift segmented image
- Canny edge map
- MSE value
- PSNR value
- Edge count
- Region count

The exact numerical results depend on the input image and segmentation parameters.

## Limitations

The project is primarily designed for educational demonstration.

The quality of segmentation depends on the input image and selected parameters. K-Means requires an appropriate choice of cluster count, while Mean Shift depends on its processing parameters.

The current system does not perform advanced semantic object recognition.

## Future Enhancements

Possible future improvements include:

- Adding Region Growing segmentation.
- Adding Graph Cut segmentation.
- Adding watershed segmentation.
- Adding texture-based segmentation.
- Adding automatic parameter selection.
- Adding advanced object detection.
- Adding video processing.
- Adding ground-truth based segmentation accuracy metrics.
- Improving visualization and user interface.

## Applications

The techniques demonstrated in this project can be applied to:

- Object detection
- Medical image analysis
- Industrial inspection
- Autonomous systems
- Satellite image analysis
- Computer vision research
- Image processing applications

## Conclusion

The Image Segmentation & Object Analysis System demonstrates several important Digital Image Processing concepts through an interactive application.

The project combines image preprocessing, K-Means segmentation, Mean Shift segmentation, Canny edge detection, region analysis, and quantitative evaluation into a single workflow.

The application provides a practical demonstration of how different image processing techniques can be combined to analyze digital images.