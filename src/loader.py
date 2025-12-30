import streamlit as st
import joblib
import os

@st.cache_resource
def load_model():
    
    model_path = os.path.join("Models", "best_fake_news_model.joblib")
    try:
        if not os.path.exists(model_path):
            st.error(f"Fichier introuvable : {model_path}")
            return None
        model = joblib.load(model_path)
        return model
    except Exception as e:
        st.error(f"Erreur lors du chargement du modèle : {str(e)}")
        return None