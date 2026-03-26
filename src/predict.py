# predict.py

import pickle
import os
import sys
from pathlib import Path

# Get project root (one level above src)
ROOT_DIR = Path(__file__).resolve().parent.parent

# Add project root to Python path so "src" can be imported
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

# ✅ now this import will work
from src.data_preprocessig import transform_text


# Model path
MODEL_PATH = ROOT_DIR / "models" / "spam_model3.pkl"


# Load model once
with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)


def predict(text, model=model):
    """Classify text and return spam or ham"""
    processed = transform_text(text)
    prediction = model.predict([processed])[0]
    return "spam" if prediction == 1 else "ham"


def load_model(path=MODEL_PATH):
    with open(path, "rb") as f:
        return pickle.load(f)


# CLI test
if __name__ == "__main__":
    user_text = input("Enter text to classify: ")
    result = predict(user_text, model=model)
    print("Prediction:", result)