import streamlit as st
import time
from src.config import setup_page, apply_style
from src.loader import load_model
from src.ui_components import render_results

# Initialisation de l'interface
setup_page()
apply_style()

# Chargement du modele (Stockage dans la session)
if 'model' not in st.session_state:
    st.session_state.model = load_model()

# Sidebar pour les options
with st.sidebar:
    st.markdown("### Options d'affichage")
    show_confidence = st.checkbox("Afficher l'indice de certitude", value=True)
    st.markdown("---")
    st.caption("Version 1.0 - Analyseur de texte IA")

# Titre principal
st.markdown("<h1 style='text-align: center;'>Fake News Detector AI</h1>", unsafe_allow_html=True)

# Zone de saisie
st.markdown('<div class="card">', unsafe_allow_html=True)
text = st.text_area("Veuillez inserer le texte a analyser :", height=250, placeholder="Collez l'article ici...")
st.markdown('</div>', unsafe_allow_html=True)

# Bouton d'action
col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
with col_btn2:
    analyze_btn = st.button("Lancer l'analyse de credibilite", type="primary", use_container_width=True)

# Logique d'analyse
if analyze_btn:
    if not text.strip():
        st.warning("Action requise : Veuillez inserer un contenu textuel avant de lancer l'analyse.")
    elif st.session_state.model is None:
        st.error("Erreur systeme : Le modele d'analyse est introuvable dans le dossier Models.")
    else:
        with st.spinner("Analyse des vecteurs de texte en cours..."):
            # Calculs de prediction
            try:
                pred = st.session_state.model.predict([text])[0]
                proba = st.session_state.model.predict_proba([text])[0]
                confidence = max(proba) * 100
                
                # Appel du composant d'affichage (Resultats + Conseils)
                render_results(pred, confidence, show_confidence)
                
            except Exception as e:
                st.error(f"Une erreur est survenue lors du traitement : {e}")

# Pied de page
st.markdown("---")
st.markdown("<p style='text-align: center; color: #7f8c8d; font-size: 12px;'>Outil de recherche assiste par IA. L'utilisateur demeure responsable de la verification finale des informations.</p>", unsafe_allow_html=True)