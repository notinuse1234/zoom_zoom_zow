import os
import math

import pygame


class GolfBall(pygame.sprite.Sprite):

    def __init__(self, screen, vector):

        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image = pygame.image.load(
            os.path.join(os.getcwd(), "resources", "golf_ball.png")
        ).convert()
        self.rect = self.image.get_rect()

        self.area = screen.get_rect()
        self.vector = vector

    def update(self):
        newpos = self.calcnewpos(self.rect, self.vector)
        self.rect = newpos

    def calcnewpos(self, rect, vector):
        (angle,z) = vector
        (dx,dy) = (z*math.cos(angle), z*math.sin(angle))
        return rect.move(dx,dy)

    @property
    def sprite(self):
        return self.image

    def display(self):
        self.screen.blit(self.image, self.rect)
