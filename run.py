import os
import sys
import time

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

    def display_message(self, text):
        large_text = pg.font.Font(
            'freesansbold.ttf',
            int(0.075 * self.screen.get_size()[0])
        )
        text_surf, text_rect = self.text_objects(text, large_text)
        text_rect.center = (
            self.screen.get_size()[0] / 2,
            self.screen.get_size()[1] / 4
        )
        self.screen.blit(text_surf, text_rect)
        pg.display.flip()
        time.sleep(2)
        self.game_loop()

    @staticmethod
    def text_objects(text, font, color=(0, 0, 0)):
        text_surf = font.render(text, True, color)
        return text_surf, text_surf.get_rect()

    def button(self, text, x, y, w, h, ic, ac):
        """Create a buton.

        :param text: The button text
        :param x: The X position of top left
        :param y: The Y position of top left
        :param w: The width of the button
        :param h: The height of the button
        :param ic: The color of button when not hovering
        :param ac: The color of button when hovering
        """
        mouse = pg.mouse.get_pos()
        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            pg.draw.rect(
                self.screen,
                ac,
                (x, y, w, h)
            )
        else:
            pg.draw.rect(
                self.screen,
                ic,
                (x, y, w, h)
            )
        small_text = pg.font.Font(
            'freesansbold.ttf',
            int(0.02 * self.screen.get_size()[0])
        )
        text_surf, text_rect = self.text_objects(
            text, small_text
        )
        text_rect.center = ((x+(w/2)),
                            (y+(h/2)))
        self.screen.blit(text_surf, text_rect)

    def main_menu(self):
        while self.at_menu:
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        self.at_menu = False
                if event.type == pg.QUIT:
                    self.at_menu = False
            self.screen.fill(Colors.get('heavy_rough'))
            mouse = pg.mouse.get_pos()
            large_text = pg.font.Font(
                'freesansbold.ttf',
                int(0.075 * self.screen.get_size()[0])
            )
            # Title
            text_surf, text_rect = self.text_objects(
                "zOoM ZoOm zOw", large_text, Colors.get('tee_area')
            )
            text_rect.center = (
                self.screen.get_size()[0] / 2,
                self.screen.get_size()[1] / 4
            )
            self.screen.blit(text_surf, text_rect)
            # Begin button
            begin_loc = (250, 450, 100, 50)
            self.button(
                "Begin",
                *begin_loc,
                Colors.get('darkgray'),
                Colors.get('lightgray')
            )
            # Quit button
            quit_loc = (600, 450, 100, 50)
            self.button(
                "Quit",
                *quit_loc,
                Colors.get('darkgray'),
                Colors.get('lightgray')
            )
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

