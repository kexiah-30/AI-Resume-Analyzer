import streamlit as st
from PyPDF2 import PdfReader

st.title("🤖 AI Resume Analyzer")

st.write("Upload your resume (PDF) to analyze skills.")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    reader = PdfReader(uploaded_file)
    text = ""

    for page in reader.pages:
        text += page.extract_text()

    st.subheader("📄 Extracted Resume Text")
    st.write(text[:1000])  # Show first 1000 characters

    skills = ["Python", "Machine Learning", "Data Analysis", "NLP", "SQL"]

    found_skills = [skill for skill in skills if skill.lower() in text.lower()]

    st.subheader("✅ Detected Skills")
    if found_skills:
        st.write(found_skills)
    else:
        st.write("No predefined skills detected.")

