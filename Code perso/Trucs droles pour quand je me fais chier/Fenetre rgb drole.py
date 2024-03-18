import pygame
import math
import time

pygame.init()

background_colour = (0, 0, 0)
windowSize = (1600, 1000)

screen = pygame.display.set_mode(windowSize)
screen.fill(background_colour)

pygame.display.set_caption('Window')
pygame.display.flip()

running = True
color = 0

while running:
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            running = False

    if color == 0:
        color = 1
    else:
        color = 0

    screen.fill((255*abs(math.sin(time.time()*10))*color, 255*abs(math.sin(time.time()*10+math.pi/1.5))*color, 255*abs(math.sin(time.time()*10-math.pi/1.5))*color))
    pygame.display.flip()
    pygame.time.wait(40)
