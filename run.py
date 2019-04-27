import os
import sys

import pygame

pygame.init()

size = width, height = 960, 640
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load(
    os.path.join("resources", "golf_ball.png")
).convert()
ballrect = ball.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()

