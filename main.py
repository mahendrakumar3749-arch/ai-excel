import streamlit as st
import google.generativeai as genai

# 1. Page Configuration
st.set_page_config(
    page_title="AI Excel Expert",
    page_icon="📗",
    layout="wide"
)

# 2. Styling (Clean & Safe)
st.markdown("""
    <style>
    .stApp {
        background-color: #ffffff;
        color: #333333;
    }
    .stButton>button {
        background-color: #107c41;
        color: white;
        width: 100%;
        font-weight: bold;
        border-radius: 5px;
        height: 3em;
    }
    .stTextArea textarea {
        background-color: #f0f2f6;
        border-radius: 10px;
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 3. Header (Using Emoji instead of Image to prevent errors)
st.title("📗 AI Excel Formula Pro")
st.markdown("Generates complex formulas instantly.")
st.markdown("---")

# 4. API Setup (With Error Handling)
try:
    if "GOOGLE_API_KEY" in st.secrets:
        genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    else:
        st.error("🚨 Error: API Key is missing in Secrets.")
except Exception as e:
    st.error(f"Configuration Error: {e}")

# 5. Main Dashboard
c1, c2 = st.columns([1, 1])

with c1:
    st.subheader("1️⃣ Describe Problem")
    user_input = st.text_area("Type here...", height=200, placeholder="Example: Sum Column A if B is 'Yes'.")
    generate_btn = st.button("Generate Formula 🚀")

with c2:
    st.subheader("2
