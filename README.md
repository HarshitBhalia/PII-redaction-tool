# 🛡️ Privacy Shield: Enterprise PII Redaction Tool

Welcome to **Privacy Shield**! This is a full-stack, AI-powered application designed to instantly detect and redact Personally Identifiable Information (PII) from dense legal and financial documents (like Red Herring Prospectuses, IPO filings, and contracts). 

Unlike standard redaction tools that just black out text, Privacy Shield replaces sensitive data with **realistic, context-aware synthetic data** (e.g., replacing a real name with a fake name, or a real phone number with a fake one) to maintain the readability and flow of the document.

### 🔗 Links
- **Live Project**: [https://pii-redaction-tool-sigma.vercel.app/](https://pii-redaction-tool-sigma.vercel.app/)

---

## ✨ Key Features
- **Multi-Format Support**: Upload `.docx`, `.pdf`, and `.txt` files up to 50MB.
- **Format Preservation**: When processing `.docx` files, the engine modifies the underlying XML tree to replace text while perfectly preserving tables, headers, footers, fonts, and layouts.
- **Parallel Processing**: Uses multi-threading (`ThreadPoolExecutor`) to slice massive 100+ page documents into chunks, processing them across multiple CPU cores simultaneously for an 8x speed boost.
- **Financial Context-Awareness**: Equipped with a custom allowlist that prevents the AI from falsely redacting Indian financial jargon (e.g., *DRHP, SEBI, Mutual Fund, Promoter, Syndicate*).
- **Quality Evaluation Dashboard**: Dynamically calculates and displays Precision and Recall metrics for the redaction engine.

---

## 🔍 Types of PII Detected
We use a hybrid approach of deep Natural Language Processing (NLP) and strict Regular Expressions (Regex) to detect:
- 👤 **Full Names** (`PERSON`)
- 🏢 **Organizations & Companies** (`ORG`)
- 📍 **Geographic Locations** (`GPE` / `LOC`)
- 📧 **Email Addresses**
- 📞 **Phone Numbers** (International & Indian formats)
- 🔢 **Social Security Numbers (SSNs)**
- 💳 **Credit Card Numbers**
- 📅 **Dates of Birth**
- 🌐 **IP Addresses**
- 🪪 **Indian PAN Numbers**
- 🆔 **Indian Aadhaar Numbers**

---

## 🏗️ Architecture & How It Was Built

The application is split into two distinct services to handle the heavy computational load of the AI models without timing out.

### 1. The Frontend (Client Interface)
The user interface is designed to be sleek, fast, and highly interactive.
- **Framework**: Next.js & React
- **Styling**: Tailwind CSS with custom Vanilla CSS for complex animations.
- **Visuals**: A custom WebGL shader is used in the background to create a dynamic, fluid, and premium "dark mode" aesthetic.
- **Hosting**: Deployed on **Vercel** for global edge-network delivery.

### 2. The Backend (AI & API Layer)
The backend does the heavy lifting. Serverless functions (like AWS Lambda or Vercel) limit memory and timeout too quickly for 100-page document NLP analysis, so this is hosted on a dedicated server.
- **Framework**: Python & Flask (served via Gunicorn).
- **Core AI Engine**: **Microsoft Presidio** combined with **spaCy**.
- **The Brain**: We utilize spaCy's massive `en_core_web_lg` model (~500MB). This model is trained on a massive web corpus using word vectors (GloVe), allowing the AI to understand English semantics and distinguish between a person's name and a generic capitalized noun.
- **Synthetic Data Generation**: Uses the Python `Faker` library to generate localized, realistic fake replacements on the fly.
- **Hosting**: Deployed on **Render** (which supports Docker/Python environments capable of loading 500MB models into memory).

---

## ⚙️ The Process Pipeline (How it works under the hood)

1. **Upload**: The user uploads a document via the Next.js frontend. The file is sent as a `FormData` object to the Flask `/api/upload` endpoint and saved temporarily.
2. **Text Extraction**: Depending on the file type, the backend uses `python-docx` (for Word) or `PyMuPDF` (for PDFs) to rip the raw text from the document, paragraphs, and tables.
3. **Parallel Detection**: The text is chopped into segments and fed into the `en_core_web_lg` spaCy pipeline across multiple CPU threads.
4. **Scoring & Filtering**: The engine flags potential PII. It runs the flagged entities against our strict Financial Allowlist. If it's a false positive (like the word "India"), it is ignored.
5. **Redaction**: The `Faker` library generates a fake equivalent (e.g., `John Doe` -> `Peter Parker`). For `.docx` files, the XML tree is safely mutated.
6. **Download**: The final, sanitized document is packaged and a download link is sent back to the React frontend.

---
