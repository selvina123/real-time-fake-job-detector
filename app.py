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
    }

    .block-container {
        background-color: rgba(0, 0, 0, 0.6);
        padding: 2rem;
        border-radius: 15px;
    }

    textarea, .stTextInput>div>input {
        background-color: #1c1e26;
        color: #fff;
    }

    .stButton>button {
        background-color: #ff4c98;
        color: white;
        font-weight: bold;
        border-radius: 10px;
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

            # 🤖 Chatbot-style Explanation
            with st.expander("🤖 Why did the model predict this?"):
                st.markdown("**🧠 AI says:**")
                try:
                    explanation_html = explain_prediction(model_pipeline, job_input, return_html=True)
                    st.markdown(
                        f"<div style='background-color:#111111; padding:10px; border-radius:10px;'>{explanation_html}</div>",
                        unsafe_allow_html=True
                    )
                except TypeError:
                    st.error("⚠️ Explanation rendering failed. Please check `explain_prediction()` function.")

# --- Footer ---
st.markdown("""<br><hr><center>
Made with ❤️ by Selvina Swarna | Powered by AI + Streamlit
</center>""", unsafe_allow_html=True)



