from datetime import datetime
import csv
import os
import streamlit as st

LOG_FILE = "prediction_logs.csv"

# 🔹 Function to log predictions
def log_prediction(job_text, label, confidence):
    file_exists = os.path.isfile(LOG_FILE)
    with open(LOG_FILE, mode="a", newline='', encoding="utf-8") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Timestamp", "Job Description", "Prediction", "Confidence"])
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            job_text[:1000].replace('\n', ' '),
            "Fake" if label == 1 else "Real",
            round(confidence, 4)
        ])

# 🔹 Function to provide download button for logs
def download_log():
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r", encoding="utf-8") as file:
            content = file.read()
            st.download_button("📁 Download Log as CSV", data=content, file_name="prediction_logs.csv", mime="text/csv")
    else:
        st.info("📂 No log file found yet.")
