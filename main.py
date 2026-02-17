import streamlit as st
import google.generativeai as genai

# 1. Page Config (Excel Style)
st.set_page_config(
    page_title="AI Excel Expert",
    page_icon="📗",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Modern "Clean" CSS
st.markdown("""
    <style>
    /* Main Background - Light Grey for depth */
    .stApp {
        background-color: #f8f9fa;
        color: #212529;
    }
    
    /* White Cards for Input/Output */
    div.stTextArea, div.stMarkdown {
        background-color: #ffffff;
        padding: 10px;
        border-radius: 10px;
        # box-shadow: 0 2px 5px rgba(0,0,0,0.05); /* Optional shadow */
    }
    
    /* Excel Green Button */
    .stButton>button {
        background-color: #107c41; /* Excel Green */
        color: white;
        border: none;
        border-radius: 5px;
        font-size: 16px;
        font-weight: bold;
        padding: 0.5rem 1rem;
        transition: 0.3s;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #0c5e31; /* Darker Green on Hover */
        color: white;
    }

    /* Titles */
    h1 {
        color: #107c41;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* Remove default Streamlit Menu */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar (Menu)
with st.sidebar:
    st.image("https://raw.githubusercontent.com/mahendrakumar3749-arch/ai-excel/main/input_file_0.png", width=80)
    st.title("Excel AI Tool")
    st.info("💡 **Tip:** Be clear about column names (e.g., 'Sum of Column A').")
    st.markdown("---")
    st.caption("© 2026 Professional Tools Inc.")

# 4. Header Section
col_logo, col_head = st.columns([1, 12])
with col_logo:
    st.image("
