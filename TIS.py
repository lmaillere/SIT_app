import numpy as np
import streamlit as st

from utils.funTISapp import *

st.set_page_config(layout="wide", page_title = "Introduction", page_icon ="📚")

st.sidebar.header("Introduction")

col2, col3 = st.columns([5, 15], gap = "large")

#with col2:
    #st.image("img/ceratitis.png", width=250)
with col3:
    st.markdown("$~$")
    st.markdown("# Technique de l'Insecte Stérile et point de basculement")

st.markdown("## Introduction")
st.markdown("Cette application a pour but d'illustrer des situations ou l'on peut chercher à exploiter des points de basculement, plutôt que les éviter. Il s'agit ici de considérer une problématique de contrôle d'insectes ravageurs en agriculture, par la *Technique de l'Insecte Stérile*.")
st.markdown("$~$")
#st.markdown("*Crédit Photo: copyright Cécile Bresch, Lucas Etienne ; améliorations Xavier Fauvergue (@INRAe)*")