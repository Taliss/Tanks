import pygame
import sys

RIGHT = 0
LEFT = 180
UP = 90
DOWN = -90


class Base(pygame.sprite.Sprite):
    all_sprites = pygame.sprite.Group()

    def __init__(self, x, y, image_string):
        pygame.sprite.Sprite.__init__(self)
        Base.all_sprites.add(self)
        self.image = pygame.image.load(image_string)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Tanks(Base):
    all_tanks = pygame.sprite.Group()

    def __init__(self, x, y, image_string):
        Base.__init__(self, x, y, image_string)
        Tanks.all_tanks.add(self)
        self.velocity = [0, 0]
        self.left_faced = pygame.transform.rotate(self.image, LEFT)
        self.right_faced = pygame.transform.rotate(self.image, RIGHT)
        self.up_faced = pygame.transform.rotate(self.image, UP)
        self.down_faced = pygame.transform.rotate(self.image, DOWN)

    def motion(self, direction):
        if direction == LEFT:
            self.image = self.left_faced
            self.velocity[0] = -3
            self.velocity[1] = 0
        elif direction == RIGHT:
            self.image = self.right_faced
            self.velocity[0] = 3
            self.velocity[1] = 0
        elif direction == UP:
            self.image = self.up_faced
            self.velocity[0] = 0
            self.velocity[1] = -3
        elif direction == DOWN:
            self.image = self.down_faced
            self.velocity[0] = 0
            self.velocity[1] = 3
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
