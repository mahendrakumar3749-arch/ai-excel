import streamlit as st
import google.generativeai as genai

# 1. Page Config (Full Screen)
st.set_page_config(
    page_title="AI Excel Suite",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Session State (History Save karne ke liye)
if 'history' not in st.session_state:
    st.session_state.history = []

# 3. Professional Styling
st.markdown("""
    <style>
    /* Global Styles */
    .stApp { background-color: #f8f9fa; color: #212529; }
    
    /* Input & Text Area */
    .stTextArea textarea {
        background-color: #ffffff;
        border: 1px solid #d1d5db;
        border-radius: 8px;
        font-size: 15px;
    }
    
    /* Tabs Design */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: #ffffff;
        border-radius: 5px;
        color: #495057;
        font-weight: 600;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }
    .stTabs [aria-selected="true"] {
        background-color: #107c41;
        color: #ffffff !important;
    }

    /* Buttons */
    .stButton>button {
        background-color: #107c41;
        color: white;
        border-radius: 6px;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #0c5e31;
        box-shadow: 0 4px 10px rgba(0,0,0,0.15);
    }
    
    /* Remove default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 4. Sidebar (History)
with st.sidebar:
    st.title("📂 History")
    st.info("Your recent generations will appear here.")
    st.markdown("---")
    
    if len(st.session_state.history) > 0:
        for i, item in enumerate(reversed(st.session_state.history)):
            st.text(f"📝 {item['type']}")
            st.code(item['code'], language="excel")
            st.markdown("---")
    else:
        st.caption("No history yet.")

# 5. Header
col_logo, col_title = st.columns([1, 15])
with col_logo:
    st.image("https://upload.wikimedia.org/wikipedia/commons/3/34/Microsoft_Office_Excel_%282019%E2%80%93present%29.svg", width=60)
with col_title:
    st.title("AI Excel Suite 2.0")
    st.write("Generate Formulas, Macros, and Queries in seconds.")

# API Setup
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("🚨 API Key Missing.")
    st.stop()

# 6. Main TABS Interface (New Feature!)
tab1, tab2, tab3 = st.tabs(["📗 Excel Formula", "📜 VBA Macro", "🗄️ SQL Query"])

# --- TAB 1: FORMULAS ---
with tab1:
    c1, c2 = st.columns([1, 1], gap="large")
    with c1:
        st.subheader("Describe Logic")
        input_formula = st.text_area("What do you want to calculate?", height=200, placeholder="e.g. Sum of Column A if Column B says 'Paid'")
        btn_formula = st.button("Generate Formula ⚡", key="btn1")
    
    with c2:
        st.subheader("Result")
        if btn_formula and input_formula:
            with st.spinner("Analyzing..."):
                try:
                    model = genai.GenerativeModel('gemini-pro')
                    resp = model.generate_content(f"Excel formula for: {input_formula}. Only code.")
                    st.success("✅ Formula Ready")
                    st.code(resp.text, language="excel")
                    
                    # Add to History
                    st.session_state.history.append({"type": "Formula", "code": resp.text})
                except Exception as e:
                    st.error(f"Error: {e}")

# --- TAB 2: VBA MACROS ---
with tab2:
    st.info("💡 Use VBA to automate repetitive tasks (e.g., 'Send email to everyone in list').")
    c1, c2 = st.columns([1, 1], gap="large")
    with c1:
        input_vba = st.text_area("Describe Automation", height=200, placeholder="e.g. Create a macro to PDF all sheets and save them.")
        btn_vba = st.button("Generate Macro 📜", key="btn2")
    
    with c2:
        if btn_vba and input_vba:
            with st.spinner("Writing Code..."):
                try:
                    model = genai.GenerativeModel('gemini-pro')
                    resp = model.generate_content(f"Write a VBA Subroutine for: {input_vba}. Only code.")
                    st.success("✅ VBA Code Ready")
                    st.code(resp.text, language="vb")
                    st.session_state.history.append({"type": "Macro", "code": "See VBA Tab"})
                except Exception as e:
                    st.error(f"Error: {e}")

# --- TAB 3: SQL QUERIES ---
with tab3:
    st.warning("For Database Users")
    input_sql = st.text_area("Describe Query", placeholder="e.g. Select all users who joined in 2024")
    if st.button("Generate SQL 🗄️", key="btn3"):
        with st.spinner("Querying..."):
            model = genai.GenerativeModel('gemini-pro')
            resp = model.generate_content(f"SQL query for: {input_sql}. Only code.")
            st.code(resp.text, language="sql")
            st.session_state.history.append({"type": "SQL", "code": resp.text})
