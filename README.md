# 📧 Spam Message Detection using NLP

A machine learning project that classifies SMS messages as **Spam** or **Ham (Not Spam)** using Natural Language Processing (NLP) techniques and a Naive Bayes classifier. The project includes data preprocessing, model training, experimentation with different algorithms, and a Streamlit web interface for real-time prediction.

---

## 📌 Table of Contents

- Overview  
- Problem Statement  
- Dataset  
- Tools & Technologies  
- Project Structure  
- Data Cleaning & Preprocessing  
- Exploratory Data Analysis (EDA)  
- Model Building  
- Model Comparison  
- Streamlit Application  
- How to Run This Project  
- Future Improvements  
- Author & Contact  

---

# Overview

Spam messages are a common problem in messaging platforms and email systems. Detecting spam automatically helps protect users from phishing, scams, and unwanted advertisements.

This project builds an **SMS spam classifier using Natural Language Processing (NLP)**. The system processes text messages, converts them into numerical representations using **TF-IDF vectorization**, and classifies them using **Machine Learning models**.

The project includes:

- Data cleaning and preprocessing pipeline  
- Feature engineering using NLP techniques  
- Multiple model experiments and comparisons  
- A trained **Naive Bayes classification model**  
- An interactive **Streamlit web application**

---

# Problem Statement

Given a text message, the system should automatically determine whether it is:

- **Spam** → promotional, fraudulent, or unwanted message  
- **Ham** → legitimate or normal message  

The goal is to build a reliable classification model that can **accurately detect spam messages using machine learning and NLP techniques**.

---

# Dataset

The project uses the **SMS Spam Collection Dataset**, which contains labeled SMS messages.

Each message is labeled as:

- **ham** → normal message  
- **spam** → unwanted promotional or scam message  

Dataset files used in this project:

dataset/raw/spam.csv  
dataset/processed/spam_cleaned.csv  

The processed dataset includes additional columns such as:

- transformed_text  
- num_characters  
- num_words  
- num_sentences  

---

# Tools & Technologies

### Programming Language
- Python

### Development Environment
- Visual Studio Code (VS Code)

### Data Analysis
- Pandas  
- NumPy  

### Visualization
- Matplotlib  
- Seaborn  
- WordCloud  

### Natural Language Processing
- NLTK  
- Stopword Removal  
- Tokenization  
- Porter Stemming  

### Machine Learning
- Scikit-learn  
- TF-IDF Vectorizer  
- Multinomial Naive Bayes  
- Logistic Regression  
- Support Vector Machine  
- Random Forest  
- Gradient Boosting  

### Application
- Streamlit  

### Version Control
- Git  
- GitHub  

---

# Project Structure

Spam Message Detection using NLP/

├── app/  
│   └── streamlit_app.py  

├── dataset/  
│   ├── raw/  
│   │   └── spam.csv  
│   │  
│   └── processed/  
│       ├── spam.csv  
│       └── spam_cleaned.csv  

├── models/  
│   └── spam_model3.pkl  

├── notebook/  
│   ├── spam.ipynb  
│   └── differnet_models.ipynb  

├── src/  
│   ├── __init__.py  
│   ├── data_preprocessing.py  
│   ├── predict.py  
│   └── train.py  

├── requirements.txt  
├── .gitignore  
└── README.md  

---

# Data Cleaning & Preprocessing

The dataset undergoes several preprocessing steps.

### Removing Unnecessary Columns

Columns with large numbers of missing values were removed:

- Unnamed:2  
- Unnamed:3  
- Unnamed:4  

### Renaming Columns

Original dataset columns were renamed:

v1 → target  
v2 → text  

### Label Encoding

ham → 0  
spam → 1  

### Removing Duplicates

Duplicate messages were removed to avoid bias in the model.

### Text Processing Pipeline

The preprocessing function performs several NLP operations:

1. Convert text to lowercase  
2. Tokenize words using NLTK  
3. Remove punctuation and special characters  
4. Remove stopwords  
5. Apply stemming using Porter Stemmer  

Example:

Original:  
"Congratulations! You have won a free prize."

Processed:  
"congratul free prize"

---

# Exploratory Data Analysis (EDA)

Several analyses were performed to understand the dataset.

### Message Distribution

Spam vs Ham distribution visualized using a pie chart.

Observation:

- Ham messages dominate the dataset  
- Spam messages represent a smaller proportion  

### Text Statistics

Additional features created:

- Number of characters  
- Number of words  
- Number of sentences  

These features help analyze patterns between spam and ham messages.

### Word Frequency Analysis

Common spam words discovered using WordCloud and frequency analysis:

free  
win  
offer  
prize  
call  

---

# Model Building

Text messages were converted into numerical vectors using **TF-IDF Vectorization**.

Text → TF-IDF Vector → Machine Learning Model

The final classification model used:

**Multinomial Naive Bayes**

Pipeline:

TF-IDF Vectorizer  
↓  
Multinomial Naive Bayes  

The trained pipeline was saved using pickle:

models/spam_model3.pkl  

---

# Model Comparison

Multiple models were tested during experimentation:

- Gaussian Naive Bayes  
- Multinomial Naive Bayes  
- Bernoulli Naive Bayes  
- Logistic Regression  
- Support Vector Machine  
- Random Forest  
- Gradient Boosting  

Vectorization methods compared:

- TF-IDF  
- Count Vectorizer  

Results showed that **TF-IDF + Multinomial Naive Bayes performed best**.

---

# Streamlit Application

The project includes a **Streamlit web application** that allows users to classify messages interactively.

Features:

- Enter a message  
- Click **Classify**  
- Get prediction instantly  

Possible outputs:

SPAM  
HAM  

Run the app:

streamlit run app/streamlit_app.py

---

# How to Run This Project

Clone the repository:

git clone https://github.com/yourusername/spam-message-detection-nlp.git

Install dependencies:

pip install -r requirements.txt

Train the model:

python src/train.py

This will generate:

models/spam_model3.pkl

Run the Streamlit app:

streamlit run app/streamlit_app.py

---

# Future Improvements

Possible enhancements:

- Add probability score for predictions  
- Deploy using Streamlit Cloud  
- Improve preprocessing using lemmatization  
- Train deep learning models (LSTM / BERT)  
- Add email spam detection support  

---

# Author & Contact

**Ritresh Kumar**

BCA Student | Aspiring Data Scientist & Machine Learning Engineer

Skills:

- Python  
- Machine Learning  
- Natural Language Processing  
- Data Analysis  
- Deep Learning  

📧 Email: ritresh273@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/feed/)  
🔗 [GitHub](https://github.com/Ritresh/Ritresh)
