import os
import sys

import pygame as pg

from objects import GolfBall
from resources import Colors, Events

FPS = 30


class App():
    def __init__(self):
        pg.init()
        pg.display.set_caption("zOoM ZoOm zOw")
        self.clock = pg.time.Clock()
        self.size = width, height = 960, 640
        self.screen = pg.display.set_mode(self.size)
        self.ball = GolfBall(self.screen)
        self.running = True

    def game_loop(self):
        while self.running:
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.running = False
                if event.type == pg.QUIT:
                    self.running = False

            pressed_keys = pg.key.get_pressed()

            self.screen.fill(Colors.get('tee_area'))
            self.ball.update(pressed_keys)
            pg.display.flip()
            self.clock.tick(FPS)

if __name__ == '__main__':
    app = App()
    app.game_loop()
    pg.quit()
    sys.exit()

