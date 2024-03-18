def decale(m,dx,dy):
    """ 
    Entrée : une matrice de 0-1
    Renvoie une nouvelle matrice obtenue de la précédente en 
    décalant tous les "1" de `dx` cases vers la droite et `dy` vers le bas. 

    Lorsqu'une valeur recherchée dépasse du bord, on obtient la valeur en "bouclant" à partir du bord opposé. 
    Dit autrement: les accès à la matrice m sont effectués "modulo" la longueur correspondante.
    """
    # initialiser
    r = [[0]*len(m[0]) for i in range(len(m))]
    # ou directement r = [[0 for x in ligne] for ligne in m]
    for y in range(len(m)):
        for x in range(len(m[0])):
            r[(y+dy)%len(m)][(x+dx)%len(m[0])] = m[y][x]
            # A compléter: remplacer les ... ci dessus.
    return r

# Test:
m=[[0,1,0,0],[0,1,1,0],[0,0,0,0],[0,0,0,0]]
print(decale(m,0,1)==[[0, 0, 0, 0], [0, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 0]])

import matplotlib.pyplot as plt
plt.subplot(1,2,1)
plt.imshow(m,cmap='Greys_r')
plt.title("image d'origine")
plt.subplot(1,2,2)
plt.imshow(decale(m,0,1),cmap='Greys_r')
plt.title("image décalée dx=0, dy=1")
plt.show()


def convolution_px(m,masque,i,j):
    """
    Entrée : 
    - une matrice m de triplets, 
    - une seconde matrice 3x3 formant le masque de convolution.
    - deux indices i<len(m),j<len(m[0])
    Renvoie: la valeur lorsqu'on lui applique le produit de convolution entre les 3x3 pixels entourant (i,j) et le masque.
    Les accès à la matrice m sont effectués "modulo" dans le cas où l'on accède à un pixel hors de la matrice 

    i ordonnée
    j abscisse


    """
    som = 0

    for y in range(-1, 2):
        for x in range(-1, 2):
            som += m[(i+y)%4][(j+x)%4] * masque[1-y][1-x]
    return som
    # A compléter

# Test:
m = [[0,1,0,0],
     [0,1,1,0],
     [0,0,0,0],
     [0,0,0,0]]
masque = [[0,0,0],
          [0,0,0],
          [0,1,0]]
print(convolution_px(m,masque,0,0)==0)
print(convolution_px(m,masque,1,1)==1)
print(convolution_px(m,masque,0,1)==0)

m = [[0,1,2,3],[0,4,5,6],[0,7,8,9],[0,10,11,12]]
masque = [[1,2,3],[40,50,60],[700,800,900]]
print(convolution_px(m,masque,2,2)==13044)


def convolution(m,masque):
    """
    Entrée:
    - une matrice m
    - une seconde matrice 3x3 formant le masque de convolution.
    Renvoie une matrice, 
    dont la valeur (i,j) est le résultat obtenu en appliquant la fonction précédente à i,j.
    applique à chaque pixel l
    """
    res_mat = [[0 for i in range(len(m[0]))] for i in range(len(m))]

    for y in range(len(res_mat)):
        for x in range(len(res_mat[0])):
            res_mat[y][x] = convolution_px(m, masque, y, x)
    return res_mat


m = [[0,1,0,0],[0,1,1,0],[0,0,0,0],[0,0,0,0]]
masque = [[0,0,0],[0,0,0],[0,1,0]]
print('décalage_bas:',... ) # A compléter ici pour remplacer ... par l'image transformée.

import matplotlib.pyplot as plt
plt.subplot(1,2,1)
plt.imshow(m,cmap='Greys_r')
plt.title("image d'origine")
plt.subplot(1,2,2)
plt.imshow(convolution(m, masque),cmap='Greys_r') # A compléter: remplacer ... par l'image transformée.
plt.title("image obtenue par convolution")
plt.show()