import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib
import os

# Load from local CSV
df = pd.read_csv("fake_job_postings.csv")
df = df[["description", "fraudulent"]].dropna()

X_train, X_test, y_train, y_test = train_test_split(df['description'], df['fraudulent'], test_size=0.2, random_state=42)

pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words='english', max_features=5000)),
    ('clf', LogisticRegression(max_iter=1000))
])

pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)

print(classification_report(y_test, y_pred))

os.makedirs("models", exist_ok=True)
joblib.dump(pipeline, "models/fake_job_model.pkl")
