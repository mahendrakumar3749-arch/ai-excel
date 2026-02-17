import streamlit as st
import google.generativeai as genai

# 1. Page Configuration
st.set_page_config(
    page_title="AI Excel Expert",
    page_icon="📗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Professional CSS (Excel Look)
st.markdown("""
    <style>
    .stApp {
        background-color: #f8f9fa;
        color: #212529;
    }
    .stTextArea textarea {
        background-color: #ffffff;
        border: 1px solid #ced4da;
        border-radius: 8px;
    }
    .stButton>button {
        background-color: #107c41;
        color: white;
        border: none;
        border-radius: 6px;
        height: 3em;
        width: 100%;
        font-weight: bold;
        font-size: 16px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #0c5e31;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/3/34/Microsoft_Office_Excel_%282019%E2%80%93present%29.svg", width=60)
    st.title("Excel AI Tool")
    st.markdown("---")
    st.info("💡 **Tip:** Be specific! (e.g., 'Sum Column A if B is > 50')")
    st.caption("© 2026 AI Excel Wrapper")

# 4. Main Header
st.title("📗 Excel Formula Generator")
st.markdown("Turn your instructions into complex Excel formulas instantly.")
st.markdown("---")

# 5. API Setup
try:
    if "GOOGLE_API_KEY" in st.secrets:
        genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    else:
        st.error("API Key Missing")
except:
    st.error("Configuration Error")

# 6. Dashboard Layout
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.subheader("1️⃣ Describe Problem")
    user_input = st.text_area("Type here...", height=250, placeholder="Example: I want to count cells in Column A that contain 'Paid'...")
    generate_btn = st.button("Generate Formula 🚀")

with col2:
    st.subheader("2️⃣ Your Result")
    
    if generate_btn and user_input:
        with st.spinner("AI is thinking..."):
            try:
                model = genai.GenerativeModel('gemini-pro')
                response = model.generate_content(f"Act as an Excel Expert. Give ONLY the Excel formula for: {user_input}. Do not write explanation.")
                
                # Logic explanation
                explanation = model.generate_content(f"Explain this excel formula in 1 short sentence: {response.text}")
                
                st.success("✅ Formula Ready!")
                st.code(response.text, language="excel")
                st.info(f"ℹ️ **Logic:** {explanation.text}")
                
            except Exception as e:
                st.error(f"Error: {e}")

    elif not user
