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
    def __init__(self, xpos:int, ypos:int, laby:Labyrinth):
        self.pos = Position(xpos, ypos)
        self.laby = laby
        self.steps = 0

    def move(self, dir):
        flag = 0
        if dir == "d":
            if self.pos.x < self.laby.xlen and self.pos.x >= 0:
                if not self.laby.labytinth[self.pos.y][self.pos.x+1]:
                    self.pos.x += 1
                else:
                    flag = 1
            else:
                flag = 1
        elif dir == "q":
            if self.pos.x <= self.laby.xlen and self.pos.x > 0:
                if not self.laby.labytinth[self.pos.y][self.pos.x-1]:
                    self.pos.x -= 1
                else:
                    flag = 1
            else:
                flag = 1
        elif dir == "z":
            if self.pos.y <= self.laby.ylen and self.pos.y > 0:
                if not self.laby.labytinth[self.pos.y-1][self.pos.x]:
                    self.pos.y -= 1
                else:
                    flag = 1
            else:
                flag = 1
        elif dir == "s":
            if self.pos.y < self.laby.ylen and self.pos.y >= 0:
                if not self.laby.labytinth[self.pos.y+1][self.pos.x]:
                    self.pos.y += 1
                else:
                    flag = 1
            else:
                flag = 1
        afficher_laby(self)
        if flag:
            print("Bloqué")


    def outside_labyrinth(self)->bool:
        if self.pos.y == 0 or self.pos.y == self.laby.ylen:
            return True
        elif self.pos.x == 0 or self.pos.x == self.laby.xlen:
            return True
        return False


def afficher_laby(player:Player):
    for i in range(player.laby.ylen + 1):
        for j in range(player.laby.xlen + 1):
            if player.pos.x == j and player.pos.y == i:
                print("x", end=" ")
            elif player.laby.labytinth[i][j]:
                print("■", end=" ")
            else:
                print("□", end=" ")
        print("", end="\n")

labyrinthe = Labyrinth([[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                        [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
                        [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
                        [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
                        [1, 0, 0, 0, 1, 0, 0, 1, 0, 1],
                        [1, 1, 1, 0, 1, 1, 0, 1, 0, 0],
                        [1, 0, 1, 0, 0, 1, 0, 1, 1, 1],
                        [1, 0, 1, 0, 1, 1, 0, 0, 0, 1],
                        [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]])

maxime = Player(1, 1, labyrinthe)

afficher_laby(maxime)

while not maxime.outside_labyrinth():
    deplacement = input("zqsd ?")
    maxime.move(deplacement)
    maxime.steps += 1

print("Bien joué, tu as gagné en " + str(maxime.steps) + " coups !")

while True:
    pass