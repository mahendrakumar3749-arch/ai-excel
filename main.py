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
    st.image("https://raw.githubusercontent.com/mahendrakumar3749-arch/ai-excel/main/input_file_0.png", width=60)
with col_title:
    st.title("AI Excel Wizard Pro")
    st.caption("🚀 Generating complex formulas in milliseconds.")

st.markdown("---")

# API Setup
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
except:
    st.warning("⚠️ API Key not found. Please configure it in Streamlit Secrets.")

# 5. Dashboard Layout
c1, c2 = st.columns([1, 1], gap="medium")

with c1:
    st.markdown("### 1️⃣ Describe Task")
    user_input = st.text_area(
        "What do you need?",
        height=200,
        placeholder="Example: Count cells in Column A that are red and have value > 50..."
    )
    generate_btn = st.button("✨ Generate Magic Formula")

with c2:
    st.markdown("### 2️⃣ Your Result")
    
    if generate_btn and user_input:
        with st.spinner("🤖 AI is coding..."):
            try:
                model = genai.GenerativeModel('gemini-pro')
                prompt = f"Act as a professional Excel developer. Give ONLY the formula for: {user_input}. No text."
                response = model.generate_content(prompt)
                
                # Result Card
                st.success("Formula Ready!")
                st.code(response.text, language="excel")
                
                # Explanation inside an expander to keep it clean
                explanation = model.generate_content(f"Explain this excel formula in 1 line: {response.text}")
                with st.expander("ℹ️ Logic Explanation"):
                    st.write(explanation.text)
                    
            except Exception as e:
                st.error("Connection Error. Try again.")
    
    elif not user_input:
         st.info("Waiting for your input on the left...")

# Footer
st.markdown("---")
st.markdown("<center style='color: #555;'>Designed for Professionals</center>", unsafe_allow_html=True)
