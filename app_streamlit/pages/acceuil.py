import streamlit as st
import pandas as pd
from scipy.io import loadmat


def show():
    st.title('Accueil')
    st.write("Charger les spectres de la base de données pour commencer.")

    # Vérifier si des données existent déjà dans la session
    if 'df' not in st.session_state:
        st.session_state.df = None

    # Uploader les fichiers `.mat`
    uploaded_files = st.file_uploader(
        "Choisir des fichiers au format .mat",
        type="mat",
        accept_multiple_files=True
    )

    # Initialisation du dictionnaire pour l'ensemble d'entraînement
    spectre_uploaded = {'id': [], 'spectre': [], 'wavelengths': []}

    if uploaded_files:
        st.subheader("Informations contenues dans les fichiers chargés ")

        for file in uploaded_files:
            try:
                # Charger le fichier `.mat`
                data = loadmat(file)

                # Vérifier les clés attendues dans le fichier
                if all(key in data for key in ['spectre', 'wavelengths']):
                    spectre_uploaded['id'].append(file.name)
                    spectre_uploaded['spectre'].append(data['spectre'].flatten())
                    spectre_uploaded['wavelengths'].append(data['wavelengths'].flatten())
                else:
                    st.error(f"Clés manquantes dans le fichier : {file.name}")
            except Exception as e:
                st.error(f"Erreur lors du chargement du fichier {file.name}: {e}")

        # Conversion du dictionnaire en DataFrame
        if spectre_uploaded['id']:
            df = pd.DataFrame(spectre_uploaded)
            st.write("Tableau récapitulatif des spectres chargés :")
            st.dataframe(df)
            # Stocker le DataFrame dans la session
            st.session_state.df = df
        else:
            st.warning("Aucune donnée valide n'a été chargée.")
    elif st.session_state.df is not None:
        # Si des données ont déjà été chargées, les afficher
        st.write("Tableau récapitulatif des spectres chargés (données existantes) :")
        st.dataframe(st.session_state.df)


# Appeler la fonction
show()
