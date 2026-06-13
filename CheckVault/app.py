import streamlit as st

from modules.ocr import extract_text
from modules.parser import parse_salary_slip
from modules.metadata import analyze_metadata
from modules.risk import calculate_risk
from modules.ela import perform_ela

# ---------------------------
# PAGE CONFIG
# ---------------------------

st.set_page_config(
    page_title="CheckVault",
    page_icon="🛡️",
    layout="wide"
)

# ---------------------------
# HEADER
# ---------------------------

st.title("🛡️ CheckVault")
st.subheader("AI-Powered Document Verification & Fraud Detection System")

# ---------------------------
# FILE UPLOAD
# ---------------------------

uploaded_file = st.file_uploader(
    "Upload a document image",
    type=["png", "jpg", "jpeg"]
)

# ---------------------------
# MAIN ANALYSIS
# ---------------------------

if uploaded_file:

    st.image(
        uploaded_file,
        caption="Uploaded Document",
        use_container_width=True
    )

    if st.button("Run Full Analysis"):

        # OCR
        st.header("📄 OCR Analysis")

        with st.spinner("Extracting text..."):
            text = extract_text(uploaded_file)

        st.text(text)

        # PARSER
        st.header("📊 Structured Data")

        parsed_data = parse_salary_slip(text)

        st.json(parsed_data)

        # METADATA
        st.header("📋 Metadata Analysis")

        metadata = analyze_metadata(uploaded_file)

        st.json(metadata)

        # RISK
        st.header("🚨 Risk Assessment")

        risk_data = calculate_risk(metadata)

        st.json(risk_data)

        # ELA
        st.header("🔍 Error Level Analysis (ELA)")

        ela_image = perform_ela(uploaded_file)

        st.image(
            ela_image,
            caption="ELA Tampering Heatmap",
            use_container_width=True
        )

        # RECOMMENDATION
        st.header("🏦 Underwriting Recommendation")

        score = risk_data["risk_score"]

        if score <= 20:

            st.success("✅ APPROVE")

            st.write(
                "Document appears genuine based on current checks."
            )

        elif score <= 50:

            st.warning("⚠️ MANUAL REVIEW")

            st.write(
                "Additional verification recommended."
            )

        else:

            st.error("❌ REJECT / INVESTIGATE")

            st.write(
                "Potential fraud indicators detected."
            )

        st.divider()

        st.subheader("📌 Final Fraud Summary")

        st.write(f"Risk Score: **{risk_data['risk_score']}**")
        st.write(f"Risk Level: **{risk_data['risk_level']}**")

        if len(risk_data["reasons"]) > 0:

            st.write("Detected Issues:")

            for reason in risk_data["reasons"]:
                st.write(f"• {reason}")

        else:

            st.write("No significant fraud indicators detected.")