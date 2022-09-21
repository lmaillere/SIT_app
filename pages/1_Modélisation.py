import numpy as np
import streamlit as st

from utils.funTISapp import *

st.set_page_config(layout="wide", page_title = "Modélisation", page_icon = "🌳")

st.sidebar.header("Modélisation")

col2, col3 = st.columns([5, 15], gap = "large")

with col2:
    st.image("https://forgemia.inra.fr/ludovic.mailleret/figures/-/raw/master/ceratitis_capitata/ceratitis_small.png", width=250)
with col3:
    st.markdown("$~$")
    st.markdown("# Technique de l'Insecte Stérile et point de basculement")

col12, col13 = st.columns([11, 10],gap = "large")

with col12:
    st.markdown("### Modèle à deux sexes et mâles stériles")
    st.markdown("Le modèle comporte 2 variables :")
    st.markdown("- la densité de femelles sauvages dans l'environnement $f$,")
    st.markdown("- la densité de mâles sauvages dans l'environnement $m$,")
    st.markdown("- la densité de mâles stériles $m_s$ est considérée constante.")
    st.markdown("##### Le modèle s'écrit :")
    st.markdown(r"$$\left\{\begin{array}{l}\displaystyle \dot f = r (1-p) f \frac{m}{m+m_s} c(f) - \mu f,\\[.3cm]\displaystyle \dot m = r p f \frac{m}{m+m_s}  c(f) - \mu m.\end{array}\right.$$")
    st.markdown(r"- $r$ représente le nombre d'œufs pondus par femelle,")
    st.markdown(r"- $p$ la proportion de mâles dans la descendance,")
    st.markdown(r"- $c(f)$ la compétition entre les femelles pour l'accès aux sites de pontes,")
    st.markdown(r"- $\mu$ le taux de mortalité de la population.")

with col13:
    st.markdown("#")
    st.markdown("##### Influence des mâles stériles")
    st.markdown(r"- en l'absence de mâles stériles ($m_s = 0$), les femelles sauvages s'accouplent avec les mâles sauvages et pondent des oeufs à une vitesse proportionnelle au NO nombre de mâles et de femelles sauvages, pondérée par la compétition entre femelles : $r f\,c(f)$")
    st.markdown("- en présence de mâles stériles ($m_s > 0$) ")
