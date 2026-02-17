import streamlit as st
import google.generativeai as genai

# 1. Page Setup (Wide & Professional)
st.set_page_config(
    page_title="AI Excel Pro",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. ULTIMATE PRO CSS (The "Expensive" Look)
st.markdown("""
    <style>
    /* Main Background - Dark Midnight Blue */
    .stApp {
        background-color: #050505;
        background-image: radial-gradient(circle at 50% 0%, #1c1c2e 0%, #050505 100%);
        color: #e0e0e0;
    }
    
    /* Input Areas - Glassmorphism Style */
    .stTextArea textarea {
        background-color: rgba(255, 255, 255, 0.05);
        color: #ffffff;
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        font-size: 16px;
    }
    .stTextArea textarea:focus {
        border: 1px solid #FFD700; /* Gold Border on Focus */
        box-shadow: 0 0 10px rgba(255, 215, 0, 0.2);
    }

    /* The "Money" Button (Gold Gradient) */
    .stButton>button {
        background: linear-gradient(135deg, #FFD700 0%, #FDB931 100%);
        color: #000000;
        border: none;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 18px;
        font-weight: 800;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 50px;
        width: 100%;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(253, 185, 49, 0.4);
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(253, 185, 49, 0.6);
    }

    /* Headers */
    h1 {
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 700;
        color: #ffffff;
        letter-spacing: -1px;
    }
    h3 {
        color: #a0a0a0 !important;
        font-weight: 400;
    }

    /* Success Message Box */
    .stSuccess {
        background-color: rgba(0, 255, 0, 0.1);
        border-left: 5px solid #00ff00;
        color: #00ff00;
    }

    /* Hide Streamlit Junk */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar (Premium Menu)
with st.sidebar:
    st.image("https://raw.githubusercontent.com/mahendrakumar3749-arch/ai-excel/main/input_file_0.png", width=80)
    st.markdown("### 💎 AI Excel Pro")
    st.markdown("---")
    st.success("Plan: **Professional**")
    st.markdown("Use this tool to generate complex formulas, VBA macros, and SQL queries instantly.")
    st.markdown("---")
