import os
import math

import pygame as pg


class GolfBall(pg.sprite.Sprite):

    def __init__(self, screen):
        """Initialize the golf ball.

        :param screen: The pygame display
        """
        super(GolfBall, self).__init__()
        self.screen = screen
        self.size = 12, 12
        # Set the radius for detecting collisions
        self.radius = 6
        # Set the image and set it to the defined size 
        self.surf = pg.transform.scale(
            pg.image.load(
                os.path.join(os.getcwd(), "resources", "golf_ball.png")
            ).convert_alpha(),
            self.size
        )
        # Set the rectangle, or the box where it is drawn
        self.rect = self.surf.get_rect()
        self.original_bottom_loc = self.screen.get_size()[1] - 90
        self.original_right_loc = self.screen.get_size()[0] / 2 - 17.5
        self.rect.bottom = self.original_bottom_loc
        self.rect.right = self.original_right_loc
        self.vector = [0, 0]
        self.speed = 0
        self.on_ground = True

    def update(self, power=None, accuracy=None):
        """Update the golf ball's location.

        :param power: The power the golfer hit with
        :param accuracy: The accuracy the golfer hit with
        """
        if power is not None and accuracy is not None:
            if power > 0:
                self.on_ground = False
            self.vector[1] = -power
            self.vector[0] = accuracy
        # Actually move the ball on the screen
        self.rect.move_ip(*self.vector)
        # Keep ball on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.screen.get_size()[0]:
            self.rect.right = self.screen.get_size()[0]
        if self.rect.top < 0:
            self.on_ground = True
            self.rect.top = 0
        if self.rect.bottom > self.screen.get_size()[1]:
            self.rect.bottom = self.screen.get_size()[1]
        self.display()

    def tee_up(self):
        self.vector = [0, 0]
        self.on_ground = True
        self.rect.bottom = self.original_bottom_loc
        self.rect.right = self.original_right_loc

    def calcnewpos(self, rect, vector):
        (angle,z) = vector
        (dx,dy) = (z*math.cos(angle), z*math.sin(angle))
        return rect.move(dx,dy)

    @property
    def image(self):
        return self.surf

    def display(self):
        self.screen.blit(self.surf, self.rect)


class BigGolfBall(GolfBall):
    def __init__(self, screen):
        """Initialize the golf ball.

        :param screen: The pygame display
        """
        super(BigGolfBall, self).__init__(screen)
        self.size = 96, 96
        # Set the radius for detecting collisions
        self.radius = 48
        # Set the image and set it to the defined size 
        self.surf = pg.transform.scale(
            pg.image.load(
                os.path.join(os.getcwd(), "resources", "golf_ball.png")
            ).convert_alpha(),
            self.size
        )
        # Set the rectangle, or the box where it is drawn
        self.rect = self.surf.get_rect()
        self.original_bottom_loc = self.screen.get_size()[1] - 20
        self.original_right_loc = self.screen.get_size()[0] - 20
        self.rect.bottom = self.original_bottom_loc
        self.rect.right = self.original_right_loc
        self.vector = [0, 0]
        self.speed = 0

    def update(self):
        self.display()

