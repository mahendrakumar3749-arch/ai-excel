import streamlit as st
import google.generativeai as genai

# 1. पेज कॉन्फ़िगरेशन (असली ऐप वाली फीलिंग के लिए)
st.set_page_config(
    page_title="AI Excel Wizard",
    page_icon="📊",
    layout="wide",  # यह ऐप को पूरी स्क्रीन पर फैला देगा
    initial_sidebar_state="expanded"
)

# 2. कस्टम CSS (Streamlit का नाम छिपाने और बटन सुंदर बनाने के लिए)
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stButton>button {
        width: 100%;
        background-color: #FF4B4B;
        color: white;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. साइडबार (Sidebar) - ऐप के बारे में जानकारी
with st.sidebar:
    st.image("https://raw.githubusercontent.com/mahendrakumar3749-arch/ai-excel/main/input_file_0.png", width=100)
    st.title("AI Excel Wizard")
    st.info("यह टूल AI का उपयोग करके आपके लिए जटिल Excel फॉर्मूले बनाता है।")
    st.warning("⚠️ टिप: अपनी समस्या को विस्तार से लिखें।")
    st.write("---")
    st.write("Made with ❤️ by You")

# 4. मुख्य स्क्रीन (Main Screen)
col1, col2 = st.columns([1, 8]) # लोगो और टाइटल के लिए कॉलम

with col1:
    st.image("https://raw.githubusercontent.com/mahendrakumar3749-arch/ai-excel/main/input_file_0.png", width=80)

with col2:
    st.title("Excel Formula Generator")

st.write("---") # एक लाइन खींचने के लिए

# API Key चेक
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
except:
    st.error("🚨 API Key Missing! प्लीज सेटिंग्स चेक करें।")

# 5. इनपुट और आउटपुट सेक्शन (दो कॉलम में)
col_input, col_result = st.columns(2)

with col_input:
    st.subheader("1. अपनी समस्या बताएं 👇")
    user_input = st.text_area("यहाँ लिखें...", height=150, placeholder="Example: अगर A1 में 50 से ज्यादा है तो 'Pass' लिखो, वरना 'Fail'...")
    generate_btn = st.button("Formula बनाओ 🚀")

with col_result:
    st.subheader("2. आपका फार्मूला यहाँ आएगा 👇")
    if generate_btn and user_input:
        with st.spinner("AI फार्मूला लिख रहा है..."):
            try:
                model = genai.GenerativeModel('gemini-pro')
                response = model.generate_content(f"Create a complex Excel formula for: {user_input}. Only give the formula code.")
                st.success("सफलतापूर्वक बन गया! ✅")
                st.code(response.text, language="excel") # कॉपी बटन इसके साथ खुद आता है
                st.caption("ऊपर दिए गए छोटे आइकन से कॉपी करें।")
            except Exception as e:
                st.error(f"Error: {e}")
    elif generate_btn and not user_input:
        st.warning("पहले कुछ लिखें तो सही! 😅")
    else:
        st.info("परिणाम का इंतज़ार है...")
