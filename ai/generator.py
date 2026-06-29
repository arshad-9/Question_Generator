import os
import streamlit as st
import requests

from dotenv import load_dotenv

load_dotenv()

try:
    API_KEY = st.secrets["GROQ_API_KEY"]
except Exception:
    API_KEY = os.getenv("GROQ_API_KEY")

def generate_question_paper(
        text,
        difficulty,
        question_types,
        num_questions,
        instructions
):
    
    prompt = f"""
You are an examination paper setter.

Generate ONLY a question paper from the provided study material.

STRICT RULES:

IMPORTANT FORMATTING RULES:

1. Every question MUST be numbered.
2. Never write questions in paragraph form.
3. Each question must start on a new line.
4. Use the following format exactly:

1. Question text

2. Question text

3. Question text

5. For mcq type:
    Question Number . Question text 
    a. option 1 b. option 2 c. option 3 d. option 4
6. Do NOT include explanations.
7. Do NOT include answers.
8. Do NOT include notes to the teacher.
9. Provide Appropriate spacing between questions.
10. Return only the question paper.

Difficulty: {difficulty}

Question Types:
{', '.join(question_types)}

Number of Questions:
{num_questions}

Additional Instructions:
{instructions}

Study Material:
{text}
"""

   

    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "llama-3.3-70b-versatile",
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "temperature": 0.7
        }
    )

    
    data = response.json()
    
    if response.status_code != 200:
        raise Exception(
            f"HTTP {response.status_code}\n{data}"
        )
    
    if "choices" not in data:
        raise Exception(
            f"Unexpected Response:\n{data}"
        )
    
    return data["choices"][0]["message"]["content"]


def generate_answer_key(question_paper,extracted_text):

    prompt = f"""
You are an expert teacher.

Generate a complete answer key for the following question paper.

Rules:
1. Follow the same numbering.
2. Give concise and accurate answers.
3. For MCQs provide the correct option.
4. For descriptive questions provide model answers.
5. Do not re write the questions for answering them.

Question Paper:

{question_paper}

From This Study Material:
{extracted_text}
"""

    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "llama-3.3-70b-versatile",
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }
    )

    data = response.json()

    if response.status_code != 200:
        raise Exception(
            f"HTTP {response.status_code}\n{data}"
        )
    
    if "choices" not in data:
        raise Exception(
            f"Unexpected Response:\n{data}"
        )
    
    return data["choices"][0]["message"]["content"]