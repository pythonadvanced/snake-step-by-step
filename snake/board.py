from itertools import product
from typing import Tuple, Iterator

import pygame

Position = Tuple[int, int]
Size = Tuple[int, int]
Color = Tuple[int, int, int]

BLACK: Color = (0, 0, 0)


class Board:
    """
    Le plateau de jeu.
    """

    def __init__(self, board_size: Size, cell_size: Size, fill_color: Color = BLACK):
        """
        Initialize le plateau.
        :param board_size: la taille du plateau de jeu, en cellules
        :param cell_size: la taille de chaque cellule, en pixels
        :param fill_color: la couleur de fond du plateau
        """
        self.board_size = board_size
        self.cell_size = cell_size
        self.fill_color = fill_color
        # on initialize la fenêtre avec le nombre total de pixels
        self.screen = pygame.display.set_mode(self.window_size)

    @property
    def window_size(self) -> Size:
        """
        :return: la taille du plateau, en pixels
        """
        width, height = self.board_size
        cell_w, cell_h = self.cell_size
        return width * cell_w, height * cell_h

    @property
    def cells(self) -> Iterator[Position]:
        """
        :return: un itérateur retournant toutes les cellules du plateau
        """
        width, height = self.board_size
        return product(range(width), range(height))

    def clear(self):
        """Efface le plateau."""
        self.screen.fill(self.fill_color)

    def draw_cell(self, board_pos: Position, color: Color):
        """
        Remplit une cellule du plateau avec une color donnée.
        :param board_pos: la position de la cellule
        :param color: la couleur de fond
        """
        for screen_pos in self._pixels_for(board_pos):
            self.screen.set_at(screen_pos, color)

    def wrap(self, position: Position) -> Position:
        """
        Adapte une position donnée aux limites du plateau
        :param position:
        """
        x, y = position
        width, height = self.board_size
        return x % width, y % height

    def _pixels_for(self, board_pos: Position) -> Iterator[Position]:
        """
        Retourne un iterable de toutes les positions de tous les pixels de la cellule.
        """
        x, y = board_pos
        width, height = self.cell_size
        # coin en haut à gauche
        start_x, start_y = width * x, height * y
        # position relative, dans la cellule
        relative_pos = product(range(height), range(width))
        # et on retourne un générateur
        return ((start_x + col, start_y + line) for (line, col) in relative_pos)

