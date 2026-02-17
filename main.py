import streamlit as st
import google.generativeai as genai

# 1. Page Configuration
st.set_page_config(
    page_title="AI Excel Architect",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Professional Dark Theme CSS
st.markdown("""
    <style>
    /* Dark Background */
    .stApp {
        background-color: #0E1117;
        color: #E0E0E0;
    }
    
    /* Input Box Styling */
    .stTextArea textarea {
        background-color: #262730;
        color: #ffffff;
        border: 1px solid #4A4A4A;
        border-radius: 8px;
    }
    .stTextArea textarea:focus {
        border: 1px solid #FF4B4B;
        box-shadow: 0 0 5px rgba(255, 75, 75, 0.5);
    }
    
    /* Modern Button */
    .stButton>button {
        background: linear-gradient(90deg, #FF4B4B 0%, #FF4B4B 100%);
        color: white;
        border: none;
        padding: 12px 24px;
        border-radius: 8px;
        font-weight: 600;
        letter-spacing: 0.5px;
        width: 100%;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        box-shadow: 0 4px 12px rgba(255, 75, 75, 0.3);
        transform: translateY(-1px);
    }
    
    /* Success Message */
    .stSuccess {
        background-color: rgba(0, 255, 0, 0.05);
        border: 1px solid #00ff00;
        color: #00ff00;
    }

    /* Hide Streamlit Default UI */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar (Menu)
with st.sidebar:
    st.title("🚀 AI Architect")
    st.markdown("---")
    st.info("💡 **Pro Tip:** Be specific. Mention column names like 'Column A' or 'Cell B2'.")
    st.markdown("### ⚡ Capabilities")
    st.markdown("- Complex Nested Formulas")
    st.markdown("- VBA Macro Automation")
    st.markdown("- SQL Queries")
    st.markdown("---")
    st.caption("© 2026 AI Excel
