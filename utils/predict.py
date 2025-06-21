import joblib
from utils.preprocess import clean_text

model = joblib.load("model/rf_model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")

def predict_fake_job(text):
    text_cleaned = clean_text(text)
    vec = vectorizer.transform([text_cleaned])
    prediction = model.predict(vec)[0]
    prob = model.predict_proba(vec)[0][1]
    return prediction, prob
