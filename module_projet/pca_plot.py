import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
def plot_pca_variance(pca):
    """
    Visualise la variance expliquée par les composantes principales.

    Parameters:
    pca : PCA object
        L'objet PCA ajusté contenant les informations sur les composantes principales.
    """
    plt.bar(range(1, pca.n_components_ + 1), pca.explained_variance_ratio_ * 100)
    plt.step(range(1, len(pca.explained_variance_ratio_.cumsum() * 100) + 1), 
             pca.explained_variance_ratio_.cumsum() * 100, where='mid', color='red', 
             label='Variance cumulative')
    plt.plot([0, pca.n_components_], [95, 95], color='green', linestyle='--')
    plt.xlabel("Composantes principales")
    plt.ylabel("Variance expliquée")
    plt.legend()
    plt.show()



def plot_pca_score(score, labels, category=None, x=0, y=1):
    """
    Visualise les scores PCA avec les catégories en couleurs et les labels affichés.
    
    Parameters:
        score : array, scores sur les composantes principales.
        labels : array, labels des individus (affichés sur la figure).
        category : array ou None, catégories pour colorer les points (facultatif).
        x, y : int, indices des composantes principales (par défaut 0 et 1).
    """
    # Créer un DataFrame pour faciliter l'association des données
    import pandas as pd
    df = pd.DataFrame({
        'PCx': score[:, x],
        'PCy': score[:, y],
        'Labels': labels,
        'Category': category if category is not None else 'Tous'
    })
    
    # Créer le scatter plot
    fig = px.scatter(
        df, 
        x='PCx', y='PCy', 
        color='Category',
        labels={'PCx': f'PC{x+1}', 'PCy': f'PC{y+1}'}
    )
    
    # Ajouter les labels à côté des points
    for i in range(len(df)):
        fig.add_annotation(
            x=df['PCx'][i],
            y=df['PCy'][i],
            text=str(df['Labels'][i]),
            showarrow=False,
            font=dict(size=10)
        )
    
    fig.show()
