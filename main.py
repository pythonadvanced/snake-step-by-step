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
snake = [(1, 2), (2, 2), (3, 2)]

for pos in snake:
    draw_cell(*pos)
pygame.display.update()


# on améliore un peu la boucle principale
# on peut sortir avec 'q' ou avec le bouton qui ferme la fenêtre
# ça nous permet aussi de voir quand on reçoit des événements
running = True
while running:
    for event in pygame.event.get():
        print('.', end='', flush=True)
        if event.type == pygame.QUIT:
            running = False   
        elif event.type == pygame.KEYDOWN and event.key == K_q:
            running = False

# comme on ne sort plus brutalement avec exit()
# le programme continue après la boucle principale
print("\nGame over")