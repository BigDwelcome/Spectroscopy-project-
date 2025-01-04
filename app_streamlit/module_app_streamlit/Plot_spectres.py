from plotly import graph_objects as go
import plotly.express as px
import streamlit as st
# Fonction pour afficher les spectres
def plot_spectres(df, column='spectre'):
    """
    Afficher les spectres dans un graphique interactif.
    df : DataFrame
        DataFrame contenant les données des spectres
    column : str
        Nom de la colonne contenant les spectres à afficher
    """
    # Créer une figure pour afficher les spectres
    fig = go.Figure()
    
    # Ajouter les courbes de spectres
    for i, row in df.iterrows():
        fig.add_trace(go.Scatter(x=row['wavelengths'], y=row[column], mode='lines', name=row['id']))
    
    # Mettre à jour le layout de la figure
    fig.update_layout(
        title="Spectres chargés",
        xaxis_title="Longueur d'onde (nm)",
        yaxis_title="Intensité",
        template='plotly_dark'
    )
    # Afficher la figure dans Streamlit
    st.plotly_chart(fig, use_container_width=True)
    