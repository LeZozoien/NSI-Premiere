def afficher_laby(labyrinthe, player_x, player_y): # La fonction prend en entrée le labyrinthe à afficher, ainsi que la position du joueur

    for y in range(len(labyrinthe)): # On commence par énumérer chaque ligne
        for x in range(len(labyrinthe[0])): # Puis on énumère chaque élément (colonne) pour chaque ligne

            if player_x == x and player_y == y: # Si les coordonnées du joueur coincident avec la case qu'on vérifie, on print une croix
                print("x", end=" ")
            
            elif [y, x] == [6, 1] or [y, x] == [1, 3]:
                print("O", end=" ")

            elif labyrinthe[y][x]:  # Si la case est un mur, on affiche un carré plein
                print("■", end=" ")
            else:                   # Si la case est vide, on affiche un carré vide
                print("□", end=" ")
        
        print("", end="\n")         # On retourne à la ligne


def outside_labyrinth(posx, posy, laby)->bool: # La fonction prend la position du joueur et le labyrinthe en entrée, et retourne un booléen
        
        if posy == 0 or posy == len(laby)-1:      # Si le joueur est sur la première ou dernière ligne, il est sur le bord
            return True
        elif posx == 0 or posx == len(laby[0])-1: # Si le joueur est sur la première ou dernière colonne, il est sur le bord
            return True
        return False # Sinon, il est à l'interieur


def move(dir, player_x, player_y): # La fonction prend en entrée la direction du déplacement ainsi que la position du joueur et le labyrinthe

    x = 0
    y = 0



    if dir == "z" or dir == "s": # On identifie la direction souhaitée et on règle les variables x et y en accordance
        if dir == "z":
            y = -1
        else:
            y = 1
    else:
        if dir == "d":
            x = 1
        else:
            x = -1

    if [player_y+y, player_x+x] == [1, 3]:
        player_y = 6
        player_x = 1
    elif [player_y+y, player_x+x] == [6, 1]:
        player_y = 1
        player_x = 3
    elif not labyrinthe[player_y+y][player_x+x]: # Si la case sur laquelle le joueur veut se déplacer est vide, il s'y déplace
        player_y += y
        player_x += x

    return player_x, player_y
    

labyrinthe = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 1, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# On définit la position du joueur et on met le nombre d'étapes à 0
player_x = 1
player_y = 1
steps = 0

# On affiche le labyrinthe une première fois
print(len(labyrinthe))


while not outside_labyrinth(player_x, player_y, labyrinthe): # Tant que le joueur n'est pas sorti du labyrinthe

    afficher_laby(labyrinthe, player_x, player_y) # On affiche le labyrinthe
    deplacement = input("zqsd ?") # On demande au joueur dans quelle direction il veut se déplacer
    player_x, player_y = move(deplacement, player_x, player_y) # le joueur se déplace dans la direction choisie
    steps += 1 # On ajoute 1 au nombre d'étapes

print(f"Bien joué ! Tu as résolu le labyrinthe en {steps} coups !") # À la fin, on félicite le joueur et on lui affiche le nombre d'étapes mises pour sortir

while True:
    pass