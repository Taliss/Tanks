import pygame
import sys
from Tanks import *


class Normal_Enemy_Tank(Tanks):
    normal_enemy = pygame.sprite.Group()

    def __init__(self,  x, y, image_string, speed):
        Tanks.__init__(self, x, y, image_string, speed)
        Normal_Enemy_Tank.normal_enemy.add(self)
