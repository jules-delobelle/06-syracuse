"""
Ce module calcule et affiche des propriétés de la suite de Syracuse.
"""

# imports
from plotly.graph_objects import Scatter, Figure

def syr_plot(lsyr):
    """
    Génère et affiche un graphique de la suite de Syracuse.

    Args:
        lsyr (list): La suite de Syracuse
    """
    title = "Syracuse" + " (n = " + str(lsyr[0]) + " )"
    fig = Figure({
        'layout': {
            'title': {'text': title},
            'xaxis': {'title': {'text': "x"}},
            'yaxis': {'title': {'text': "y"}},
        }
    })

    x = list(range(len(lsyr)))
    t = Scatter(x=x, y=lsyr, mode="lines+markers", marker_color="blue")
    fig.add_trace(t)
    fig.show()

def syracuse_l(n):
    """
    Retourne la suite de Syracuse de source n.

    Args:
        n (int): La source de la suite

    Returns:
        list: La suite de Syracuse de source n
    """
    l = [n]
    while n not in (1, 0):
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        l.append(n)
    return l

def temps_de_vol(l):
    """
    Retourne le temps de vol d'une suite de Syracuse.

    Args:
        l (list): La suite de Syracuse

    Returns:
        int: Le temps de vol
    """
    return len(l) - 1

def temps_de_vol_en_altitude(l):
    """
    Retourne le temps de vol en altitude d'une suite de Syracuse.

    Args:
        l (list): La suite de Syracuse

    Returns:
        int: Le temps de vol en altitude
    """
    return next(i for i, x in enumerate(l) if x < l[0]) - 1

def altitude_maximale(l):
    """
    Retourne l'altitude maximale d'une suite de Syracuse.

    Args:
        l (list): La suite de Syracuse

    Returns:
        int: L'altitude maximale
    """
    return max(l)

def main():
    """
    Fonction principale qui exécute les appels aux fonctions de Syracuse.
    """
    lsyr = syracuse_l(15)
    syr_plot(lsyr)
    print(temps_de_vol(lsyr))
    print(temps_de_vol_en_altitude(lsyr))
    print(altitude_maximale(lsyr))

if __name__ == "__main__":
    main()
