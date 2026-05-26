import os
from bs4 import BeautifulSoup
from email import policy
from email.parser import BytesParser
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import joblib

# --------- LOAD MODEL & VECTORIZER ----------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "Models", "phishing_model.pkl")
VEC_PATH = os.path.join(BASE_DIR, "Models", "vectorizer.pkl")

try:
    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VEC_PATH)
except Exception as e:
    messagebox.showerror("Model Load Error", f"Could not load ML model:\n{e}")
    raise SystemExit()


# --------- EMAIL EXTRACTION ----------
def extract_email_data(file_path):
    try:
        with open(file_path, "rb") as f:
            msg = BytesParser(policy=policy.default).parse(f)

        subject = msg["subject"] or ""
        body = ""

        if msg.is_multipart():
            for part in msg.walk():
                ctype = part.get_content_type()

                if ctype == "text/plain":
                    body = part.get_content()
                    break

                elif ctype == "text/html":
                    html = part.get_content()
                    soup = BeautifulSoup(html, "html.parser")
                    body = soup.get_text(separator="\n")
                    break
        else:
            body = msg.get_content()

        return subject, body

    except Exception as e:
        messagebox.showerror("Error", f"Could not read email:\n{e}")
        return "", ""


# --------- SCAN EMAIL ----------
def scan_email():
    if not email_path.get():
        messagebox.showwarning("Select File", "Please choose an .eml file.")
        return

    subject, body = extract_email_data(email_path.get())
    text = subject + " " + body

    try:
        text_vec = vectorizer.transform([text])
        pred = model.predict(text_vec)[0]
    except Exception as e:
        messagebox.showerror("Prediction Error", f"Model failed to predict:\n{e}")
        return

    result_label.config(
        text=f"Prediction: {pred.upper()}",
        fg=("red" if pred == "spam" else "green")
    )

    # Show email body
    output_box.config(state=tk.NORMAL)
    output_box.delete(1.0, tk.END)
    output_box.insert(tk.END, body[:5000])
    output_box.config(state=tk.DISABLED)


# --------- BROWSE FILE ----------
def browse_file():
    file_path = filedialog.askopenfilename(
        title="Select Email File",
        filetypes=[("Email files", "*.eml")]
    )
    if file_path:
        email_path.set(file_path)


# --------- GUI SETUP ----------
window = tk.Tk()
window.title("AI-Powered Phishing Email Detector")
window.geometry("800x650")
window.configure(bg="#f0f4f7")
window.resizable(False, False)

email_path = tk.StringVar()

# Title
title_label = tk.Label(window, text="AI-Powered Phishing Email Detector",
                       font=("Helvetica", 18, "bold"), bg="#f0f4f7", fg="#333")
title_label.pack(pady=10)

# Email Selection Frame
frame_select = tk.Frame(window, bg="#ffffff", bd=2, relief=tk.RIDGE)
frame_select.pack(padx=20, pady=10, fill=tk.X)

tk.Label(frame_select, text="Select Email File (.eml):", font=("Arial", 12), bg="#ffffff").pack(
    side=tk.LEFT, padx=5, pady=5)
tk.Entry(frame_select, textvariable=email_path, width=60, font=("Arial", 11)).pack(
    side=tk.LEFT, padx=5)
tk.Button(frame_select, text="Browse", command=browse_file, width=12,
          bg="#4caf50", fg="white").pack(side=tk.LEFT, padx=5)

# Scan Button
scan_btn = tk.Button(window, text="Scan Email", command=scan_email,
                     bg="#2196f3", fg="white",
                     font=("Arial", 12, "bold"), width=20)
scan_btn.pack(pady=10)

# Result Label
result_label = tk.Label(window, text="Prediction: ",
                        font=("Arial", 16, "bold"), bg="#f0f4f7")
result_label.pack(pady=5)

# Email Body Label
tk.Label(window, text="Email Body Preview:",
         font=("Arial", 12), bg="#f0f4f7").pack(pady=5)

# Email Body Display
output_box = scrolledtext.ScrolledText(
    window, width=95, height=25,
    font=("Consolas", 10), bd=2, relief=tk.SUNKEN
)
output_box.pack(padx=10, pady=5)
output_box.config(state=tk.DISABLED)

# Run the app
window.mainloop()
