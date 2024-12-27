import streamlit as st
import pandas as pd
import sys
sys.path.append('/Users/douati/Documents/GitHub/Spectroscopy-project-/app_streamlit')
from module_app_streamlit.Plot_spectres import plot_spectres

def show():
    st.title('Visualisation')
    st.write("Visualiser les spectres chargés.")
    
    # Charger les données
    df = st.session_state.df

    # Vérifier si les données sont chargées
    if df is None:
        st.warning("Veuillez charger des données pour visualiser les spectres.")
    else:
        plot_spectres(df)

# Appeler la fonction
show()
