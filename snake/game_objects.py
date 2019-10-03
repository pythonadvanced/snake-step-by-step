from typing import Tuple, Optional

import pygame
from pygame.locals import *
from random import choice

from .board import Board
from .entities import Egg, Snake, Direction

Position = Tuple[int, int]
Size = Tuple[int, int]


class Timer:
    """
    Cette class gère le framerate tu jeu, et permet d'exécuter une action
    (déplacer le serpent) toutes les 200ms.
    """

    def __init__(self, framerate: int = 60, timer_delay_ms: int = 200):
        """
        Initialise le Timer.
        :param framerate: nombre d'images par secondes souhaité
        :param timer_delay_ms: délai entre deux expirations du timer (qui déplace le serpent)
        """
        self.framerate = framerate
        self.timer_delay_ms = timer_delay_ms
        # l'objet pygame Clock gère le framerate
        self.clock = pygame.time.Clock()
        self.time_since_last_update_ms = 0

    def tick(self):
        """Appelé à chaque frame, limite le framerate."""
        self.time_since_last_update_ms += self.clock.tick(self.framerate)

    @property
    def is_timer_expired(self) -> bool:
        """
        Vérifie l'expiration du Timer.
        :return: True si le timer a expiré, False sinon.
        """
        if self.time_since_last_update_ms > self.timer_delay_ms:
            self.time_since_last_update_ms = 0
            return True
        return False


class StopGame(Exception):
    """Exception levée si le jeu est annulé (par un appui sur Q ou en fermant la fenêtre)."""
    pass


class Game:
    """
    La classe Game encapsule la logique du jeu.
    """
    egg: Egg

    def __init__(self, board_size: Size, cell_size: Size):
        self.board = Board(board_size, cell_size)
        self.snake = Snake()
        self.timer = Timer()

        # et on place l'oeuf aléatoirement
        self.egg = Egg((0, 0))
        self.place_egg()

    def run(self):
        """
        Lance le jeu.
        Cette fonction ne retourne pas avant la fin du jeu.
        """
        try:
            self._game_loop()
        except StopGame:
            return None

    def _game_loop(self):
        """
        La boucle principale du jeu.
        Elle suit un schéma très classique:
          1. on détecte les actions de l'utilisateur
          2. on update l'état du jeu
          3. on dessine à l'écran
        """
        direction = None
        while not self.snake.bites_himself:
            self.timer.tick()

            # 1. détection des touches
            direction = self.poll_keys() or direction

            # 2. MAJ du state
            if self.timer.is_timer_expired:
                eats = self.snake.can_eat(self.egg)
                if direction:
                    self.snake.direction = direction
                    direction = None
                self.snake.move(self.board, eats)
                if eats:
                    self.place_egg()

            # 3. dessin, dans l'ordre du fond vers l'avant
            self.board.clear()
            self.egg.draw(self.board)
            self.snake.draw(self.board)
            pygame.display.update()

    def poll_keys(self) -> Optional[Direction]:
        """
        Détecte les touches pressées par l'utilisateur.
        :return: une Direction correspondant à la saisie utilisateur, ou None
        :raises: StopGame si l'utilisateur annule le jeu
        """
        for event in pygame.event.get():
            if event.type == QUIT:
                raise StopGame()
            elif event.type == KEYDOWN:
                if event.key == K_q:
                    raise StopGame()
                elif event.key == K_UP:
                    return Direction.UP
                elif event.key == K_DOWN:
                    return Direction.DOWN
                elif event.key == K_LEFT:
                    return Direction.LEFT
                elif event.key == K_RIGHT:
                    return Direction.RIGHT

    def place_egg(self):
        """Place l'oeuf à une position aléatoire"""
        position = self._find_empty_position()
        self.egg = Egg(position)

    def _find_empty_position(self):
        available_cells = [pos for pos in self.board.cells if pos != self.egg.position and pos not in self.snake.cells]
        return choice(available_cells)
