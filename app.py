import streamlit as st
from utils.predict import predict_fake_job

st.set_page_config(page_title="Fake Job Detector", layout="centered")
st.title("🚨 Real-Time Fake Job Detector")

job_input = st.text_area("Paste a job description here:", height=300)

if st.button("Check Now"):
    if not job_input.strip():
        st.warning("Please enter a job description.")
    else:
        label, confidence = predict_fake_job(job_input)
        label_text = "❌ Fake" if label == 1 else "✅ Real"
        st.markdown(f"### Prediction: **{label_text}**")
        st.markdown(f"Confidence: **{round(confidence*100, 2)}%**")
