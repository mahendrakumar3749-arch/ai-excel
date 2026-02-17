import streamlit as st
import google.generativeai as genai

# 1. Page Config (Must be the first line)
st.set_page_config(
    page_title="AI Excel Pro",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Professional Premium CSS
st.markdown("""
    <style>
    /* Main Background */
    .stApp {
        background-color: #f8f9fa;
        color: #212529;
    }
    
    /* Input Box Styling */
    .stTextArea textarea {
        background-color: #ffffff;
        border: 1px solid #e0e0e0;
        border-radius: 10px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        font-size: 16px;
    }
    
    /* The "Pro" Button */
    .stButton>button {
        background: linear-gradient(45deg, #107c41, #1e8e3e);
        color: white;
        border: none;
        padding: 12px 24px;
        border-radius: 8px;
        font-weight: bold;
        width: 100%;
        transition: all 0.3s ease;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0,0,0,0.15);
    }

    /* Headers */
    h1 {
        font-family: 'Helvetica Neue', sans-serif;
        color: #1a1a1a;
        font-weight: 700;
    }
    
    /* Hide Streamlit Default Elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar (App Info)
with st.sidebar:
    st.title("📊 AI Excel Pro")
    st.markdown("---")
    st.info("💡 **Pro Tip:** Describe your logic in plain English.")
    st.markdown("### 🛠️ Capabilities")
    st.markdown("- Complex Formulas")
    st.markdown("- Data Cleaning Logic")
    st.markdown("- Financial Calculations")
    st.markdown("---")
    st.caption("© 2026 AI Wrapper Inc.")

# 4. Main App Interface
st.title("🚀 Excel Formula Generator")
st.markdown("#### Transform instructions into ready-to-use Excel formulas.")
st.markdown("---")

# API Check
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("🚨 API Key Missing! Please check your Secrets.")
    st.stop()

# 5. Dashboard Columns
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.subheader("✍️ Describe Requirement")
    user_input = st.text_area(
        "Type here...",
        height=250,
        placeholder="Example: I want to calculate the bonus. If Sales (Column A) is > 1000, give 10%, otherwise 5%. If cell is empty, show nothing."
    )
    st.write("") # Spacer
    generate_btn = st.button("Generate Formula ✨")

with col2:
    st.subheader("🎯 Generated Result")
