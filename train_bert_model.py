
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import torch
from torch.utils.data import DataLoader
from transformers import BertTokenizer, BertForSequenceClassification, Trainer, TrainingArguments
from datasets import Dataset

# Load and preprocess data
df = pd.read_csv("fake_job_postings.csv")
df = df[["description", "fraudulent"]].dropna()

label_encoder = LabelEncoder()
df["label"] = label_encoder.fit_transform(df["fraudulent"])

# Split data
train_texts, val_texts, train_labels, val_labels = train_test_split(
    df["description"].tolist(), df["label"].tolist(), test_size=0.2, random_state=42)

# Tokenization
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

def tokenize(batch):
    return tokenizer(batch["description"], padding="max_length", truncation=True)

train_dataset = Dataset.from_dict({"description": train_texts, "label": train_labels}).map(tokenize, batched=True)
val_dataset = Dataset.from_dict({"description": val_texts, "label": val_labels}).map(tokenize, batched=True)

train_dataset.set_format("torch", columns=["input_ids", "attention_mask", "label"])
val_dataset.set_format("torch", columns=["input_ids", "attention_mask", "label"])

# Load model
model = BertForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=2)

# Training arguments
training_args = TrainingArguments(
    output_dir="./bert_output",
    evaluation_strategy="epoch",
    logging_dir="./logs",
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    num_train_epochs=3,
    save_total_limit=1,
    load_best_model_at_end=True,
)

# Train
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=val_dataset,
    tokenizer=tokenizer,
)

trainer.train()

# Save model & tokenizer
model.save_pretrained("bert_model")
tokenizer.save_pretrained("bert_model")
