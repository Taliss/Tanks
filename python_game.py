import pygame
import sys
from Tanks import *
from process import move


pygame.init()

SCREEN = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode(SCREEN)
clock = pygame.time.Clock()


background = pygame.Surface(SCREEN)
tank = Player_Tank(0, SCREEN_HEIGHT - 60,
                   'images/tank1.png', 10, PLAYER1_CONTOLS)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill((0, 255, 168))
    move(tank)
    TOTAL_FRAMES += 1
    tank.motion(SCREEN_WIDTH, SCREEN_HEIGHT)
    Base.all_sprites.draw(screen)
    tank.shoot()
    pygame.display.flip()
    clock.tick(FPS)
