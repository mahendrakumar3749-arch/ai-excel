import streamlit as st
import google.generativeai as genai

# 1. Page Configuration
st.set_page_config(
    page_title="AI Excel Wizard",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. PREMIUM DARK THEME CSS (Design Magic)
st.markdown("""
    <style>
    /* Dark Background */
    .stApp {
        background-image: linear-gradient(to right bottom, #0e1117, #161b22, #0d1117);
        color: #ffffff;
    }
    
    /* Input Box Styling */
    .stTextArea textarea {
        background-color: #1f2937;
        color: white;
        border: 1px solid #374151;
        border-radius: 10px;
    }
    
    /* Button Styling */
    .stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #FF4B4B 0%, #FF914D 100%);
        color: white;
        font-weight: bold;
        border: none;
        border-radius: 8px;
        padding: 12px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0px 4px 15px rgba(255, 75, 75, 0.4);
    }

    /* Headings */
    h1 {
        background: -webkit-linear-gradient(#eee, #999);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 700;
    }
    h2, h3 {
        color: #e0e0e0 !important;
    }

    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar
with st.sidebar:
    st.image("https://raw.githubusercontent.com/mahendrakumar3749-arch/ai-excel/main/input_file_0.png", width=100)
    st.title("Settings")
    st.info("💡 Pro Tip: Be specific with column names (e.g., 'Col A', 'Col B').")
    st.markdown("---")
    st.caption("v2.0 | AI Excel Wizard")

# 4. Main Header Area
col_logo, col_title = st.columns([1, 10])
with col_logo:
    st.image("https://raw.githubusercontent.com/mahendrakumar3749-arch/ai-excel/main/input_file_0.png", width=6
