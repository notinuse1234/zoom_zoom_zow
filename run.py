import os
import sys

import pygame as pg

from objects import GolfBall
from resources import Colors, Events

FPS = 30
SCREEN_WIDTH = 960
SCREEN_HEIGHT = 640

class App():
    def __init__(self):
        pg.init()
        pg.display.set_caption("zOoM ZoOm zOw")
        self.clock = pg.time.Clock()
        self.size = SCREEN_WIDTH, SCREEN_HEIGHT
        self.screen = pg.display.set_mode(self.size)
        self.ball = GolfBall(self.screen)
        self.at_menu = True
        self.running = False

    @staticmethod
    def text_objects(text, font):
        text_surf = font.render(text, True, Colors.get('tee_area'))
        return text_surf, text_surf.get_rect()

    def main_menu(self):
        while self.at_menu:
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.at_menu = False
                if event.type == pg.QUIT:
                    self.at_menu = False
            self.screen.fill(Colors.get('heavy_rough'))
            large_text = pg.font.Font(
                'freesansbold.ttf',
                int(0.075 * self.screen.get_size()[0])
            )
            text_surf, text_rect = self.text_objects(
                "zOoM ZoOm zOw", large_text
            )
            text_rect.center = (
                self.screen.get_size()[0] / 2,
                self.screen.get_size()[1] / 4
            )
            self.screen.blit(text_surf, text_rect)
            pg.display.flip()
            self.clock.tick(FPS/5)

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
    app.main_menu()
    pg.quit()
    sys.exit()

