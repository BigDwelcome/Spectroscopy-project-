import streamlit as st
import pandas as pd
import numpy as np
import pickle
import sys
sys.path.append('/Users/douati/Documents/GitHub/Spectroscopy-project-/app_streamlit')

def show():
    # Titre de la page
    st.title('Prédiction de la concentration d\'amylose')
    # Charger les données
    df = st.session_state.get('df', None)
    # charger le modèle
    model = pickle.load(open('app_streamlit/data_app/model.pkl', 'rb'))
    # Vérifier si les données sont chargées
    if df is None:
        st.warning("Veuillez charger des données pour prédire la concentration d'amylose.")
        return
    # prediction des résultats
    if '[amylose](%)' not in df.columns:
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
        df['[amylose](%)'] = model.predict(df['spectre_converti'].tolist())
    
    # Afficher les résultats
    st.write("Résultats de la prédiction :")
    st.write(df[['id', '[amylose](%)']])

show()