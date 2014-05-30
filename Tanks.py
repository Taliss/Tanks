import pygame
import sys

RIGHT = 360
LEFT = 180
UP = 90
DOWN = 270


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

    def __init__(self, x, y, image_string, speed):
        Base.__init__(self, x, y, image_string)
        Tanks.all_tanks.add(self)
        self.speed = speed
        self.velocity = {'horizontal':0, 'vertical': 0}
        self.width = self.rect[2]
        self.height = self.rect[3]
        self.image = pygame.image.load(image_string)
        self.left_faced = pygame.transform.rotate(self.image, LEFT)
        self.right_faced = pygame.transform.rotate(self.image, RIGHT)
        self.up_faced = pygame.transform.rotate(self.image, UP)
        self.down_faced = pygame.transform.rotate(self.image, DOWN)


class Player_Tank(Tanks):
    player_tanks = pygame.sprite.Group()

    def __init__(self, x, y, image_string, speed, controls):
        Tanks.__init__(self, x, y, image_string, speed)
        Player_Tank.player_tanks.add(self)
        self.player_controls = controls

    def motion(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        predicted_horizontal_location = self.rect.x + self.velocity['horizontal']
        predicted_vertical_location = self.rect.y + self.velocity['vertical']

        if predicted_horizontal_location < 0:
            self.velocity['horizontal'] = 0
        elif predicted_horizontal_location + self.width > SCREEN_WIDTH:
            self.velocity['horizontal'] = 0
        elif predicted_vertical_location < 0:
            self.velocity['vertical'] = 0
        elif predicted_vertical_location + self.height > SCREEN_HEIGHT:
            self.velocity['vertical'] = 0
        self.rect.x += self.velocity['horizontal']
        self.rect.y += self.velocity['vertical']
