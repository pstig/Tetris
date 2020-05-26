import pygame
class Board:
    def draw(self, surface):
        surface.fill((255,255,255))
        pygame.draw.rect(surface, (0,0,255), (0,0,50,50))
