
import streamlit as st
from ai.generator import (generate_question_paper,generate_answer_key)
from ocr.extractor import (
    extract_pdf_text,
    extract_image_text
)


if "question_paper" not in st.session_state:
    st.session_state["question_paper"] = ""

if "answer_key" not in st.session_state:
    st.session_state["answer_key"] = ""

st.set_page_config(
    page_title="Smart Learning Assistant",
    page_icon="📚",
    layout="wide"
)

# ---------- CUSTOM CSS ----------

st.markdown("""
<style>

.stApp{
    background: linear-gradient(
        135deg,
        #0f172a 0%,
        #1e293b 30%,
        #312e81 70%,
        #4f46e5 100%
    );
}

.main-title{
    font-size: 3rem;
    font-weight: 800;
    color:white;
    margin-bottom:0.5rem;
}

.sub-title{
    font-size:1.1rem;
    color:#cbd5e1;
    margin-bottom:2rem;
}

.feature-card{
    background: rgba(255,255,255,0.06);
    border:1px solid rgba(255,255,255,0.12);
    border-radius:16px;
    padding:15px;
    margin-top:12px;
    color:white;
}
   .question-paper{
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(10px);
    border:1px solid rgba(255,255,255,0.15);
    border-radius:20px;
    padding:25px;
    margin-top:20px;
    color:white;
}
   .question-title{
    font-size:1.8rem;
    font-weight:700;
    margin-bottom:15px;
    color:white;
}

.stButton button{
    width:100%;
    border:none;
    border-radius:12px;
    height:50px;
    font-size:18px;
    font-weight:600;
    color:white;
    background: linear-gradient(
        90deg,
        #8b5cf6,
        #6366f1
    );
}

.stButton button:hover{
    transform:scale(1.02);
}

section[data-testid="stFileUploader"]{
    border:1px dashed rgba(255,255,255,0.4);
    border-radius:15px;
    padding:15px;
}

label{
    color:white !important;
    font-weight:600 !important;
}

</style>
""", unsafe_allow_html=True)

# ---------- LAYOUT ----------

left, right = st.columns([1, 1.2])

# ---------- LEFT SIDE ----------

with left:


   

    st.markdown(
        """
        <div class='main-title'>
        📚 Smart Learning Assistant
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class='sub-title'>
        Upload a chapter, PDF, or image and generate a customized
        question paper in seconds.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class='feature-card'>
        <h4>📌 Important Notes</h4>
        <ul>
        <li>Use <b>clear, high-quality PDFs</b> for the best OCR accuracy.</li>
        <li>Review generated questions and answer keys before classroom or examination use.</li>
        <li>If Generation fails, wait a few seconds and try again. It's due to Temporary AI service limitations or API rate limits may occasionally interrupt the request.</li>
           </ul>
           </div>
      """, unsafe_allow_html=True)

    st.markdown("""
    <div class='feature-card'>
    📝 Generate MCQs, Short & Long Questions
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='feature-card'>
    🎯 Difficulty Based Question Generation
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='feature-card'>
    📄 Export Question Paper as PDF
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='feature-card'>
    🤖 Powered by OCR + AI
    </div>
    """, unsafe_allow_html=True)

# ---------- RIGHT SIDE ----------

with right:

    

    uploaded_file = st.file_uploader(
        "📤 Upload PDF or Image",
        type=["pdf", "png", "jpg", "jpeg"]
    )

    difficulty = st.selectbox(
        "🎯 Difficulty",
        ["Easy", "Medium", "Hard"]
    )

    question_types = st.multiselect(
        "📝 Question Types",
        [
            "MCQ",
            "Short Answer",
            "Long Answer",
            "True/False",
            "Fill in the Blanks"
        ]
    )

    num_questions = st.number_input(
        "🔢 Number of Questions",
        min_value=1,
        max_value=100,
        value=20
    )

    instructions = st.text_area(
        "📋 Additional Instructions",
        placeholder="Include numerical problems, assertion-reason questions..."
    )

    if st.button("🚀 Generate Question Paper"):

        if uploaded_file is None:
            st.error("Please upload a file.")

        elif len(question_types) == 0:
            st.error("Please select at least one question type.")

        else:

            with st.spinner("Processing file..."):

                extracted_text = ""

                # PDF
                if uploaded_file.type == "application/pdf":

                    extracted_text = extract_pdf_text(
                        uploaded_file
                    )

                    st.success(
                        "✅ PDF processed successfully"
                    )

                # Image OCR
                else:

                    extracted_text = extract_image_text(
                        uploaded_file
                    )

                    st.success(
                        "✅ Image processed successfully"
                    )

            st.markdown("---")

            st.subheader("📊 Extraction Summary")

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "Words Detected",
                    len(extracted_text.split())
                )

            with col2:
                st.metric(
                    "Characters",
                    len(extracted_text)
                )

            st.subheader("📄 Extracted Text")

            st.text_area(
                "",
                extracted_text,
                height=350
            )

            # Store text for Gemini step
            st.session_state["extracted_text"] = extracted_text
            if len(extracted_text.strip()) < 100:

                st.error(
                    "Not enough text detected. Please upload a clearer document."
            )

                st.stop()
            MAX_CHARS = 50000

            if len(extracted_text) > MAX_CHARS:

                 st.error(
                     f"Document contains {len(extracted_text)} characters.\n\n"
                     f"Maximum allowed is {MAX_CHARS} characters.\n\n"
                     "Please upload a smaller chapter or topic."
                 )
             
                 st.stop()  

                

            with st.spinner("🤖 Generating Question Paper..."):
             question_paper = generate_question_paper(
                  text=extracted_text,
                  difficulty=difficulty,
                  question_types=question_types,
                  num_questions=num_questions,
                  instructions=instructions
                        )
             question_paper = question_paper.replace("**", "")
             st.session_state["question_paper"] = question_paper

    st.markdown("---")
    
    with st.spinner("🤖 Generating Question Paper..."):
        if st.session_state["question_paper"]:
          st.markdown(
              """
              <div class="question-title">
                  📝 Generated Question Paper
              </div>
              """,
              unsafe_allow_html=True
          )
      
          st.markdown(
              f"""
              <div class="question-paper">
                  {st.session_state["question_paper"]}
              </div>
              """,
              unsafe_allow_html=True
          )
    if st.button("📖 Show Answer Key"):
              
        with st.spinner("Generating Answer Key..."):

            st.session_state["answer_key"] = generate_answer_key(
                st.session_state["question_paper"],
                st.session_state["extracted_text"]
            )
              
    if st.session_state["answer_key"]:
    
     st.markdown(
         """
         <div class="question-title">
             ✅ Answer Key
         </div>
         """,
         unsafe_allow_html=True
     )
    
     st.markdown(
         f"""
         <div class="question-paper">
             <pre style="
                 white-space: pre-wrap;
                 color:white;
                 font-size:16px;
                 line-height:1.8;
                 font-family:inherit;
                 margin:0;
             ">
     {st.session_state["answer_key"]}
             </pre>
         </div>
         """,
         unsafe_allow_html=True
     )