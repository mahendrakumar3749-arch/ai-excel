import streamlit as st
import sys

st.set_page_config(page_title="Error Finder", page_icon="🕵️")

st.title("🕵️ एरर पकड़ने वाला (Error Finder)")

# 1. Check Library
st.write("Checking Library...")
try:
    import google.generativeai as genai
    st.success("✅ Library (google-generativeai) सही है!")
except ImportError as e:
    st.error(f"❌ Library Missing: {e}")
    st.warning("⚠️ Solution: अपने GitHub पर 'requirements.txt' नाम की फाइल बनाएं और उसमें 'google-generativeai' लिखें।")
    st.stop()

# 2. Check API Key
st.write("Checking API Key...")
try:
    if "GOOGLE_API_KEY" in st.secrets:
        api_key = st.secrets["GOOGLE_API_KEY"]
        genai.configure(api_key=api_key)
        st.success("✅ API Key कनेक्ट हो गई!")
    else:
        st.error("❌ API Key नहीं मिली!")
        st.info("Solution: Streamlit Settings > Secrets में जाकर GOOGLE_API_KEY चेक करें।")
        st.stop()
except Exception as e:
    st.error(f"❌ API Key Error: {e}")
    st.stop()

# 3. Final Result
st.balloons()
st.success("🎉 सब कुछ ठीक है! अब आप अपना मेन कोड डाल सकते हैं।")
st.write("अगर आपको यह हरे रंग के बॉक्स (Green Boxes) दिख रहे हैं, तो इसका मतलब आपका सेटअप 100% सही है।")
