import pandas as pd
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
import joblib

# -------------------------------------------
# 1. CLEANING FUNCTION
# -------------------------------------------
def clean_email(text):
    if not isinstance(text, str):
        return ""

    text = text.lower()
    text = re.sub(r"http\S+|www\S+", " ", text)   # Remove URLs
    text = re.sub(r"[^a-z0-9\s]", " ", text)      # Remove special chars
    text = re.sub(r"\s+", " ", text).strip()      # Normalize spaces
    return text


# -------------------------------------------
# 2. LOAD THE DATASET
# -------------------------------------------
DATA_PATH = r"C:\Users\ADMIN\OneDrive\Desktop\phisingproject\Data\spamassassin\emails_dataset.csv"

df = pd.read_csv(DATA_PATH)

print("Columns found in dataset:", df.columns.tolist())

# -------------------------------------------
# 3. COMBINE SUBJECT + BODY → TEXT
# -------------------------------------------
df["text"] = df["subject"].fillna("") + " " + df["body"].fillna("")

# Clean the combined text
df["text"] = df["text"].apply(clean_email)

# -------------------------------------------
# 4. FEATURES AND LABELS
# -------------------------------------------
X = df["text"]
y = df["label"]

# -------------------------------------------
# 5. TF-IDF VECTORIZATION
# -------------------------------------------
vectorizer = TfidfVectorizer(stop_words="english", max_features=8000)
X_vec = vectorizer.fit_transform(X)

# -------------------------------------------
# 6. SPLIT DATA
# -------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X_vec, y, test_size=0.2, random_state=42
)

# -------------------------------------------
# 7. TRAIN MODEL
# -------------------------------------------
model = LogisticRegression(max_iter=3000)
model.fit(X_train, y_train)

# -------------------------------------------
# 8. EVALUATE MODEL
# -------------------------------------------
preds = model.predict(X_test)

print("\nAccuracy:", accuracy_score(y_test, preds))
print("\nClassification Report:\n", classification_report(y_test, preds))

# -------------------------------------------
# 9. SAVE MODEL + VECTORIZER
# -------------------------------------------
MODEL_PATH = r"C:\Users\ADMIN\OneDrive\Desktop\phisingproject\Data\spamassassin\phishing_model.pkl"
VEC_PATH = r"C:\Users\ADMIN\OneDrive\Desktop\phisingproject\Data\spamassassin\vectorizer.pkl"

joblib.dump(model, MODEL_PATH)
joblib.dump(vectorizer, VEC_PATH)

print("\n✅ Model training complete!")
print(f"Saved phishing_model.pkl to {MODEL_PATH}")
print(f"Saved vectorizer.pkl to {VEC_PATH}")
