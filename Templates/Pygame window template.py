import pygame

pygame.init()

background_colour = (0, 0, 0)
windowSize = (1920, 1080)

screen = pygame.display.set_mode(windowSize)
screen.fill(background_colour)

pygame.display.set_caption('Window')
pygame.display.flip()

running = True

while running:
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            running = False