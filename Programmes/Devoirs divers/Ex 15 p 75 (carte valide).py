from random import choice

def carte_valide(carte:tuple)->bool:

    if not isinstance(carte, (list, tuple)) : raise TypeError
    if len(carte) != 2 : raise ValueError
    if not isinstance(carte[0], int) : raise TypeError
    if not isinstance(carte[1], str) : raise TypeError

    valeur, couleur = carte

    if valeur < 2 or valeur > 14:
        return False
    
    match couleur:
        case "Carreau": pass
        case "Pique": pass
        case "Trèfle": pass
        case "Coeur": pass
        case _: return False

    return True


def nom_carte(carte:tuple)->str:

    if not carte_valide(carte): raise ValueError

    val_sortie = ""

    valeur, couleur = carte

    match valeur:
        case 11: val_sortie += "Valet "
        case 12: val_sortie += "Dame "
        case 13: val_sortie += "Roi "
        case 14: val_sortie += "As "
        case _: val_sortie += str(valeur) + " "

    val_sortie += "de " + couleur

    return val_sortie

def all_cards()->list[tuple]:
    cartes = []
    couleurs = ["Carreau", "Trèfle", "Coeur", "Pique"]
    for couleur in couleurs:
        for i in range(2, 15):
            cartes.append((i, couleur))
    return cartes

def random_card():
    return nom_carte(choice(all_cards()))

print(random_card())