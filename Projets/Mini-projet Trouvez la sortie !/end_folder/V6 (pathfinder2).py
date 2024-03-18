import pygame
import random

labyrinth = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
            [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
            [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1],
            [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1],
            [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
            [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1],
            [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1],
            [1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1],
            [1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1],
            [1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
            [1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1],
            [1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1],
            [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
            ]

windowSize = (900, 900)
nbcolonnes = nblignes = len(labyrinth)

size = (windowSize[0])/nbcolonnes
grid = []
stack = []
openset = []
closedset = []
path = []


def heuristic(a, b):
    dx = abs(a.x-b.x)
    dy = abs(a.y-b.y)
    dh = max(dx, dy)-min(dx, dy)
    dd = (2*(min(dx, dy)**2))**0.5
    return dh+dd

class Spot:
    def __init__(self, i, j, w):
        self.x, self.y = i, j
        self.realx, self.realy = self.x*size, self.y*size
        self.f = 0
        self.g = 0
        self.h = 0
        self.neighbors = []
        self.previous = None
        self.wall = w
    
    def show(self, color):
        if self.wall:
            pygame.draw.rect(screen, (0, 0, 0), (self.realx, self.realy, size, size))
        else:
            pygame.draw.rect(screen, color, (self.realx, self.realy, size, size))

    def add_neighbours(self):
        
        self.neighbors = []
        if self.x > 0:
            self.neighbors.append(grid[self.x-1][self.y])
        if self.y > 0:
            self.neighbors.append(grid[self.x][self.y-1])
        if self.x < nbcolonnes-1:
            self.neighbors.append(grid[self.x+1][self.y])
        if self.y < nblignes-1:
            self.neighbors.append(grid[self.x][self.y+1])
        if self.x > 0 and self.y > 0:
            self.neighbors.append(grid[self.x-1][self.y-1])
        if self.x > 0 and self.y < nblignes-1:
            self.neighbors.append(grid[self.x-1][self.y+1])
        if self.x < nbcolonnes-1 and self.y > 0:
            self.neighbors.append(grid[self.x+1][self.y-1])
        if self.x < nbcolonnes-1 and self.y < nblignes-1:
            self.neighbors.append(grid[self.x+1][self.y+1])
    


pygame.init()

background_colour = (0, 0, 0)

screen = pygame.display.set_mode(windowSize)
screen.fill(background_colour)
clock = pygame.time.Clock()

pygame.display.set_caption('Window')
pygame.display.flip()


for x in range(nbcolonnes):
    line = []
    for y in range(nblignes):
        spot = Spot(x, y, labyrinth[x][y])
        line.append(spot)
    grid.append(line)

for x in range(nbcolonnes):
    for y in range(nblignes):
        grid[x][y].add_neighbours()

start = grid[1][1]
end = grid[nbcolonnes-2][nblignes-2]

openset.append(start)


running = True
found = False
end.wall = 0
start.wall = 0

while running:
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            running = False

    for x in range(nbcolonnes):
        for y in range(nblignes):
            grid[x][y].show((255, 255, 255))


    if len(openset) > 0 and found == False:

        lowestIndex = 0

        for x in range(len(openset)):
            if openset[x].f < openset[lowestIndex].f:
                lowestIndex = x
            openset[x].show((0, 255, 0))

        current = openset[lowestIndex]

        if current == end:
            print("fini")
            found = True

        closedset.append(current)
        openset.remove(current)

        neighbors = current.neighbors

        for n in neighbors:
            newpath = False
            if n in closedset:
                continue
            elif not n in openset and not n.wall:
                newpath = True
                openset.append(n)
                if n.g > current.g+1:
                    n.g = current.g+1
            elif not n.wall:
                if n.g > current.g+1:
                    newpath = True
                    n.g = current.g+1

            if (newpath):
                n.h = heuristic(n, end)
                n.f = n.h+n.g
                n.previous = current

            path = []
            temp = current
            path.append(current)
            while temp.previous != None:
                path.append(temp.previous)
                temp = temp.previous
    

    if len(closedset) > 0:
        for x in range(len(closedset)):
            closedset[x].show((255, 0, 0))

    if len(path) > 0:
        for x in range(len(path)):
            path[x].show((0, 0, 255))

    pygame.display.flip()
    clock.tick(8)