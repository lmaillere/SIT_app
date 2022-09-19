import numpy as np
import streamlit as st

from utils.funTISapp import *

st.set_page_config(layout="wide", page_title = "Introduction", page_icon ="📚")

st.sidebar.header("Introduction")

col2, col3 = st.columns([5, 15], gap = "large")


with col2:
    st.image("img/ceratitis.png", width=300)
with col3:
    st.markdown("$~$")
    st.markdown("# Technique de l'Insecte Stérile et point de basculement")