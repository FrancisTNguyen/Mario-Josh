import pygame
import sys
from pygame.locals import *

import constants


def check_events(mario, goomba, koopa):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown(event=event, mario=mario)
        elif event.type == pygame.KEYUP:
            check_keyup(event=event, mario=mario)


def check_keydown(event, mario):
    """ Respond to keypresses  """
    # Movement flags set to true
    if event.key == pygame.K_RIGHT or event.key == K_d:
        mario.moving_right = True
        mario.facing_right = True
        mario.facing_left = False
    elif event.key == pygame.K_LEFT or event.key == K_a:
        mario.moving_left = True
        mario.facing_left = True
        mario.facing_right = False
    elif event.key == pygame.K_UP or event.key == K_w or event.key == pygame.K_SPACE:
        mario.is_jumping = True
        mario.jump()
    elif event.key == pygame.K_DOWN or event.key == K_s:
        # mario.crouch = True
        pass
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup(event, mario):
    """ Respond to key releases """
    if event.key == pygame.K_RIGHT or event.key == K_d:
        mario.moving_right = False
        mario.facing_right = True
    elif event.key == pygame.K_LEFT or event.key == K_a:
        mario.moving_left = False
        mario.facing_left = True
    elif event.key == pygame.K_UP or event.key == K_w or event.key == pygame.K_SPACE:
        mario.is_jumping = True
    elif event.key == pygame.K_DOWN or event.key == K_s:
        # mario.crouch = False
        pass


def check_mario_enemy_collision(mario, enemies, koopas):
    for enemy in enemies:
        if pygame.sprite.collide_rect(mario, enemy):
            if enemy.rect.top - 5 <= mario.rect.bottom <= enemy.rect.top + 5:
                enemies.remove(enemy)
            elif enemy.rect.left - 5 <= mario.rect.right <= enemy.rect.left + 5:
                print("HELP")

    for koopa in koopas:
        if pygame.sprite.collide_rect(mario, koopa):
            if koopa.rect.top - 5 <= mario.rect.bottom <= koopa.rect.top + 5:
                koopa.shell_mode = True
                print("shell mode")
                # koopas.remove(koopa)
            if mario.rect.right >= koopa.rect.left and not koopa.shell_mode:
                print("mario hit")
            elif mario.rect.right >= koopa.rect.left and koopa.shell_mode:
                koopa.shell_mode = False
                koopa.shell_mode_moving = True
                print("move shell")


def update_mario(mario, enemies, koopas):
    mario.update()
    check_mario_enemy_collision(mario=mario, enemies=enemies, koopas=koopas)


def update_screen(screen, mario, enemies, koopas):
    screen.fill(constants.bg_color)
    mario.blitme()
    for enemy in enemies:
        enemy.blitme()
    for koopa in koopas:
        koopa.blitme()
    pygame.display.flip()
