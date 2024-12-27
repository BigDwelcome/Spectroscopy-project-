import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def plot_residuals(y_values, residuals, xlabel="Valeurs réelles", ylabel="Résidus", title="Analyse des résidus"):
    """
    Trace un graphique des résidus (valeurs réelles vs résidus).

    Parameters:
        y_values (array-like): Les valeurs réelles (axe x du graphique).
        residuals (array-like): Les résidus (axe y du graphique).
        xlabel (str): Étiquette de l'axe x.
        ylabel (str): Étiquette de l'axe y.
        title (str): Titre du graphique.
    """
    # S'assurer que les résidus sont un tableau unidimensionnel
    residuals = np.asarray(residuals).ravel()

    # Tracé principal
    fig, ax = plt.subplots(figsize=(16, 9))
    ax.scatter(y_values, residuals, color='b', label='Résidus', alpha=0.6)
    ax.axhline(0, linestyle='--', color='r', label='Zéro')

    # Configurations des axes
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.legend(loc='upper right')

    plt.show()


def plot_residual_distribution(residuals, ylabel="Densité", title="Distribution des résidus"):
    """
    Trace la distribution des résidus.

    Parameters:
        residuals (array-like): Les résidus à analyser.
        ylabel (str): Étiquette de l'axe y.
        title (str): Titre du graphique.
    """
    # S'assurer que les résidus sont un tableau unidimensionnel
    residuals = np.asarray(residuals).ravel()

    # Tracé de la distribution
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.kdeplot(residuals, ax=ax, color='green', fill=True, alpha=0.3, bw_adjust=1.2, label='Distribution normale')

    # Configurations des axes
    ax.set_xlabel("Résidus")
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.legend(loc='upper right')

    plt.show()





def plot_predictions(y_true, y_pred, xlabel="True values", ylabel="Predicted values", title="Prediction results"):
    """
    Trace un graphique des valeurs réelles contre les valeurs prédites.

    Parameters:
        y_true (array-like): Les valeurs réelles (axe x du graphique).
        y_pred (array-like): Les valeurs prédites (axe y du graphique).
        xlabel (str): Étiquette de l'axe x.
        ylabel (str): Étiquette de l'axe y.
        title (str): Titre du graphique.
    """
    # Création de la figure
    fig, ax = plt.subplots(figsize=(16, 9))
    
    # Tracé des points (valeurs réelles vs prédites)
    ax.scatter(y_true, y_pred, color='b', label='Prédictions')
    
    # Ligne de référence (y = x)
    ax.plot([y_true.min(), y_true.max()], [y_true.min(), y_true.max()], linestyle='--', color='r', label='Ligne y=x')
    
    # Configurations des axes
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    
    # Légende
    ax.legend(loc='upper left')
    
    # Affichage du graphique
    plt.show()
