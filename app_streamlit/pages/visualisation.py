import streamlit as st
import pandas as pd
import numpy as np
from chemotools.scatter import StandardNormalVariate
from chemotools.derivative import SavitzkyGolay
from sklearn.pipeline import make_pipeline
import sys
sys.path.append('/Users/douati/Documents/GitHub/Spectroscopy-project-/app_streamlit')
from module_app_streamlit.Plot_spectres import plot_spectres

def show():
    st.title('Visualisation')
    st.write("Visualiser les spectres chargés.")
    
    # Charger les données
    df = st.session_state.get('df', None)

    # Vérifier si les données sont chargées
    if df is None:
        st.warning("Veuillez charger des données pour visualiser les spectres.")
        return

    # Aperçu des données avant traitement
    st.write("Aperçu des données :")
    st.write(df.head())

    # Nettoyer la colonne 'spectre' et convertir en listes de floats
    def safe_convert(x):
        try:
            # Si x est déjà un tableau numpy ou une liste, on le retourne tel quel
            if isinstance(x, (np.ndarray, list)):
                return list(x)
            # Si x est une chaîne de caractères, on tente de le convertir
            if isinstance(x, str):
                return [float(i) for i in x.split(",")]
            # Sinon, lever une exception
            raise ValueError("Format non reconnu pour le spectre")
        except Exception as e:
            st.warning(f"Erreur de conversion dans la ligne: {x}. Erreur: {e}")
            return []

    # Vérifier si la colonne "spectre_converti" existe déjà
    if "spectre_converti" not in df.columns:
        # Appliquer la conversion en utilisant la fonction de nettoyage
        df["spectre_converti"] = df["spectre"].apply(safe_convert)

        # Vérifier si la colonne contient des listes non vides
        if df["spectre_converti"].apply(len).sum() == 0:
            st.warning("Les données de spectre ne sont pas correctement formatées.")
            return

    # Convertir la colonne en tableau numpy
    spectre_array = np.array(df['spectre_converti'].tolist())

    # Initialiser les transformateurs
    snv = StandardNormalVariate()
    first_derivative = SavitzkyGolay(15, 2, 1)
    second_derivative = SavitzkyGolay(15, 2, 2)

    # Appliquer les transformations si elles n'ont pas déjà été calculées
    if "spectre_snv" not in df.columns:
        df["spectre_snv"] = snv.fit_transform(spectre_array).tolist()
    if "spectre_first_derivative" not in df.columns:
        df["spectre_first_derivative"] = first_derivative.fit_transform(spectre_array).tolist()
    if "spectre_second_derivative" not in df.columns:
        df["spectre_second_derivative"] = second_derivative.fit_transform(spectre_array).tolist()

    # Choisir quel spectre afficher
    st.write("Visualiser les spectres transformés")
    transformation = st.radio(
        "Choisissez une transformation à visualiser :",
        ("Aucun", "SNV", "1ère dérivée", "2ème dérivée")
    )

    # Afficher les spectres transformés
    if transformation == "Aucun":
        plot_spectres(df, column='spectre')
    elif transformation == "SNV":
        plot_spectres(df, column="spectre_snv")
    elif transformation == "1ère dérivée":
        plot_spectres(df, column="spectre_first_derivative")
    elif transformation == "2ème dérivée":
        plot_spectres(df, column="spectre_second_derivative")

# Appeler la fonction
show()
