# train_model.py
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib
import re

# Load the data
df = pd.read_csv("fake_job_postings.csv")
df = df.dropna(subset=["description", "fraudulent"])

# Clean text
def clean_text(text):
    text = re.sub(r"http\\S+", "", text)
    text = re.sub(r"[^a-zA-Z\\s]", "", text)
    return text.lower().strip()

df["description"] = df["description"].astype(str).apply(clean_text)

# Feature and label
X = df["description"]
y = df["fraudulent"]

# Vectorize
vectorizer = TfidfVectorizer(stop_words="english", max_features=5000)
X_vec = vectorizer.fit_transform(X)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_vec, y)

# Save model and vectorizer locally
joblib.dump(model, "model/rf_model.pkl")
joblib.dump(vectorizer, "model/vectorizer.pkl")

print("✅ Model trained and saved on your machine!")
