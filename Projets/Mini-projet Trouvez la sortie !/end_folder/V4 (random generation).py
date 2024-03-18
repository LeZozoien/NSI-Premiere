import random
import pygame


# Initialisation des constantes

WINDOWSIZE = (900, 900)
NBCOLONNES = NBLIGNES = 100
SIZE = (WINDOWSIZE[0])/NBCOLONNES
grid = []
stack = []


# Fonction permettant d'avoir l'index d'une cellule à partir de sa position x, y

def index(x, y):

    if x < 0 or y < 0 or x > NBCOLONNES-1 or y > NBLIGNES-1:
        return None

    return x*NBCOLONNES+y


# Fonction permettant de retirer les murs entre 2 cases du labyrinthe

def removeWalls(a, b):

    x = a.x - b.x

    if x == 1:
        a.walls[3] = False
        b.walls[1] = False
    if x == -1:
        a.walls[1] = False
        b.walls[3] = False

    y = a.y - b.y

    if y == 1:
        a.walls[0] = False
        b.walls[2] = False
    if y == -1:
        a.walls[2] = False
        b.walls[0] = False


# Classe de chaque cellule comprise dans le labyrinthe

class Cell:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.realx, self.realy = self.x*SIZE, self.y*SIZE
        self.walls = [True, True, True, True] # Top, Right, Bottom, Left
        self.visited = False
        self.highlight = False
     
    def draw(self):
        if self.visited:
            pygame.draw.rect(screen, (255, 255, 0), (self.realx+1, self.realy+1, SIZE, SIZE))
        if self.walls[0]:
            pygame.draw.line(screen, WHITE, (self.realx, self.realy), (self.realx + SIZE, self.realy))
        if self.walls[1]:
            pygame.draw.line(screen, WHITE, (self.realx + SIZE, self.realy), (self.realx + SIZE, self.realy + SIZE))
        if self.walls[2]:
            pygame.draw.line(screen, WHITE, (self.realx, self.realy + SIZE), (self.realx + SIZE, self.realy + SIZE))
        if self.walls[3]:
            pygame.draw.line(screen, WHITE, (self.realx, self.realy), (self.realx, self.realy + SIZE))
        if self.highlight:
            pygame.draw.rect(screen, YELLOW, (self.realx+1, self.realy+1, SIZE, SIZE))
    
    def checkNeighbors(self):

        neighbors = []

        try:top = grid[index(self.x-1, self.y)]
        except:pass
        try:right = grid[index(self.x, self.y-1)]
        except:pass
        try:bottom = grid[index(self.x+1, self.y)]
        except:pass
        try:left = grid[index(self.x, self.y+1)]
        except:pass

        try:
            if not top.visited:
                neighbors.append(top)
        except:pass
        try:
            if not right.visited:
                neighbors.append(right)
        except:pass
        try:
            if not bottom.visited:
                neighbors.append(bottom)
        except:pass
        try:
            if not left.visited:
                neighbors.append(left)
        except:pass


        if len(neighbors)>0:
            r = random.randint(0, len(neighbors)-1)
            return neighbors[r]
        else:
            return None


# Classe du joueur comprenant ses informations

class Player:
    def __init__(self):
        self.x = 0
        self.y = 0

    def move(self, dir):
        x = 0
        y = 0
        wall = 0
        match dir:
            case "z": 
                if self.y > 0 : y = -1; wall = 0
            case "s":
                if self.y < NBLIGNES : y = 1; wall = 2
            case "d":
                if self.x < NBCOLONNES : x = 1; wall = 1
            case "q":
                if self.x > 0 : x = -1; wall = 3


        if not grid[index(self.x, self.y)].walls[wall]:
            self.x += x
            self.y += y

            pygame.draw.rect(screen, (0, 100, 0), ((self.x-x)*SIZE + 1, (self.y-y)*SIZE + 1, SIZE-1, SIZE-1))

    def draw(self):
        pygame.draw.rect(screen, (255, 0, 0), ((self.x)*SIZE + 1, (self.y)*SIZE + 1, SIZE-1, SIZE-1))

    def end(self)->bool:
        if self.x == NBCOLONNES-1 and self.y == NBLIGNES-1:
            return True
        else:
            return False
        
    def goto(self, x, y):
        self.x, self.y = x, y


# Création de la grille

for x in range(NBCOLONNES):
    for y in range(NBLIGNES):
        cell = Cell(x, y)
        grid.append(cell)

current = grid[0]
current.visited = True


# Création de la fenêtre

pygame.init()

BACKGROUND_COLOR = (0, 0, 0)
YELLOW = (150, 150, 0)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode(WINDOWSIZE)
screen.fill(BACKGROUND_COLOR)

pygame.display.set_caption('Labyrinthe')
pygame.display.flip()

creating = True
clock = pygame.time.Clock()


# Creation du labyrinthe

while creating:

    current.highlight = 1
    
    next = current.checkNeighbors()
    if next:
        removeWalls(current, next)
        stack.append(current)
        next.visited = True
        current.highlight = 0
        current = next
    elif len(stack) != 0:
        current = stack.pop()
    else:
        for cell in grid:
            cell.draw()
        pygame.display.flip()
        creating = False


# Lancement du jeu

running = True
player = Player()

# Boucle du jeu

screen.fill(BACKGROUND_COLOR)
for cell in grid:
    cell.draw()


while running:
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                player.move("z")
            if event.key == pygame.K_s:
                player.move("s")
            if event.key == pygame.K_d:
                player.move("d")
            if event.key == pygame.K_q:
                player.move("q")
    
    
    player.draw()

    pygame.display.flip()

    if player.end():
        running = False


pygame.quit()
