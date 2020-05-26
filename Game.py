import pygame
import random
from Board import Board
from IPiece import IPiece
from TPiece import TPiece
from JPiece import JPiece
from LPiece import LPiece
from OPiece import OPiece
from SPiece import SPiece
from ZPiece import ZPiece


class Game:

    # scoring
    # gravity
    # lines complete
    # stats
    # events
    choices = [IPiece, JPiece, LPiece, OPiece, SPiece, ZPiece, TPiece]

    def __init__(self):
        self.R_wins_LR_tie = True
        self.R_keydown = False
        self.L_keydown = False
        self.LR_counter = 0
        self.col_count = 10
        self.row_count = 24
        self._board = Board(self.col_count, self.row_count)
        self._tick_count = 0
        self.active_piece = None
        self.active_piece_location = None
        self.set_new_piece()
        level = 0

    def draw(self, surface):
        self._board.draw(surface, self.active_piece, self.active_piece_location)

    def game_tick(self):
        self._tick_count += 1
        if self._tick_count % 10 == 0:
            self.move_piece((1, 0), down_tick=True)
        if self.R_keydown or self.L_keydown:
            self.LR_counter += 1
            if self.LR_counter % 6 == 0:
                if self.R_keydown and self.L_keydown and self.R_wins_LR_tie:
                    self.move_piece((0, 1))
                else:
                    self.move_piece((0, -1 if self.L_keydown else 1))

    def set_new_piece(self):
        self.active_piece = random.choice(Game.choices)()
        offset = self.active_piece.get_spawn_offset()
        self.active_piece_location = [-2,3]
        self.active_piece_location[0] += offset[0]
        self.active_piece_location[1] += offset[1]

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
            elif event.key == pygame.K_LEFT:
                self.R_wins_LR_tie = False
                self.L_keydown = True
                self.move_piece((0, -1), down_tick=False)
            elif event.key == pygame.K_RIGHT:
                self.R_wins_LR_tie = True
                self.R_keydown = True
                self.move_piece((0, 1), down_tick=False)
            elif event.key == pygame.K_SPACE:
                self.hard_drop()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.R_wins_LR_tie = True
                self.L_keydown = False
                self.LR_counter = 0
                if not self.R_keydown:
                    self.LR_counter = 0
            elif event.key == pygame.K_RIGHT:
                self.R_wins_LR_tie = False
                self.R_keydown = False
                if not self.L_keydown:
                    self.LR_counter = 0

    def check_piece_legal(self):
        piece_offsets = self.active_piece.get_locations()
        for offset in piece_offsets:
            filled_loc_row = self.active_piece_location[0] + offset[0]
            filled_loc_col = self.active_piece_location[1] + offset[1]
            if not 0 <= filled_loc_col < self.col_count:
                return False
            if filled_loc_row < 0:
                continue
            if not filled_loc_row < self.row_count:
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
                self.set_new_piece()
                self._board.clear_rows()
            else:
                self.active_piece_location = past_location
            return False
        return True

    def hard_drop(self):
        while self.move_piece((1, 0), down_tick=True):
            pass
