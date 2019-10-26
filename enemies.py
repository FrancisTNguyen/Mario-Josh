import pygame
from pygame.sprite import Sprite
from Spritesheet import SpriteSheet
from timer import Timer


class Enemy(Sprite):
    def __init__(self, screen, walk_list, death_list):
        super(Enemy, self).__init__()

        # get screen dimensions
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        # list to hold animation images
        self.walk_list = walk_list
        self.death_list = death_list

        # Timer class to animate sprites
        self.animation = Timer(frames=self.walk_list)
        self.animation = Timer(frames=self.death_list)

        # get the rect of the image
        self.image = self.animation.imagerect()
        self.death_image = self.animation.imagerect()
        self.rect = self.image.get_rect()
        self.rect = self.death_image.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # store objects exact position
        self.x = float(self.rect.centerx)

        # movement flags
        self.moving_left = False
        self.moving_right = False
        self.direction = 1

        # death flag
        self.died = False

    def blitme(self):
        if self.died:
            self.screen.blit(pygame.transform.flip(self.death_image, False, True), self.rect)
        if not self.died:
            self.screen.blit(self.image, self.rect)

    def update(self):
        self.x += (0.5 * self.direction)
        self.rect.x = self.x
        # self.image = self.walk_list[self.animation.frame_index()]

        if not self.died:
            self.image = self.walk_list[self.animation.frame_index()]
            print("walking image")
            if self.rect.right >= self.screen_rect.centerx + 150:
                self.direction *= -1
            elif self.rect.left <= self.screen_rect.centerx - 150:
                self.direction *= -1

        if self.died:
            self.direction = 0
            self.death_image = self.death_list[self.animation.frame_index()]
            print("flipped static")


class Goomba(Enemy):
    def __init__(self, screen):
        sprite_sheet = SpriteSheet("images/enemies.png")
        self.goombas = []
        self.goombas_died = []
        image = pygame.transform.scale(sprite_sheet.get_image(0, 4, 16, 16), (32, 32))
        self.goombas.append(image)
        image = pygame.transform.scale(sprite_sheet.get_image(30, 4, 16, 16), (32, 32))
        self.goombas.append(image)
        death_image = pygame.transform.scale(sprite_sheet.get_image(0, 4, 16, 16), (32, 32))
        self.goombas_died.append(death_image)
        # next image for squished goomba
        """image = pygame.transform.scale(sprite_sheet.get_image(60, 5, 16, 16), (30, 30))
        self.goombas.append(image)"""
        super().__init__(screen=screen, walk_list=self.goombas, death_list=self.goombas_died)
