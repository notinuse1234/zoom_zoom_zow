import os
import math

import pygame as pg

from resources import Colors


class SwingMeter():

    def __init__(self, screen, golfer):
        """Initialize the golf club.

        :param screen: The pygame display
        :param golfer: The golf player
        """
        super(SwingMeter, self).__init__()
        self.screen = screen
        self.size = 500, 20
        # Set the rectangle, or the box where it is drawn
        self.x = self.screen.get_size()[0] // 2 - 300
        self.y = self.screen.get_size()[1] - 40
        # Objects
        self.golfer = golfer
        # Booleans
        self.in_swing = False
        self.in_backswing = False
        self.in_followthru = False
        # Integers
        self.power = 0
        self.accuracy = 0
        self.perfect_power = self.x
        self.perfect_accuracy = self.x + self.size[0] - (self.size[0] / 5)

    def update(self, pressed_keys):
        """The swing meter."""
        w, h = self.size
        # draw the black outline
        pg.draw.rect(
            self.screen,
            Colors.get('black'),
            (self.x-2, self.y-2, w+4, h+4)
        )
        # draw the gray box
        pg.draw.rect(
            self.screen,
            Colors.get('darkdarkgray'),
            (self.x, self.y, w, h)
        )
        if self.golfer.is_in_swing:
            pg.draw.rect(
                self.screen,
                Colors.get('water'),
                (self.x, self.y, w, h)
            )
        # draw each bar
        for i in range(self.x, self.x+w, 10):
            if i == self.perfect_accuracy:
                color = Colors.get('flag')
            else:
                color = Colors.get('darkgray')
            pg.draw.rect(
                self.screen,
                color,
                (i+2, self.y+2, 6, h-2)
            )

