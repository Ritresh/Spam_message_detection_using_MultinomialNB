# 📧 Spam Message Detection using NLP


_A machine learning project that classifies SMS messages as **Spam** or **Ham (Not Spam)** using Natural Language Processing (NLP). The system processes message text using text preprocessing techniques and TF-IDF vectorization, and then classifies the message using a Multinomial Naive Bayes model._

---

## 📌 Table of Contents
- <a href="#overview">Overview</a>
- <a href="#problem-statement">Problem-Statement</a>
- <a href="#dataset">Dataset</a>
- <a href="#tools--technologies">Tools & Technologies</a>
- <a href="#project-structure">Project Structure</a>
- <a href="#data-preprocessing">Data Preprocessing</a>
- <a href="#exploratory-data-analysis">Exploratory Data Analysis</a>
- <a href="#model-building">Model Building</a>
- <a href="#streamlit-application">Streamlit Application</a>
- <a href="#how-to-run-this-project">How to Run This Project</a>
- <a href="#future-improvements">Future Improvements</a>
- <a href="#author--contact">Author & Contact</a>

---

<h2><a class="anchor" id="overview"></a>Overview</h2>

Spam messages are common in SMS and email communication. These messages often contain advertisements, scams, or phishing links. Automatically detecting spam helps protect users from unwanted and potentially harmful messages.

This project builds a **Spam Detection System using Natural Language Processing (NLP)**. The system processes SMS text data, cleans and transforms the text, and converts it into numerical features using **TF-IDF Vectorization**. A machine learning model then classifies each message as **Spam** or **Ham**.

The project also includes a **Streamlit web application** where users can enter a message and instantly see whether it is spam or not.

---

<h2><a class="anchor" id="problem-statement"></a>Problem-Statement</h2>

With the increasing use of mobile messaging and online communication, spam messages have become a major issue.

The goal of this project is to:

- Automatically classify SMS messages as spam or ham.
- Apply Natural Language Processing techniques to clean and process text.
- Transform text data into numerical features for machine learning.
- Train and evaluate different machine learning models.
- Provide an interactive interface for real-time message classification.

---

<h2><a class="anchor" id="dataset"></a>Dataset</h2>

The project uses the **SMS Spam Collection Dataset**, which contains labeled SMS messages.

Each message in the dataset is labeled as:
- **ham** → normal message
- **spam** → unwanted promotional or fraudulent message

Dataset files used in this project:

- spam.csv (original dataset)
- spam_cleaned.csv (processed dataset)

Dataset location:

```
dataset/raw/
dataset/processed/
```

The processed dataset includes additional engineered features such as:

- transformed_text
- number of characters
- number of words
- number of sentences

---

<h2><a class="anchor" id="tools--technologies"></a>Tools & Technologies</h2>

Programming & Libraries
- Python
- Pandas
- NumPy
- Scikit-Learn
- NLTK

Machine Learning / NLP
- TF-IDF Vectorizer
- Multinomial Naive Bayes
- Text Tokenization
- Stopword Removal
- Porter Stemmer

Visualization
- Matplotlib
- Seaborn
- WordCloud

Application
- Streamlit

Others
- Pickle
- Jupyter Notebook (VS Code Jupyter Extension)
- Git & GitHub

---

<h2><a class="anchor" id="project-structure"></a>Project Structure</h2>

```
Spam Message Detection using NLP/
│
├── app/
│   └── streamlit_app.py
│
├── dataset/
│   ├── raw/
│   │   └── spam.csv
│   │
│   └── processed/
│       ├── spam.csv
│       └── spam_cleaned.csv
│
├── models/
│   └── spam_model3.pkl
│
├── notebook/
│   ├── spam.ipynb
│   └── differnet_models.ipynb
│
├── src/
│   ├── __init__.py
│   ├── data_preprocessing.py
│   ├── predict.py
│   └── train.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

<h2><a class="anchor" id="data-preprocessing"></a>Data Preprocessing</h2>

The preprocessing pipeline prepares the SMS text data for machine learning.

Key steps include:

1. Data Cleaning
   - Remove unnecessary columns.
   - Rename columns for clarity.

2. Label Encoding
   Convert labels into numerical values:
   - ham → 0
   - spam → 1

3. Removing Duplicates
   - Duplicate messages are removed to avoid bias.

4. Text Processing
   The text preprocessing pipeline performs:

   - Convert text to lowercase
   - Tokenize words
   - Remove punctuation
   - Remove stopwords
   - Apply stemming using Porter Stemmer

Example:

Original Message:
"Congratulations! You have won a free prize."

Processed Text:
"congratul free prize"

---

<h2><a class="anchor" id="exploratory-data-analysis"></a>Exploratory Data Analysis</h2>

Exploratory Data Analysis (EDA) was performed to understand the dataset.

Analysis performed:

- Distribution of spam vs ham messages
- Character count analysis
- Word count analysis
- Sentence count analysis
- Word frequency analysis

Visualizations used:

- Pie charts
- Pair plots
- WordClouds

These analyses help understand the patterns that differentiate spam messages from normal messages.

---

<h2><a class="anchor" id="model-building"></a>Model Building</h2>

After preprocessing, the text data is converted into numerical features.

**TF-IDF Vectorization**

TF-IDF converts text messages into numerical feature vectors.

Example pipeline:

Text Message  
↓  
TF-IDF Vectorizer  
↓  
Machine Learning Model

Several machine learning models were tested:

- Gaussian Naive Bayes
- Multinomial Naive Bayes
- Bernoulli Naive Bayes
- Logistic Regression
- Support Vector Machine
- Random Forest
- Gradient Boosting

The best performing model for this project was:

**Multinomial Naive Bayes with TF-IDF Vectorization**

The trained pipeline is saved as:

```
models/spam_model3.pkl
```

---

<h2><a class="anchor" id="streamlit-application"></a>Streamlit Application</h2>

A simple Streamlit web application allows users to classify messages.

Features:

- Enter a message in the text box
- Click **Classify**
- Instantly see whether the message is **Spam** or **Ham**

Run the interface:

```
streamlit run app/streamlit_app.py
```

---

<h2><a class="anchor" id="how-to-run-this-project"></a>How to Run This Project</h2>

1. Clone the repository:

```bash
git clone https://github.com/yourusername/spam-message-detection.git
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Train the model:

```bash
python src/train.py
```

This will generate:

```
models/spam_model3.pkl
```

4. Run the Streamlit application:

```bash
streamlit run app/streamlit_app.py
```

5. Use the application:
- Enter a message
- Click **Classify**
- See whether the message is spam or ham

---

<h2><a class="anchor" id="future-improvements"></a>Future Improvements</h2>

- Deploy the application on cloud
- Improve preprocessing using lemmatization
- Use deep learning models (LSTM, BERT)
- Add probability scores for predictions
- Extend the system for email spam detection

---

<h2><a class="anchor" id="author--contact"></a>Author & Contact</h2>

**Ritresh Kumar**  
BCA Student | Aspiring Data Scientist

Skills:
- Python
- Machine Learning
- Natural Language Processing
- Data Analysis
- Deep Learning

📧 Email: ritresh273@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/feed/)  
🔗 [GitHub](https://github.com/Ritresh/Ritresh)
