from transformers import pipeline
import torch

# Load the AI model for scam detection
device = "cuda" if torch.cuda.is_available() else "cpu"

# Sentiment analysis (already tested)
sentiment_model = pipeline("sentiment-analysis", device=0 if torch.cuda.is_available() else -1)

def analyze_sentiment(text):
    result = sentiment_model(text)
    return result

# FinBERT Model for Scam Detection
scam_model = pipeline("text-classification", model="ProsusAI/finbert", device=0 if torch.cuda.is_available() else -1)

def detect_scam(text):
    result = scam_model(text)
    return result
