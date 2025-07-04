import streamlit as st
import base64
import time
import streamlit.components.v1 as components
from pathlib import Path
from utils.utils_predict import predict_fake_job
from utils.utils_email_alert import send_alert_email
from utils.utils_dashboard import plot_prediction_bar  # Now includes animation!
from utils.utils_explain_model import explain_prediction

# --- Page Config ---
st.set_page_config(page_title="🚨 Fake Job Detector", layout="wide")

# --- Background Styling ---
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("assets/background.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        color: #f5f5f5;
    }

    .block-container {
        background-color: rgba(14, 17, 23, 0.8);
        padding: 2rem;
        border-radius: 15px;
    }

    textarea, .stTextInput>div>input {
        background-color: #1f1f2e;
        color: #f5f5f5;
        border: 1px solid #ff69b4;
        border-radius: 8px;
    }

    .stButton>button {
        background-color: #ff69b4;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        transition: 0.3s;
    }

    .stButton>button:hover {
        background-color: #ff85c1;
        transform: scale(1.02);
    }

    .stMarkdown h1, h2, h3, h4 {
        color: #90ee90 !important;
    }

    .stMetric label {
        color: #f5f5f5;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# --- Title Header ---
st.markdown("## 🚨 Real-Time Fake Job Detector")
st.markdown("### 💡 Paste a job description to check if it’s Real or Fake.")

# --- Example Input Toggle ---
col1, col2 = st.columns([1, 3])
with col1:
    st.radio("🌗 Theme:", ["Dark"], horizontal=True)
with col2:
    use_example = st.checkbox("💬 Use Example")
    example_text = (
        "We are seeking an enthusiastic individual to work remotely, no experience needed. "
        "Earn $2000/week just by posting ads online!"
    ) if use_example else ""

# --- Text Input ---
job_input = st.text_area("📝 Job Description", value=example_text, height=250)

# --- Analyze Button ---
if st.button("🔍 Analyze"):
    if not job_input.strip():
        st.warning("⚠️ Please enter a job description.")
    else:
        with st.spinner("🤖 Analyzing with AI..."):
            label, confidence, model_pipeline = predict_fake_job(job_input)
            label_text = "❌ Fake" if label == 1 else "✅ Real"
            confidence_percent = round(confidence * 100, 2)

            # Auto-scroll to results
            st.markdown("<script>window.scrollTo(0, document.body.scrollHeight);</script>", unsafe_allow_html=True)

            # 🎉 Confetti for Real Jobs
            if label == 0:
                st.balloons()

            # --- Results Display ---
            st.subheader("🎯 Prediction Results")
            st.metric(label="🔎 Prediction", value=label_text)
            plot_prediction_bar(label, confidence)  # Now includes animation + legend + accessibility

            # 🔉 Sound Alert if high-risk fake
            if label == 1 and confidence > 0.9:
                send_alert_email(job_input, confidence)
                st.warning("🚨 High-Risk Fake Job Detected!")
                st.audio("https://www.soundjay.com/button/beep-07.wav")

            

# --- Footer ---
st.markdown("""<br><hr><center>
Made by by Selvina Swarna | Powered by AI + Streamlit
</center>""", unsafe_allow_html=True)



