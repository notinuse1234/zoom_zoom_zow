import pygame as pg

class Events():

    @staticmethod
    @property
    def BEGINSWING():
        return pg.USEREVENT + 1

    @staticmethod
    @property
    def ENDSWING():
        return pg.USEREVENT + 2

