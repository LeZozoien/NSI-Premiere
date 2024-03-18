import random as rm
import turtle as trt

def toit_circulaire(largeur_bat):
    pos = trt.position()
    trt.color(0, 0, 0)
    trt.goto(pos[0]+largeur_bat, pos[1])
    trt.pd()
    trt.begin_fill()
    trt.lt(90)
    trt.circle(largeur_bat//2,180)
    trt.lt(90)
    trt.end_fill()
    trt.pu()

def toit_triangulaire(largeur_bat):
    trt.color(0, 0, 0)
    pos_old = trt.position()
    hauteur_toit = max(rm.gauss(0.6, 0.3), 0.1) * largeur_bat
    trt.pd()
    trt.begin_fill()
    trt.goto(pos_old[0]+largeur_bat, pos_old[1])
    trt.goto(pos_old[0]+(largeur_bat//2), pos_old[1]+hauteur_toit)
    trt.goto(pos_old[0], pos_old[1])
    trt.end_fill()
    trt.pu()

def toit_plat(largeur_bat):
    trt.color(0, 0, 0)
    taille = trt.pensize()
    trt.pensize(10)
    pos = trt.position()
    trt.pd()
    trt.goto(pos[0]+largeur_bat, pos[1])
    trt.pu()
    trt.pensize(taille)

def etage(couleur, largeur, hauteur):
    oldcolor = trt.color()
    trt.color(couleur)
    trt.pd()
    trt.begin_fill()
    for i in range(2):
        trt.fd(largeur);trt.lt(90)
        trt.fd(hauteur);trt.lt(90)
    trt.end_fill()
    trt.pu()
    trt.color(oldcolor[0])

def fenetre_carre(largeur_bat:int,couleur:str,balcon:bool):
    trt.seth(0)
    "Dessine une fenêtre carrée en partant du coin inférieur gauche."
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

    if balcon == True :
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
    if balcon == True :
        trt.goto(old_pos)
    trt.seth(0)
        
def fenetre_ronde(largeur_bat:int,couleur:str):
    "Dessine une fenêtre ronde en partant du coin inférieur droit."
    trt.pensize(5)
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
    '''Donne un emplacement aléatoire entre 0 et 2 pour la porte'''
    emplacement_porte = rm.randint(0, 2)
    porte = rm.choice(["ronde", "carrée"])
    return emplacement_porte, porte

def etage_random():
    '''Renvoie une liste de 3 booléens pour savoir s'il y a un balcon à chacune des 3 fenêtres et le type de ces 3 fenêtres'''
    balcons = [(rm.randint(0, 1)) for i in range(3)]
    fenetres = rm.choices(["ronde", "carrée"], k=3)
    return balcons, fenetres

def toit_random():
    '''Donne un toit aléatoire entre les 3 disponibles'''
    toits = ["plat", "rond", "triangle"]
    return rm.choice(toits)

def batiment_random(hauteur:int):
    '''Utilise les 3 fonctions base_random(), etage_random() et toit_random() pour générer un batiment completement aléatoire'''
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
    NBIMMEUBLES = int(input("Combien d'immeubles ? (entre 3 et 6)(nombre entier)(teste pas plus ou moins ça marche pas)"))
    assert NBIMMEUBLES > 2 and NBIMMEUBLES < 7, "J'avais prévenu que ça marche pas"
    # nbimmeubles = rm.randint(4, 6)
    LARGEUR_BLOC = 700//NBIMMEUBLES
    LARGEUR_IMMEUBLE = LARGEUR_BLOC//1.3
    HAUTEUR_IMMEUBLE = 80
    immeubles = []
    trt.bgcolor("#aaffff")
    main()
    trt.goto(-350, -300)
    for i in range(NBIMMEUBLES):
        etages = rm.randint(1, 5)
        immeubles.append(batiment_random(etages))
    return immeubles, HAUTEUR_IMMEUBLE, LARGEUR_IMMEUBLE, LARGEUR_BLOC, NBIMMEUBLES

def creer_la_rue_aleatoire_mais_genre_completement_aleatoire_sans_faille_mais_avec_le_premier_etage_plus_grand_que_les_autres_si_tu_regardes_de_près_sinon_ça_passe(args):
    """Fonction principale du programme"""


    assert len(args)==5, "mauvais arguments d'entrée"

    immeubles, HAUTEUR_IMMEUBLE, LARGEUR_IMMEUBLE, LARGEUR_BLOC, NBIMMEUBLES = args[0], args[1], args[2], args[3], args[4]
    for i, bat in enumerate(immeubles):
        couleur = bat["couleur"]
        porte = bat["base"]
        etages = bat["etages"]
        toit = bat["toit"]
        print(porte)

        trt.goto(-350+i*LARGEUR_BLOC, -300)
        etage(couleur, LARGEUR_IMMEUBLE, HAUTEUR_IMMEUBLE)
        trt.seth(0)
        pos = trt.pos()
        pos_porte = -350+i*LARGEUR_BLOC, -300
        pos_porte = pos_porte[0] + (LARGEUR_IMMEUBLE/6) + ((2 * LARGEUR_IMMEUBLE * porte[0])/8), pos_porte[1]
        print(pos_porte)
        trt.goto(pos_porte)
        match porte[1]:
            case "carrée":
                porte_carree(LARGEUR_IMMEUBLE, HAUTEUR_IMMEUBLE, "#501000")
            case "ronde":
                porte_ronde(LARGEUR_IMMEUBLE, HAUTEUR_IMMEUBLE, "#501000")
        trt.seth(0)
        for level in range(len(etages)):
            trt.seth(0)
            fenetres = etages[level][1]
            balcons = etages[level][0]
            trt.goto(-350+i*LARGEUR_BLOC, -300+(level+1)*HAUTEUR_IMMEUBLE)
            etage(couleur, LARGEUR_IMMEUBLE, HAUTEUR_IMMEUBLE)
            for offset in range(3):
                trt.goto(-350+i*LARGEUR_BLOC + (offset+0.5)*(150/NBIMMEUBLES), -300+(level+1)*HAUTEUR_IMMEUBLE+30)
                match fenetres[offset]:
                    case "ronde":
                        fenetre_ronde(LARGEUR_IMMEUBLE, "#000000")
                    case "carrée":
                        fenetre_carre(LARGEUR_IMMEUBLE, "#000000", balcons[offset])
                    case _:
                        print("bruh")

        trt.goto(-350+i*LARGEUR_BLOC, -300+(len(etages)+1)*HAUTEUR_IMMEUBLE)
        match toit:
            case "triangle":
                toit_triangulaire(LARGEUR_IMMEUBLE)
            case "rond":
                toit_circulaire(LARGEUR_IMMEUBLE)
            case "plat":
                toit_plat(LARGEUR_IMMEUBLE)
    trt.mainloop()

if __name__ == '__main__':
    creer_la_rue_aleatoire_mais_genre_completement_aleatoire_sans_faille_mais_avec_le_premier_etage_plus_grand_que_les_autres_si_tu_regardes_de_près_sinon_ça_passe(setup())