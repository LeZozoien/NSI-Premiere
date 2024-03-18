import pygame

SIZE = SIZEX, SIZEY = 500, 500
iter_max = 500

def get_value(x, y):
    alr_val = []
    n = 0
    xn, yn = x, y
    while (xn * xn + yn * yn) < 4 and n < iter_max and not ([xn, yn] in alr_val): # on teste que le carré de la distance est inférieur à 4 -> permet d'économiser un calcul de racine carrée coûteux en terme de performances
        alr_val.append([xn, yn])
        # Calcul des coordonnes de Mn
        tmp_x = xn
        tmp_y = yn
        xn = tmp_x * tmp_x - tmp_y * tmp_y + x
        yn = 2 * tmp_x * tmp_y + y
        n = n + 1
    if n == iter_max or [xn, yn] in alr_val:
        return (0, 0, 0) # On colore le pixel en noir -> code RGB : (0,0,0)
    elif (xn * xn + yn * yn) > 4:
        return ((255-(255*n/iter_max)), (255-(255*n/iter_max)), (255-(255*n/iter_max)))
    else:
        return (255, 255, 255)

grid = []

background_colour = (0, 0, 0)
windowSize = SIZE

screen = pygame.display.set_mode(windowSize)
screen.fill(background_colour)

pygame.display.set_caption('Window')
pygame.display.flip()

running = True

xpos = -0.5
ypos = 0
zoom = 100

while running:
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            running = False
        if pygame.key.get_pressed()[pygame.K_z]:
            xpos += 0.1
        if pygame.key.get_pressed()[pygame.K_q]:
            xpos -= 0.1
        if pygame.key.get_pressed()[pygame.K_d]:
            xpos += 0.1
        if pygame.key.get_pressed()[pygame.K_s]:
            ypos -= 0.1
        if pygame.key.get_pressed()[pygame.K_r]:
            zoom *= 1.1
        if pygame.key.get_pressed()[pygame.K_f]:
            zoom /= 1.1
        print(xpos, ypos, zoom)

    grid = []
    iter_max = 50

    for i in range(SIZEX):
        x = ((i-SIZEX/2)/zoom)+xpos
        colonne = []
        for j in range(SIZEY):
            y = ((j-SIZEY/2)/zoom)+ypos
            colonne.append(get_value(x, y))
        grid.append(colonne)

    for x in range(SIZEX):
        for y in range(SIZEY):
            pygame.draw.rect(screen, grid[x][y], (x, y, 1, 1))
    pygame.display.flip()
    
