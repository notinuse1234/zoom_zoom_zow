import os
import math

import pygame as pg


class Golfer(pg.sprite.Sprite):

    def __init__(self, screen, club):
        """Initialize the golfer.

        :param screen: The pygame display
        :param club: The golfer's club
        """
        super(Golfer, self).__init__()
        self.screen = screen
        self.size = 110, 200
        # Set the radius for detecting collisions
        self.radius = 50
        self.set_resting()
        # Set the rectangle, or the box where it is drawn
        self.rect = self.surf.get_rect()
        self.rect.bottom = self.screen.get_size()[1] - 20
        self.rect.right = self.screen.get_size()[0] / 2 - 75
        self.vector = [0, 0]
        self.speed = 0
        self.club = club

    def set_image(self, image_name):
        # Set the image and set it to the defined size
        self.surf = pg.transform.scale(
            pg.image.load(
                os.path.join(os.getcwd(), "resources", image_name)
            ).convert_alpha(),
            self.size
        )

    def set_resting(self):
        self.set_image("golfer.png")

    def set_mid_swing(self):
        self.set_image("golfer_mid.png")

    def set_full_swing(self):
        self.set_image("golfer_full.png")

    def set_followthru(self):
        self.set_image("golfer_followthru.png")

    def update(self, pressed_keys):
        """Update the golfer's location.

        :param pressed_keys: A dict of pressed keys this fram
        """
        self.vector = [0, 0]
        if pressed_keys[pg.K_UP]:
            self.vector[1] = -self.speed
            self.set_full_swing()
            self.club.set_full_swing()
        if pressed_keys[pg.K_DOWN]:
            self.vector[1] = self.speed
            self.set_resting()
            self.club.set_resting()
        if pressed_keys[pg.K_LEFT]:
            self.vector[0] = -self.speed
            self.set_followthru()
            self.club.set_followthru()
        if pressed_keys[pg.K_RIGHT]:
            self.vector[0] = self.speed
            self.set_mid_swing()
            self.club.set_mid_swing()
        # Actually move the ball on the screen
        self.rect.move_ip(*self.vector)
        # Keep ball on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.screen.get_size()[0]:
            self.rect.right = self.screen.get_size()[0]
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > self.screen.get_size()[1]:
            self.rect.bottom = self.screen.get_size()[1]
        self.display()

    def calcnewpos(self, rect, vector):
        (angle,z) = vector
        (dx,dy) = (z*math.cos(angle), z*math.sin(angle))
        return rect.move(dx,dy)

    @property
    def image(self):
        return self.surf

    def display(self):
        self.screen.blit(self.surf, self.rect)
