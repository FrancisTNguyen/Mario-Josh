import pygame
import sys
from pygame.locals import *

import constants


def check_events(mario):
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


def check_koopa_enemy_collision(enemies, koopas):
    for koopa in koopas:
        for enemy in enemies:
            if koopa.shell_mode_moving:
                if pygame.sprite.collide_rect(enemy, koopa):
                    # if enemy.rect.left - 5 <= koopa.rect.right <= enemy.rect.left + 5:
                    enemy.died = True
                    # enemies.remove(enemy)
                    print("enemy removed")


def check_mario_enemy_collision(mario, enemies, koopas):
    for enemy in enemies:
        if pygame.sprite.collide_rect(mario, enemy):
            if enemy.rect.top - 5 <= mario.rect.bottom <= enemy.rect.top + 5:
                enemies.remove(enemy)
            elif enemy.rect.left - 5 <= mario.rect.right <= enemy.rect.left + 5:
                print("HELP")

    for koopa in koopas:
        if pygame.sprite.collide_rect(mario, koopa):
            if mario.rect.bottom > koopa.rect.top - 10:
                mario.jump()
                koopa.shell_mode = True
                print('SHELL MODE TRUE')
                # koopas.remove(koopa)

            if mario.rect.right >= koopa.rect.left and not koopa.shell_mode:
                print("mario hit")
            if mario.rect.right >= koopa.rect.left and koopa.shell_mode:
                print("mario hit")
            if mario.rect.bottom > koopa.rect.top - 5 and mario.center > koopa.x and koopa.shell_mode:
                koopa.shell_mode = False
                koopa.direction = 1
                koopa.shell_mode_moving = True
            if mario.rect.bottom > koopa.rect.top - 5 and mario.center < koopa.x and koopa.shell_mode:
                koopa.shell_mode = False
                koopa.direction = -1
                koopa.shell_mode_moving = True


def update_mario(mario, enemies, koopas):
    mario.update()
    check_mario_enemy_collision(mario=mario, enemies=enemies, koopas=koopas)
    check_koopa_enemy_collision(enemies=enemies, koopas=koopas)


def update_screen(screen, mario, enemies, koopas):
    screen.fill(constants.bg_color)
    mario.blitme()
    for enemy in enemies:
        enemy.blitme()
    for koopa in koopas:
        koopa.blitme()
    pygame.display.flip()
