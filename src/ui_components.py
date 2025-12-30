import streamlit as st
import plotly.graph_objects as go

def render_results(pred, confidence, show_confidence):
    """Affiche les resultats de l'analyse et les conseils de verification."""
    st.markdown('<div class="fade-in">', unsafe_allow_html=True)
    
    # 1. Zone de Resultat Principal
    if pred == 1:  # Fiable
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown("""
                <div style="background: linear-gradient(135deg, #d1f2eb 0%, #a3e4d7 100%); 
                            padding: 25px; border-radius: 10px; border-left: 6px solid #27ae60;">
                    <h3 style="color: #145a32; margin-top: 0;">ANALYSE : INFORMATION CREDIBLE</h3>
                    <p style="color: #145a32;">Le modele identifie ce contenu comme presentant les caracteristiques standards d'une information fiable.</p>
                </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
                <div style="text-align: center; padding: 25px; background: #27ae60; border-radius: 10px; color: white;">
                    <div style="font-size: 20px; font-weight: bold;">VERIFIE</div>
                </div>
            """, unsafe_allow_html=True)
    else:  # Suspect
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown("""
                <div style="background: linear-gradient(135deg, #fadbd8 0%, #f5b7b1 100%); 
                            padding: 25px; border-radius: 10px; border-left: 6px solid #e74c3c;">
                    <h3 style="color: #78281f; margin-top: 0;">ANALYSE : INFORMATION SUSPECTE</h3>
                    <p style="color: #78281f;">Le modele detecte des structures linguistiques souvent associees a la propagation de fausses informations.</p>
                </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
                <div style="text-align: center; padding: 25px; background: #e74c3c; border-radius: 10px; color: white;">
                    <div style="font-size: 20px; font-weight: bold;">ALERTE</div>
                </div>
            """, unsafe_allow_html=True)

    # 2. Section Conseils et Protocole
    st.markdown("---")
    st.subheader("Protocole de verification recommande")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("""
        **Analyse de la source**
        * Verifier l'identite de l'auteur ou de l'organisme emetteur.
        * Consulter la rubrique "A propos" du site d'origine.
        * Examiner si d'autres medias de reference confirment les faits.
        """)
    with col_b:
        st.markdown("""
        **Examen du contenu**
        * Evaluer la neutralite du ton employe (absence de termes sensationnalistes).
        * Verifier la date de publication originale des images et du texte.
        * Identifier si les sources citees sont accessibles et officielles.
        """)

    # 3. Jauge de certitude
    if show_confidence and confidence:
        render_gauge(confidence)
    
    st.markdown('</div>', unsafe_allow_html=True)

def render_gauge(confidence):
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = confidence,
        number = {'suffix': '%', 'font': {'size': 30}},
        title = {'text': "Indice de certitude algorithmique", 'font': {'size': 16}},
        gauge = {
            'axis': {'range': [None, 100]},
            'bar': {'color': "#3498db"},
            'bgcolor': "white",
            'borderwidth': 1,
            'bordercolor': "#bdc3c7"
        }
    ))
    fig.update_layout(height=250, margin=dict(t=50, b=10, l=10, r=10))
    st.plotly_chart(fig, use_container_width=True)