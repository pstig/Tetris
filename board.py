import pygame


class Board:
    def __init__(self):
        self.col_count = 10
        self.row_count = 24
        self._tiles = [
            [0 for _ in range(self.col_count)] for _ in range(self.row_count)
        ]

    def draw(self, surface):
        surface.fill((255, 255, 255))
        pygame.draw.rect(surface, (0, 0, 255), (0, 0, 50, 50))
