import os
import pandas as pd
from email import policy
from email.parser import BytesParser
from bs4 import BeautifulSoup

# REAL folders where emails actually exist
folders = {
    "ham": [
        r"C:\Users\ADMIN\OneDrive\Desktop\phisingproject\Data\spamassassin\easy_ham\easy_ham",
        r"C:\Users\ADMIN\OneDrive\Desktop\phisingproject\Data\spamassassin\hard_ham\hard_ham"
    ],
    "spam": [
        r"C:\Users\ADMIN\OneDrive\Desktop\phisingproject\Data\spamassassin\spam_2\spam_2"
    ]
}

data = []

def extract_email(path, label):
    try:
        with open(path, "rb") as f:
            msg = BytesParser(policy=policy.default).parse(f)

        subject = msg["subject"] if msg["subject"] else ""
        body = ""

        if msg.is_multipart():
            for part in msg.walk():
                if part.get_content_type() == "text/plain":
                    body += part.get_payload(decode=True).decode(errors="ignore")
        else:
            body = msg.get_payload(decode=True).decode(errors="ignore")

        soup = BeautifulSoup(body, "html.parser")
        clean_body = soup.get_text()

        return {"subject": subject, "body": clean_body, "label": label}
    except:
        return None


for label, paths in folders.items():
    for folder in paths:
        print(f"Processing: {folder}")
        for root, dirs, files in os.walk(folder):
            for file in files:
                filepath = os.path.join(root, file)
                email = extract_email(filepath, label)
                if email:
                    data.append(email)

print(f"\n📌 Total emails found: {len(data)}")

df = pd.DataFrame(data)
save_path = r"C:\Users\ADMIN\OneDrive\Desktop\phisingproject\Data\spamassassin\emails_dataset.csv"
df.to_csv(save_path, index=False)

print(f"\n✅ Saved updated dataset to {save_path}")
