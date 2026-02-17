import streamlit as st
import google.generativeai as genai

# 1. Sabse upar naam aur icon set karein
st.set_page_config(page_title="AI Excel Wizard", page_icon="📊", layout="centered")

# 2. Logo lagane ke liye (Ise st.title ke upar rakhein)
st.image("https://raw.githubusercontent.com/mahendrakumar3749-arch/ai-excel/main/input_file_0.png", width=100)

st.title("📊 AI Excel Formula Wizard")
st.markdown("Apni problem likhein aur AI se Excel formula banwayein!")

# API Key Secrets se uthayein
api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)

# Input area
user_input = st.text_area("Aap Excel mein kya karna chahte hain?", placeholder="Example: Column A aur B ko jodo")

if st.button("Formula banao 🚀"):
    if user_input:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(f"Write only the Excel formula for: {user_input}")
        st.success(f"Aapka Formula: `{response.text}`")
    else:
        st.warning("Kripya kuch likhein!")
