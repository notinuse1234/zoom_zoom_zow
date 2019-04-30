import os
import sys

import pygame

from objects import GolfBall
from resources import Colors, Events

FPS = 30


class App():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("zOoM ZoOm zOw")
        self.clock = pygame.time.Clock()
        self.size = width, height = 960, 640
        self.screen = pygame.display.set_mode(self.size)
        self.ball = GolfBall(self.screen)
        self.running = True

    def game_loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                if event.type == pygame.QUIT:
                    self.running = False

            pressed_keys = pygame.key.get_pressed()

            self.screen.fill(Colors.get('tee_area'))
            self.ball.update(pressed_keys)
            pygame.display.flip()
            self.clock.tick(FPS)

if __name__ == '__main__':
    app = App()
    app.game_loop()
    pygame.quit()
    sys.exit()

