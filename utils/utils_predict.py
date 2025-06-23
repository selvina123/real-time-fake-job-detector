# utils_predict.py
import joblib
import numpy as np

model = joblib.load("model/rf_model.pkl")  # your current filename
vectorizer = joblib.load("model/vectorizer.pkl")  # your current filename

def predict_fake_job(text):
    vectorized = vectorizer.transform([text])
    prediction = model.predict(vectorized)[0]
    confidence = np.max(model.predict_proba(vectorized))
    return prediction, confidence, model
