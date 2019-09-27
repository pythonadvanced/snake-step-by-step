import sys
import pygame
from pygame.locals import *

# on doit "initialiser" PyGame
pygame.init()

# et définir la taille de la fenêtre (400x400)
screen = pygame.display.set_mode((400, 400))

# une façon d'écrire la boucle principale 
# taper 'q' pour quitter

while True:
    for event in pygame.event.get(KEYDOWN):
        print(f"received event {event.key}")
        if event.key == K_q: # pygame.locals.K_q
            sys.exit() # quitte le programme
