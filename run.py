import os
import sys

import pygame

from objects import GolfBall

pygame.init()

size = width, height = 960, 640
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = GolfBall(screen, speed)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

    screen.fill(black)
    ball.update()
    ball.display()
    pygame.display.flip()

