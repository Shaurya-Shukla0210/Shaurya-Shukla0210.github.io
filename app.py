import streamlit as st
import cv2
import numpy as np
from PIL import Image

from preprocessing import resize_image, apply_gaussian_blur
from segmentation import get_segmented_regions
from analysis import analyze_segmentation, detect_edges


# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------

st.set_page_config(
    page_title="Image Segmentation & Object Analysis",
    page_icon="🖼️",
    layout="wide"
)


# ---------------------------------------------------------
# TITLE
# ---------------------------------------------------------

st.title("🖼️ Image Segmentation & Object Analysis System")

st.write(
    "A computer vision system for image preprocessing, "
    "segmentation, edge detection, and region analysis."
)


# ---------------------------------------------------------
# SIDEBAR SETTINGS
# ---------------------------------------------------------

st.sidebar.header("⚙️ Project Settings")

method = st.sidebar.selectbox(
    "Select Segmentation Method",
    ["K-Means", "Mean Shift"]
)

k = 3

if method == "K-Means":
    k = st.sidebar.slider(
        "Number of Clusters (K)",
        min_value=2,
        max_value=8,
        value=3
    )


# ---------------------------------------------------------
# IMAGE UPLOAD
# ---------------------------------------------------------

uploaded_file = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png"]
)


if uploaded_file is not None:

    # Read image
    image = Image.open(uploaded_file).convert("RGB")

    # Convert RGB to OpenCV BGR
    image_rgb = np.array(image)
    image_bgr = cv2.cvtColor(
        image_rgb,
        cv2.COLOR_RGB2BGR
    )

    # Resize
    image_bgr = resize_image(image_bgr)

    # -----------------------------------------------------
    # PREPROCESSING
    # -----------------------------------------------------

    blurred_image = apply_gaussian_blur(
        image_bgr
    )

    # -----------------------------------------------------
    # SEGMENTATION
    # -----------------------------------------------------

    segmented_image = get_segmented_regions(
        blurred_image,
        method,
        k
    )

    # -----------------------------------------------------
    # EDGE DETECTION
    # -----------------------------------------------------

    edges = detect_edges(
        segmented_image
    )

    # -----------------------------------------------------
    # ANALYSIS
    # -----------------------------------------------------

    metrics = analyze_segmentation(
        image_bgr,
        segmented_image
    )

    # -----------------------------------------------------
    # CONVERT IMAGES FOR DISPLAY
    # -----------------------------------------------------

    original_display = cv2.cvtColor(
        image_bgr,
        cv2.COLOR_BGR2RGB
    )

    blurred_display = cv2.cvtColor(
        blurred_image,
        cv2.COLOR_BGR2RGB
    )

    segmented_display = cv2.cvtColor(
        segmented_image,
        cv2.COLOR_BGR2RGB
    )
        # -----------------------------------------------------
    # DOWNLOAD SEGMENTED IMAGE
    # -----------------------------------------------------

    segmented_pil = Image.fromarray(segmented_display)

    import io

    image_buffer = io.BytesIO()
    segmented_pil.save(image_buffer, format="PNG")

    st.download_button(
        label="⬇️ Download Segmented Image",
        data=image_buffer.getvalue(),
        file_name="segmented_image.png",
        mime="image/png"
    )


    # -----------------------------------------------------
    # IMAGE RESULTS
    # -----------------------------------------------------

    st.subheader("📊 Image Processing Results")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.write("### Original Image")
        st.image(
            original_display,
            use_container_width=True
        )

    with col2:
        st.write("### Preprocessed Image")
        st.image(
            blurred_display,
            use_container_width=True
        )

    with col3:
        st.write("### Segmented Image")
        st.image(
            segmented_display,
            use_container_width=True
        )


    # -----------------------------------------------------
    # EDGE DETECTION RESULT
    # -----------------------------------------------------

    st.subheader("🔎 Edge Detection")

    edge_col1, edge_col2 = st.columns(2)

    with edge_col1:
        st.write("### Canny Edge Map")
        st.image(
            edges,
            use_container_width=True
        )

    with edge_col2:
        st.write("### Analysis")
        st.write(
            "Canny edge detection identifies important "
            "boundaries in the segmented image."
        )

        st.write(
            f"**Detected Edge Pixels:** "
            f"{metrics['Edge Count']}"
        )

        st.write(
            f"**Connected Regions:** "
            f"{metrics['Region Count']}"
        )


    # -----------------------------------------------------
    # PERFORMANCE METRICS
    # -----------------------------------------------------

    st.subheader("📈 Segmentation Analysis")

    metric1, metric2, metric3, metric4 = st.columns(4)

    with metric1:
        st.metric(
            "MSE",
            metrics["MSE"]
        )

    with metric2:
        st.metric(
            "PSNR",
            metrics["PSNR"]
        )

    with metric3:
        st.metric(
            "Edge Count",
            metrics["Edge Count"]
        )

    with metric4:
        st.metric(
            "Region Count",
            metrics["Region Count"]
        )


    # -----------------------------------------------------
    # PROCESSING INFORMATION
    # -----------------------------------------------------

    st.subheader("🔍 Processing Information")

    st.write(
        f"**Segmentation Method:** {method}"
    )

    if method == "K-Means":
        st.write(
            f"**Number of Clusters:** {k}"
        )

    st.write(
        "**Processing Pipeline:** "
        "Image Upload → Resizing → Gaussian Filtering → "
        "Segmentation → Canny Edge Detection → "
        "Region Analysis → Performance Evaluation"
    )


else:

    st.info(
        "👆 Upload a JPG, JPEG, or PNG image "
        "to start the analysis."
    )