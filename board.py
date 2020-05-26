import pygame


class Board:
    def __init__(self):
        self.col_count = 10
        self.row_count = 24
        # array of rows, top to bottom
        self._tiles = [
            [0 for _ in range(self.col_count)] for _ in range(self.row_count)
        ]

    def draw(self, surface):
        surface.fill((255, 255, 255))
        pygame.draw.rect(surface, (0, 0, 255), (0, 0, 50, 50))
        self.clear_rows()

    def clear_rows(self):
        remove_count = 0
        for row in self._tiles:
            if(all(row)):
                remove_count += 1

        for _ in range(remove_count):
            self._tiles.pop()
            self._tiles.insert(0, [0 for _ in range(self.col_count)])
            
