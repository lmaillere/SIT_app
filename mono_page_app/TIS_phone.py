import numpy as np
import streamlit as st

from utils.funTISapp import *



col1, col2, col3 = st.columns([0.5, 5, 1])

with col2:
    st.image("https://forgemia.inra.fr/ludovic.mailleret/figures/-/raw/master/ceratitis_capitata/ceratitis_small.png", width = 400)
    st.markdown("## Technique de l'Insecte Stérile et points de bascule")
