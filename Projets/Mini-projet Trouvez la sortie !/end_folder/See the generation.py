import random
import pygame

windowSize = (900, 900)
nbcolonnes = nblignes = 75
size = (windowSize[0])/nbcolonnes
grid = []
stack = []

def index(x, y):

    if x < 0 or y < 0 or x > nbcolonnes-1 or y > nblignes-1:
        return None

    return x*nbcolonnes+y


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


class Cell:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.realx, self.realy = self.x*size, self.y*size
        self.walls = [True, True, True, True] # Top, Right, Bottom, Left
        self.visited = False
        self.highlight = False
     
    def draw(self):
        if self.visited:
            pygame.draw.rect(screen, (100, 0, 0), (self.realx+1, self.realy+1, size, size))
        if self.walls[0]:
            pygame.draw.line(screen, (255, 255, 255), (self.realx, self.realy), (self.realx + size, self.realy))
        if self.walls[1]:
            pygame.draw.line(screen, (255, 255, 255), (self.realx + size, self.realy), (self.realx + size, self.realy + size))
        if self.walls[2]:
            pygame.draw.line(screen, (255, 255, 255), (self.realx, self.realy + size), (self.realx + size, self.realy + size))
        if self.walls[3]:
            pygame.draw.line(screen, (255, 255, 255), (self.realx, self.realy), (self.realx, self.realy + size))
        if self.highlight:
            pygame.draw.rect(screen, (0, 100, 0), (self.realx+1, self.realy+1, size, size))   

    
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
                if self.y < nblignes : y = 1; wall = 2
            case "d":
                if self.x < nbcolonnes : x = 1; wall = 1
            case "q":
                if self.x > 0 : x = -1; wall = 3


        if not grid[index(self.x, self.y)].walls[wall]:
            self.x += x
            self.y += y

    def draw(self):
        pygame.draw.rect(screen, (100, 100, 100), ((self.x)*size + 1, (self.y)*size + 1, size-1, size-1))

    def end(self)->bool:
        if self.x == nbcolonnes-1 and self.y == nblignes-1:
            return True
        else:
            return False


# Création de la grille

for x in range(nbcolonnes):
    for y in range(nblignes):
        cell = Cell(x, y)
        grid.append(cell)

current = grid[0]
current.visited = True



# Fenêtre

pygame.init()

background_colour = (0, 0, 0)

screen = pygame.display.set_mode(windowSize)
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
        for cell in grid:
            cell.draw()
        pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            creating = False