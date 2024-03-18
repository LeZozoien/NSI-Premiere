import pygame
import sys as sys

class Labyrinth:
    def __init__(self, laby:list[list[bool]]):
        self.labytinth = laby
        self.xlen = len(laby[0])-1
        self.ylen = len(laby)-1

class Position:
    def __init__(self, posx:int, posy:int):
        self.x = posx
        self.y = posy

class Player:
    def __init__(self, xpos:int, ypos:int, laby:Labyrinth, screen, view_range):
        self.pos = Position(xpos, ypos)
        self.laby = laby
        self.steps = 0
        self.screen = screen
        self.laby.labytinth[self.pos.y][self.pos.x] = 2
        self.view_range = view_range
        self.pixelsizex = pygame.display.get_window_size()[0]/(self.view_range*2+1)
        self.pixelsizey = pygame.display.get_window_size()[1]/(self.view_range*2+1)
        self.see()
    

    def see(self):
        self.VisualRange = []
        for y in range(self.pos.y - self.view_range, self.pos.y + self.view_range+1):
            inVisualRangex = []
            for x in range(self.pos.x - self.view_range, self.pos.x + self.view_range+1):
                if x >= 0 and y >= 0:
                    try:
                        inVisualRangex.append(self.laby.labytinth[y][x])
                    except:
                        inVisualRangex.append(0)
                else:
                    inVisualRangex.append(0)
            self.VisualRange.append(inVisualRangex)
        self.VisualRange = Labyrinth(self.VisualRange)
        self.afficher_laby()


    def update(self):
        self.pixelsizex = pygame.display.get_window_size()[0]/(self.view_range*2+1)
        self.pixelsizey = pygame.display.get_window_size()[1]/(self.view_range*2+1)
        self.afficher_laby()


    def move(self, dir):
        flag = 0
        if dir == "d":
            if self.pos.x < self.laby.xlen and self.pos.x >= 0:
                if not self.laby.labytinth[self.pos.y][self.pos.x+1]==1:
                    self.pos.x += 1
                else:
                    flag = 1
            else:
                flag = 1
        elif dir == "q":
            if self.pos.x <= self.laby.xlen and self.pos.x > 0:
                if not self.laby.labytinth[self.pos.y][self.pos.x-1]==1:
                    self.pos.x -= 1
                else:
                    flag = 1
            else:
                flag = 1
        elif dir == "z":
            if self.pos.y <= self.laby.ylen and self.pos.y > 0:
                if not self.laby.labytinth[self.pos.y-1][self.pos.x]==1:
                    self.pos.y -= 1
                else:
                    flag = 1
            else:
                flag = 1
        elif dir == "s":
            if self.pos.y < self.laby.ylen and self.pos.y >= 0:
                if not self.laby.labytinth[self.pos.y+1][self.pos.x]==1:
                    self.pos.y += 1
                else:
                    flag = 1
            else:
                flag = 1
        self.see()
        self.afficher_laby()
        self.steps += 1
        if flag:
            print("Bloqué")
        self.laby.labytinth[self.pos.y][self.pos.x] = 2
    

    def afficher_laby(self):
        for y in range(self.VisualRange.ylen + 1):
            for x in range(self.VisualRange.xlen + 1):
                if x == self.view_range and y == self.view_range:
                    pygame.draw.rect(self.screen, (0, 255, 0), pygame.Rect(self.pixelsizex * x, self.pixelsizey * y, self.pixelsizex, self.pixelsizey))
                elif self.VisualRange.labytinth[y][x]==1:
                    pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(self.pixelsizex * x, self.pixelsizey * y, self.pixelsizex, self.pixelsizey))
                elif self.VisualRange.labytinth[y][x]==2:
                    pygame.draw.rect(self.screen, (255, 0, 0), pygame.Rect(self.pixelsizex * x, self.pixelsizey * y, self.pixelsizex, self.pixelsizey))
                else:
                    pygame.draw.rect(self.screen, (0, 0, 255), pygame.Rect(self.pixelsizex * x, self.pixelsizey * y, self.pixelsizex, self.pixelsizey))
        pygame.display.flip()
        

    def outside_labyrinth(self)->bool:
        if self.pos.y == 0 or self.pos.y == self.laby.ylen:
            return True
        elif self.pos.x == 0 or self.pos.x == self.laby.xlen:
            return True
        return False



labyrinthe = Labyrinth([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                        [1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
                        [1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1],
                        [1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 1],
                        [1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1],
                        [1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1],
                        [1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1],
                        [1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1],
                        [1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1],
                        [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1],
                        [1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
                        [1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
                        [1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 1],
                        [1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])


background_colour = (0, 0, 255)
screen = pygame.display.set_mode((498, 498))
pygame.display.set_caption('Labyrinthe')
screen.fill(background_colour)
pygame.display.flip()

louis = Player(1, 1, labyrinthe, screen, 4)
louis.afficher_laby()

running = True

while running:
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                louis.move("z")
            if event.key == pygame.K_q:
                louis.move("q")
            if event.key == pygame.K_s:
                louis.move("s")
            if event.key == pygame.K_d:
                louis.move("d")
    if louis.outside_labyrinth():
        print("Bien joué, tu as gagné en " + str(louis.steps) + " coups !")
        running = False
    louis.update()