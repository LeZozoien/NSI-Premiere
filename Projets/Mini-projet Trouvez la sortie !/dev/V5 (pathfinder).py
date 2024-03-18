import math
import random
import pygame


# Initialisation des constantes

WINDOWSIZE = (900, 900)
NBCOLONNES = NBLIGNES = 50
SIZE = (WINDOWSIZE[0])/NBCOLONNES
grid = []
stack = []
TARGET_POINT = [random.randint(1, NBCOLONNES-1), random.randint(1, NBLIGNES-1)]
open_cells = []
closed_cells = []
chemin = []


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
        self.hcost = 0
        self.gcost = 0
        self.fcost = 0
        self.parent = None
        self.path_len = 0
     
    def draw(self):
        if self.visited:
            pygame.draw.rect(screen, (0, 0, 0), (self.realx+1, self.realy+1, SIZE, SIZE))
        if self.x == TARGET_POINT[0] and self.y == TARGET_POINT[1]:
            pygame.draw.rect(screen, (0, 100, 0), (self.realx+1, self.realy+1, SIZE, SIZE))
        # if self in open_cells:
        #     pygame.draw.rect(screen, (0, 255, 0), (self.realx+1, self.realy+1, SIZE, SIZE))
        if self in closed_cells:
            pygame.draw.rect(screen, (255, 0, 0), (self.realx+1, self.realy+1, SIZE, SIZE))
        if self.highlight:
            pygame.draw.rect(screen, (255, 0, 20), (self.realx+1, self.realy+1, SIZE, SIZE))
        if self.walls[0]:
            pygame.draw.line(screen, (255, 255, 255), (self.realx, self.realy), (self.realx + SIZE, self.realy))
        if self.walls[1]:
            pygame.draw.line(screen, (255, 255, 255), (self.realx + SIZE, self.realy), (self.realx + SIZE, self.realy + SIZE))
        if self.walls[2]:
            pygame.draw.line(screen, (255, 255, 255), (self.realx, self.realy + SIZE), (self.realx + SIZE, self.realy + SIZE))
        if self.walls[3]:
            pygame.draw.line(screen, (255, 255, 255), (self.realx, self.realy), (self.realx, self.realy + SIZE))

    
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
        
    def evaluate_fcost(self):
        self.gcost = math.dist([self.x, self.y], [0, 0])
        self.hcost = math.dist([self.x, self.y], TARGET_POINT)
        self.fcost = self.gcost + self.fcost

    def neighbours(self):
        empty = Cell(0, 0)
        empty.walls = [True, True, True, True]

        neighbors = []

        try:neighbors.append(grid[index(self.x, self.y-1)])
        except:neighbors.append(empty)
        try:neighbors.append(grid[index(self.x+1, self.y)])
        except:neighbors.append(empty)
        try:neighbors.append(grid[index(self.x, self.y+1)])
        except:neighbors.append(empty)
        try:neighbors.append(grid[index(self.x-1, self.y)])
        except:neighbors.append(empty)

        return neighbors
    
    def eval_path_len(self):
        return self.parent.path_len+1
    
    def __repr__(self) -> str:
        return f"[{self.x}, {self.y}]" 

    def __str__(self) -> str:
        return f"Cellule x:{self.x}; y:{self.y}"  
    
    def draw_chemin(self):
        pygame.draw.rect(screen, (0, 128, 128), (self.realx+1, self.realy+1, SIZE-1, SIZE-1))
        

# Classe du joueur comprenant ses informations

class Pathfinder:
    def __init__(self):
        self.x = 0
        self.y = 0

    def move(self, dir):
        x = 0
        y = 0
        wall = 0
        match dir:
            case 0: 
                if self.y > 0 : y = -1; wall = 0
            case 2:
                if self.y < NBLIGNES : y = 1; wall = 2
            case 1:
                if self.x < NBCOLONNES : x = 1; wall = 1
            case 3:
                if self.x > 0 : x = -1; wall = 3


        if not grid[index(self.x, self.y)].walls[wall]:
            self.x += x
            self.y += y

            pygame.draw.rect(screen, (0, 100, 0), ((self.x-x)*SIZE + 1, (self.y-y)*SIZE + 1, SIZE-1, SIZE-1))

    def draw(self):
        pygame.draw.rect(screen, (255, 0, 0), ((self.x)*SIZE + 1, (self.y)*SIZE + 1, SIZE, SIZE))


# Création de la grille

for x in range(NBCOLONNES):
    for y in range(NBLIGNES):
        cell = Cell(x, y)
        grid.append(cell)

current = grid[0]
current.visited = True


# Création de la fenêtre

pygame.init()

background_colour = (0, 0, 0)

screen = pygame.display.set_mode(WINDOWSIZE)
screen.fill(background_colour)

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
finder = Pathfinder()

# Boucle du jeu

screen.fill(background_colour)
for cell in grid:
    cell.draw()
    cell.highlight = 0

open_cells.append(grid[index(finder.x, finder.y)])
found = 0

while running:
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            running = False

    if not found:

        current_node = open_cells[0]
        for node in open_cells:
            node.evaluate_fcost()
            if node.fcost <= current_node.fcost:
                if node.fcost < current_node.fcost or current_node.hcost > node.hcost:
                    current_node = node

        open_cells.remove(current_node)
        closed_cells.append(current_node)

        if current_node.x == TARGET_POINT[0] and current_node.y == TARGET_POINT[1]:
            found = 1
        

        for i, neighbour in enumerate(current_node.neighbours()):

            if neighbour.path_len == 0:
                neighbour.parent = current_node
                neighbour.path_len = neighbour.eval_path_len()

        max_path_len = 10000000
        for i, neighbour in enumerate(current_node.neighbours()):
        
            if neighbour in closed_cells or current_node.walls[i]:
                pass
            elif ((not(neighbour in open_cells)) or neighbour.eval_path_len()<max_path_len) and not current_node.walls[i]:
                neighbour.evaluate_fcost()
                neighbour.parent = current_node
                if not (neighbour in open_cells):
                    open_cells.append(neighbour)
                if neighbour.eval_path_len()<max_path_len:
                    max_path_len = neighbour.eval_path_len()
        
        finder.draw()

        for cell in grid:
            cell.draw()
    
    else:
        for cell in grid:
            cell.highlight = False
        for cell in range(NBCOLONNES*NBLIGNES):
            parent = grid[index(TARGET_POINT[0], TARGET_POINT[1])]
            for iter in range(cell):
                parent = parent.parent
            chemin.append(parent)
        closed_cells = []
        screen.fill(background_colour)
        for cell in chemin:
            cell.draw()
            cell.draw_chemin()
        grid[index(TARGET_POINT[0], TARGET_POINT[1])].draw()
        pygame.display.flip()
        while running:
            for event in pygame.event.get():  
                if event.type == pygame.QUIT:
                    running = False
                    exit()



    current_node.highlight = True

    pygame.display.flip()

    current_node.highlight = False