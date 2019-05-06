import pygame as pg


class Spritesheet(object):
    def __init__(self, filename):
        self.sheet = pg.image.load(filename).convert_alpha()

    def image_at(self, rectangle, colorkey=None):
        """Load image from x,y,*rect."""
        rect = pg.Rect(rectangle)
        image = pg.Surface(rect.size, pg.SRCALPHA)
        image.fill((0,0,0,0))
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey, pg.RLEACCEL)
        return image

    def images_at(self, rects, colorkey=None):
        """Return a list of images given a list of coordinates."""
        return [self.image_at(rect, colorkey) for rect in rects]

    def load_strip(self, rect, image_count, colorkey=None):
        """Load a strip of images and return them as a list."""
        coords = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3])
                  for x in range(image_count)]
        return self.images_at(coords, colorkey)

