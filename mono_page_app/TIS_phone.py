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

        st.markdown("La technique de l'insecte stérile est une méthode de contrôle de ravageurs qui repose sur l'introduction dans l'environnement d'individus mâles de l'espèce cible, préalablement stérilisés dans des biofabriques. Les accouplements de ces mâles avec les femelles sauvages ne produisent pas de descendance, ce qui diminue le taux de croissance de la population.")

        st.markdown("Le modèle comporte 2 variables :")
        st.markdown("- la densité de femelles sauvages dans l'environnement $f$,")
        st.markdown("- la densité de mâles sauvages dans l'environnement $m$,")
        st.markdown("- la densité de mâles stériles $m_s$ est elle considérée constante.")
        st.markdown("##### Le modèle s'écrit :")
        st.markdown(r"$$\left\{\begin{array}{l}\displaystyle \dot f = r (1-p) f \frac{m}{m+m_s} c(f) - \mu f,\\[.3cm]\displaystyle \dot m = r p f \frac{m}{m+m_s}  c(f) - \mu m.\end{array}\right.$$")
        st.markdown(r"- $r$ représente le nombre d'œufs pondus par femelle,")
        st.markdown(r"- $p$ la proportion de mâles dans la descendance,")
        st.markdown(r"- $c(f)$ la compétition entre les femelles pour l'accès aux sites de pontes,")
        st.markdown(r"- $\mu$ le taux de mortalité de la population.")




    with tab2:
        st.markdown("### Calculs et simulations")

        f0 = st.slider(' Densité de femelles sauvages initiale', min_value = 0.1, max_value = K, value = 3., step=0.1, disabled = False)  
        m0 = st.slider(' Densité de mâles sauvages initiale', min_value = 0.1, max_value = K, value = K/2, step=0.1) 
        mS =  st.slider(' Densité de mâles stériles', min_value = .1, max_value = 1.75, value = 1., step = 0.05)  

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
