import pygame
import sys
from Tanks import *
from Enemies import *
from process import move

PLAYER1_CONTOLS = {
 "left": ord('a'),
 "right": ord('d'),
 "up": ord('w'),
 "down": ord('s')
}

PLAYER2_CONTOLS = {
 "left": ord('j'),
 "right": ord('l'),
 "up": ord('i'),
 "down": ord('k')
}


pygame.init()
SCREEN_WIDTH = 640
SCREEN_HEIGHT =480
SCREEN = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode(SCREEN)
clock = pygame.time.Clock()
FPS = 24
keys = pygame.key.get_pressed()
background = pygame.Surface(SCREEN)
tank = Player_Tank(0, 100, 'images/tank1.png', 6, PLAYER1_CONTOLS)
tank2 = Player_Tank(300, 300, 'images/tank2.png', 3, PLAYER2_CONTOLS)
# enemy1 = Normal_Enemy_Tank(500, 300, 'images/normal_enemy_tank.png', 3)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    move(tank2)
    tank2.motion(SCREEN_WIDTH, SCREEN_HEIGHT)

    move(tank)
    tank.motion(SCREEN_WIDTH, SCREEN_HEIGHT)


    screen.fill((0, 255, 168))
    Player_Tank.player_tanks.draw(screen)
    Base.all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(FPS)
