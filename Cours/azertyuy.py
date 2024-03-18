
# Une marche aléatoire (1D) : la ruine du joueur.
# ===============================================
# 
# 1) Compléter le fichier `marche.py` pour créer un tableau `marche` de 100 entiers commençant par 20 tel que chaque entier est obtenu aléatoirement en ajoutant ou retranchant (avec la même probabilité) 1 à l’entier précédent.
# 
# Afficher cette **marche aléatoire** avec la fonction `plot` de la bibliothèque `matplotlib` :
# 


from random import randint
def creer_une_marche():
    t = [20 for i in range(100)] # creer un tableau de 100 entiers de valeur 20: [20,...]
    print(t)
    for i in range(len(t)-1):
        t[i+1]= t[i] + (randint(0, 1)*2-1)
    return t

# Test
print(len(creer_une_marche())==100)
print(creer_une_marche()[0]==20)

marche = creer_une_marche()
import matplotlib.pyplot as plt
plt.plot(marche)
plt.show()

# 2) Cette marche peut représenter un joueur dont le capital initial `c` est de 20€ et qui gagne ou perd 1€ à chaque étape. Écrire une fonction `creer_marche` qui prend deux arguments, `nbjoueurs` et `c`, et qui génère de la même manière une matrice de dimensions `nb_joueurs x 100`. Chaque ligne contiendra une marche aléatoire comme ci-dessus, mais on souhaite désormais qu’une marche atteignant 0 (joueur ruiné) reste ensuite à 0.

def creer_marche(nb_joueurs, c):
    """ 
    Entree : 2 entiers, 
    - nb_joueur :  le nombre de joueurs 
    - c : le capital initial de chaque joueur.
    Sortie : 
    - un tableau de tableaux (matrice nb_joueur * 100). 
    Chacun des nb_joueur tableaux est la marche d'un joueur de capital initial c, et a pour longueur 100.
    Contrairement a creer_une_marche, une marche qui atteint 0 reste ensuite a 0.
    """
    marches = [None] * nb_joueurs
    for n in range(nb_joueurs):
        marche = ... # initialiser un tableau marche de 100 entiers de valeur c
        for i in range(99):
            if marche[i] == 0:
                ...
            else:
                ...
        marches[n] = marche # on insere ce tableau dans la ligne
    return marches

# Test:
print(creer_marche(2,4))


# 3) Écrire une fonction qui prend deux arguments `nbjoueurs` et `c`, génère une matrice en faisant appel à `creer_marche` et calcule la liste des joueurs ayant été ruinés, c’est-à-dire les indices des marches correspondant à des joueurs ruinés.

def calcul_stats_v1(nb_joueurs, c):
    """ genere une matrice de nb_joueurs marches, et renvoie la liste des joueurs ruines """
    marches = creer_marche(nb_joueurs, c)
    id_joueurs_ruines = [i for i in ... if marches[i][-1] == ...]
    return id_joueurs_ruines

# Test:
print(calcul_stats_v1(2,4))
# Ce test a peu d'intérêt; on peut juste vérifier:
# - que la fonction renvoie une liste d'entiers distincts
# - que chaqun de ces entiers est compris entre 0 et nb_joueurs-1

# Pour vérifier plus sérieusement la correction, 
# il faudrait afficher la matrice des marches pour vérifier.
# Si l'énoncé n'imposait pas de générer la marche à l'intérieur de la fonction,
# il aurait aussi été raisonnable de passer la matrice des marches en argument de la fonction.

# 4) Compléter la fonction précédente pour calculer la proportion de joueurs ayant été ruinés, le capital moyen des joueurs au bout des 100 étapes, et le temps moyen avant d’être ruiné (pour les joueurs qui ont été ruinés). Afficher ces trois valeurs.

def calcul_stats_v2(nb_joueurs, c):
    """ genere une matrice de nb_joueurs marches, et renvoie la liste des joueurs ruines. 
    Affiche:
    - la proportion de joueurs ruines
    - le capital moyen des joueurs (ruines ou non) au bout des 100 etapes.
    - le temps moyen avant la ruine pour les joueurs ruines, ou -1 s'il n'y en a pas.
    on considere qu'un joueur est ruine au temps i>=0 si sa marche vaut 0 a partir de l'indice i.
    """
    marches = creer_marche(nb_joueurs, c)
    id_joueurs_ruines = ...
    proportion_ruines = ...
    capital_total = 0
    for i in range(nb_joueurs):
        capital_total = capital_total + ...
    capital_moyen = ...
    temps_moyen_ruine = -1
    if len(id_joueurs_ruines) > 0:
        ...
    print("proportion de joueurs ruinés:", proportion_ruine)
    print("capital moyen:", capital_moyen)
    print("temps moyen:", temps_moyen_ruine)

# Test
print(calcul_stats_v2(1,4))
print(calcul_stats_v2(3,5))

# 5) Évaluer votre fonction sur 150 joueurs ayant un capital de départ de 6. Puis l’évaluer avec un capital de départ de 80.
