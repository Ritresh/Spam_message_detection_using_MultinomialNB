# train.py
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle
import pandas as pd

# Load your cleaned & preprocessed dataset
df = pd.read_csv('dataset/processed/spam_cleaned.csv')  # or train_processed.csv if that’s the file name

X = df['transformed_text']
y = df['target']

# Handle NaN values
df = df.dropna(subset=['transformed_text'])
X = df['transformed_text']
y = df['target']

# split train test 
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=42)

pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(max_features=3000)),
    ('mnb', MultinomialNB())
])

pipeline.fit(X_train, y_train)   # ✅ THIS WAS MISSING

import os
import pickle

# Make sure the folder exists
os.makedirs('models', exist_ok=True)  # creates 'models' folder if missing

# Save the trained pipeline in the models folder
pickle.dump(pipeline, open('models/spam_model3.pkl', 'wb'))
print("Model trained and saved as models/spam_model3.pkl")

