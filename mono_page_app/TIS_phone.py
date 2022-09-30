import numpy as np
import streamlit as st

from utils.funTISapp import *



col1, col2, col3 = st.columns([0.5, 4.5, 1])

with col2:
    st.image("https://forgemia.inra.fr/ludovic.mailleret/figures/-/raw/master/ceratitis_capitata/ceratitis_small.png", width = 350)
    st.markdown("## Technique de l'Insecte Stérile et points de bascule")

with col2:
    tab1, tab2 = st.tabs(["Modèle", "Simulations"]) 

    with tab1:
        st.markdown("### Modèle TIS")





    with tab2:
        st.markdown("### Calculs et simulations")

        f0 = st.slider(' Densité de femelles sauvages initiale', min_value = 0.1, max_value = K, value = 3., step=0.1, disabled = False)  
        m0 = st.slider(' Densité de mâles sauvages initiale', min_value = 0.1, max_value = K, value = K/2, step=0.1) 
        mS =  st.slider(' Densité de mâles stériles', min_value = .0, max_value = 1.75, value = 1., step = 0.05)  

        # intial condition
        etat0 = np.array([f0, m0])


        plotChoice = st.radio("Que voulez vous tracer ?",
                        ("Dynamiques", "Synthèse des dynamiques", "Plan de phase", "Bifurcations / mâles stériles"), index=0)

        if plotChoice == "Dynamiques":
            fig_sim = plotSim(etat0 = etat0, mS = mS, params_sim = params_sim)
            st.pyplot(fig_sim)
        elif plotChoice == "Synthèse des dynamiques":
            fig_all = plotSimAll(mS = mS, params_sim = params_sim)
            st.pyplot(fig_all)
        elif plotChoice == "Plan de phase":
            fig_plane = plotPlane(mS = mS, params_sim = params_sim)
            st.pyplot(fig_plane)
        elif plotChoice == "Bifurcations / mâles stériles":
            fig_bif = plotBif(params_sim = params_sim)
            st.pyplot(fig_bif)
