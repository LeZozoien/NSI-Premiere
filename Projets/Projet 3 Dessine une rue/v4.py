# Projet 3 par Clément Favier et Enzo Rodriguez

# ______              _                                                   
# |  _  \            (_)                                                  
# | | | |___  ___ ___ _ _ __   ___    _   _ _ __   ___    _ __ _   _  ___ 
# | | | / _ \/ __/ __| | '_ \ / _ \  | | | | '_ \ / _ \  | '__| | | |/ _ \
# | |/ /  __/\__ \__ \ | | | |  __/  | |_| | | | |  __/  | |  | |_| |  __/
# |___/ \___||___/___/_|_| |_|\___|   \__,_|_| |_|\___|  |_|   \__,_|\___|

import random as rm
import turtle as trt

def toit_circulaire(largeur_bat:int):
    """Dessine un toit circulaire en partant de la gauche vers la droite.

    Args:
        largeur_bat (int): Largeur du batiment
    """

    assert type(largeur_bat) == int, "La largeur du batiment n'est pas un nombre entier."
    assert largeur_bat != 0, "La largeur du batiment est nulle."

    old_pos = trt.position()
    trt.pensize(5)
    trt.color("#000000")
    trt.pd()
    trt.begin_fill()
    trt.goto(old_pos[0]+largeur_bat, old_pos[1])
    trt.lt(90)
    trt.circle(largeur_bat//2,180)
    trt.end_fill()
    trt.pu()

def toit_triangulaire(largeur_bat:int):
    """Dessine un toit triangulaire dont la hauteur est aléatoire en partant de la gauche vers la droite.

    Args:
        largeur_bat (int): Largeur du batiment
    """
    
    assert type(largeur_bat) == int, "La largeur du batiment n'est pas un nombre entier."
    assert largeur_bat != 0, "La largeur du batiment est nulle."
    
    old_pos = trt.position()
    trt.pensize(5)
    trt.color("#000000")
    hauteur_toit = max(rm.gauss(0.6, 0.3), 0.1) * largeur_bat
    trt.pd()
    trt.begin_fill()
    trt.goto(old_pos[0]-largeur_bat*0.1,old_pos[1])
    trt.goto(old_pos[0]+largeur_bat*0.5,old_pos[1]+hauteur_toit)
    trt.goto(old_pos[0]+largeur_bat*1.1,old_pos[1])
    trt.goto(old_pos)
    trt.end_fill()
    trt.pu()

def toit_plat(largeur_bat:int):
    """Dessine un toit plat  en partant de la gauche vers la droite.

    Arguments:
        largeur_bat (int): Largeur du batiment
    """

    assert type(largeur_bat) == int, "La largeur du batiment n'est pas un nombre entier."
    assert largeur_bat != 0, "La largeur du batiment est nulle."

    old_pos = trt.pos()
    trt.pensize(8)
    trt.color("#000000")
    trt.pd()
    trt.goto(old_pos[0]-largeur_bat*0.1,old_pos[1])
    trt.goto(old_pos[0]+largeur_bat*1.2,old_pos[1])
    trt.pu()

def etage(couleur:str, largeur_bat:int, hauteur_étage:int):
    """Dessine un étage de l'immeuble.

    Arguments:
        couleur (str): Code hexadécimal de la couleur à utiliser
        largeur_bat(int): Largeur du batiment
        hauteur (int): Hauteur de l'étage
    """

    assert type(largeur_bat) == int, "La largeur du batiment n'est pas un nombre entier."
    assert largeur_bat != 0, "La largeur du batiment est nulle."
    assert type(hauteur_étage) == int, "La hauteur de l'étage n'est pas un nombre entier."
    assert largeur_bat != 0, "La hauteur de l'étage est nulle."
    assert type(couleur) == str,"La couleur donnée n'est pas un string."
    trt.seth(0)
    trt.color(couleur)
    trt.pd()
    trt.begin_fill()
    for i in range(2):
        trt.fd(largeur_bat);trt.lt(90)
        trt.fd(hauteur_étage);trt.lt(90)
    trt.end_fill()
    trt.pu()

def fenetre_carre(largeur_bat:int,couleur:str,balcon:int):
    """"Dessine une fenêtre carrée en partant du coin inférieur gauche.

    Args:
        largeur_bat (int): Largeur du batiment
        couleur (str): Code hexadécimal de la couleur à utiliser
        balcon (int): Valeur décidant de la présence d'un balcon
    """

    assert type(largeur_bat) == int, "La largeur du batiment n'est pas un nombre entier."
    assert largeur_bat != 0, "La largeur du batiment est nulle."
    assert type(balcon) == int, "Le balcon n'est pas un entier."
    assert type(couleur) == str,"La couleur donnée n'est pas un string."

    trt.seth(0)
    trt.pensize(4)
    trt.color(couleur, "#88ffff")
    cote = largeur_bat//4
    old_pos = trt.pos()
    trt.pd()
    trt.begin_fill()
    trt.goto(old_pos[0],old_pos[1]+cote)
    trt.goto(old_pos[0]+cote,old_pos[1]+cote)
    trt.goto(old_pos[0]+cote,old_pos[1])
    trt.goto(old_pos)
    trt.pu()
    trt.end_fill()
    trt.pensize(3)
    trt.goto(old_pos[0],old_pos[1]+cote/2)
    trt.goto(old_pos[0]+cote,old_pos[1]+cote/2)
    trt.pu()
    trt.goto(old_pos[0]+cote/2,old_pos[1])
    trt.pd()
    trt.goto(old_pos[0]+cote/2,old_pos[1]+cote)
    trt.pu()

    if balcon == 1 :
        trt.pu()
        trt.pensize(2)
        trt.color('#777777')
        trt.goto(old_pos[0]-cote//6,old_pos[1]-cote//6)
        trt.pd()
        trt.lt(90)
        for i in range(int(cote//6)):
            trt.fd(cote//3)
            trt.rt(90)
            trt.fd(cote//8)
            trt.rt(90)
            trt.fd(cote//3)
            trt.lt(90)
            trt.fd(cote//8)
            trt.lt(90)
        trt.fd(cote//3)
        end_pos = trt.pos()
        trt.goto(old_pos[0]-cote//6,old_pos[1]+cote//6)
        trt.goto(old_pos[0]-cote//6,old_pos[1]-cote//6)
        trt.goto(end_pos[0],end_pos[1]-cote//3)
    trt.pu()
    if balcon == 1 :
        trt.goto(old_pos)
    trt.seth(0)
        
def fenetre_ronde(largeur_bat:int,couleur:str):
    """Dessine une fenêtre ronde en partant du coin inférieur droit.

    Args:
        largeur_bat (int): Largeur batiment
        couleur (str): Code hexadécimal de la couleur à utiliser
    """

    assert type(largeur_bat) == int, "La largeur du batiment n'est pas un nombre entier."
    assert largeur_bat != 0, "La largeur du batiment est nulle."
    assert type(couleur) == str,"La couleur donnée n'est pas un string."

    trt.pensize()
    trt.pu()
    trt.color(couleur, "#88ffff")
    rayon = largeur_bat/8
    old_pos = trt.pos()
    trt.goto(old_pos[0]+rayon,old_pos[1])
    trt.pd()
    trt.begin_fill()
    trt.circle(rayon)
    trt.pensize(3)
    trt.goto(old_pos[0]+rayon,old_pos[1]+2*rayon)
    trt.end_fill()
    trt.pu()
    trt.goto(old_pos[0],old_pos[1]+rayon)
    trt.pd()
    trt.begin_fill()
    trt.goto(old_pos[0]+2*rayon,old_pos[1]+rayon)
    trt.end_fill()
    trt.pu()
    trt.seth(0)

def porte_carree(largeur_bat:int, hauteur_étage:int,couleur:str):
    """Dessine une porte carrée en partant du coin inférieur droit

    Args:
        largeur_bat (int): Largeur du batiment
        hauteur_étage (int): Hauteur de l'étage
        couleur (str): Code hexadécimal de la couleur à utiliser
    """

    assert type(largeur_bat) == int, "La largeur du batiment n'est pas un nombre entier."
    assert largeur_bat != 0, "La largeur du batiment est nulle."
    assert type(hauteur_étage) == int, "La hauteur de l'étage n'est pas un nombre entier."
    assert hauteur_étage != 0
    assert type(couleur) == str,"La couleur donnée n'est pas un string."

    trt.pensize(5)
    trt.color(couleur)
    old_pos = trt.pos()
    trt.begin_fill()
    trt.pd()
    trt.goto(old_pos[0],old_pos[1]+hauteur_étage*3/5)    
    trt.goto(old_pos[0]+largeur_bat/4,old_pos[1]+hauteur_étage*3/5)
    trt.goto(old_pos[0]+largeur_bat/4,old_pos[1])
    trt.goto(old_pos)
    trt.end_fill()
    trt.pu()
    trt.seth(0)

def porte_ronde(largeur_bat:int, hauteur_étage:int,couleur:str):
    """Dessine une porte carrée en partant du coin inférieur droit

    Args:
        largeur_bat (int): Largeur du batiment
        hauteur_étage (int): Hauteur de l'étage
        couleur (str): Code hexadécimal de la couleur à utiliser
    """

    assert type(largeur_bat) == int, "La largeur du batiment n'est pas un nombre entier."
    assert largeur_bat != 0, "La largeur du batiment est nulle."
    assert type(hauteur_étage) == int, "La hauteur de l'étage n'est pas un nombre entier."
    assert hauteur_étage != 0, "La hauteur de l'étage est nulle."
    assert type(couleur) == str,"La couleur donnée n'est pas un string."

    trt.pensize(4)
    trt.color(couleur)
    old_pos = trt.pos()
    trt.pd()
    trt.begin_fill()
    trt.goto(old_pos[0]+largeur_bat/4,old_pos[1])
    trt.goto(old_pos[0]+largeur_bat/4,old_pos[1]+hauteur_étage*3/5)
    trt.left(90)
    trt.circle(largeur_bat/8,180)
    trt.goto(old_pos)
    trt.end_fill()
    trt.pu()
    trt.goto(old_pos[0]+largeur_bat/8,old_pos[1]+hauteur_étage*3/10)
    trt.pensize(3)
    trt.seth(0)

def main():
    """Fonction principale du programme
    """
    trt.setup(800, 800)
    trt.update()
    trt.pu()
    trt.speed(0)
    trt.hideturtle()
    trt.goto(-400, -301)
    trt.color("#000000")
    trt.pd()
    trt.begin_fill()
    trt.goto(400, -301)
    trt.goto(400, -400)
    trt.goto(-400, -400)
    trt.goto(-400, -301)
    trt.end_fill()
    trt.pu()

def base_random():
    """Donne un emplacement aléatoire entre 0 et 2 pour la porte

    Returns:
        int: Définit la position de la porte
        str: Définit le type de porte
    """

    emplacement_porte = rm.randint(0, 2)
    porte = rm.choice(["ronde", "carrée"])
    return emplacement_porte, porte

def etage_random():
    """Renvoie une liste de 3 booléens pour savoir s'il y a un balcon à chacune des 3 fenêtres et le type de ces 3 fenêtres.

    Returns:
        list : Liste aléatoire des balcons à mettre dans un étage
        list: Liste aléatoire des fenetres à mettre dans un étage
    """
    
    balcons = [(rm.randint(0, 1)) for i in range(3)]
    fenetres = rm.choices(["ronde", "carrée"], k=3)
    return balcons, fenetres

def toit_random():
    """Donne un toit aléatoire entre les 3 disponibles

    Returns:
        str: Toit choisi
    """

    toits = ["plat", "rond", "triangle"]
    return rm.choice(toits)

def batiment_random(hauteur:int):
    """Utilise les 3 fonctions base_random(), etage_random() et toit_random() pour générer un batiment completement aléatoire

    Args:
        hauteur (int):  Hauteur de l'image en termes du nombre d'étage  

    Returns:
        dict: Dictionnaire avec toutes les caractéristiques d'un immeuble
    """

    if not isinstance(hauteur, int):
        raise TypeError("hauteur doit être un int, mais un " + str(type(hauteur)) + " a été donné")
    if hauteur < 1:
        raise ValueError("hauteur doit être positif et supérieur à 1")
    batiment = {}
    couleur = "#" + "".join([rm.choice("0123456789abcdef") for i in range(6)])
    batiment["couleur"]=couleur
    batiment["base"]=base_random()
    etages = []
    if hauteur != 1:
        for etage in range(hauteur-1):
            etages.append(etage_random())
    batiment["etages"]=etages
    batiment["toit"]=toit_random()
    return batiment

def setup():
    """Définit les variables initiales du programme

    Returns:
        list: Nombre d'étage par immeuble 
        int: Hauteur d'un étage
        int: Découpe de la rue en fonction du nombre d'immeuble
        int: Largeur des immeubles afin de garantir de l'espace entre les immeubles
        int: Nombre d'immeuble
    """
    nbimmeubles = int(input("Combien d'immeubles voulez-vous ? (entre 3 et 6)(nombre entier)(Ne testez pas plus ou moins ça marchera pas)"))
    assert nbimmeubles > 2 and nbimmeubles < 7, "J'avais prévenu que ça marche pas, il fallait mettre un nombre entre 3 et 6 inclus."
    assert type(nbimmeubles)==int, "Vous avez tout cassé, il fallait mettre un entier"
    largeur_bloc = int(700//nbimmeubles)
    largeur_immeuble = int(largeur_bloc//1.3)
    hauteur_étage = 80
    immeubles = []
    trt.bgcolor("#aaffff")
    main()
    trt.goto(-350, -300)
    for i in range(nbimmeubles):
        etages = rm.randint(1, 5)
        etages = rm.randint(1, 5)
        immeubles.append(batiment_random(etages))
    return immeubles, hauteur_étage, largeur_bloc, largeur_immeuble, nbimmeubles

def creation_de_la_rue_aleatoire_mais_genre_completement_aleatoire(args):
    """Fonction créant la rue de A à Z

    Args:
        args (liste): Liste des caractéristiques nécessaires à la génération des batiments
    """
    immeubles, hauteur_étage, largeur_bloc, largeur_immeuble, nbimmeubles = args[0], args[1], args[2], args[3], args[4]
    for i, bat in enumerate(immeubles):
        couleur = bat["couleur"]
        porte = bat["base"]
        etages = bat["etages"]
        toit = bat["toit"]

        trt.goto(-350 + i*largeur_bloc, -300)
        etage(couleur, largeur_immeuble, hauteur_étage)
        trt.seth(0)
        pos = trt.pos()
        pos_porte = -350 + i*largeur_bloc, -300
        pos_porte = pos_porte[0] + (largeur_immeuble/6) + ((2 * largeur_immeuble * porte[0])/8), pos_porte[1]
        trt.goto(pos_porte)
        match porte[1]:
            case "carrée":
                porte_carree(largeur_immeuble, hauteur_étage, "#501000")
            case "ronde":
                porte_ronde(largeur_immeuble, hauteur_étage, "#501000")
        trt.seth(0)
        for level in range(len(etages)):
            trt.seth(0)
            fenetres = etages[level][1]
            balcons = etages[level][0]
            trt.goto(-350+i*largeur_bloc, -300+(level+1)*hauteur_étage)
            etage(couleur, largeur_immeuble, hauteur_étage)
            for offset in range(3):
                trt.goto(-350+i*largeur_bloc + (offset+0.5)*(150/nbimmeubles), -300+(level+1)*hauteur_étage+30)
                match fenetres[offset]:
                    case "ronde":
                        fenetre_ronde(largeur_immeuble, "#000000")
                    case "carrée":
                        fenetre_carre(largeur_immeuble, "#000000", balcons[offset])
                    case _:
                        print("bruh")

        trt.goto(-350+i*largeur_bloc, -300+(len(etages)+1)*hauteur_étage)
        match toit:
            case "triangle":
                toit_triangulaire(largeur_immeuble)
            case "rond":
                toit_circulaire(largeur_immeuble)
            case "plat":
                toit_plat(largeur_immeuble)
    trt.mainloop()
 
creation_de_la_rue_aleatoire_mais_genre_completement_aleatoire(setup())