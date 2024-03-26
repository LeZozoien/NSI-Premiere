from random import randint

cases = [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],]

begin_case = (randint(0, 3), randint(0, 3))

cases[begin_case[0]][begin_case[1]] = 2

def move(dir, grid):
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
                        if grid[y][x] == grid[y-1][x]:
                            grid[y][x], grid[y-1][x] = 0, grid[y-1][x]*2
                        elif grid[y-1][x] == 0:
                            grid[y][x], grid[y-1][x] = 0, grid[y][x]
        case 1:
            for i in range(3):
                for y in range(4):
                    for x in range(0, 3):
                        if grid[y][x] == grid[y][x+1]:
                            grid[y][x], grid[y][x+1] = 0, grid[y][x+1]*2
                        elif grid[y][x+1] == 0:
                            grid[y][x], grid[y][x+1] = 0, grid[y][x]
        case 2:
            for i in range(3):
                for x in range(4):
                    for y in range(0, 3):
                        if grid[y][x] == grid[y+1][x]:
                            grid[y][x], grid[y+1][x] = 0, grid[y+1][x]*2
                        elif grid[y+1][x] == 0:
                            grid[y][x], grid[y+1][x] = 0, grid[y][x]
        case 3:
            for i in range(3):
                for y in range(4):
                    for x in range(3, 0, -1):
                        if grid[y][x] == grid[y][x-1]:
                            grid[y][x], grid[y][x-1] = 0, grid[y][x-1]*2
                        elif grid[y][x-1] == 0:
                            grid[y][x], grid[y][x-1] = 0, grid[y][x]
    return grid

def show_grid(grid):
    for line in grid:
        print(line)

def is_full(grid)->bool:
    for line in grid:
        for value in line:
            if value == 0:
                return False
    return True
    
def add_value(grid):
    found = False
    while not found:
        case_random = (randint(0, 3), randint(0, 3))
        if grid[case_random[0]][case_random[1]] == 0:
            found = True
            grid[case_random[0]][case_random[1]] = 2
    return grid

while not is_full(cases):
    show_grid(cases)
    cases = move(int(input("dir")), cases)
    cases = add_value(cases)
show_grid(cases)