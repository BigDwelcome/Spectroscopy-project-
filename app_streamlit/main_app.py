import streamlit as st
from app_streamlit.pages import acceuil, visualisation

# Titre de l'application
st.title("Application de prediction de la quantité d'amylose dans le riz")
st.write("Cette application permet de charger des spectres de riz et de prédire la quantité d'amylose dans le riz.")

# Navigation
menu = st.sidebar.radio("Menu", ["Accueil", "Visualisation", "Prédiction"])

# Afficher la page sélectionnée
if menu == "Accueil":
    acceuil.show()  # Afficher la page d'accueil
elif menu == "Visualisation":
    visualisation.show()  # Afficher la page de visualisation
elif menu == "Prédiction":
    visualisation.show()
