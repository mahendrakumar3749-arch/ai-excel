import streamlit as st
import google.generativeai as genai

# 1. Page Configuration
st.set_page_config(
    page_title="AI Excel Workspace",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Session State for History
if 'history' not in st.session_state:
    st.session_state.history = []

# 3. ULTRA-MODERN CSS (The "SaaS" Look)
st.markdown("""
    <style>
    /* 1. Main Background - Not White, but Soft Blue-Grey */
    .stApp {
        background-color: #F0F2F6;
    }
    
    /* 2. Floating White Cards (Container Styling) */
    div.stTextArea, div.stButton, div.stMarkdown {
        # background-color: transparent;
    }
    
    /* Input Box Styling - Modern & Clean */
    .stTextArea textarea {
        background-color: #FFFFFF;
        border: 1px solid #E0E0E0;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.04);
        padding: 15px;
        font-size: 16px;
        color: #333;
    }
    .stTextArea textarea:focus {
        border: 1px solid #107c41;
        box-shadow: 0 4px 12px rgba(16, 124, 65, 0.15);
    }
    
    /* 3. Modern Tabs (Like App Buttons) */
    .stTabs [data-baseweb="tab-list"] {
        gap: 20px;
        background-color: #FFFFFF;
        padding: 10px 20px;
        border-radius: 50px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        display: flex;
        justify-content: center;
    }
    .stTabs [data-baseweb="tab"] {
        height: 45px;
        border-radius: 30px;
        background-color: #f8f9fa;
        color: #555;
        font-weight: 600;
        border: none;
        padding: 0 25px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #107c41; /* Excel Green */
        color: #ffffff !important;
        box-shadow: 0 4px 10px rgba(16, 124, 65, 0.3);
    }

    /* 4. The "Action" Button */
    .stButton>button {
        background: linear-gradient(135deg, #107c41 0%, #0d5e31 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 12px 24px;
        font-weight: bold;
        width: 100%;
        transition: transform 0.2s;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .stButton>button:hover {
        transform: scale(1.02);
    }

    /* Titles */
    h1, h2, h3 {
        font-family: 'Inter', sans-serif;
        color: #2c3e50;
    }

    /* Hide Streamlit Junk */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 4. Header Section
col_logo, col_head = st.columns([1, 14])
with col_logo:
    st.image("https://upload.wikimedia.org/wikipedia/commons/3/34/Microsoft_Office_Excel_%282019%E2%80%93present%29.svg", width=65)
with col_head:
    st.title("AI Excel Workspace")
    st.markdown("##### Enterprise-grade automation suite")

st.markdown("---")

# API Setup
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("⚠️ API Key is missing.")
    st.stop()

# 5. Sidebar with Card Effect
with st.sidebar:
    st.markdown("### 📜 Recent Activity")
    st.markdown("---")
    if len(st.session_state.history) > 0:
        for item in reversed(st.session_state.history[-5:]): # Show last 5
            st.caption(f"🕒 {item['type']}")
            st.code(item['code'], language="excel")
            st.markdown("---")
    else:
        st.info("No history yet. Start generating!")

# 6. Main Tabs (The "Pill" Design)
tab1, tab2, tab3 = st.tabs(["📊 Formula Generator", "🤖 VBA Macros", "💾 SQL Queries"])

# --- TAB 1: FORMULA ---
with tab1:
    st.markdown("#### &nbsp;") # Spacer
    c1, c2 = st.columns([1, 1], gap="large")
    
    with c1:
        st.markdown("##### 1️⃣ Input Requirement")
        input_f = st.text_area("What do you need?", height=220, placeholder="Example: If Column A is 'Yes', sum Column B. Otherwise, leave blank.")
        btn_f = st.button("Generate Formula 🚀", key="f_btn")
    
    with c2:
        st.markdown("##### 2️⃣ Result")
        if btn_f and input_f:
            with st.spinner("Processing..."):
                try:
                    model = genai.GenerativeModel('gemini-pro')
                    resp = model.generate_content(f"Excel formula for: {input_f}. Only code.")
                    
                    st.success("✅ Generated Successfully")
                    st.code(resp.text, language="excel")
                    
                    # Logic Explanation Card
                    expl = model.generate_content(f"Explain this excel formula in 1 short sentence: {resp.text}")
                    st.info(f"ℹ️ **Logic:** {expl.text}")
                    
                    st.session_state.history.append({"type": "Formula", "code": resp.text})
                except Exception as e:
                    st.error("Error connecting to AI.")
        elif not input_f and btn_f:
            st.warning("Please describe your problem first.")
        else:
            st.info("Waiting for input...")

# --- TAB 2: MACROS ---
with tab2:
    st.markdown("#### &nbsp;")
    c1, c2 = st.columns([1, 1], gap="large")
    with c1:
        st.markdown("##### 1️⃣ Macro Description")
        input_v = st.text_area("Describe Automation", height=220, placeholder="Example: Create a button that saves the current sheet as PDF.")
        btn_v = st.button("Generate VBA Code 📜", key="v_btn")
    
    with c2:
        st.markdown("##### 2️⃣ VBA Code")
        if btn_v and input_v:
            with st.spinner("Coding..."):
                try:
                    model = genai.GenerativeModel('gemini-pro')
                    resp = model.generate_content(f"VBA code for: {input_v}. Only code.")
                    st.success("✅ Macro Created")
                    st.code(resp.text, language="vb")
                    st.session_state.history.append({"type": "Macro", "code": "VBA Code Generated"})
                except:
                    st.error("Error.")

# --- TAB 3: SQL ---
with tab3:
    st.markdown("#### &nbsp;")
    input_s = st.text_area("Describe Query", height=150, placeholder="Select users where date is today...")
    if st.button("Generate SQL 🗄️", key="s_btn"):
        with st.spinner("Querying..."):
            model = genai.GenerativeModel('gemini-pro')
            resp = model.generate_content(f"SQL query for: {input_s}. Only code.")
            st.code(resp.text, language="sql")
            st.session_state.history.append({"type": "SQL", "code": resp.text})
