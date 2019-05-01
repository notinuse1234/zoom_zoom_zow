import os
import math

import pygame as pg


class GolfClub(pg.sprite.Sprite):

    def __init__(self, screen):
        """Initialize the golf club.

        :param screen: The pygame display
        """
        super(GolfClub, self).__init__()
        self.screen = screen
        self.size = 100, 100
        # Set the radius for detecting collisions
        self.radius = 50
        # Set the rectangle, or the box where it is drawn
        self.original_bottom_loc = self.screen.get_size()[1] - 20
        self.original_right_loc = self.screen.get_size()[0] / 2 - 30
        self.vector = [0, 0]
        self.speed = 0
        self.set_resting()

    def set_image(self, image_name):
        # Set the image and set it to the defined size 
        self.surf = pg.transform.scale(
            pg.image.load(
                os.path.join(os.getcwd(), "resources", image_name)
            ).convert_alpha(),
            self.size
        )
        if not hasattr(self, 'rect'):
            self.rect = self.surf.get_rect()

    def set_resting(self):
        self.set_image("golf_club.png")
        self.rect.right = self.original_right_loc
        self.rect.bottom = self.original_bottom_loc

    def set_mid_swing(self):
        self.set_image("golf_club_mid.png")
        self.rect.right = self.original_right_loc - 100
        self.rect.bottom = self.original_bottom_loc

    def set_full_swing(self):
        self.set_image("golf_club_full.png")
        self.rect.right = self.original_right_loc - 110
        self.rect.bottom = self.original_bottom_loc - 120

    def set_followthru(self):
        self.set_image("golf_club_followthru.png")
        self.rect.right = self.original_right_loc - 110
        self.rect.bottom = self.original_bottom_loc - 120

    def update(self, pressed_keys):
        """Update the golf club's location.

        :param pressed_keys: A dict of pressed keys this fram
        """
        self.vector = [0, 0]
        if pressed_keys[pg.K_UP]:
            self.vector[1] = -self.speed
        if pressed_keys[pg.K_DOWN]:
            self.vector[1] = self.speed
        if pressed_keys[pg.K_LEFT]:
            self.vector[0] = -self.speed
        if pressed_keys[pg.K_RIGHT]:
            self.vector[0] = self.speed
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
