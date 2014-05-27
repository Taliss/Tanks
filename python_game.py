import pygame
import sys
from Tanks import *
pygame.init()
HALF_WIDTH = 640
HALF_HEIGHT = 480
HALF_SCREEN = tuple([HALF_WIDTH, HALF_HEIGHT])
screen = pygame.display.set_mode(HALF_SCREEN)
clock = pygame.time.Clock()
FPS = 24
background = pygame.Surface(HALF_SCREEN)

tank = Tanks(100, 100, 'images/tank1.png')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_d]:
        tank.motion(RIGHT)
    elif keys[pygame.K_a]:
        tank.motion(LEFT)
    elif keys[pygame.K_w]:
        tank.motion(UP)
    elif keys[pygame.K_s]:
        tank.motion(DOWN)

    screen.fill((0, 255, 168))
    Base.all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)
