import pygame
import random

class Grid:
    def __init__(self, xsize, ysize) -> None:
        self.grid = [[False for i in range(xsize)] for j in range(ysize)]
        self.bgcol = (0, 0, 0)
        self.alivecol = (255, 255, 255)
        self.sqsize = min(windowSize) // max(xsize, ysize)


    def get_neighbor_number(self, grid, x, y):
        n = 0
        for y1 in range(-1, 2):
            for x1 in range(-1, 2):
                if grid[(y+y1)%len(grid)][(x+x1)%len(grid[0])]:
                    n += 1
        if grid[y][x]:
            n -= 1
        return n

    def toggle_square(self, x, y):
        self.grid[y][x] = not self.grid[y][x]

    def update_cell(self, buf, x, y):
        if self.get_neighbor_number(buf, x, y) > 3:
            self.grid[y][x] = False
        elif self.get_neighbor_number(buf, x, y) < 2:
            self.grid[y][x] = False
        elif self.get_neighbor_number(buf, x, y) == 2:
            self.grid[y][x] = self.grid[y][x]
        else:
            self.grid[y][x] = True

    def update_grid(self):
        buffer = self.grid
        for y in range(len(buffer)):
            for x in range(len(buffer[0])):
                self.update_cell(buffer, x, y)

    def draw(self):
        for y in range(len(self.grid)):
            for x in range(len(self.grid[0])):
                if self.grid[y][x]: pygame.draw.rect(screen, self.alivecol, (x*self.sqsize, y*self.sqsize, self.sqsize, self.sqsize))
                else: pygame.draw.rect(screen, self.bgcol, (x*self.sqsize, y*self.sqsize, self.sqsize, self.sqsize))

    def __repr__(self) -> str:
        return self.grid
    

pygame.init()

background_colour = (0, 0, 0)
windowSize = (800, 800)

screen = pygame.display.set_mode(windowSize)
screen.fill(background_colour)

pygame.display.set_caption('Window')
pygame.display.flip()

board = Grid(100, 100)

for i in range(700):
    board.toggle_square(random.randint(0, len(board.grid[0])-1), random.randint(0, len(board.grid)-1)) 

running = True

while running:
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            running = False
    
    board.update_grid()
    board.draw()

    pygame.time.delay(20)

    pygame.display.flip()