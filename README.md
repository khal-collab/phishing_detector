# 🛡️ AI-Powered Phishing Email Detector

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![ML](https://img.shields.io/badge/ML-Naive%20Bayes-green.svg)
![Accuracy](https://img.shields.io/badge/Accuracy-98%25-brightgreen.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

A machine learning-powered desktop application that detects phishing emails with **98% accuracy**, built using Python, Naive Bayes classification, and the SpamAssassin public dataset.

---

## 📌 Overview

Phishing emails remain one of the most common and damaging cyberattack vectors worldwide. This tool provides an accessible, AI-driven solution that analyzes email content and instantly classifies it as **SPAM (phishing)** or **HAM (legitimate)**.

Built as part of an initiative to apply machine learning to real-world cybersecurity problems.

---

## ✨ Features

- 📧 Parses real `.eml` email files (subject, body, HTML content)
- 🤖 Naive Bayes ML model trained on 5,000+ SpamAssassin emails
- 🎯 98% classification accuracy
- 🖥️ Clean desktop GUI built with Tkinter
- ⚡ Real-time email scanning and prediction
- 🎨 Color-coded results (red for spam, green for ham)

---

## 📁 Project Structure

```
phishingproject/
│
├── Data/
│   └── spamassassin/       # Raw email dataset (easyham, hardham, spam)
│
├── Models/
│   ├── phishing_model.pkl  # Trained Naive Bayes model
│   └── vectorizer.pkl      # TF-IDF vectorizer
│
├── Src/
│   ├── build_dataset.py    # Builds CSV dataset from raw emails
│   ├── train_model.py      # Trains and saves the ML model
│   └── phishing_detector_ai.py  # Core detection logic
│
├── phishing_gui.py         # Main application entry point
├── requirements.txt        # Project dependencies
├── LICENSE                 # MIT License
└── README.md               # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/khal_collab/phishing-detector.git
cd phishing-detector
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
python phishing_gui.py
```

---

## 🧠 How It Works

1. **Data Collection** — SpamAssassin public dataset (easyham, hardham, spam categories)
2. **Dataset Building** — `build_dataset.py` processes raw emails into structured CSV
3. **Model Training** — `train_model.py` trains a Naive Bayes classifier using TF-IDF vectorization
4. **Detection** — GUI loads the trained model and classifies any `.eml` file in real time

---

## 📊 Model Performance

| Metric | Score |
|--------|-------|
| Accuracy | 98% |
| Dataset Size | 5,000+ emails |
| Algorithm | Multinomial Naive Bayes |
| Vectorization | TF-IDF |

---

## 🖼️ Screenshot

> ### ✅ Legitimate Email (HAM)
![HAM Result](docs/Screenshot%20(62).png)

### 🚨 Phishing Email (SPAM)
![SPAM Result](docs/Screenshot%20(63).png)

---

## 📦 Requirements

```
scikit-learn
joblib
beautifulsoup4
```

---

## 🔮 Future Improvements

- [ ] Add URL scanning within email body
- [ ] Support for more email formats
- [ ] Deep learning model comparison
- [ ] Export scan reports as PDF
- [ ] Real-time email inbox integration

---

## 👤 Author

**Saidi Khalid Ramadhan**  
Bachelor of Computer Security and Forensics  
Kabarak University, Kenya

📧 [khalidramadhan774@gmail.com](mailto:khalidramadhan774@gmail.com)  
💼 [LinkedIn — Khalid Ramadhan](https://www.linkedin.com/in/khalid-ramadhan)  
🐙 [GitHub — khal_collab](https://github.com/khal_collab)

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

> *"If it runs on the internet, it is hackable — so let's detect the attack before it lands."*
