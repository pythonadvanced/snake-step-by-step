from typing import Tuple

import pygame
from .game_objects import Game

Size = Tuple[int, int]

def run(board_size: Size, cell_size: Size):
    pygame.init()
    game = Game(board_size, cell_size)
    game.run()

