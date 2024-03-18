import pygame
import sys

# Initialisation de pygame
pygame.init()

# Définition des couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
SILVER = (192, 192, 192)
YELLOW = (255, 255, 0)

niveau = input("Souhaitez-vous n1, n2, n3 ?")[1]
programme = 0
taille = 0

tpr1 = 470
tpr23 = 800 
ex1 = 10
ex2 = 20
ex3 = 100

records = []
try:
    with open("best_score", 'r') as file:
        records = file.read().split()
except:
    with open("best_score", 'w+') as file:
        records = [0, 0, 0]
        file.write("0\n0\n0")

print(records)

match niveau:
    case "1":
        programme = ex1
        taille = tpr1

    case "2":
        programme = ex2
        taille = tpr23

    case "3":
        programme = ex3
        taille = tpr23

# Définition de la taille de la fenêtre et du labyrinthe
width, height = taille, taille
square_size = width//programme
WINDOW_SIZE = (width, height)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Infernal")

# Fonction pour dessiner le quadrillage
def draw_grid():
    for x in range(0, width, square_size):
        pygame.draw.line(screen, SILVER, (x, 0), (x, height))
    for y in range(0, height, square_size):
        pygame.draw.line(screen, SILVER, (0, y), (width, y))

def deplacement_possible()->bool:
    if y > 2 and L[y - 3][x] != 1:
        return True
    if y < len(L) - 3 and L[y + 3][x] != 1:
        return True
    if x > 2 and L[y][x - 3] != 1:
        return True
    if x < len(L[0]) - 3 and L[y][x + 3] != 1:
        return True
    if y < len(L) - 2 and x < len(L) - 2 and L[y + 2][x + 2] != 1:
        return True
    if y < len(L) - 2 and x > 1 and L[y + 2][x - 2] != 1:
        return True
    if y > 1 and x > 1 and L[y - 2][x - 2] != 1:
        return True
    if y > 1 and x < len(L) - 2 and L[y - 2][x + 2] != 1:
        return True
    print("Perdu ! Aucun mouvement possible", score, "cases fermées") 
    return False
# Création du labyrinthe
L = [[0 for _ in range(programme)]for _ in range(programme)]
# Position initiale du joueur
x, y = 0, 0
score = 0
# Boucle principale
running = True
while running:
    if not deplacement_possible(): 
        running = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_z:
                if y > 2 and L[y - 3][x] != 1:
                    L[y][x] = 1
                    score = score + 1
                    y -= 3
                    print("Le nombre de tours !", score)
                    
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                if y < len(L) - 3 and L[y + 3][x] != 1:
                    L[y][x] = 1
                    score = score + 1 
                    y += 3
                    print("Le nombre de tours !", score)

            elif event.key == pygame.K_LEFT or event.key == pygame.K_q:
                if x > 2 and L[y][x - 3] != 1:
                    L[y][x] = 1
                    score = score + 1
                    x -= 3
                    print("Le nombre de tours !", score)

            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                if x < len(L[0]) - 3 and L[y][x + 3] != 1:
                    L[y][x] = 1
                    score = score + 1
                    x += 3
                    print("Le nombre de tours !", score)

            elif event.key == pygame.K_x:
                if y < len(L) - 2 and x < len(L) - 2 and L[y + 2][x + 2] != 1:
                    L[y][x] = 1
                    score = score + 1
                    x += 2 
                    y += 2
                    print("Le nombre de tours !", score)

            elif event.key == pygame.K_w:
                if y < len(L) - 2 and x > 1 and L[y + 2][x - 2] != 1:
                    L[y][x] = 1
                    score = score + 1
                    x -= 2
                    y += 2
                    print("Le nombre de tours !", score)

            elif event.key == pygame.K_a:
                if y > 1 and x > 1 and L[y - 2][x - 2] != 1:
                    L[y][x] = 1
                    score = score + 1
                    x -= 2
                    y -= 2
                    print("Le nombre de tours !", score)

            elif event.key == pygame.K_e:
                if y > 1 and x < len(L) - 2 and L[y - 2][x + 2] != 1:
                    L[y][x] = 1
                    score = score + 1
                    x += 2
                    y -= 2
                    print("Le nombre de tours !", score)

# Option de quitter ! 
            elif event.key == pygame.K_c:
                pygame.quit()
                sys.exit()

    # Effacer l'écran
    screen.fill(WHITE)

    # Dessiner le quadrillage
    draw_grid()

    # Afficher le labyrinthe
    for i in range(len(L)):
        for j in range(len(L[i])):
            if L[i][j] == 1:
                pygame.draw.rect(screen, BLACK, (j * square_size, i * square_size, square_size, square_size))

    # Afficher le joueur comme un carré bleu
    pygame.draw.rect(screen, BLUE, (x * square_size, y * square_size, square_size, square_size))

    # Rafraîchir l'écran
    pygame.display.flip()

# Sauvegarder si meilleur score

if score > int(records[int(niveau)-1]):
    records[int(niveau)-1] = score

# Convertir records en string

for x, value in enumerate(records):
    records[x] = str(value)

# Remplacer le fichier
with open("best_score", 'w') as file:
    for i in records:
        file.write(i+'\n')

# Quitter pygame
pygame.quit()
sys.exit()