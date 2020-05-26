from IPiece import IPiece
from JPiece import JPiece
from LPiece import LPiece
from OPiece import OPiece
import pygame
import random


class Board:
    piece_to_color_idx = {
        "I": 1,
        "J": 2,
        "L": 3,
        "O": 4,
        "S": 5,
        "T": 6,
        "Z": 7,
    }
    colors = [
        pygame.Color("white"),
        pygame.Color("cyan"),
        pygame.Color("darkblue"),
        pygame.Color("orange"),
        pygame.Color("yellow"),
        pygame.Color("lightgreen"),
        pygame.Color("purple"),
        pygame.Color("red"),
    ]

    def __init__(self):
        self.col_count = 10
        self.row_count = 24
        self.active_piece = JPiece()
        self.active_piece_location = [6, 6]
        # Array of rows, top to bottom
        self._tiles = [
            [0 for _ in range(self.col_count)] for _ in range(self.row_count)
        ]

    def fill_tile(self, surface, row, col, color):

        rectW = surface.get_width() / self.col_count
        rectH = surface.get_height() / self.row_count
        pygame.draw.rect(
            surface, color, (col * rectW, row * rectH, rectW, rectH),
        )

    def draw(self, surface):
        surface.fill((255, 255, 255))
        for j in range(self.col_count):
            for i in range(self.row_count):
                if self._tiles[i][j] != 0:
                    self.fill_tile(surface, j, i, Board.colors[self._tiles[i][j]])
        piece_offsets = self.active_piece.get_locations()
        piece_color_idx = Board.piece_to_color_idx[
            self.active_piece.get_character_name()
        ]
        for offset in piece_offsets:
            self.fill_tile(
                surface,
                self.active_piece_location[0] + offset[0],
                self.active_piece_location[1] + offset[1],
                Board.colors[piece_color_idx],
            )
    def check_piece_legal(self):
        piece_offsets = self.active_piece.get_locations()
        for offset in piece_offsets:
            filled_loc_row = self.active_piece_location[0] + offset[0]
            filled_loc_col = self.active_piece_location[1] + offset[1]
            if self._tiles[filled_loc_row][filled_loc_col]:
                return False
        return True

    def move_piece(self, delta):
        past_location = self.active_piece_location
        self.active_piece_location[0] += delta[0]
        self.active_piece_location[1] += delta[1]
        if not self.check_piece_legal():
            self.active_piece_location = past_location


    def clear_rows(self):
        remove_count = 0
        for row in self._tiles:
            if all(row):
                remove_count += 1

        for _ in range(remove_count):
            self._tiles.pop()
            self._tiles.insert(0, [0 for _ in range(self.col_count)])
