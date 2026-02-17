import streamlit as st
import google.generativeai as genai

# पेज सेटअप
st.set_page_config(
    page_title="AI Excel", 
    page_icon="📊", 
    layout="centered"
)
st.image("Gemini_Generated_Image_n2q0lvn2q0lvn2q0.png", width=150)
st.title("📊 Excel Formula Generator")
st.write("अपनी समस्या लिखें और चुटकियों में Excel फार्मूला पाएं!")

# API Key मांगना
api_key = st.secrets["GOOGLE_API_KEY"]

# यूजर का सवाल
user_query = st.text_area("आपको क्या करना है? (जैसे: A और B को जोड़ो अगर C में 'Pass' लिखा हो)", height=100)

if st.button("Formula बनाओ 🚀"):
    if not api_key:
        st.error("कृपया पहले साइडबार में API Key डालें।")
    elif not user_query:
        st.warning("कृपया पहले कुछ लिखें!")
    else:
        try:
            genai.configure(api_key=api_key)
            
            # --- जादू: यह कोड खुद सही मॉडल ढूंढेगा ---
            active_model = "gemini-1.5-flash" # डिफॉल्ट
            try:
                for m in genai.list_models():
                    if 'generateContent' in m.supported_generation_methods:
                        if 'gemini' in m.name:
                            active_model = m.name
                            break
            except:
                pass
            # ---------------------------------------

            model = genai.GenerativeModel(active_model)
            
            prompt = f"""
            You are an expert in Excel. Write a formula for: {user_query}.
            Output ONLY the formula. No explanation.
            """
            
            with st.spinner(f'AI ({active_model}) काम कर रहा है...'):
                response = model.generate_content(prompt)
                st.success("यह रहा आपका फार्मूला:")
                st.code(response.text.strip(), language='excel')
                
        except Exception as e:

            st.error(f"Error: {e}")



