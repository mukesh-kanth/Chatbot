import streamlit as st
from chatbot_logic import get_hr_response
from config import COMPANY_NAME

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>
"""

st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.set_page_config(
    page_title="AI HR Automation System",
    page_icon="🤖",
    layout="centered"
)

# -------------------------
# CUSTOM CSS - DARK FUTURISTIC UI
# -------------------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;500;600;700;800&family=Space+Mono:wght@400;700&display=swap');

/* ---- ROOT VARIABLES ---- */
:root {
  --bg-deep:        #0a0a12;
  --bg-panel:       #0f0f1c;
  --bg-card:        #14141f;
  --bg-input:       #1a1a2e;
  --bg-hover:       #1e1e32;
  --border:         rgba(138, 90, 255, 0.18);
  --border-bright:  rgba(138, 90, 255, 0.45);
  --accent:         #8a5aff;
  --accent-2:       #b87eff;
  --accent-glow:    rgba(138, 90, 255, 0.35);
  --text-primary:   #f0ecff;
  --text-secondary: #9b96b8;
  --text-muted:     #5a5677;
  --user-bubble:    #1d1040;
  --bot-bubble:     #12122a;
  --success:        #4ade80;
  --radius-sm:      8px;
  --radius-md:      14px;
  --radius-lg:      22px;
  --radius-xl:      32px;
  --shadow:         0 8px 32px rgba(0,0,0,0.5);
  --glow:           0 0 24px rgba(138, 90, 255, 0.3);
}

/* ---- GLOBAL RESET ---- */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"] {
  background: var(--bg-deep) !important;
  font-family: 'Syne', sans-serif !important;
  color: var(--text-primary) !important;
}

[data-testid="stAppViewContainer"] {
  background:
    radial-gradient(ellipse 80% 50% at 50% -10%, rgba(138,90,255,0.22) 0%, transparent 70%),
    radial-gradient(ellipse 60% 40% at 80% 100%, rgba(90,50,180,0.15) 0%, transparent 60%),
    var(--bg-deep) !important;
  min-height: 100vh;
}

/* ---- HIDE STREAMLIT CHROME ---- */
#MainMenu, footer, header,
[data-testid="stToolbar"],
[data-testid="stDecoration"],
[data-testid="stStatusWidget"] { display: none !important; }

/* ---- MAIN BLOCK CONTAINER ---- */
.main .block-container {
  max-width: 780px !important;
  padding: 1.5rem 1rem 5rem !important;
  margin: 0 auto !important;
}

/* ---- HEADINGS ---- */
h1, h2, h3 {
  font-family: 'Syne', sans-serif !important;
  font-weight: 800 !important;
  letter-spacing: -0.02em;
}

/* ========================
   LOGIN PAGE
   ======================== */
.login-wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 88vh;
  gap: 0;
}

.login-orb {
  width: 96px; height: 96px;
  border-radius: 50%;
  background: radial-gradient(circle at 35% 35%, #c084fc, #7c3aed 55%, #1e0a4e);
  box-shadow: 0 0 60px rgba(138,90,255,0.55), 0 0 120px rgba(138,90,255,0.2);
  margin-bottom: 28px;
  animation: orbPulse 3s ease-in-out infinite;
  flex-shrink: 0;
}

@keyframes orbPulse {
  0%, 100% { box-shadow: 0 0 60px rgba(138,90,255,0.55), 0 0 120px rgba(138,90,255,0.2); transform: scale(1); }
  50%       { box-shadow: 0 0 80px rgba(138,90,255,0.7),  0 0 160px rgba(138,90,255,0.3); transform: scale(1.04); }
}

.login-title {
  font-size: clamp(1.8rem, 5vw, 2.6rem) !important;
  font-weight: 800 !important;
  background: linear-gradient(135deg, #f0ecff 0%, #b87eff 60%, #7c3aed 100%);
  -webkit-background-clip: text !important;
  -webkit-text-fill-color: transparent !important;
  background-clip: text !important;
  text-align: center;
  margin-bottom: 8px !important;
}

.login-sub {
  color: var(--text-secondary) !important;
  font-family: 'Space Mono', monospace !important;
  font-size: 0.78rem;
  text-align: center;
  margin-bottom: 40px;
  letter-spacing: 0.08em;
}

.login-card {
  width: 100%;
  height: auto;
  max-width: 440px;
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--radius-xl);
  padding: 36px 32px 32px;
  box-shadow: var(--shadow), inset 0 1px 0 rgba(255,255,255,0.05);
  backdrop-filter: blur(20px);
}

.login-label {
  font-family: 'Space Mono', monospace !important;
  font-size: 0.72rem !important;
  color: var(--text-muted) !important;
  letter-spacing: 0.12em !important;
  text-transform: uppercase !important;
  margin-bottom: 8px !important;
}

/* Input fields */
.stTextInput > div > div {
  background: var(--bg-input) !important;
  border: 1px solid var(--border) !important;
  border-radius: var(--radius-md) !important;
  padding: 0 !important;
  transition: border-color 0.2s, box-shadow 0.2s !important;
}
.stTextInput > div > div:focus-within {
  border-color: var(--accent) !important;
  box-shadow: 0 0 0 3px var(--accent-glow) !important;
}
.stTextInput input {
  background: transparent !important;
  color: var(--text-primary) !important;
  font-family: 'Syne', sans-serif !important;
  font-size: 1rem !important;
  padding: 14px 16px !important;
  border: none !important;
  outline: none !important;
}
.stTextInput input::placeholder { color: var(--text-muted) !important; }

/* Buttons */
.stButton > button {
  width: 100% !important;
  background: linear-gradient(135deg, #7c3aed 0%, #9f5aff 50%, #b87eff 100%) !important;
  color: #fff !important;
  border: none !important;
  border-radius: var(--radius-md) !important;
  font-family: 'Syne', sans-serif !important;
  font-weight: 700 !important;
  font-size: 0.95rem !important;
  padding: 14px 24px !important;
  letter-spacing: 0.04em !important;
  cursor: pointer !important;
  transition: all 0.2s ease !important;
  box-shadow: 0 4px 20px rgba(138,90,255,0.4) !important;
  margin-top: 8px !important;
}
.stButton > button:hover {
  transform: translateY(-2px) !important;
  box-shadow: 0 8px 30px rgba(138,90,255,0.6) !important;
}
.stButton > button:active { transform: translateY(0) !important; }

/* ========================
   CHAT PAGE HEADER
   ======================== */
.chat-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 16px 20px;
  background: var(--bg-card);
  border: 1px solid var(--border);
  border-radius: var(--radius-lg);
  margin-bottom: 20px;
  box-shadow: var(--shadow);
}

.chat-header-left {
  display: flex;
  align-items: center;
  gap: 12px;
}

.chat-header-orb {
  width: 42px; height: 42px;
  border-radius: 50%;
  background: radial-gradient(circle at 35% 35%, #c084fc, #7c3aed 55%, #1e0a4e);
  box-shadow: 0 0 20px rgba(138,90,255,0.5);
  flex-shrink: 0;
}

.chat-header-title {
  font-size: 1.1rem !important;
  font-weight: 700 !important;
  color: var(--text-primary) !important;
  line-height: 1.2;
  margin: 0 !important;
}

.chat-header-status {
  display: flex;
  align-items: center;
  gap: 5px;
  font-family: 'Space Mono', monospace;
  font-size: 0.68rem;
  color: var(--success);
  margin-top: 2px;
}

.status-dot {
  width: 6px; height: 6px;
  background: var(--success);
  border-radius: 50%;
  animation: blink 2s ease-in-out infinite;
}

@keyframes blink {
  0%, 100% { opacity: 1; }
  50%       { opacity: 0.3; }
}

.chat-header-badge {
  font-family: 'Space Mono', monospace;
  font-size: 0.68rem;
  color: var(--text-muted);
  background: var(--bg-input);
  border: 1px solid var(--border);
  border-radius: 20px;
  padding: 4px 10px;
}

/* ========================
   CHAT MESSAGES
   ======================== */
[data-testid="stChatMessage"] {
  background: transparent !important;
  border: none !important;
  padding: 4px 0 !important;
  gap: 12px !important;
}

/* User messages */
[data-testid="stChatMessage"][data-testid*="user"],
.stChatMessage:has([data-testid="chatAvatarIcon-user"]) {
  flex-direction: row-reverse !important;
}

[data-testid="stChatMessageContent"] {
  background: var(--bot-bubble) !important;
  border: 1px solid var(--border) !important;
  border-radius: 18px 18px 18px 4px !important;
  padding: 14px 18px !important;
  font-size: 0.93rem !important;
  line-height: 1.65 !important;
  color: var(--text-primary) !important;
  max-width: 85% !important;
  box-shadow: 0 2px 12px rgba(0,0,0,0.3) !important;
}

/* Avatar icons */
[data-testid="chatAvatarIcon-user"] {
  background: linear-gradient(135deg, #7c3aed, #b87eff) !important;
  border: 2px solid rgba(138,90,255,0.4) !important;
  border-radius: 50% !important;
}
[data-testid="chatAvatarIcon-assistant"] {
  background: radial-gradient(circle at 35% 35%, #c084fc, #7c3aed 55%, #1e0a4e) !important;
  border: 2px solid rgba(138,90,255,0.3) !important;
  border-radius: 50% !important;
}

/* Spinner */
[data-testid="stSpinner"] > div {
  border-color: var(--accent) transparent transparent transparent !important;
}

/* ========================
   CHAT INPUT
   ======================== */
[data-testid="stChatInput"] {
  position: fixed !important;
  bottom: 0 !important;
  left: 50% !important;
  transform: translateX(-50%) !important;
  width: 100% !important;
  padding: 12px 16px 16px !important;
  background: linear-gradient(to top, var(--bg-deep) 70%, transparent) !important;
  z-index: 999 !important;
}

[data-testid="stChatInput"] > div {
  background: var(--bg-card) !important;
  border: 1px solid var(--border-bright) !important;
  border-radius: var(--radius-xl) !important;
  box-shadow: 0 0 0 4px var(--accent-glow), var(--shadow) !important;
  transition: box-shadow 0.2s !important;
  overflow: hidden !important;
}

[data-testid="stChatInput"] > div:focus-within {
  box-shadow: 0 0 0 5px rgba(138,90,255,0.4), var(--shadow) !important;
}

[data-testid="stChatInput"] textarea {
  background: transparent !important;
  border-radius: 20% !important;
  font-family: 'Syne', sans-serif !important;
  font-size: 0.95rem !important;
  padding: 14px 20px !important;
  border: none !important;
  outline: none !important;
  resize: none !important;
}
[data-testid="stChatInput"] textarea::placeholder { color: var(--text-muted) !important; }

[data-testid="stChatInput"] button {
  background: linear-gradient(135deg, #7c3aed, #b87eff) !important;
  border: none !important;
  border-radius: 50% !important;
  width: 38px !important; height: 38px !important;
  margin: 6px 8px !important;
  box-shadow: 0 0 16px rgba(138,90,255,0.5) !important;
  transition: all 0.2s !important;
  flex-shrink: 0 !important;
}
[data-testid="stChatInput"] button:hover {
  transform: scale(1.1) !important;
  box-shadow: 0 0 24px rgba(138,90,255,0.7) !important;
}
[data-testid="stChatInput"] button svg { fill: #fff !important; }

/* ========================
   SIDEBAR
   ======================== */
[data-testid="stSidebar"] {
  background: var(--bg-panel) !important;
  border-right: 1px solid var(--border) !important;
}

[data-testid="stSidebar"] > div {
  padding: 28px 18px !important;
}

[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {
  color: var(--text-primary) !important;
  font-size: 1rem !important;
  font-weight: 700 !important;
  letter-spacing: 0.06em !important;
  text-transform: uppercase !important;
  margin-bottom: 16px !important;
}

[data-testid="stSidebar"] .stButton > button {
  background: var(--bg-input) !important;
  border: 1px solid var(--border) !important;
  color: var(--text-secondary) !important;
  border-radius: var(--radius-md) !important;
  box-shadow: none !important;
  font-size: 0.88rem !important;
  font-weight: 600 !important;
  padding: 11px 16px !important;
  transition: all 0.2s !important;
}
[data-testid="stSidebar"] .stButton > button:hover {
  background: var(--bg-hover) !important;
  border-color: var(--border-bright) !important;
  color: var(--text-primary) !important;
  transform: none !important;
  box-shadow: none !important;
}

/* caption / sub-text */
.stCaption, [data-testid="stCaptionContainer"] {
  color: var(--text-muted) !important;
  font-family: 'Space Mono', monospace !important;
  font-size: 0.7rem !important;
  letter-spacing: 0.06em !important;
}

/* divider */
hr { border-color: var(--border) !important; margin: 16px 0 !important; }

/* ========================
   MARKDOWN within chat
   ======================== */
[data-testid="stMarkdownContainer"] p {
  color: var(--text-primary) !important;
  font-size: 0.93rem !important;
  line-height: 1.7 !important;
}

/* ========================
   SCROLLBAR
   ======================== */
::-webkit-scrollbar { width: 4px; background: transparent; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: var(--border-bright); border-radius: 4px; }
::-webkit-scrollbar-thumb:hover { background: var(--accent); }

/* ========================
   MOBILE RESPONSIVE
   ======================== */
@media (max-width: 640px) {
  .main .block-container { padding: 1rem 0.75rem 5.5rem !important; }
  .login-card { padding: 28px 20px 24px; border-radius: var(--radius-lg); }
  .chat-header { padding: 12px 14px; border-radius: var(--radius-md); }
  .chat-header-orb { width: 34px; height: 34px; }
  .chat-header-title { font-size: 0.95rem !important; }
  [data-testid="stChatInput"] { max-width: 100% !important; padding: 8px 10px 12px !important; }
  [data-testid="stChatMessageContent"] { max-width: 92% !important; font-size: 0.88rem !important; }
}
</style>
""", unsafe_allow_html=True)


# -------------------------
# SESSION STATES
# -------------------------
if "user_name" not in st.session_state:
    st.session_state.user_name = ""
if "messages" not in st.session_state:
    st.session_state.messages = []


# -------------------------
# LOGIN PAGE
# -------------------------
if st.session_state.user_name == "":

    st.markdown("""
    <div class="login-wrapper">
      <div class="login-orb"></div>
      <h1 class="login-title">AI HR Assistant</h1>
      <p class="login-sub">POWERED BY ARTIFICIAL INTELLIGENCE</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 2.2, 1])
    with col2:
        # st.markdown('<div class="login-card">', unsafe_allow_html=True)
        st.markdown('<p class="login-label">Your Name</p>', unsafe_allow_html=True)
        name = st.text_input(
            "name_input",
            placeholder="Enter your full name...",
            label_visibility="collapsed"
        )
        if st.button("✦  Start Conversation"):
            if name.strip():
                st.session_state.user_name = name.strip()
                welcome = (
                    f"Hello {name.strip()}, welcome to {COMPANY_NAME}! 👋 "
                    f"I'm your AI HR Assistant, here to help you with information "
                    f"about our job roles, company culture, and hiring process. "
                    f"What would you like to know?"
                )
                st.session_state.messages.append(("assistant", welcome))
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)


# -------------------------
# CHAT INTERFACE
# -------------------------
else:

    # — Header bar —
    st.markdown(f"""
    <div class="chat-header">
      <div class="chat-header-left">
        <div class="chat-header-orb"></div>
        <div>
          <div class="chat-header-title">{COMPANY_NAME} HR Assistant</div>
          <div class="chat-header-status">
            <span class="status-dot"></span> Online &amp; ready
          </div>
        </div>
      </div>
      <div class="chat-header-badge">
        👤 {st.session_state.user_name}
      </div>
    </div>
    """, unsafe_allow_html=True)

    # — Message history —
    for sender, message in st.session_state.messages:
        with st.chat_message("user" if sender == "user" else "assistant"):
            st.write(message)

    # — Input —
    user_input = st.chat_input("Ask HR anything...")
    if user_input:
        user_input = user_input.strip()
        st.session_state.messages.append(("user", user_input))
        with st.chat_message("user"):
            st.write(user_input)
        with st.chat_message("assistant"):
            with st.spinner(""):
                response = get_hr_response(
                    user_input,
                    st.session_state.user_name,
                    st.session_state.messages
                )
                st.write(response)
        st.session_state.messages.append(("assistant", response))

    # — Sidebar —
    with st.sidebar:
        st.markdown("### Menu")
        st.markdown("---")
        if st.button("🗑️  Clear Chat"):
            st.session_state.messages = []
            st.rerun()
        if st.button("🚪  Logout"):
            st.session_state.user_name = ""
            st.session_state.messages = []
            st.rerun()