import numpy as np
import streamlit as st

from utils.funTISapp import *



col1, col2, col3 = st.columns([0.5, 5, 1])

with col2:
    st.image("https://forgemia.inra.fr/ludovic.mailleret/figures/-/raw/master/ceratitis_capitata/ceratitis_small.png", width = 350)
    st.markdown("## Technique de l'Insecte Stérile et points de bascule")

with col2:
    tab1, tab2 = st.tabs(["Modèle", "Simulations"]) 

    with tab1:
        st.markdown("### Modèle TIS")

    with tab2:
        st.markdown("### Calculs et simulations")

        plotChoice = st.radio("Que voulez vous tracer ?",
                        ("Dynamiques", "Synthèse des dynamiques", "Plan de phase", "Bifurcations / mâles stériles"), index=0)

        if plotChoice == "Dynamiques":


        elif plotChoice == "Synthèse des dynamiques":


        elif plotChoice == "Plan de phase":


        elif plotChoice == "Bifurcations / mâles stériles":
