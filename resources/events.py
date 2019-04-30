import pygame

class Events():

    @staticmethod
    @property
    def BEGINSWING():
        return pygame.USEREVENT + 1

    @staticmethod
    @property
    def ENDSWING():
        return pygame.USEREVENT + 2

