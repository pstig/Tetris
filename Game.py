import pygame
from Board import Board


class Game:

    #scoring
    #gravity
    #lines complete
    #stats
    #events

    def __init__(self):
        self._board = Board()
        self._tick_count = 0
        level = 0

    def draw(self, surface):
        self._board.draw(surface)

    def game_tick(self):
        self._tick_count += 1
        if (self._tick_count % 10 == 0):
            self._board.move_piece((1,0), down_tick=True)

    def on_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self._board.active_piece.rotate_right()
                if not self._board.check_piece_legal():
                    self._board.active_piece.rotate_left()
            elif event.key == pygame.K_z:
                self._board.active_piece.rotate_left()
                if not self._board.check_piece_legal():
                    self._board.active_piece.rotate_right()
