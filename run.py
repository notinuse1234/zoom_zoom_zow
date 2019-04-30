import os
import sys

import pygame

from objects import GolfBall


class App():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("zOoM ZoOm zOw")
        self.clock = pygame.time.Clock()
        self.size = width, height = 960, 640
        self.screen = pygame.display.set_mode(self.size)
        self.ball = GolfBall(self.screen)
        self.running = True
        self.colors = {
            'black': (0, 0, 0),
            'lawn': (86, 176, 0),
            'fairway': (90, 215, 85),
            'flag': (190, 80, 0),
            'green': (0, 169, 0),
            'green_fringe': (36, 168, 33),
            'green_rough': (75, 210, 70),
            'heavy_rough': (0, 99, 3),
            'light_rough': (0, 170, 3),
            'tee_area': (90, 215, 85),
            'tree': (0, 45, 3),
            'white': (255, 255, 255)
        }

    def game_loop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                if event.type == pygame.QUIT:
                    self.running = False

            pressed_keys = pygame.key.get_pressed()

            self.screen.fill(self.colors.get('green'))
            self.ball.update(pressed_keys)
            pygame.display.flip()
            self.clock.tick(30)

if __name__ == '__main__':
    app = App()
    app.game_loop()
    pygame.quit()
    sys.exit()

