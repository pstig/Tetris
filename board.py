import pygame
import random


class Board:
    def __init__(self):
        self.col_count = 10
        self.row_count = 24
        # array of rows, top to bottom
        self._tiles = [
            [random.randint(0, 1) for _ in range(self.col_count)]
            for _ in range(self.row_count)
        ]

    def draw(self, surface):
        surface.fill((255, 255, 255))
        rectW = surface.get_width() / self.col_count
        rectH = surface.get_height() / self.row_count
        for j in range(self.col_count):
            for i in range(self.row_count):
                if self._tiles[i][j] == 1:
                    pygame.draw.rect(
                        surface, (0, 0, 255), (j * rectW, i * rectH, rectW, rectH)
                    )

    def clear_rows(self):
        remove_count = 0
        for row in self._tiles:
            if(all(row)):
                remove_count += 1

        for _ in range(remove_count):
            self._tiles.pop()
            self._tiles.insert(0, [0 for _ in range(self.col_count)])
            
