# -*- coding: utf-8 -*-

import pygame.sprite

import engine
import ennemies
import goals
import platforms
import players


class Level(object):
    def __init__(self):
        self.platform_sprites = pygame.sprite.Group()
        self.player_sprites = pygame.sprite.Group()
        self.ennemy_sprites = pygame.sprite.Group()
        self.goal_sprites = pygame.sprite.Group()
        self.background = None
        self.red_player = None
        self.blue_player = None
        self.goal = None

    def update(self):
        screen = pygame.display.get_surface()

        for sprite in self.player_sprites:
            screen.blit(self.background, sprite.rect, sprite.rect)

        for sprite in self.ennemy_sprites:
            screen.blit(self.background, sprite.rect, sprite.rect)

        for sprite in self.platform_sprites:
            screen.blit(self.background, sprite.rect, sprite.rect)

        for sprite in self.goal_sprites:
            screen.blit(self.background, sprite.rect, sprite.rect)

        self.player_sprites.update()
        self.player_sprites.draw(screen)

        self.ennemy_sprites.update()
        self.ennemy_sprites.draw(screen)

        self.platform_sprites.update()
        self.platform_sprites.draw(screen)

        self.goal_sprites.update()
        self.goal_sprites.draw(screen)
      
    def players_die(self):
        return pygame.sprite.groupcollide(
                self.ennemy_sprites, self.player_sprites,
                False, False,
                collided=pygame.sprite.collide_mask)
    
    def players_win(self):
        return self.goal.reached()


    def create_ennemy(self):
        ennemy = ennemies.Ennemy()
        self.ennemy_sprites.add(ennemy)
        return ennemy
    
    def create_red_player(self):
        red = players.Red()
        red.level = self
        self.player_sprites.add(red)
        self.red_player = red
        return red

    def create_blue_player(self):
        blue = players.Blue()
        blue.level = self
        self.player_sprites.add(blue)
        self.blue_player = blue
        return blue

    def create_platform(self, x, y):
        platform = platforms.Platform()
        platform.rect.x = x
        platform.rect.y = y
        self.platform_sprites.add(platform)
        return platform
       
    def create_goal(self, x, y):
        goal = goals.Goal()
        goal.level = self
        goal.rect.x = x
        goal.rect.y = y
        self.goal = goal
        self.goal_sprites.add(goal)
        return goal


def display_level_1(screen, game):
    level = Level()
    level.background = pygame.image.load("gfx/background.png").convert()

    TEXT_COLOR = (200, 0, 0)
    hearts = u"♥" * game.lives
    text = engine.build_message(hearts, TEXT_COLOR) 
    textpos = text.get_rect(
            centerx=level.background.get_width()/2,
            )
    level.background.blit(text, textpos)

    screen.blit(level.background, (0, 0))

    level.create_ennemy()
    red = level.create_red_player()
    blue = level.create_blue_player()

    level.create_platform(300, 350)
    level.create_goal(500, 400)

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

    _run = True
    while _run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                _run = False
                game.status = "Quit"
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    _run = False
                    game.status = "Quit"
                elif event.key in player_actions.keys():
                    player_actions[event.key]["start_action"]()
            elif event.type == pygame.KEYUP:
                if event.key in player_actions.keys():
                    player_actions[event.key]["stop_action"]()

        level.update()
        pygame.display.update()

        pygame.time.delay(10)

        if level.players_die():
            _run = False
            game.status = "Lose"
            game.lives -= 1

        if level.players_win():
            _run = False
            game.status = "Win"
            game.won_levels += 1
    return game


def display_level_0(screen, game):
    level = Level()
    level.background = pygame.image.load("gfx/background.png").convert()

    TEXT_COLOR = (200, 0, 0)
    hearts = u"♥" * game.lives
    text = engine.build_message(hearts, TEXT_COLOR)
    textpos = text.get_rect(
            centerx=level.background.get_width()/2,
            )
    level.background.blit(text, textpos)

    screen.blit(level.background, (0, 0))

    level.create_ennemy()
    red = level.create_red_player()
    blue = level.create_blue_player()

    level.create_platform(350, 50)
    level.create_platform(350, 100)
    level.create_goal(400, 400)

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

    _run = True
    while _run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                _run = False
                game.status = "Quit"
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    _run = False
                    game.status = "Quit"
                elif event.key in player_actions.keys():
                    player_actions[event.key]["start_action"]()
            elif event.type == pygame.KEYUP:
                if event.key in player_actions.keys():
                    player_actions[event.key]["stop_action"]()

        level.update()
        pygame.display.update()

        pygame.time.delay(10)

        if level.players_die():
            _run = False
            game.status = "Lose"
            game.lives -= 1

        if level.players_win():
            _run = False
            game.status = "Win"
            game.won_levels += 1
    return game

