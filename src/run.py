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

    objects = []
    ennemy = ennemies.Ennemy()
    objects.append(ennemy)
    red = players.Red()
    objects.append(red)
    blue = players.Blue()
    objects.append(blue)

    player_actions = {
            pygame.K_UP: lambda : blue.move_enable("up"),
            pygame.K_RIGHT: lambda : blue.move_enable("right"),
            pygame.K_DOWN: lambda : blue.move_enable("down"),
            pygame.K_LEFT: lambda : blue.move_enable("left"),

            pygame.K_z: lambda : red.move_enable("up"),
            pygame.K_d: lambda : red.move_enable("right"),
            pygame.K_s: lambda : red.move_enable("down"),
            pygame.K_q: lambda : red.move_enable("left"),
            }

    red_player_sprites = pygame.sprite.Group([red])
    blue_player_sprites = pygame.sprite.Group([blue])

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                elif event.key in player_actions.keys():
                    player_actions.get(event.key)()

        for o in objects:
            screen.blit(background, o.position, o.position)

        for o in objects:
            o.update()
            screen.blit(o.image, o.position)
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

