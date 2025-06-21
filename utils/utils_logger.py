import datetime

def log_prediction(text, label, confidence):
    with open("prediction_log.csv", "a") as f:
        f.write(f"{datetime.datetime.now()},{label},{confidence:.2f},\"{text}\"\n")
