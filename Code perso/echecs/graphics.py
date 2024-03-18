import pygame
from Outdated import *

P = pygame.image.load("Pieces/tile000.png")

def draw_board(screen:pygame.Surface):
    for y in range(8):
        for x in range(8):
            if (x+y)%2 == 0:
                pygame.draw.rect(screen, WHITE, (x*SQ_SIZE, y*SQ_SIZE, SQ_SIZE, SQ_SIZE))
            else:
                pygame.draw.rect(screen, BLACK, (x*SQ_SIZE, y*SQ_SIZE, SQ_SIZE, SQ_SIZE))
    for y in range(8):
        for x in range(8):
            determine_piece(board, 56-y*8+x)
            screen.blit()
pygame.init()

BGCOLOR = (100, 100, 100)
WHITE = (200, 200, 200)
BLACK = (0, 0, 0)

WINDOWSIZE = WIDTH, HEIGHT = (500, 500)
HALFW, HALFH = WIDTH/2, HEIGHT/2
SQ_SIZE = WIDTH / 8

screen = pygame.display.set_mode(WINDOWSIZE)
pygame.display.set_caption("Echecs")

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BGCOLOR)

    draw_board(screen)
    pygame.display.flip()