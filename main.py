import pygame
from pygame.locals import *
from Board import Board
from Game import Game


class App:
    def __init__(self):
        self._game = Game()
        self._running = True
        self._display_surf = None
        self.size = self.width, self.height = 300, 720  # 30 * col/row

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(
            self.size, pygame.HWSURFACE | pygame.DOUBLEBUF
        )
        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        self._game.on_event(event)

    def on_loop(self):
        pass

    def on_render(self):
        self._game.game_tick()
        self._game.draw(self._display_surf)
        pygame.display.update()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        clock = pygame.time.Clock()
        if self.on_init() == False:
            self._running = False

        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
            clock.tick(60)
        self.on_cleanup()


if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
