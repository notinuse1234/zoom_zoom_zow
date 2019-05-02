import os
import math

import pygame as pg


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
        self.images, self.image_indices = self.get_images()
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
        """Get all images defined by the filenames and return them.

        :return: A dict of filename: pygame.Surface and index dict
        :rtype: dict of str: pygame.Surface and dict of int: function
        """
        filenames = [
            'golfer.png', 'golfer_mid.png',
            'golfer_full.png', 'golfer_followthru.png'
        ]
        return (
            {
                filename: pg.transform.scale(
                    pg.image.load(
                        os.path.join(os.getcwd(), "resources", filename)
                    ).convert_alpha(),
                    self.size
                ) for filename in filenames 
            }, {
                0: self.set_resting,
                1: self.set_mid_swing,
                2: self.set_full_swing,
                3: self.set_mid_swing,
                4: self.set_resting,
                5: self.set_followthru
            }
        )

    def set_image(self, image_index=None, image_name='golfer.png'):
        # Set the image and set it to the defined size
        if image_index is not None and \
           image_index in range(0, len(self.image_indices)):
            self.image_indices.get(image_index)()
        elif image_name and image_name in self.images:
            self.surf = self.images.get(image_name)

    def set_resting(self):
        self.set_image(image_name="golfer.png")
        self.club.set_resting()
        #self.club.display()

    def set_mid_swing(self):
        self.set_image(image_name="golfer_mid.png")
        self.club.set_mid_swing()
        #self.club.display()

    def set_full_swing(self):
        self.set_image(image_name="golfer_full.png")
        self.club.set_full_swing()
        #self.club.display()

    def set_followthru(self):
        self.set_image(image_name="golfer_followthru.png")
        self.club.set_followthru()
        #self.club.display()

    def update_frame_dependent(self):
        """Update the sprite image every 5 frames during a swing."""
        power, speed = 0, 0
        self.current_frame += 1
        if self.current_frame >= self.animation_frames:
            self.current_frame = 0
            if self.image_index == len(self.image_indices) - 2:
                power, speed = 10, 0
            if self.image_index == len(self.image_indices) - 1:
                self.is_in_swing = False
            self.image_index = (self.image_index + 1) % \
                               len(self.image_indices)
            self.set_image(image_index=self.image_index)
        self.club.update()
        self.display()
        return power, speed

    def update(self, pressed_keys):
        """Update the golfer's location.

        :param pressed_keys: A dict of pressed keys this fram
        """
        if self.is_in_swing:
            return self.update_frame_dependent()
        if pressed_keys[pg.K_SPACE]:
            self.is_in_swing = True
            self.update_frame_dependent()
            return None, None
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
