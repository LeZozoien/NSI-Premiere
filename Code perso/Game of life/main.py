grid = [[False for i in range(10)] for j in range(10)]

def get_neighbor_number(grid, x, y):
    n = 0
    for y1 in range(-1, 2):
        for x1 in range(-1, 2):
            if grid[(y+y1)%len(grid)][(x+x1)%len(grid[0])]:
                n += 1
    if grid[y][x]:
        n -= 1
    return n

def toggle_square(x, y):
    grid[y][x] = not grid[y][x]

def update_cell(buf, x, y):
    if get_neighbor_number(buf , x, y) > 3:
        grid[y][x] = False
    elif get_neighbor_number(buf , x, y) < 2:
        grid[y][x] = False
    elif get_neighbor_number(buf , x, y) == 2:
        grid[y][x] = grid[y][x]
    else:
        grid[y][x] = True

def update_grid(grid):
    buffer = grid
    for y in range(len(buffer)):
        for x in range(len(buffer[0])):
            update_cell(buffer, x, y)
    show(grid)

def show(grid):
    print("┌", end="")
    for x in range(len(grid[0])-1):
        print("───┬", end="")
    print("───┐")

    for y in range(len(grid)-1):
        for x in range(len(grid[0])):
            if grid[y][x]: print("│ X ", end="")
            else: print("│   ", end="")
        print("│")
        print("├", end="")
        for x in range(len(grid[0])-1):
            print("───┼",end="")
        print("───┤")
    for x in range(len(grid[0])):
        if grid[len(grid)-1][x]: print("│ X ", end="")
        else: print("│   ", end="")
    print("│")
    print("└", end="")
    for x in range(len(grid[0])-1):
        print("───┴",end="")
    print("───┘")
