import os

import pygame


class GolfBall():

    def __init__(self, screen):
        self._sprite = pygame.image.load(
            os.path.join(os.getcwd(), "resources", "golf_ball.png")
        ).convert()
        self._sprite_rect = self._sprite.get_rect()
        self.screen = screen

    @property
    def sprite(self):
        return self._sprite

    def display(self):
        self.screen.blit(self._sprite, self._sprite_rect)
