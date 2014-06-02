import pygame
import sys


def move(player):
    keys = pygame.key.get_pressed()
    
    if keys[player.player_controls['left']]:
        player.image = player.left_faced
        player.set_direction('left')
        player.velocity['horizontal'] = -player.speed
        player.velocity['vertical'] = 0
    elif keys[player.player_controls['right']]:
        player.image = player.right_faced
        player.position['right'] = True
        player.set_direction('right')
        player.velocity['horizontal'] = player.speed
        player.velocity['vertical'] = 0
    elif keys[player.player_controls['down']]:
        player.image = player.down_faced
        player.set_direction('down')
        player.velocity['vertical'] = player.speed
        player.velocity['horizontal'] = 0
    elif keys[player.player_controls['up']]:
        player.set_direction('up')
        player.image = player.up_faced
        player.velocity['vertical'] = - player.speed
        player.velocity['horizontal'] = 0
    else:
        player.velocity['vertical'] = 0
        player.velocity['horizontal'] = 0