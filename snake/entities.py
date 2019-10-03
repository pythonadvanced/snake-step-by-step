from enum import Enum
from typing import Tuple, List

from .board import Board

Position = Tuple[int, int]
Size = Tuple[int, int]
Color = Tuple[int, int, int]

WHITE: Color = (255, 255, 255)
YELLOW: Color = (255, 255, 0)
DEFAULT_SNAKE_CELLS = [(1, 1), (2, 1), (3, 1)]

class Egg:
    """L'oeuf."""

    def __init__(self, position: Position, color: Color = YELLOW):
        """
        Construit un oeuf.
        :param position: la position de l'oeuf sur le plateau
        :param color: la couleur de l'oeuf
        """
        self.position = position
        self.color = color

    def draw(self, board: Board):
        """Dessine l'oeuf sur le plateau."""
        board.draw_cell(self.position, self.color)


class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

    def delta(self):
        if self == self.UP:
            return 0, -1
        elif self == self.DOWN:
            return 0, 1
        elif self == self.LEFT:
            return -1, 0
        elif self == self.RIGHT:
            return 1, 0

class Snake:
    """"Le serpent."""

    def __init__(self,
                 cells: List[Position] = None,
                 direction: Direction = Direction.RIGHT,
                 color: Color = WHITE):
        """
        Construit un serpent.
        :param cells: la liste des positions initiales du serpent
        :param direction: la direction initiale du serpent
        :param color: la couleur du serpent
        """
        self.cells = cells if cells else DEFAULT_SNAKE_CELLS
        self._direction = direction
        self.color = color

    @property
    def head(self) -> Position:
        """:return: la position de la tête du serpent."""
        return self.cells[-1]

    @property
    def tail(self) -> List[Position]:
        """:return: la liste des positions du serpent, sauf la tête."""
        return self.cells[:-1]

    def can_eat(self, egg) -> bool:
        """:return: True si le serpent peut manger l'oeuf, False sinon."""
        return egg.position == self.head

    @property
    def bites_himself(self):
        """:return: True si le serpent se mord la queue, False sinon."""
        return any(pos == self.head for pos in self.tail)

    @property
    def direction(self) -> Direction:
        """La direction dans laquelle se déplace le serpent."""
        return self._direction

    @direction.setter
    def direction(self, direction: Direction):
        if not direction or self._directions_incompatible(self._direction, direction):
            return
        self._direction = direction

    @staticmethod
    def _directions_incompatible(dir1: Direction, dir2: Direction):
        return (dir1 == Direction.UP and dir2 == Direction.DOWN) or (
                dir1 == Direction.DOWN and dir2 == Direction.UP) or (
                       dir1 == Direction.LEFT and dir2 == Direction.RIGHT) or (
                       dir1 == Direction.RIGHT and dir2 == Direction.LEFT)

    def draw(self, board: Board):
        """Dessine le serpent sur le plateau."""
        for position in self.cells:
            board.draw_cell(position, self.color)

    def move(self, board: Board, grows: bool):
        """
        Déplace le serpent d'une case dans sa direction actuelle.
        :param board: le plateau
        :param grows: si True le serpent s'allonge d'une case.
        """
        x, y = self.head
        dx, dy = self.direction.delta()
        # MAJ de la tête
        new_head = board.wrap((x + dx, y + dy))
        self.cells.append(new_head)
        # on "coupe" la queue
        if not grows:
            self.cells.pop(0)
