import streamlit as st
from config import COMPANY_NAME
from resume_analyzer import extract_text, calculate_ats_score

st.set_page_config(page_title="Resume Analyzer", page_icon="📄", layout="centered")

# reuse some of the CSS from main app for consistent look
st.markdown("""
<style>
.main-title{ text-align:center; font-size:2rem; font-weight:700; color:#333; }
.sub-title{ text-align:center; color:#666; margin-bottom:1.5rem; }
.section-box{ padding:1.5rem; border-radius:12px; background:#fafafa; margin:auto; max-width:600px; border:1px solid #eee; }
</style>
""", unsafe_allow_html=True)

st.markdown(f"<div class='main-title'>📄 {COMPANY_NAME} Resume Analyzer</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Upload your CV to check ATS compatibility</div>", unsafe_allow_html=True)

st.markdown("<div class='section-box'>", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

if uploaded_file:
    text = extract_text(uploaded_file)
    score = calculate_ats_score(text)
    st.success(f"ATS Score: {score}/100")

st.markdown("</div>", unsafe_allow_html=True)
