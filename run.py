import os
import sys

import pygame

from objects import GolfBall


pygame.init()
pygame.display.set_caption("zOoM ZoOm zOw")

size = width, height = 960, 640
black = 0, 0, 0

screen = pygame.display.set_mode(size)
ball = GolfBall(screen)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        if event.type == pygame.QUIT:
            running = False

    screen.fill(black)
    ball.update()
    ball.display()
    pygame.display.flip()

