# -*- coding: utf-8 -*-

import pygame


import consts
import ennemies
import players


def start():
    pygame.init()
    pygame.key.set_repeat(10, 0)

    screen = pygame.display.set_mode(consts.WINDOW_SIZE)
    run = True
    
    background = pygame.image.load("gfx/background.png").convert()
    screen.blit(background, (0, 0))

    all_sprites = []
    ennemy = ennemies.Ennemy()
    all_sprites.append(ennemy)
    red = players.Red()
    all_sprites.append(red)
    blue = players.Blue()
    all_sprites.append(blue)

    player_actions = {
            pygame.K_UP: lambda : blue.jump(),
            pygame.K_RIGHT: lambda : blue.go_to_right(),
            pygame.K_LEFT: lambda : blue.go_to_left(),

            pygame.K_z: lambda : red.jump(),
            pygame.K_d: lambda : red.go_to_right(),
            pygame.K_q: lambda : red.go_to_left(),
            }

    player_stop_actions = {
            pygame.K_RIGHT: lambda : blue.stop_go_to_right(),
            pygame.K_LEFT: lambda : blue.stop_go_to_left(),

            pygame.K_d: lambda : red.stop_go_to_right(),
            pygame.K_q: lambda : red.stop_go_to_left(),
            }
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                elif event.key in player_actions.keys():
                    player_actions[event.key]()
            elif event.type == pygame.KEYUP:
                if event.key in player_stop_actions.keys():
                    player_stop_actions[event.key]()


        for sprite in all_sprites:
            screen.blit(background, sprite.rect, sprite.rect)

        for sprite in all_sprites:
            sprite.update()
            screen.blit(sprite.image, sprite.rect)
        pygame.display.update()

        if ennemy.touch(red):
            print "red lost 1 life"
        if ennemy.touch(blue):
            print "blue lost 1 life"

        pygame.time.delay(10)


if __name__ == '__main__':
    print "Let's play!"
    start()
    pygame.quit()

