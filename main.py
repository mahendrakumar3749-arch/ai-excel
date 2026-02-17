import streamlit as st
import google.generativeai as genai

# 1. ऐप की मुख्य सेटिंग्स
st.set_page_config(
    page_title="AI Excel Wizard", 
    page_icon="📊", 
    layout="centered"
)

# 2. लोगो लगाने का तरीका (Direct Link)
logo_url = "https://raw.githubusercontent.com/mahendrakumar3749-arch/ai-excel/main/input_file_0.png"
st.image(logo_url, width=120)

st.title("📊 AI Excel Wizard")
st.write("अपने काम का विवरण लिखें और तुरंत Excel Formula पाएं!")

# 3. नाम बदलने के लिए CSS का जादू
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# API Key
api_key = st.secrets["GOOGLE_API_KEY"]
genai.configure(api_key=api_key)

# Input area
user_input = st.text_area("आपको क्या करना है? (जैसे: A और B को जोड़ें)", placeholder="यहाँ लिखें...")

if st.button("Formula बनाओ 🚀"):
    if user_input:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(f"Write only the Excel formula for: {user_input}")
        st.success(f"आपका फार्मूला: `{response.text}`")
    else:
        st.warning("कृपया कुछ लिखें!")
