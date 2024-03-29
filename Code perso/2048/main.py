from random import randint
import pygame

cases = [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],]

COLORS = {
    0:(0, 0, 0),
    2:(0, 0, 127),
    4:(0, 0, 255),
    8:(0, 127, 0),
    16:(0, 127, 127),
    32:(0, 127, 255),
    64:(0, 255, 0),
    128:(0, 255, 127),
    256:(0, 255, 255),
    512:(255, 0, 0),
    1024:(255, 0, 127),
    2048:(255, 0, 255),
    4096:(255, 127, 0),
    8192:(255, 127, 127),
    16384:(255, 127, 255),
    32768:(255, 255, 0),
    65536:(255, 255, 127),
    131072:(255, 255, 255),
}

begin_case = (randint(0, 3), randint(0, 3))

cases[begin_case[0]][begin_case[1]] = 2

def move(dir, grid):
    temp = grid
    """Dir -->\n
    0 = up\n
    1 = right\n
    2 = down\n
    3 = left"""
    match dir:
        case 0:
            for i in range(3):
                for x in range(4):
                    for y in range(3, 0, -1):
                        if temp[y][x] == temp[y-1][x]:
                            temp[y][x], temp[y-1][x] = 0, temp[y-1][x]*2
                        elif temp[y-1][x] == 0:
                            temp[y][x], temp[y-1][x] = 0, temp[y][x]
        case 1:
            for i in range(3):
                for y in range(4):
                    for x in range(0, 3):
                        if temp[y][x] == temp[y][x+1]:
                            temp[y][x], temp[y][x+1] = 0, temp[y][x+1]*2
                        elif temp[y][x+1] == 0:
                            temp[y][x], temp[y][x+1] = 0, temp[y][x]
        case 2:
            for i in range(3):
                for x in range(4):
                    for y in range(0, 3):
                        if temp[y][x] == temp[y+1][x]:
                            temp[y][x], temp[y+1][x] = 0, temp[y+1][x]*2
                        elif temp[y+1][x] == 0:
                            temp[y][x], temp[y+1][x] = 0, temp[y][x]
        case 3:
            for i in range(3):
                for y in range(4):
                    for x in range(3, 0, -1):
                        if temp[y][x] == temp[y][x-1]:
                            temp[y][x], temp[y][x-1] = 0, temp[y][x-1]*2
                        elif temp[y][x-1] == 0:
                            temp[y][x], temp[y][x-1] = 0, temp[y][x]
    return temp

def show_grid(grid):
    for line in grid:
        print(line)

def is_full(grid)->bool:
    last_grid = []
    for line in grid:
        last_grid_line = []
        for value in line:
            last_grid_line.append(value)
        last_grid.append(last_grid_line)
    
    if (move(0, last_grid) == cases) and (move(2, last_grid) == cases) and (move(1, last_grid) == cases) and (move(3, last_grid) == cases):
        return True
    return False
    
def add_value(grid):
    found = False
    while not found:
        case_random = (randint(0, 3), randint(0, 3))
        if grid[case_random[0]][case_random[1]] == 0:
            found = True
            grid[case_random[0]][case_random[1]] = 2
    return grid

def draw_game(arg):
    screen.fill((0, 0, 0))
    for x in range(4):
        for y in range(4):
            cellColor = COLORS[arg[y][x]]
            pygame.draw.rect(screen, cellColor, ((x*cellSize[0], y*cellSize[1]), cellSize))


pygame.init()

background_colour = (0, 0, 0)
windowSize = (400, 400)
halfSize = (200, 200)
cellSize = (windowSize[0]//4, windowSize[1]//4)

screen = pygame.display.set_mode(windowSize)
screen.fill(background_colour)

pygame.display.set_caption('Window')
pygame.display.flip()


running = True

while running:
    old_pos = []
    for line in cases:
        old_pos_line = []
        for value in line:
            old_pos_line.append(value)
        old_pos.append(old_pos_line)
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                if not move(2, old_pos) == cases:
                    cases = move(2, cases)
                    cases = add_value(cases)
            if event.key == pygame.K_UP:
                if not move(0, old_pos) == cases:
                    cases = move(0, cases)
                    cases = add_value(cases)
            if event.key == pygame.K_LEFT:
                if not move(3, old_pos) == cases:
                    cases = move(3, cases)
                    cases = add_value(cases)
            if event.key == pygame.K_RIGHT:
                if not move(1, old_pos) == cases:
                    cases = move(1, cases)
                    cases = add_value(cases)
    if is_full(cases): running = False
    # show_grid(cases)
    draw_game(cases)
    pygame.display.flip()

show_grid(cases)
score = 0
for line in cases:
    for value in line:score += value
print(score)