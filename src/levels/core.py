# -*- coding: utf-8 -*-
import abc

import pygame.display
import pygame.sprite

import engine
import ennemies
import goals
import platforms
import players


class Level(object):
    def __init__(self, game, background_path):
        self.platform_sprites = pygame.sprite.Group()
        self.player_sprites = pygame.sprite.RenderUpdates()
        self.ennemy_sprites = pygame.sprite.Group()
        self.goal_sprites = pygame.sprite.Group()
        self.ink_sprites = pygame.sprite.Group()
        self.background = None
        self.red_player = self.create_red_player()
        self.blue_player = self.create_blue_player()
        self.goal = None
        self.all_sprites = pygame.sprite.LayeredUpdates()

        self.screen = pygame.display.get_surface()
        self.game = game

        self.background = pygame.image.load(background_path).convert()
        TEXT_COLOR = (200, 0, 0)
        hearts = u"♥" * game.lives
        text = engine.build_message(hearts, TEXT_COLOR)
        textpos = text.get_rect(
                centerx=self.background.get_width()/2,
                )
        self.background.blit(text, textpos)
    
        self.screen.blit(self.background, (0, 0))
    

    def update(self):
        for sprite in self.all_sprites:
            self.screen.blit(self.background, sprite.rect, sprite.rect)

        self.all_sprites.clear(self.screen, self.background)
        self.all_sprites.update()
        self.all_sprites.draw(self.screen)

    def players_collisions(self):
        return pygame.sprite.groupcollide(
                self.ennemy_sprites, self.player_sprites,
                False, False,
                collided=pygame.sprite.collide_mask)
    
    def players_win(self):
        return self.goal.reached()

    @abc.abstractmethod
    def create_ennemies(self):
        pass
    
    def create_red_player(self):
        red = players.Red()
        red.level = self
        self.player_sprites.add(red)
        return red

    def create_blue_player(self):
        blue = players.Blue()
        blue.level = self
        self.player_sprites.add(blue)
        return blue

    def create_default_platform(self, x, y):
        platform = platforms.DefaultPlatform()
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

    def play(self):
        player_actions = {
                pygame.K_UP: {
                    "start_action": self.blue_player.jump,
                    "stop_action": lambda: None,
                    },
                pygame.K_RIGHT: {
                    "start_action": self.blue_player.go_to_right,
                    "stop_action": self.blue_player.stop_go_to_right,
                    },
                pygame.K_LEFT: {
                    "start_action": self.blue_player.go_to_left,
                    "stop_action": self.blue_player.stop_go_to_left,
                    },
                pygame.K_z: {
                    "start_action": self.red_player.jump,
                    "stop_action": lambda: None,
                    },
                pygame.K_d: {
                    "start_action": self.red_player.go_to_right,
                    "stop_action": self.red_player.stop_go_to_right,
                    },
                pygame.K_q: {
                    "start_action": self.red_player.go_to_left,
                    "stop_action": self.red_player.stop_go_to_left,
                    }
                }

        _run = True
        while _run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    _run = False
                    self.game.status = self.game.QUIT
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        _run = False
                        self.game.status = self.game.QUIT
                    elif event.key in player_actions.keys():
                        player_actions[event.key]["start_action"]()
                elif event.type == pygame.KEYUP:
                    if event.key in player_actions.keys():
                        player_actions[event.key]["stop_action"]()

            self.update()
            pygame.display.update()

            pygame.time.delay(10)

            for ennemy in self.players_collisions():
                ennemy.touch_player(self.game)

            if self.players_win():
                self.game.status = self.game.WIN
                self.game.won_levels += 1

            if self.game.status in (self.game.LOSE, self.game.WIN):
                _run = False
        return self.game

    def create_slow_bouncing_ennemy(self, x, y):
        ennemy = ennemies.SlowBouncingEnnemy(x, y)
        self.ennemy_sprites.add(ennemy)

    def create_fast_bouncing_ennemy(self, x, y):
        ennemy = ennemies.FastBouncingEnnemy(x, y)
        self.ennemy_sprites.add(ennemy)

    def create_octopus(self, x, y):
        ennemy = ennemies.Octopus(x, y, self)
        self.ennemy_sprites.add(ennemy)

    def create_left_bird(self, y):
        ennemy = ennemies.LeftBird(y)
        self.ennemy_sprites.add(ennemy)

    def create_right_bird(self, y):
        ennemy = ennemies.RightBird(y)
        self.ennemy_sprites.add(ennemy)
        print ennemy

    def create_octopus_platform(self, x, y):
        platform = platforms.OctopusGeneratorPlatform(self)
        platform.rect.x = x
        platform.rect.y = y
        self.platform_sprites.add(platform)
        return platform

    def finalize_level(self):
        for platform in self.platform_sprites:
            self.all_sprites.add(platform)
        self.all_sprites.add(self.goal)
        self.all_sprites.add(self.blue_player)
        self.all_sprites.add(self.red_player)
        for ennemy in self.ennemy_sprites:
            self.all_sprites.add(ennemy)
        for ink in self.ink_sprites:
            self.all_sprites.add(ink)

