import streamlit as st
import google.generativeai as genai

# 1. Page Configuration
st.set_page_config(
    page_title="AI Excel Suite Pro",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Session State (History)
if 'history' not in st.session_state:
    st.session_state.history = []

# 3. PREMIUM COLORED CSS (The "Glassmorphism" Look)
st.markdown("""
    <style>
    /* 1. Main Background - COOL GRADIENT (Not White!) */
    .stApp {
        background: rgb(240,242,246);
        background: linear-gradient(135deg, #E3F2FD 0%, #E8EAF6 50%, #F3E5F5 100%);
        background-attachment: fixed;
    }
    
    /* 2. Glassy Cards for Input/Result */
    div.stTextArea, div.stMarkdown {
        # background: transparent;
    }
    
    /* Input Box: Semi-transparent White */
    .stTextArea textarea {
        background-color: rgba(255, 255, 255, 0.8) !important;
        border: 1px solid rgba(255, 255, 255, 0.5);
        border-radius: 15px;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.07);
        backdrop-filter: blur(4px);
        font-size: 16px;
        color: #1F2937;
    }
    .stTextArea textarea:focus {
        border: 2px solid #6C63FF;
        box-shadow: 0 0 15px rgba(108, 99, 255, 0.2);
    }
    
    /* 3. Sidebar (Clean White for contrast) */
    section[data-testid="stSidebar"] {
        background-color: #FFFFFF;
        box-shadow: 2px 0 10px rgba(0,0,0,0.05);
    }
    
    /* 4. Modern Pill Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 15px;
        background-color: rgba(255, 255, 255, 0.6);
        padding: 10px 20px;
        border-radius: 50px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        backdrop-filter: blur(5px);
    }
    .stTabs [data-baseweb="tab"] {
        height: 45px;
        border-radius: 30px;
        font-weight: 700;
        color: #555;
        border: none;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(90deg, #6C63FF 0%, #4834D4 100%);
        color: #ffffff !important;
        box-shadow: 0 4px 15px rgba(108, 99, 255, 0.4);
    }

    /* 5. Gradient Buttons */
    .stButton>button {
        background: linear-gradient(90deg, #6C63FF 0%, #4834D4 100%);
        color: white;
        border: none;
        padding: 12px 24px;
        border-radius: 12px;
        font-weight: bold;
        width: 100%;
        transition: transform 0.2s;
        box-shadow: 0 4px 15px rgba(108, 99, 255, 0.3);
    }
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 6px 20px rgba(108, 99, 255, 0.5);
    }

    /* Headings */
    h1 {
        background: -webkit-linear-gradient(#4834D4, #6C63FF);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
    }

    /* Hide Streamlit Junk */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 4. Sidebar (History Feature)
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/732/732220.png", width=50) # Excel Icon
    st.title("History Log")
    st.markdown("---")
    
    if len(st.session_state.history) > 0:
        for i, item in enumerate(reversed(st.session_state.history[-5:])):
            st.caption(f"🕒 {item['type']}")
            st.code(item['code'], language="excel" if item['type'] == "Formula" else "sql")
            st.markdown("---")
        if st.button("Clear History", type="secondary"):
            st.session_state.history = []
            st.rerun()
    else:
        st.info("No recent activity.")
        st.caption("Start generating to see history.")

# 5. Main Header
col1, col2 = st.columns([12, 4])
with col1:
    st.title("AI Excel Suite Pro")
    st.markdown("##### The ultimate automation tool for formulas, macros & SQL.")

# API Setup
try:
    if "GOOGLE_API_KEY" in st.secrets:
        genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    else:
        st.error("⚠️ API Key Missing.")
        st.stop()
except:
    st.error("Configuration Error.")

# 6. TABS Interface
st.write("") # Spacer
tab1, tab2, tab3 = st.tabs(["💎 Excel Formulas", "📜 VBA Macros", "🗄️ SQL Queries"])

# --- TAB 1: FORMULAS ---
with tab1:
    st.markdown("### &nbsp;")
    c1, c2 = st.columns([1, 1], gap="large")
    
    with c1:
        st.markdown("##### 1️⃣ Describe Logic")
        input_f = st.text_area("What do you need?", height=220, placeholder="Example: If Column A is 'Yes', sum Column B. Otherwise, leave blank.", key="in_f")
        btn_f = st.button("Generate Formula ✨", key="btn_f")
    
    with c2:
        st.markdown("##### 2️⃣ Result")
        if btn_f and input_f:
            with st.spinner("Processing..."):
                try:
                    model = genai.GenerativeModel('gemini-pro')
                    resp = model.generate_content(f"Act as an Excel Expert. Excel formula for: {input_f}. Only code.")
                    
                    st.success("✅ Formula Generated")
                    st.code(resp.text, language="excel")
                    
                    # Logic
                    expl = model.generate_content(f"Explain this excel formula in 1 short English sentence: {resp.text}")
                    st.info(f"ℹ️ **Logic:** {expl.text}")
                    
                    st.session_state.history.append({"type": "Formula", "code": resp.text})
                    
                except Exception as e:
                    st.error("Connection Error.")

# --- TAB 2: MACROS ---
with tab2:
    st.markdown("### &nbsp;")
    c1, c2 = st.columns([1, 1], gap="large")
    
    with c1:
        st.markdown("##### 1️⃣ Automation Task")
        input_v = st.text_area("What should the macro do?", height=220, placeholder="Example: Save current sheet as PDF and email it.", key="in_v")
        btn_v = st.button("Generate Macro 📜", key="btn_v")
    
    with c2:
        st.markdown("##### 2️⃣ VBA Code")
        if btn_v and input_v:
            with st.spinner("Writing VBA Code..."):
                try:
                    model = genai.GenerativeModel('gemini-pro')
                    resp = model.generate_content(f"Write a VBA Macro for: {input_v}. Only code.")
                    
                    st.success("✅ Code Ready")
                    st.code(resp.text, language="vb")
                    st.session_state.history.append({"type": "VBA", "code": "View in VBA Tab"})
                except:
                    st.error("Error.")

# --- TAB 3: SQL ---
with tab3:
    st.markdown("### &nbsp;")
    st.markdown("##### 🗄️ Database Query Generator")
    input_s = st.text_area("Write your data question...", height=150, placeholder="Example: Select all customers from 'Users' table who signed up in 2024.")
    if st.button("Generate SQL Query 🚀", key="btn_s"):
        with st.spinner("Querying..."):
            try:
                model = genai.GenerativeModel('gemini-pro')
                resp = model.generate_content(f"SQL query for: {input_s}. Only code.")
                st.code(resp.text, language="sql")
                st.session_state.history.append({"type": "SQL", "code": resp.text})
            except:
                st.error("Error.")
