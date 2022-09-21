import numpy as np
import streamlit as st

from utils.funTISapp import *

st.set_page_config(layout="wide", page_title = "Introduction", page_icon ="📚")

st.sidebar.header("Introduction")

col2, col3 = st.columns([5, 15], gap = "large")

with col2:
    st.image("https://forgemia.inra.fr/ludovic.mailleret/figures/-/raw/master/ceratitis_capitata/ceratitis_small.png", width=250)
with col3:
    st.markdown("$~$")
    st.markdown("# Technique de l'Insecte Stérile et point de basculement")

st.markdown("## Introduction")
st.markdown("Cette application a pour but d'illustrer des situations ou l'on peut chercher à exploiter des points de basculement, plutôt que les éviter. Il s'agit ici de considérer une problématique de contrôle d'insectes ravageurs en agriculture, par la *Technique de l'Insecte Stérile*.")

st.markdown("La technique de l'insecte stérile est une méthode de contrôle de ravageurs ou vecteurs relevant du biocontrôle.")
st.markdown("- La technique repose sur l'introduction dans l'environnement d'individus mâles de l'espèce cible, préalablement multipliés et stérilisés dans des biofabriques.") 
st.markdown("- Les accouplements avec les femelles sauvages, n'entraînent pas de descendance ce qui diminue le taux de croissance de la population sauvage et permet de ramener la population de ravageurs à des niveaux acceptables.")

st.markdown("La première espèce contrôlée *via* cette technique fut la lucilie bouchère, une mouche parasite des mammifères, dans la seconde moitié du XXe siècle sur différents endroits du globe. Depuis, des recherches sont conduites pour adapter la technique à des vecteurs de maladie comme les  moustiques, ou des ravageurs des cultures, comme les mouches des fruits (*e.g. Ceratitis capitata* (en photo ci-dessus), ou *Drosophila suzukii*).")
st.markdown("$~$")
st.markdown("*Crédit Photo: copyright Cécile Bresch, Lucas Etienne ; améliorations Xavier Fauvergue (@INRAe)*")