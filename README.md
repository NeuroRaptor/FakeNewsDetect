![Docker Build & Push](https://github.com/NeuroRaptor/FakeNewsDetect/actions/workflows/docker-build.yml/badge.svg)


# 📰 Fake News Detection — Deployment

![Status](https://img.shields.io/badge/Status-Deployed-brightgreen)
![License](https://img.shields.io/badge/License-MIT-blue.svg)

## 🌐 Live Demo

🚀 Try the live app here:  
👉 [https://fakenewsdetect-yhif.onrender.com](https://fakenewsdetect-yhif.onrender.com)

---

## 📦 Overview

This repository contains the **Flask web application** that serves a trained **Fake News Detection** model. The app allows users to input a news headline or article and classifies it as **Real** or **Fake** using a machine learning model.

The app loads:
- A pre-trained **Support Vector Machine (SVM)** model
- A **TF-IDF vectorizer** for transforming input text

Both artifacts were developed in the model training repo linked below.

---

## 🔗 Model Training Repository

The machine learning model used in this app was developed, trained, and evaluated in a separate repository:

➡️ [`Fake-News-Detection`](https://github.com/NeuroRaptor/Fake-News-Detection)

That repo includes:
- EDA and preprocessing with NLP (NLTK)
- Comparison of models: SVM, Naive Bayes, Logistic Regression, CNN, LSTM, BERT
- Model performance analysis (Accuracy, F1 Score)
- Export of final SVM model and TF-IDF vectorizer

The exported files used here:
- `models/svm_text_model.pkl`
- `models/tfidf_vectorizer.pkl`

---

## 🗂️ Repository Structure

```
FakeNewsDetect/
├── models/
│   ├── svm_text_model.pkl        # Trained SVM model
│   └── tfidf_vectorizer.pkl      # TF-IDF vectorizer
├── templates/
│   └── index.html                # HTML form for input
├── app.py                        # Flask app entry point
├── requirements.txt              # Dependencies
├── .gitignore
├── Dockerfile
├── .dockerignore
├── .python-version
├── FakeNewsDetect.code-workspace
└── .github/
    └── workflows/
        └── docker-build.yml  # CI/CD pipeline
```

---

## 🧠 How It Works

1. User submits a news article via web interface
2. Text is vectorized using `tfidf_vectorizer.pkl`
3. Vector is passed to `svm_text_model.pkl` for prediction
4. Output is displayed as "Real" or "Fake"

---

## 🖥️ Run the App Locally

### 1. Clone the repository
```bash
git clone https://github.com/NeuroRaptor/FakeNewsDetect.git
cd FakeNewsDetect
```

### 2. Create a virtual environment (Optional but recommended)
```bash
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Flask app
```bash
python app.py
```

### 5. Visit in browser
Go to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

cat >> README.md << 'EOF'

---

## 🐳 Run with Docker
```bash
docker pull ghcr.io/neuroraptor/fakenewsdetect:latest
docker run -p 5000:5000 ghcr.io/neuroraptor/fakenewsdetect:latest
```

Then open [http://localhost:5000](http://localhost:5000)

---

## 📊 Model Results

### Classical Models

| Model | Accuracy | F1 Score |
|-------|----------|----------|
| **SVM** ⭐ (deployed) | **86.52%** | **86.41%** |
| Random Forest | 86.14% | 86.13% |
| Logistic Regression | 85.53% | 85.53% |
| Naive Bayes | 80.94% | 80.01% |

### Deep Learning & Transformer

| Model | Test Accuracy | Notes |
|-------|--------------|-------|
| CNN | 84.91% | Early stopping at epoch 11 |
| LSTM | 84.74% | Early stopping at epoch 11 |
| BERT (fine-tuned) | 76.00% | Underperformed on binary task |

> Trained on 73,265 articles across LIAR, FakeNewsNet, and ISOT datasets.
EOF
---
## 🔧 Technologies Used

- Python
- Flask
- scikit-learn
- NLTK
- HTML/CSS (Jinja templates)
- Render (for deployment)

---

## 🙋‍♂️ Contact

- 💼 LinkedIn: [https://www.linkedin.com/in/arpitamborkar/](#)
- 📧 Email: arpitamborkar1@gmail.com 

---

## 🙏 Acknowledgment

This web application was created as part of a **Capstone Project** under the guidance of **Dr. Hoomera Noor**.

---

