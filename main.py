import pygame

import constants
import game_functions as gf
from enemies import Goomba
from Koopa import RegularKoopa
from mario import LittleMario, SuperMario


def main():
    pygame.init()
    screen = pygame.display.set_mode((constants.WINDOW_WIDTH, constants.WINDOW_HEIGHT))
    screen.fill(constants.bg_color)
    pygame.display.set_caption("Super Mario Bros")
    mario = LittleMario(screen=screen)
    super_mario = SuperMario(screen=screen)
    goomba = Goomba(screen=screen)
    koopa = RegularKoopa(screen=screen)
    enemies = [goomba]
    koopas = [koopa]

    while True:
        gf.check_events(mario=mario)
        gf.update_mario(mario=mario, enemies=enemies, koopas=koopas)
        goomba.update()
        koopa.update()
        gf.update_screen(screen=screen, mario=mario, enemies=enemies, koopas=koopas)


if __name__ == "__main__":
    main()
