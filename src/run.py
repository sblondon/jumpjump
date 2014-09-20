# -*- coding: utf-8 -*-

import pygame


import players

WINDOW_SIZE = 640, 480


class Enneny(object):

    def __init__(self, y=250):
        self.image = pygame.image.load("gfx/ennemy.png").convert_alpha()
        self.speed = [2, 2]
        self.position = self.get_rect().move(y, 150)


    def get_rect(self):
        return self.image.get_rect()

    def move(self):
        self.position = self.position.move(self.speed)
        if self.position.left < 0 or self.position.right > WINDOW_SIZE[0]:
            self.speed[0] = -self.speed[0]
        if self.position.top < 0 or self.position.bottom > WINDOW_SIZE[1]:
            self.speed[1] = -self.speed[1]

    def should_move(self):
        return True



def start():
    pygame.init()
    pygame.key.set_repeat(10, 0)

    width, height = WINDOW_SIZE
    
    screen = pygame.display.set_mode(WINDOW_SIZE)
    run = True
    
    background = pygame.image.load("gfx/background.png").convert()
    screen.blit(background, (0, 0))

    objects = []
    ennemy = Enneny()
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
            if o.should_move():
                o.move()
            screen.blit(o.image, o.position)
        pygame.display.update()

        pygame.time.delay(10)


if __name__ == '__main__':
    print "Let's play!"
    start()
    pygame.quit()

