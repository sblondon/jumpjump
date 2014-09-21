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
            pygame.K_UP: {
                "start_action": blue.jump,
                "stop_action": lambda: None,
                },
            pygame.K_RIGHT: {
                "start_action": blue.go_to_right,
                "stop_action": blue.stop_go_to_right,
                },
            pygame.K_LEFT: {
                "start_action": blue.go_to_left,
                "stop_action": blue.stop_go_to_left,
                },
            pygame.K_z: {
                "start_action": red.jump,
                "stop_action": lambda: None,
                },
            pygame.K_d: {
                "start_action": red.go_to_right,
                "stop_action": red.stop_go_to_right,
                },
            pygame.K_q: {
                "start_action": red.go_to_left,
                "stop_action": red.stop_go_to_left,
                }
            }

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                elif event.key in player_actions.keys():
                    player_actions[event.key]["start_action"]()
            elif event.type == pygame.KEYUP:
                if event.key in player_actions.keys():
                    player_actions[event.key]["stop_action"]()


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

