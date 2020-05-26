import pygame
import random
from Board import Board
from IPiece import IPiece
from JPiece import JPiece
from LPiece import LPiece
from OPiece import OPiece


class Game:

    # scoring
    # gravity
    # lines complete
    # stats
    # events
    choices = [IPiece, JPiece, LPiece, OPiece]

    def __init__(self):
        self.col_count = 10
        self.row_count = 24
        self._board = Board(self.col_count, self.row_count)
        self._tick_count = 0
        self.active_piece = JPiece()
        self.active_piece_location = [6, 6]
        level = 0

    def draw(self, surface):
        self._board.draw(surface, self.active_piece, self.active_piece_location)

    def game_tick(self):
        self._tick_count += 1
        if self._tick_count % 10 == 0:
            self.move_piece((1, 0), down_tick=True)

    def set_new_piece(self):
        self.active_piece = random.choice(Game.choices)()

    def on_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.active_piece.rotate_right()
                if not self.check_piece_legal():
                    self.active_piece.rotate_left()
            elif event.key == pygame.K_z:
                self.active_piece.rotate_left()
                if not self.check_piece_legal():
                    self.active_piece.rotate_right()

    def check_piece_legal(self):
        piece_offsets = self.active_piece.get_locations()
        for offset in piece_offsets:
            filled_loc_row = self.active_piece_location[0] + offset[0]
            filled_loc_col = self.active_piece_location[1] + offset[1]
            if not 0 <= filled_loc_col < self.col_count:

                return False
            if not 0 <= filled_loc_row < self.row_count:
                return False
            if self._board._tiles[filled_loc_row][filled_loc_col]:
                return False
        return True

    def move_piece(self, delta, down_tick=False):
        past_location = self.active_piece_location[:]
        self.active_piece_location[0] += delta[0]
        self.active_piece_location[1] += delta[1]
        if not self.check_piece_legal():
            if down_tick:
                self._board.add_piece_to_tiles(self.active_piece, past_location)
                self.active_piece_location = [6, 6]
                self.set_new_piece()
            else:
                self.active_piece_location = past_location
