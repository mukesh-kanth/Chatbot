import streamlit as st
from config import COMPANY_NAME
from interview_bot import get_next_question

st.set_page_config(page_title="Interview Bot", page_icon="🎤", layout="centered")

st.markdown("""
<style>
.main-title{ text-align:center; font-size:2rem; font-weight:700; color:#333; }
.sub-title{ text-align:center; color:#666; margin-bottom:1.5rem; }
.section-box{ padding:1.5rem; border-radius:12px; background:#fafafa; margin:auto; max-width:600px; border:1px solid #eee; }
</style>
""", unsafe_allow_html=True)

st.markdown(f"<div class='main-title'>🎤 {COMPANY_NAME} Interview Assistant</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>Practice your answers with AI-driven questions</div>", unsafe_allow_html=True)

st.markdown("<div class='section-box'>", unsafe_allow_html=True)

if "q_index" not in st.session_state:
    st.session_state.q_index = 0

if st.button("Start Interview"):
    question = get_next_question(st.session_state.q_index)
    st.write(question)
    st.session_state.q_index += 1

st.markdown("</div>", unsafe_allow_html=True)
