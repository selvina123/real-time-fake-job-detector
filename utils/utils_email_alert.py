import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

load_dotenv()  # Load from .env

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD")
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")

def send_alert_email(job_description, confidence_score):
    subject = "🚨 Fake Job Detected Alert"
    body = f"""
    A suspicious job posting was detected:

    📝 Job Description:
    {job_description}

    🔐 Confidence: {round(confidence_score * 100, 2)}%

    Please verify this post immediately.
    """

    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECEIVER_EMAIL
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.send_message(msg)
            print("✅ Alert email sent successfully!")
    except Exception as e:
        print("❌ Failed to send email:", e)
