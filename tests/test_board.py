from unittest import TestCase

from snake.board import Board

class TestBoard(TestCase):
    def setUp(self) -> None:
        self.board = Board(
            board_size=(20, 20),
            cell_size=(20, 20)
        )

    def test_window_size(self):
        self.assertEqual((400, 400), self.board.window_size)

    def test_cells(self):
        cells = list(self.board.cells)
        # taille
        self.assertEqual(400, len(cells))
        # cas de base
        self.assertIn((10, 10), cells)
        self.assertNotIn((30, 10), cells)

    def test_wrap(self):
        # pas de changement si on est à l'intérieur du plateau
        self.assertEqual((10, 10), self.board.wrap((10, 10)))
        # "wrapping" au bord du plateau
        self.assertEqual((1, 10), self.board.wrap((21, 10)))
