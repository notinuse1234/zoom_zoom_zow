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
        self.size = 80, 48
        # Set the radius for detecting collisions
        self.radius = 40
        # Set the image and set it to the defined size 
        self.surf = pg.transform.scale(
            pg.image.load(
                os.path.join(os.getcwd(), "resources", "golf_ball.png")
            ).convert(),
            self.size
        )
        # Set the rectangle, or the box where it is drawn
        self.rect = self.surf.get_rect()
        self.rect.bottom = self.screen.get_size()[1] - 10
        self.rect.right = self.screen.get_size()[0] / 2
        self.vector = [0, 0]
        self.speed = 20

    def update(self, pressed_keys):
        """Update the golf ball's location.

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
