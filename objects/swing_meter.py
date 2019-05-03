import os
import math

import pygame as pg

from resources import Colors


class SwingMeter(pg.sprite.Sprite):

    def __init__(self, screen, golfer):
        """Initialize the golf club.

        :param screen: The pygame display
        :param golfer: The golf player
        """
        super(SwingMeter, self).__init__()
        self.screen = screen
        self.size = 500, 20
        # Set the rectangle, or the box where it is drawn
        self.original_bottom_loc = self.screen.get_size()[0] // 2 - 300
        self.original_right_loc = self.screen.get_size()[1] - 40
        # Objects
        self.golfer = golfer

    def update(self, pressed_keys):
        """The swing meter."""
        x = self.original_bottom_loc
        y = self.original_right_loc
        w, h = self.size
        # draw the black outline
        pg.draw.rect(
            self.screen,
            Colors.get('black'),
            (x-2, y-2, w+4, h+4)
        )
        # draw the gray box
        pg.draw.rect(
            self.screen,
            Colors.get('darkdarkgray'),
            (x, y, w, h)
        )
        if self.golfer.is_in_swing:
            pg.draw.rect(
                self.screen,
                Colors.get('water'),
                (x, y, w, h)
            )
        # draw each bar
        for i in range(x, x+w, 10):
            if i == x + w - (w / 5):
                color = Colors.get('flag')
            else:
                color = Colors.get('darkgray')
            pg.draw.rect(
                self.screen,
                color,
                (i+2, y+2, 6, h-2)
            )

