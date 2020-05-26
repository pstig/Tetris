import pygame
import random


class Board:
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
        # array of rows, top to bottom
        self._tiles = [
            [random.randint(0, 7) for _ in range(self.col_count)]
            for _ in range(self.row_count)
        ]

    def draw(self, surface):
        surface.fill((255, 255, 255))
        rectW = surface.get_width() / self.col_count
        rectH = surface.get_height() / self.row_count
        for j in range(self.col_count):
            for i in range(self.row_count):
                if self._tiles[i][j] != 0:
                    pygame.draw.rect(
                        surface,
                        Board.colors[self._tiles[i][j]],
                        (j * rectW, i * rectH, rectW, rectH),
                    )

    def clear_rows(self):
        remove_count = 0
        for row in self._tiles:
            if all(row):
                remove_count += 1

        for _ in range(remove_count):
            self._tiles.pop()
            self._tiles.insert(0, [0 for _ in range(self.col_count)])
