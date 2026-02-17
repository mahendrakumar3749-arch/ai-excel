import streamlit as st
import google.generativeai as genai

# 1. Page Configuration
st.set_page_config(
    page_title="AI Excel Suite Pro",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Setup Session & Styles
if 'history' not in st.session_state:
    st.session_state.history = []

st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #E3F2FD 0%, #E8EAF6 50%, #F3E5F5 100%);
        background-attachment: fixed;
    }
    .stTextArea textarea {
        background-color: rgba(255, 255, 255, 0.8) !important;
        border: 1px solid rgba(255, 255, 255, 0.5);
        border-radius: 12px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        font-size: 16px; 
    }
    .stButton>button {
        background: linear-gradient(90deg, #6C63FF 0%, #4834D4 100%);
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 10px;
        font-weight: bold;
        width: 100%;
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar
with st.sidebar:
    st.title("💎 AI Suite")
    st.info("Requirement: Create 'requirements.txt' in GitHub with 'google-generativeai' inside it.")
    st.markdown("---")

# 4. API Setup (Debug Mode)
try:
    if "GOOGLE_API_KEY" in st.secrets:
        genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    else:
        st.error("🚨 API Key Missing! Go to App Settings > Secrets.")
        st.stop()
except Exception as e:
    st.error(f"🚨 API Error: {e}")

# 5. Main Tabs
st.title("AI Excel Suite Pro")
tab1, tab2, tab3 = st.tabs(["Formula", "Macro", "SQL"])

with tab1:
    col1, col2 = st.columns(2)
    with col1:
        inp = st.text_area("Describe Logic:", height=150, placeholder="Example: Sum Column A if B is 'Yes'")
        btn = st.button("Generate Formula ✨")
    with col2:
        if btn and inp:
            with st.spinner("Connecting to Google Brain..."):
                try:
                    model = genai.GenerativeModel('gemini-pro')
                    resp = model.generate_content(f"Excel formula for: {inp}. Only code.")
                    st.success("Success!")
                    st.code(resp.text, language="excel")
                except Exception as e:
                    # यह लाइन असली एरर दिखाएगी
                    st.error(f"❌ Error Detail: {e}")
                    st.warning("💡 Hint: Did you create 'requirements.txt' file in GitHub?")
