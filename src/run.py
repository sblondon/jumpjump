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
            pygame.K_UP: lambda : blue.move_enable("up"),
            pygame.K_RIGHT: lambda : blue.move_enable("right"),
            pygame.K_LEFT: lambda : blue.move_enable("left"),

            pygame.K_z: lambda : red.move_enable("up"),
            pygame.K_d: lambda : red.move_enable("right"),
            pygame.K_q: lambda : red.move_enable("left"),
            }

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                elif event.key in player_actions.keys():
                    player_actions.get(event.key)()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and blue.change_x < 0:
                    blue.stop()
                elif event.key == pygame.K_RIGHT and blue.change_x > 0:
                    blue.stop()
                if event.key == pygame.K_q and red.change_x < 0:
                    red.stop()
                elif event.key == pygame.K_d and red.change_x > 0:
                    red.stop()


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

