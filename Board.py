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

    def __init__(self, col_count, row_count):
        self.col_count = col_count
        self.row_count = row_count

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

    def draw(self, surface, piece, piece_location):
        surface.fill((255, 255, 255))
        for j in range(self.col_count):
            for i in range(self.row_count):
                if self._tiles[i][j] != 0:
                    self.fill_tile(surface, i, j, Board.colors[self._tiles[i][j]])

        piece_offsets = piece.get_locations()
        piece_color_idx = Board.piece_to_color_idx[piece.get_character_name()]
        for offset in piece_offsets:
            self.fill_tile(
                surface,
                piece_location[0] + offset[0],
                piece_location[1] + offset[1],
                Board.colors[piece_color_idx],
            )

    def clear_rows(self):
        remove_count = 0
        for row in self._tiles:
            if all(row):
                remove_count += 1

        for _ in range(remove_count):
            self._tiles.pop()
            self._tiles.insert(0, [0 for _ in range(self.col_count)])

    def add_piece_to_tiles(self, piece, piece_location):
        piece_offsets = piece.get_locations()
        piece_color_idx = Board.piece_to_color_idx[piece.get_character_name()]

        for offset in piece_offsets:
            self._tiles[piece_location[0] + offset[0]][
                piece_location[1] + offset[1]
            ] = piece_color_idx
