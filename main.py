import streamlit as st
import google.generativeai as genai

# 1. Page Configuration
st.set_page_config(
    page_title="AI Excel Suite Pro",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Session State (History)
if 'history' not in st.session_state:
    st.session_state.history = []

# 3. PREMIUM COLORED CSS (The "Glassmorphism" Look)
st.markdown("""
    <style>
    /* 1. Main Background - COOL GRADIENT (Not White!) */
    .stApp {
        background: rgb(240,242,246);
        background: linear-gradient(135deg, #E3F2FD 0%, #E8EAF6 50%, #F3E5F5 100%);
        background-attachment: fixed;
    }
    
    /* 2. Glassy Cards for Input/Result */
    div.stTextArea, div.stMarkdown {
        # background: transparent;
    }
    
    /* Input Box: Semi-transparent White */
    .stTextArea textarea {
        background-color: rgba(255, 255, 255, 0.8) !important;
        border: 1px solid rgba(255, 255, 255, 0.5);
        border-radius: 15px;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.07);
        backdrop-filter: blur(4px);
        font-size: 16px;
        color: #1F2937;
    }
    .stTextArea textarea:focus {
        border: 2px solid #6C63FF;
        box-shadow: 0 0 15px rgba(108, 99, 255, 0.2);
    }
    
    /* 3. Sidebar (Clean White for contrast) */
    section[data-testid="stSidebar"] {
        background-color: #FFFFFF;
        box-shadow: 2px 0 10px rgba(0,0,0,0.05);
    }
    
    /* 4. Modern Pill Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 15px;
        background-color: rgba(255, 255, 255, 0.6);
        padding: 10px 20px;
        border-radius: 50px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        backdrop-filter: blur(5px);
    }
    .stTabs [data-baseweb="tab"] {
        height: 45px;
        border-radius: 30px;
        font-weight: 700;
        color: #555;
        border: none;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(90deg, #6C63FF 0%, #4834D4 100%);
        color: #ffffff !important;
        box-shadow: 0 4px 15px rgba(108, 99, 255, 0.4);
    }

    /* 5. Gradient Buttons */
    .stButton>button {
        background: linear-gradient(90deg, #6C63FF 0%, #4834D4 100%);
        color: white;
        border: none;
        padding: 12px 24px;
        border-radius: 12px;
        font-weight: bold;
        width: 100%;
        transition: transform 0.2s;
        box-shadow: 0 4px 15px rgba(108, 99, 255, 0.3);
    }
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 6px 20px rgba(108, 99, 255, 0.5);
    }

    /* Headings */
