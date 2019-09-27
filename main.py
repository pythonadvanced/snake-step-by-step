#!/usr/bin/env python

import sys
import pygame
from pygame.locals import *


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


# on doit "initialiser" PyGame
pygame.init()

# et définir la taille de la fenêtre (400x400)
screen = pygame.display.set_mode((400, 400))

# on met le fond en noir
screen.fill(BLACK)
screen.set_at((10, 20), WHITE)
pygame.display.update()

# une façon d'écrire la boucle principale 
# taper 'q' pour quitter
while True:
    for event in pygame.event.get(KEYDOWN):
        print(f"received event {event.key}")
        if event.key == K_q: # pygame.locals.K_q
            sys.exit() # quitte le programme
