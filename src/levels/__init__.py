# -*- coding: utf-8 -*-
import abc
import random

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
        self.player_sprites = pygame.sprite.Group()
        self.ennemy_sprites = pygame.sprite.Group()
        self.goal_sprites = pygame.sprite.Group()
        self.background = None
        self.red_player = self.create_red_player()
        self.blue_player = self.create_blue_player()
        self.goal = None

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

        for sprite in self.player_sprites:
            self.screen.blit(self.background, sprite.rect, sprite.rect)

        for sprite in self.ennemy_sprites:
            self.screen.blit(self.background, sprite.rect, sprite.rect)

        for sprite in self.platform_sprites:
            self.screen.blit(self.background, sprite.rect, sprite.rect)

        for sprite in self.goal_sprites:
            self.screen.blit(self.background, sprite.rect, sprite.rect)

        self.player_sprites.update()
        self.player_sprites.draw(self.screen)

        self.ennemy_sprites.update()
        self.ennemy_sprites.draw(self.screen)

        self.platform_sprites.update()
        self.platform_sprites.draw(self.screen)

        self.goal_sprites.update()
        self.goal_sprites.draw(self.screen)
      
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

            for collision in self.players_collisions():
                collision.touch_player(self.game)

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
        target = random.choice((self.red_player, self.blue_player))
        ennemy = ennemies.Octopus(x, y, target)
        self.ennemy_sprites.add(ennemy)


class TestLevel(Level):
    def __init__(self, game):
        super(TestLevel, self).__init__(game, engine.image_path("background.png"))
        self.create_ennemies()
        self.create_platform(350, 50)
        self.create_platform(350, 100)
        self.create_goal(400, 400)

    def create_ennemies(self):
        self.create_octopus(250, 150)


class Level0(Level):
    def __init__(self, game):
        super(Level0, self).__init__(game, engine.image_path("background.png"))
        self.create_ennemies()
        self.create_platform(350, 50)
        self.create_platform(350, 100)
        self.create_goal(400, 400)

    def create_ennemies(self):
        self.create_slow_bouncing_ennemy(250, 150)


class Level1(Level):
    def __init__(self, game):
        super(Level1, self).__init__(game, engine.image_path("background.png"))
        self.create_ennemies()
        self.create_platform(300, 350)
        self.create_goal(500, 400)

    def create_ennemies(self):
        self.create_fast_bouncing_ennemy(50, 50)


class Level2(Level):
    def __init__(self, game):
        super(Level2, self).__init__(game, engine.image_path("background.png"))
        self.create_ennemies()
        self.create_platform(200, 420)
        self.create_goal(300, 350)

    def create_ennemies(self):
        self.create_slow_bouncing_ennemy(250, 50)
        self.create_slow_bouncing_ennemy(450, 150)


def select_level(game):
    LVLS = {0: Level0,
            1: Level1,
            2: Level2}
    HigherLevel = LVLS[max(LVLS.keys())]
    _Level = LVLS.get(game.won_levels, HigherLevel)
    return _Level(game)

def introduce_level(game):
    msg = u"Level %d" % (game.won_levels + 1)
    engine.display_simple_message(msg)

