#!/usr/bin/env python

import sys
import pygame
from itertools import product

from pygame.locals import *


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# la taille du jeu en nombre de cellules
BOARD_SIZE = (10, 10)
BOARD_WIDTH, BOARD_HEIGHT = BOARD_SIZE

# la taille d'une cellule en nombre de pixels
CELL_SIZE = (20, 20)
CELL_WIDTH, CELL_HEIGHT = CELL_SIZE


def draw_cell(board_x, board_y, color=WHITE):
    screen_x, screen_y = CELL_WIDTH * board_x, CELL_HEIGHT * board_y
    for x, y in product(range(CELL_WIDTH), range(CELL_HEIGHT)):
        screen_coords = screen_x + x, screen_y + y
        screen.set_at(screen_coords, color)

# on doit "initialiser" PyGame
pygame.init()

# et définir la taille de la fenêtre 
# qui cette fois-ci dépend des tailles
screen = pygame.display.set_mode((BOARD_WIDTH*CELL_WIDTH, BOARD_HEIGHT*CELL_HEIGHT))

# on met le fond en noir
screen.fill(BLACK)
draw_cell(2, 5)
pygame.display.update()

# une façon d'écrire la boucle principale 
# taper 'q' pour quitter
while True:
    for event in pygame.event.get(KEYDOWN):
        print(f"received event {event.key}")
        if event.key == K_q: # pygame.locals.K_q
            sys.exit() # quitte le programme
