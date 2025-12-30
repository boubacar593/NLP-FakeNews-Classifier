import streamlit as st

def setup_page():
    st.set_page_config(
        page_title="Fake News Detector AI",
        layout="wide",
        initial_sidebar_state="expanded",
        menu_items={
            
        }
    )

def apply_style():
    st.markdown("""
    <style>
        .stApp { background: #f8f9fa; }
        h1, h2, h3 { color: #2c3e50 !important; font-family: 'Segoe UI', sans-serif; }
        .card { background: white; padding: 25px; border-radius: 10px; box-shadow: 0 3px 10px rgba(0,0,0,0.08); border: 1px solid #dee2e6; margin-bottom: 20px; }
        .stButton > button { background: #2c3e50; color: white; border-radius: 6px; font-weight: 600; transition: all 0.3s ease; }
        .stButton > button[type="primary"] { background: #3498db; }
        .result-real { background: linear-gradient(135deg, #d1f2eb 0%, #a3e4d7 100%); border-left: 6px solid #27ae60; color: #145a32; }
        .result-fake { background: linear-gradient(135deg, #fadbd8 0%, #f5b7b1 100%); border-left: 6px solid #e74c3c; color: #78281f; }
        .stat-card { background: white; padding: 15px; border-radius: 8px; text-align: center; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
        .fade-in { animation: fadeIn 0.5s ease-out; }
        @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
    </style>
    """, unsafe_allow_html=True)