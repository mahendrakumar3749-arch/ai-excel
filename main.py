import streamlit as st
import google.generativeai as genai

# 1. Page Config
st.set_page_config(page_title="Excel AI Pro", page_icon="🚀", layout="wide")

# 2. Dark Professional Theme (CSS)
st.markdown("""
    <style>
    /* Dark Background */
    .stApp {
        background-color: #0E1117;
        color: #FAFAFA;
    }
    /* Input Box */
    .stTextArea textarea {
        background-color: #262730;
        color: #ffffff;
        border: 1px solid #4e4e4e;
    }
    /* Button */
    .stButton>button {
        background-color: #FF4B4B;
        color: white;
        border-radius: 5px;
        width: 100%;
        font-weight: bold;
    }
    /* Success Box */
    .stSuccess {
        background-color: #262730;
        color: #00ff00;
    }
    #MainMenu {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar
with st.sidebar:
    st.title("🚀 Excel AI")
    st.info("Description लिखें और कोड पाएं।")
    st.markdown("---")
    st.caption("Version: 3.0 Stable")

# 4. Main App
st.title("💻 Excel Formula Generator (Pro)")
st.write("---")

# 5. API Setup (Error Proof)
try:
    if "GOOGLE_API_KEY" in st.secrets:
        genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    else:
        st.warning("⚠️ API Key Missing in Secrets.")
        st.stop()
except Exception as e:
    st.error(f"Setup Error: {e}")
    st.stop()

# 6. Dashboard Layout
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📝 अपनी समस्या लिखें")
    user_input = st.text_area("यहाँ टाइप करें...", height=200, placeholder="Example: Sum of Column A if Column B is 'Done'.")
    generate_btn = st.button("Generate Code 🔥")

with col2:
    st.subheader("💡 आपका रिजल्ट")
    
    if generate_btn and user_input:
        try:
            with st.spinner("AI काम कर रहा है..."):
                model = genai.GenerativeModel('gemini-pro')
                
                # 1. Formula Code
                response = model.generate_content(f"Excel formula for: {user_input}. Only code.")
                st.code(response.text, language="excel")
                
                # 2. Explanation
                explain = model.generate_content(f"Explain this formula in 1 short sentence: {response.text}")
                st.success(f"Logic: {explain.text}")
                
        except Exception as e:
            st.error(f"Error: {e}")
            
    elif not user_input and generate_btn:
        st.warning("कृपया पहले कुछ लिखें।")
    else:
        st.info("रिजल्ट यहाँ दिखेगा...")
