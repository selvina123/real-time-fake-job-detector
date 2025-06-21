from utils.bert_predict import predict_fake_job_bert
from utils.utils_logger import log_prediction
from utils.utils_email_alert import send_alert_email
import streamlit as st

st.set_page_config(page_title="🚨 BERT Fake Job Detector", layout="centered")

# Modern UI Styling
st.markdown("""
    <style>
    .main { background-color: #121212; color: #FFFFFF; font-family: 'Segoe UI'; }
    h1, h2 { color: #FF5F6D; }
    .stButton>button {
        background-color: #6C63FF; color: white;
        font-weight: bold; padding: 0.5em 2em;
        border-radius: 6px;
    }
    footer { visibility: hidden; }
    </style>
""", unsafe_allow_html=True)

st.title("🚨 Real-Time Fake Job Detector (BERT-Powered)")
st.markdown("🧠 *Paste a job description below and instantly detect scams using our AI.*")

job_input = st.text_area("📄 Paste Job Description", height=250)

if st.button("🔍 Detect Now"):
    if not job_input.strip():
        st.warning("⚠️ Please enter a job description to analyze.")
    else:
        label, confidence = predict_fake_job_bert(job_input)
        label_text = "❌ Fake" if label == 1 else "✅ Real"
        st.markdown(f"### Prediction: **{label_text}**")
        st.progress(confidence)
        st.markdown(f"**Confidence:** `{round(confidence * 100, 2)}%`")

        log_prediction(job_input, label, confidence)

        if label == 1 and confidence > 0.7:
            send_alert_email(job_input, confidence)

        st.markdown("---")
        st.caption("🛡️ Model powered by fine-tuned BERT + Streamlit UI")

st.markdown("""<hr><center>Made with 💻 by Selvina Swarna</center>""", unsafe_allow_html=True)
