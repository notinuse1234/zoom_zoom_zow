import os

import pygame as pg

from resources import Colors


class Button():

    def __init__(self, screen, text, x, y, w, h, ic, ac, action=None):
        """Initialize the button

        :param screen: The pygame display
        :param text: The button text
        :param x: The X position of top left
        :param y: The Y position of top left
        :param w: The width of the button
        :param h: The height of the button
        :param ic: The color of button when not hovering
        :param ac: The color of button when hovering
        :param action: The action to take when clicked
        """
        super(Button, self).__init__()
        self.screen = screen
        self.x = x
        self.y = y
        self.size = w, h
        self.text = text
        self.ic = ic
        self.ac = ac
        self.action = action

    @staticmethod
    def text_objects(text, font, color=(0, 0, 0)):
        """Create a text object.

        :param text: The text of the object
        :param font: The font of the object
        :param color: The color of the text
        """
        text_surf = font.render(text, True, color)
        return text_surf, text_surf.get_rect()

    def update(self):
        """Update a buton."""
        mouse = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()
        # If the mouse is inside the button
        if self.x+self.size[0] > mouse[0] > self.x and \
           self.y+self.size[1] > mouse[1] > self.y:
            pg.draw.rect(
                self.screen,
                self.ac,
                (self.x, self.y, self.size[0], self.size[1])
            )
            # If the mouse is clicked on the button
            if click[0] == 1 and self.action:
                self.action()
        else:
            # Normal button
            pg.draw.rect(
                self.screen,
                self.ic,
                (self.x, self.y, self.size[0], self.size[1])
            )
        # The button text
        small_text = pg.font.Font(
            os.path.join('resources', 'freesansbold.ttf'),
            int(0.02 * self.screen.get_size()[0])
        )
        text_surf, text_rect = self.text_objects(
            self.text, small_text
        )
        text_rect.center = ((self.x+(self.size[0]/2)),
                            (self.y+(self.size[1]/2)))
        self.screen.blit(text_surf, text_rect)

