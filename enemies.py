import pygame
from pygame.sprite import Sprite
from Spritesheet import SpriteSheet
from timer import Timer


class Enemy(Sprite):
    def __init__(self, screen, walk_list, walk_list_left, walk_list_right):
        super(Enemy, self).__init__()

        # get screen dimensions
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        # list to hold animation images
        self.walk_list = walk_list
        self.walk_list_left = walk_list_left
        self.walk_list_right = walk_list_right

        # Timer class to animate sprites
        self.animation = Timer(frames=self.walk_list)
        self.animation = Timer(frames=self.walk_list_left)
        self.animation = Timer(frames=self.walk_list_right)

        # get the rect of the image
        self.image = self.animation.imagerect()
        self.rect = self.image.get_rect()
        self.rect = self.imagesLeft.get_rect()
        self.rect = self.imagesRight.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # store objects exact position
        self.x = float(self.rect.centerx)

        # movement flags
        self.moving_left = False
        self.moving_right = False
        self.direction = 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.x += (2 * self.direction)
        self.rect.x = self.x
        self.image = self.walk_list[self.animation.frame_index()]

        if self.rect.right >= self.screen_rect.centerx + 150:
            self.direction *= -1
        elif self.rect.left <= self.screen_rect.centerx - 150:
            self.direction *= -1

    def updatekoopa(self):
        self.x += (2 * self.direction)
        self.rect.x = self.x

        if self.rect.right >= self.screen_rect.centerx + 150:
            self.direction *= -1
            self.imagesRight = self.walk_list_right[self.animation.frame_index()]
        elif self.rect.left <= self.screen_rect.centerx - 150:
            self.direction *= -1
            self.imagesLeft = self.walk_list_left[self.animation.frame_index()]


class Goomba(Enemy):
    def __init__(self, screen):
        sprite_sheet = SpriteSheet("images/enemies.png")
        self.goombas = []
        image = pygame.transform.scale(sprite_sheet.get_image(0, 4, 16, 16), (32, 32))
        self.goombas.append(image)
        image = pygame.transform.scale(sprite_sheet.get_image(30, 4, 16, 16), (32, 32))
        self.goombas.append(image)
        # next image for squished goomba
        """image = pygame.transform.scale(sprite_sheet.get_image(60, 5, 16, 16), (30, 30))
        self.goombas.append(image)"""
        super().__init__(screen=screen, walk_list=self.goombas, walk_list_left=self.goombas, walk_list_right=self.goombas)


class Koopa(Enemy):
    def __init__(self, screen):
        sprite_sheet = SpriteSheet("Images/enemies.png")
        self.koopas = []
        imagesRight = pygame.transform.scale(sprite_sheet.get_image(210, 0, 19, 25), (32, 32))
        self.koopas.append(imagesRight)
        imagesRight = pygame.transform.scale(sprite_sheet.get_image(240, 0, 19, 25), (32, 32))
        self.koopas.append(imagesRight)
        imagesLeft = pygame.transform.scale(sprite_sheet.get_image(179, 0, 19, 25), (32, 32))
        self.koopas.append(imagesLeft)
        imagesLeft = pygame.transform.scale(sprite_sheet.get_image(149, 0, 19, 25), (32, 32))
        self.koopas.append(imagesLeft)
        # next image for squished goomba
        """image = pygame.transform.scale(sprite_sheet.get_image(60, 5, 16, 16), (30, 30))
        self.goombas.append(image)"""
        super().__init__(screen=screen, walk_list=self.koopas, walk_list_right=self.koopas, walk_list_left=self.koopas)
