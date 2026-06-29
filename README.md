# 📚 Smart Learning Assistant

An AI-powered educational tool that transforms study material into customized question papers and answer keys within seconds.

Upload a PDF or image containing notes, textbook content, or study material, and the application automatically extracts text, analyzes content, and generates assessment-ready questions.

---

## 🚀 Features

### 📄 PDF & Image Upload

Supports:

* PDF
* PNG
* JPG
* JPEG

### 🔍 OCR-Based Text Extraction

Extracts text from:

* Scanned documents
* Notes
* Textbook pages
* Images

Using:

* EasyOCR
* PyMuPDF

### 🤖 AI Question Generation

Generate:

* Multiple Choice Questions (MCQs)
* Short Answer Questions
* Long Answer Questions
* True/False Questions
* Fill in the Blanks

### 🎯 Difficulty Selection

Choose from:

* Easy
* Medium
* Hard

### ✅ Answer Key Generation

Generate answer keys separately for the generated question paper.

### 📊 Extraction Analytics

Displays:

* Word count
* Character count

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### OCR

* EasyOCR
* PyMuPDF

### AI

* Groq API
* Llama 3.3 70B Versatile

### Programming Language

* Python

---

## 📂 Project Structure

```text
Question_Generator/
│
├── ai/
│   ├── __init__.py
│   └── generator.py
│
├── ocr/
│   ├── __init__.py
│   └── extractor.py
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/arshad-9/Question_Generator.git
cd Question_Generator
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Run Application

```bash
streamlit run app.py
```

---

## 📸 How It Works

1. Upload a PDF or image.
2. Extract text using OCR.
3. Select difficulty level.
4. Choose question types.
5. Generate question paper.
6. Generate answer key.

---

## 🎓 Use Cases

* Teachers
* Students
* Coaching Institutes
* School Assessments
* Self-Practice Tests
* Exam Preparation

---
### Current Limitations

* OCR accuracy may decrease when processing blurred, handwritten, or low-resolution documents.
* The quality of generated questions depends on the accuracy of the extracted text.
* AI-generated questions and answer keys should be reviewed before classroom or examination use.
* Answer key generation may occasionally be interrupted due to temporary AI service limitations or API rate limits.
* The application currently supports English-language documents only.
* Does Not  correctly handles documents with Diagrams 
* Complex tables, diagrams, and mathematical equations may not be extracted accurately.

## 🔮 Future Enhancements

* PDF Export
* Download Question Papers
* Multiple Language Support
* Question Bank Storage
* User Authentication
* Student Performance Analytics
* Bloom's Taxonomy-Based Questions

---

