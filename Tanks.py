import pygame
import sys
from process import move

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
FPS = 24
TOTAL_FRAMES = 0



RIGHT = 360
LEFT = 180
UP = 90
DOWN = 270

PLAYER1_CONTOLS = {
    "left": ord('a'),
    "right": ord('d'),
    "up": ord('w'),
    "down": ord('s'),
    "shoot": ord('g')
}

PLAYER2_CONTOLS = {
    "left": ord('j'),
    "right": ord('l'),
    "up": ord('i'),
    "down": ord('k'),
    "shoot": ord('p')
}


class Base(pygame.sprite.Sprite):
    all_sprites = pygame.sprite.Group()

    def __init__(self, x, y, image_string, speed):
        pygame.sprite.Sprite.__init__(self)
        Base.all_sprites.add(self)

        self.position = {
            'left': False, 'right': True, 'up': False, 'down': False}

        self.image = pygame.image.load(image_string)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.collision = False

        self.width = self.rect[2]
        self.height = self.rect[3]

        self.speed = speed
        self.velocity = {'horizontal': 0, 'vertical': 0}

        self.left_faced = pygame.transform.rotate(self.image, LEFT)
        self.right_faced = pygame.transform.rotate(self.image, RIGHT)
        self.up_faced = pygame.transform.rotate(self.image, UP)
        self.down_faced = pygame.transform.rotate(self.image, DOWN)

    @classmethod
    def get_x_position(cls):
        return cls.rect.x

    def set_direction(self, direction):
        for key in self.position:
            if key == direction:
                self.position[key] = True
            else:
                self.position[key] = False

    def detect_bord_collision(self, SCREEN_WIDTH, SCREEN_HEIGHT):

        predicted_horizontal_location = self.rect.x + \
            self.velocity['horizontal']
        predicted_vertical_location = self.rect.y + self.velocity['vertical']
        collision = self.collision

        if predicted_horizontal_location < 0 or predicted_horizontal_location + self.width - 4 > SCREEN_WIDTH:
            collision = True
        elif predicted_vertical_location < 0 or predicted_vertical_location + self.height - 4 > SCREEN_HEIGHT:
            collision = True
        else:
            collision = False
        return collision
    
    def update(self):
        collision = self.detect_bord_collision(SCREEN_WIDTH, SCREEN_HEIGHT)
        if collision:
            self.velocity['horizontal'] = 0
            self.velocity['vertical'] = 0

    def motion(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        self.update()
        self.rect.x += self.velocity['horizontal']
        self.rect.y += self.velocity['vertical']


class Tank_Projectiles(Base):
    sprites = pygame.sprite.Group()

    def __init__(self, x, y, image_string, speed):
        Base.__init__(self, x, y, image_string, speed)
        Tank_Projectiles.sprites.add(self)

    @staticmethod
    def movement():
        for bullet in Tank_Projectiles.sprites:
            bullet.rect.x += bullet.velocity['horizontal']
            bullet.rect.y += bullet.velocity['vertical']


class Player_Tank(Base):
    sprites = pygame.sprite.Group()

    def __init__(self, x, y, image_string, speed, controls):
        Base.__init__(self, x, y, image_string, speed)
        Player_Tank.sprites.add(self)
        self.player_controls = controls

    # def spawn_bullet(self, bullet_x, bullet_y, bullet_image, bullet_speed):
    #     bullet = Tank_Projectiles(
    #         bullet_x, bullet_y, bullet_image, bullet_speed)
    #     bullet_distance = 70
    #     try:
    #         difference = abs(self.rect.x - bullet.rect.x) 
    #         if difference < bullet_distance:
    #             return
    #         else:
    #             return bullet
    #     except Exception:
    #         pass

    def distance_is_bigger_than(self, bigger_than):
        return abs(Player_Tank.get_x_position - Tank_Projectiles.get_x_position) > bigger_than

    def shoot(self):
        projectile_x_position = self.rect.x + 43
        projectile_y_position = self.rect.y + 18
        keys = pygame.key.get_pressed()

        if keys[self.player_controls['shoot']]:
            bullet = Tank_Projectiles(projectile_x_position, projectile_y_position, 'images/fire.png', 15)
            if  self.position['right']:
                bullet.velocity['horizontal'] += bullet.speed
                bullet.velocity['vertical'] = 0
            elif self.position['left']:
                bullet.velocity['horizontal'] -= bullet.speed
                bullet.velocity['vertical'] = 0
            elif self.position['up']:
                bullet.image = bullet.up_faced
                bullet.velocity['vertical'] -= bullet.speed
                bullet.velocity['horizontal'] = 0
            elif self.position['down']:
                bullet.image = bullet.down_faced
                bullet.velocity['vertical'] += bullet.speed
                bullet.velocity['horizontal'] = 0
        Tank_Projectiles.movement()
        # bullet_collides = bullet.detect_bord_collision(SCREEN_WIDTH, SCREEN_HEIGHT)    

    

    # collect()


    # pass_throught(game_object)





# class Game(pygame.sprite.Sprite):


#     @classmethod
#     def start(cls):
#         player1_not_spawned = True
#         player2_not_spawned = True
#         keys = pygame.key.get_pressed()
#         players_in_game = []
#         IN_PROGRESS = False
#         if keys[pygame.K_SPACE] and player1_not_spawned:
#             player1 = Player_Tank(0, SCREEN_HEIGHT - 60, 'images/tank1.png', 10, PLAYER1_CONTOLS)
#             players_in_game.append(player1)
#             IN_PROGRESS = True
#             player1_not_spawned = False
#         elif keys[pygame.K_p] and player2_not_spawned:
#             player2 = Player_Tank(0, 0, 'images/tank2.png', 5, PLAYER2_CONTOLS)
#             players_in_game.append(player2)
#             IN_PROGRESS = True
#             player2_not_spawned = False

#         if IN_PROGRESS:
#             for player in players_in_game:
#                 move(player)
#                 player.motion(SCREEN_WIDTH, SCREEN_HEIGHT)
