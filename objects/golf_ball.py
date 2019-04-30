import os
import math

import pygame


class GolfBall(pygame.sprite.Sprite):

    def __init__(self, screen):
        super(GolfBall, self).__init__()
        self.size = 80, 48
        self.screen = screen
        self.surf = pygame.transform.scale(
            pygame.image.load(
                os.path.join(os.getcwd(), "resources", "golf_ball.png")
            ).convert(),
            self.size
        )
        self.rect = self.surf.get_rect()
        self.rect.bottom = self.screen.get_size()[1] - 10
        self.rect.right = self.screen.get_size()[0] / 2
        self.vector = (0, 0)
        self.speed = 5

    def update(self, pressed_keys):
        if pressed_keys[pygame.K_UP]:
            self.vector = (0, -self.speed)
        if pressed_keys[pygame.K_DOWN]:
            self.vector = (0, self.speed)
        if pressed_keys[pygame.K_LEFT]:
            self.vector = (-self.speed, 0)
        if pressed_keys[pygame.K_RIGHT]:
            self.vector = (self.speed, 0)
        #newpos = self.calcnewpos(self.rect, self.vector)
        #self.rect = newpos
        # Keep ball on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.screen.get_size()[0]:
            self.rect.right = self.screen.get_size()[0]
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > self.screen.get_size()[1]:
            self.rect.bottom = self.screen.get_size()[1]

        self.rect.move_ip(*self.vector)
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
