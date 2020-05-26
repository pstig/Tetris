import pygame
from Board import Board


class Game:

    #scoring
    #gravity
    #lines complete
    #stats
    def __init__(self):
        self._board = Board()
        level = 0

    def draw(self, surface):
        self._board.draw(surface)
    def move_piece(self):
        pass
