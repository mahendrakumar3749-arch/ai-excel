import streamlit as st
import google.generativeai as genai

# 1. Page Configuration
st.set_page_config(
    page_title="AI Excel Workspace",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Session State for History
if 'history' not in st.session_state:
    st.session_state.history = []

# 3. ULTRA-MODERN CSS (The "SaaS" Look)
st.markdown("""
    <style>
    /* 1. Main Background - Not White, but Soft Blue-Grey */
    .stApp {
        background-color: #F0F2F6;
    }
    
    /* 2. Floating White Cards (Container Styling) */
    div.stTextArea, div.stButton, div.stMarkdown {
        # background-color: transparent;
    }
    
    /* Input Box Styling - Modern & Clean */
    .stTextArea textarea {
        background-color: #FFFFFF;
        border: 1px solid #E0E0E0;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.04);
        padding: 15px;
        font-size: 16px;
        color: #333;
    }
    .stTextArea textarea:focus {
        border: 1px solid #107c41;
        box-shadow: 0 4px 12px rgba(16, 124, 65, 0.15);
    }
    
    /* 3. Modern Tabs (Like App Buttons) */
    .stTabs [data-baseweb="tab-list"] {
        gap: 20px;
        background-color: #FFFFFF;
        padding: 10px 20px;
        border-radius: 50px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        display: flex;
        justify-content: center;
    }
    .stTabs [data-baseweb="tab"] {
        height: 45px;
        border-radius: 30px;
        background-color: #f8f9fa;
        color: #555;
        font-weight: 600;
        border: none;
        padding: 0 25px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #107c41; /* Excel Green */
        color: #ffffff !important;
        box-shadow: 0 4px 10px rgba(16, 124, 65, 0.3);
    }

    /* 4. The "Action" Button */
    .stButton>button {
        background: linear-gradient(135deg, #107c41 0%, #0d5e31 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 12px 24px;
        font-weight: bold;
        width: 100%;
        transition: transform 0.2s;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .stButton>button:hover {
        transform: scale(1.02);
    }

    /* Titles */
    h1, h2, h3 {
        font-family: 'Inter', sans-serif;
        color: #2c3e50;
    }

    /* Hide Streamlit Junk */
    #MainMenu
