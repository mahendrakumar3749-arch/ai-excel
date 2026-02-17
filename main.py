import streamlit as st
import google.generativeai as genai
import os

# 1. Page Config
st.set_page_config(page_title="AI Excel Tool", layout="wide")

# 2. Simple CSS
st.markdown("""
<style>
    .stApp { background-color: #ffffff; color: #333333; }
    .stButton>button { background-color: #107c41; color: white; width: 100%; }
    textarea { border: 1px solid #ccc; border-radius: 5px; }
</style>
""", unsafe_allow_html=True)

# 3. Header
st.title("📗 AI Excel Formula Generator")
st.write("---")

# 4. Secure API Setup
api_key = None
if "GOOGLE_API_KEY" in st.secrets:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
else:
    st.error("🚨 Error: API Key is missing. Please check Secrets.")
    st.stop()

# 5. App Logic
col1, col2 = st.columns(2)

with col1:
    st.subheader("Input")
    user_input = st.text_area("Describe your problem:", height=150)
    btn = st.button("Generate Formula 🚀")

with col2:
    st.subheader("Result")
    if btn and user_input:
        try:
            model = genai.GenerativeModel('gemini-pro')
            response = model.generate_content(f"Excel formula for: {user_input}")
            st.success("Success!")
            st.code(response.text, language="excel")
        except Exception as e:
            st.error(f"Error: {e}")
