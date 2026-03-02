import joblib
from bs4 import BeautifulSoup
from email import policy
from email.parser import BytesParser

# Load trained model and vectorizer
model = joblib.load(r"C:\Users\ADMIN\OneDrive\Desktop\phisingproject\Data\spamassassin\phishing_model.pkl")
vectorizer = joblib.load(r"C:\Users\ADMIN\OneDrive\Desktop\phisingproject\Data\spamassassin\vectorizer.pkl")

def extract_email_data(file_path):
    """Extract subject and body from a .eml file"""
    with open(file_path, "rb") as f:
        msg = BytesParser(policy=policy.default).parse(f)

    subject = msg["subject"] or ""
    body = ""

    # Handle multipart emails
    if msg.is_multipart():
        for part in msg.walk():
            ctype = part.get_content_type()
            if ctype == "text/plain":
                body += part.get_content()
            elif ctype == "text/html":
                soup = BeautifulSoup(part.get_content(), "html.parser")
                body += soup.get_text(separator="\n")
    else:
        # Non‑multipart emails
        if msg.get_content_type() == "text/plain":
            body = msg.get_content()
        elif msg.get_content_type() == "text/html":
            soup = BeautifulSoup(msg.get_content(), "html.parser")
            body = soup.get_text(separator="\n")

    return subject, body


def classify_email(email_path):
    """Predict if email is ham or spam"""
    subject, body = extract_email_data(email_path)
    text = subject + " " + body

    text_vec = vectorizer.transform([text])
    prediction = model.predict(text_vec)[0]
    prediction_proba = model.predict_proba(text_vec)[0]

    print("\n==================== EMAIL CONTENT ====================")
    print(f"Subject: {subject}")
    print(f"\nBody Preview:\n{body[:800]}")
    
    print("\n==================== FINAL VERDICT ====================")
    print(f"Prediction: {prediction.upper()}")
    print(f"Confidence (ham/spam): {prediction_proba}")

    print("=======================================================\n")


# ---- MAIN PROGRAM ----
if __name__ == "__main__":
    email_path = input("Enter path to .eml file: ").strip()
    classify_email(email_path)
