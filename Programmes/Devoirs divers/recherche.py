tableau = [1, 3, 5, 7, 9, 11]

def recherche_index(tabl, nombre):
    tab = tabl
    longueur = len(tab)
    demi = longueur//2
    index=0
    while longueur > 0:
        if tab[demi-1] > nombre:
            new_tab = tab[0:demi]
        elif tab[demi-1] < nombre:
            index += demi
            new_tab = tab[demi::]
        else:
            index += demi//2
            return index, tabl[index]
        tab = new_tab
        longueur = len(tab)
        demi = longueur//2

print(recherche_index(tableau, 11))