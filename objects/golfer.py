import os
import math

import pygame as pg

from resources import Spritesheet


class Golfer(pg.sprite.Sprite):

    def __init__(self, screen, clock, club):
        """Initialize the golfer.

        :param screen: The pygame display
        :param clock: The pygame game clock
        :param club: The golfer's club
        """
        super(Golfer, self).__init__()
        self.screen = screen
        self.clock = clock
        self.size = 110, 200
        # Set the radius for detecting collisions
        self.radius = 50

        # Set the sprite images
        self.images, self.image_functions = self.get_images()
        self.image_index = 0
        self.set_image()

        # Set the rectangle, or the box where it is drawn
        self.rect = self.surf.get_rect()
        self.rect.bottom = self.screen.get_size()[1] - 60
        self.rect.right = self.screen.get_size()[0] / 2 - 50
        self.vector = [0, 0]
        self.speed = 0
        self.club = club
        # Set the animation stuff
        self.is_in_swing = False
        self.animation_frames = 5  # the frames per animation
        self.current_frame = 0

    def get_images(self):
        """Get all images defined by the spritesheet and return them.

        :return: A list pygame.Surface and index dict
        :rtype: list of pygame.Surface and dict of int: int
        """
        ss = Spritesheet(
            os.path.join(os.getcwd(), 'resources', 'golfer_sheet.png')
        )
        strip = ss.load_strip((0,0,220,400), 4)
        scaled_strip = []
        for sprite in strip:
            scaled_strip.append(
                pg.transform.scale(sprite, self.size)
            )
        return scaled_strip, {
                0: self.set_resting,
                1: self.set_mid_swing,
                2: self.set_full_swing,
                3: self.set_mid_swing,
                4: self.set_resting,
                5: self.set_followthru
            }

    def set_image(self, image_index=0):
        if image_index is not None and \
           image_index in range(0, len(self.images)):
            self.surf = self.images[image_index]

    def set_resting(self):
        self.set_image(image_index=0)
        self.club.set_resting()

    def set_mid_swing(self):
        self.set_image(image_index=1)
        self.club.set_mid_swing()

    def set_full_swing(self):
        self.set_image(image_index=2)
        self.club.set_full_swing()

    def set_followthru(self):
        self.set_image(image_index=3)
        self.club.set_followthru()

    def update_frame_dependent(self):
        """Update the sprite image every 5 frames during a swing."""
        power, speed = 0, 0
        self.current_frame += 1
        if self.current_frame >= self.animation_frames:
            self.current_frame = 0
            if self.image_index == len(self.image_functions) - 2:
                power, speed = self.club.power, 0
            if self.image_index == len(self.image_functions) - 1:
                self.is_in_swing = False
            self.image_index = (self.image_index + 1) % \
                               len(self.image_functions)
            self.image_functions[self.image_index]()
        self.club.update()
        self.display()
        return power, speed

    def update(self, pressed_keys, start_swing=False):
        """Update the golfer's location.

        :param pressed_keys: A dict of pressed keys this fram
        """
        if self.is_in_swing:
            return self.update_frame_dependent()
        if start_swing:
            self.is_in_swing = True
            self.update_frame_dependent()
            return None, None
        if pressed_keys[pg.K_UP]:
            self.set_full_swing()
            self.club.set_full_swing()
        if pressed_keys[pg.K_DOWN]:
            self.set_resting()
            self.club.set_resting()
        if pressed_keys[pg.K_LEFT]:
            self.set_followthru()
            self.club.set_followthru()
        if pressed_keys[pg.K_RIGHT]:
            self.set_mid_swing()
            self.club.set_mid_swing()
        self.club.update()
        self.display()
        return None, None

    def calcnewpos(self, rect, vector):
        (angle,z) = vector
        (dx,dy) = (z*math.cos(angle), z*math.sin(angle))
        return rect.move(dx,dy)

    @property
    def image(self):
        return self.surf

    def display(self):
        self.screen.blit(self.surf, self.rect)
