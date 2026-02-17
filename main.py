import streamlit as st
import google.generativeai as genai

# 1. Page Configuration (Wide Layout for Dashboard feel)
st.set_page_config(
    page_title="AI Excel Wizard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Custom CSS for Professional Look
st.markdown("""
    <style>
    .stApp {
        background-color: #ffffff;
    }
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar Configuration
with st.sidebar:
    st.image("https://raw.githubusercontent.com/mahendrakumar3749-arch/ai-excel/main/input_file_0.png", width=80)
    st.title("AI Excel Wizard")
    st.markdown("---")
    st.markdown("### 🛠️ How to use")
    st.info("1. Describe your problem in the text box.\n2. Click 'Generate Formula'.\n3. Copy the code and paste it into Excel.")
    st.markdown("---")
    st.caption("© 2024 AI Excel Wizard. All rights reserved.")

# 4. Main App Layout
st.title("📊 Excel Formula Generator")
st.markdown("#### Transform plain English into complex Excel formulas instantly.")
st.write("---")

# Setup API Key
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
except:
    st.error("⚠️ API Key missing. Please check your app secrets.")

# Creating two columns for a dashboard look
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.subheader("📝 Describe Requirement")
    user_input = st.text_area(
        "Type here...",
        height=200,
        placeholder="Example: I want to sum Column A only if Column B contains 'Paid' and Column C is greater than 500."
    )
    generate_btn = st.button("Generate Formula ⚡", type="primary")

with col2:
    st.subheader("🚀 Generated Result")
    
    if generate_btn and user_input:
        with st.spinner("Analyzing request..."):
            try:
                model = genai.GenerativeModel('gemini-pro')
                
                # Requesting Formula
                prompt_formula = f"Act as an Excel Expert. Give me ONLY the Excel formula for: {user_input}. Do not write any explanation."
                response_formula = model.generate_content(prompt_formula)
                
                # Requesting Explanation
                prompt_explain = f"Explain this Excel formula in 1 short sentence in English: {response_formula.text}"
                response_explain = model.generate_content(prompt_explain)

                # Displaying Result
                st.success("Formula generated successfully!")
                st.code(response_formula.text, language="excel")
                
                # Explanation Box
                with st.expander("ℹ️ How this formula works"):
                    st.write(response_explain.text)
                    
            except Exception as e:
                st.error(f"An error occurred: {e}")
                
    elif generate_btn and not user_input:
        st.warning("⚠️ Please enter a description first.")
    
    else:
        st.info("The generated formula will appear here.")
        # Placeholder image or text to fill space nicely
        st.markdown(
            """
            <div style="text-align: center; color: gray; margin-top: 50px;">
                Waiting for input...
            </div>
            """, unsafe_allow_html=True
        )
