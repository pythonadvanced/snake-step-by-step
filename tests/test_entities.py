from unittest import TestCase
from unittest.mock import Mock

from snake.board import Board
from snake.entities import Egg, Snake, Direction


class TestEgg(TestCase):
    def setUp(self) -> None:
        self.egg = Egg((10, 10), (0, 0, 0))

    def test_draw(self):
        # on vérifie que l'oeuf appelle "draw_cell" à la bonne position
        board = Mock()
        self.egg.draw(board)
        board.draw_cell.assert_called_with((10, 10), (0, 0, 0))


class TestSnake(TestCase):
    def test_can_eat(self):
        snake = Snake(cells=[(2, 0)])
        # il peut manger si sa tête arrive sur l'oeuf
        egg = Egg((2, 0))
        self.assertTrue(snake.can_eat(egg))
        # pas si l'oeuf est autre part
        egg = Egg((3, 3))
        self.assertFalse(snake.can_eat(egg))

    def test_bites_himself(self):
        # cas de base
        snake = Snake(cells=[(1, 0), (2, 0), (3, 0)])
        self.assertFalse(snake.bites_himself)
        # cas où le serpent se mort la queue
        snake = Snake(cells=[(1, 0), (2, 0), (2, 1), (1, 1), (1, 0)])
        self.assertTrue(snake.bites_himself)

    def test_direction(self):
        # cas général: le serpent change de direction
        snake = Snake(direction=Direction.RIGHT)
        snake.direction = Direction.DOWN
        self.assertEqual(Direction.DOWN, snake.direction)
        # cas particulieer: le serpent ne peut pas revenir sur ses pas (!)
        snake = Snake(direction=Direction.RIGHT)
        snake.direction = Direction.LEFT  # <- non pris en compte
        self.assertEqual(Direction.RIGHT, snake.direction)

    def test_move(self):
        # mouvement simple
        board = Board((20, 20), (20, 20))
        snake = Snake(cells=[(0, 0)], direction=Direction.RIGHT)
        snake.move(board, False)
        self.assertEqual([(1, 0)], snake.cells)

        self.egg = Egg((10, 10), (0, 0, 0))

    def test_draw(self):
        snake = Snake(cells=[(0, 0)], color=(1, 2, 3))
        # on que le serpent dessine bien ses cellules avec "draw_cell"
        board = Mock()
        snake.draw(board)
        board.draw_cell.assert_called_with((0, 0), (1, 2, 3))
