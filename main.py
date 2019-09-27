#!/usr/bin/env python

import sys
import pygame
from itertools import product
from random import randrange

from pygame.locals import *


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

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


def random_egg(snake):
    new_egg = randrange(BOARD_WIDTH), randrange(BOARD_HEIGHT)
    return new_egg if new_egg not in snake else random_egg(snake)


# on doit "initialiser" PyGame
pygame.init()

# et définir la taille de la fenêtre 
# qui cette fois-ci dépend des tailles
screen = pygame.display.set_mode((BOARD_WIDTH*CELL_WIDTH, BOARD_HEIGHT*CELL_HEIGHT))

clock = pygame.time.Clock()

# on met le fond en noir
snake = [(1, 2), (2, 2), (3, 2)]
egg = random_egg(snake)


def move_snake(dx, dy, keep_first):
    x, y = snake[-1]
    new_head = ( (x+dx) % BOARD_WIDTH, (y+dy) % BOARD_HEIGHT )
    allowed = True
    if len(snake) >= 2:
        if new_head == snake[-2]:
            allowed = False
    if allowed:
        # enlever la queue sauf si on vient 
        # de manger un oeuf
        if not keep_first:
            snake.pop(0)
        # check for loops
        if new_head in snake:
            print("Game over")
            sys.exit()
        # add new head
        snake.append(new_head)
    else:
        print(f"move to {new_head} is not allowed")

  
def can_eat(egg, dx, dy):
    x, y = snake[-1]
    return (x+dx, y+dy) == egg


def redraw():
    screen.fill(BLACK)
    for pos in snake:
        draw_cell(*pos)
    draw_cell(*egg, YELLOW)
    pygame.display.update()

redraw()

# on améliore un peu la boucle principale
# on peut sortir avec 'q' ou avec le bouton qui ferme la fenêtre
# ça nous permet aussi de voir quand on reçoit des événements
time_since_last_update = 0

running = True
dx, dy = 1, 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False   
        elif event.type == pygame.KEYDOWN:
            if event.key == K_q:
                running = False
            elif event.key == K_UP:
                dx, dy = (0, -1)
            elif event.key == K_RIGHT:
                dx, dy = (1, 0)
            elif event.key == K_DOWN:
                dx, dy = (0, 1)
            elif event.key == K_LEFT:
                dx, dy = (-1, 0)
            
    # grâce à l'horloge on peut accéder au temps 
    # entre deux événements, en millisecondes
    time_since_last_update += clock.tick()
    if time_since_last_update >= 200:
        time_since_last_update = 0
        eaten = can_eat(egg, dx, dy)
        move_snake(dx, dy, eaten)
        if eaten:
            egg = random_egg(snake)
    redraw()
        

# comme on ne sort plus brutalement avec exit()
# le programme continue après la boucle principale
print("\nGame over")