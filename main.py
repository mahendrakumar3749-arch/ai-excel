import streamlit as st
import google.generativeai as genai

# 1. Page Configuration
st.set_page_config(
    page_title="AI Excel Suite Pro",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Session State (For History)
if 'history' not in st.session_state:
    st.session_state.history = []

# 3. Professional SaaS Theme (Soft Grey - Not too black, not too white)
st.markdown("""
    <style>
    /* Main Background: Soft Blue-Grey */
    .stApp {
        background-color: #F4F6F9;
        color: #1F2937;
    }
    
    /* Card Style for Input/Output */
    div.stTextArea, div.stMarkdown {
        # background-color: transparent;
    }
    
    /* Input Box: White card with shadow */
    .stTextArea textarea {
        background-color: #FFFFFF;
        border: 1px solid #D1D5DB;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.02);
        font-size: 15px;
    }
    .stTextArea textarea:focus {
        border: 1px solid #2563EB;
        box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.2);
    }
    
    /* Modern Tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: #FFFFFF;
        padding: 10px;
        border-radius: 12px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }
    .stTabs [data-baseweb="tab"] {
        height: 40px;
        border-radius: 8px;
        font-weight: 600;
        color: #4B5563;
    }
    .stTabs [aria-selected="true"] {
        background-color: #2563EB; /* Pro Blue */
        color: #ffffff !important;
    }

    /* Primary Button */
    .stButton>button {
        background: linear-gradient(135deg, #2563EB 0%, #1D4ED8 100%);
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 8px;
        font-weight: bold;
        width: 100%;
        transition: 0.2s;
        box-shadow: 0 4px 6px rgba(37, 99, 235, 0.2);
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(37, 99, 235, 0.3);
    }

    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #FFFFFF;
        border-right: 1px solid #E5E7EB;
    }

    /* Hide Streamlit Junk */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 4. Sidebar (History Feature)
with st.sidebar:
    st.title("📂 History Log")
    st.markdown("---")
    
    if len(st.session_state.history) > 0:
        # Show last 5 entries
        for i, item in enumerate(reversed(st.session_state.history[-5:])):
            st.caption(f"🕒 {item['type']}")
            st.code(item['code'], language="excel" if item['type'] == "Formula" else "sql")
            st.markdown("---")
        if st.button("Clear History"):
            st.session_state.history = []
            st.rerun()
    else:
        st.info("No recent activity.")
        st.caption("Generate something to see it here.")

# 5. Main Header
col1, col2 = st.columns([1, 15])
with col1:
    st.write("💎") 
with col2:
    st.title("AI Excel Suite Enterprise")
    st.caption("The complete automation toolkit for Professionals.")

# API Setup
try:
    if "GOOGLE_API_KEY" in st.secrets:
        genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    else:
        st.error("⚠️ API Key Missing.")
        st.stop()
except:
    st.error("Configuration Error.")

# 6. TABS Interface (The Features You Wanted)
tab1, tab2, tab3 = st.tabs(["📗 Excel Formulas", "📜 VBA Macros", "🗄️ SQL Queries"])

# --- TAB 1: FORMULAS ---
with tab1:
    st.markdown("### &nbsp;")
    c1, c2 = st.columns([1, 1], gap="large")
    
    with c1:
        st.subheader("1️⃣ Input Requirement")
        input_f = st.text_area("Describe logic...", height=200, placeholder="Example: Sum Column
