import streamlit as st
import google.generativeai as genai

# 1. पेज सेटअप (इसे सबसे ऊपर रहना चाहिए)
st.set_page_config(
    page_title="AI Excel Wizard", 
    page_icon="📊", 
    layout="centered"
)

# 2. लोगो और हेडिंग
st.image("https://raw.githubusercontent.com/mahendrakumar3749-arch/ai-excel/main/input_file_0.png", width=120)
st.title("📊 AI Excel Wizard")
st.write("अपनी समस्या लिखें, AI चुटकियों में फार्मूला बनाएगा!")

# 3. API Key (Secrets से)
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
except:
    st.error("API Key नहीं मिली! कृपया Secrets चेक करें।")

# 4. यूज़र इनपुट बॉक्स
user_input = st.text_area("आपको Excel में क्या करना है?", placeholder="जैसे: A और B कॉलम को जोड़ो...")

# 5. बटन और रिजल्ट
if st.button("Formula बनाओ 🚀"):
    if user_input:
        with st.spinner("AI सोच रहा है..."):
            try:
                model = genai.GenerativeModel('gemini-pro')
                response = model.generate_content(f"Write only the Excel formula for: {user_input}")
                st.success("यह रहा आपका फार्मूला:")
                st.code(response.text, language="excel")
            except Exception as e:
                st.error(f"कुछ गड़बड़ हुई: {e}")
    else:
        st.warning("कृपया पहले कुछ लिखें!")

