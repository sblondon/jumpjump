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
        self.player_sprites = pygame.sprite.Group()
        self.ennemy_sprites = pygame.sprite.Group()
        self.goal_sprites = pygame.sprite.Group()
        self.background = None
        self.red_player = None
        self.blue_player = None
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

    @abc.abstractmethod
    def create_sprites(self):
        self.create_red_player()
        self.create_blue_player()

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
                    self.game.status = "Quit"
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        _run = False
                        self.game.status = "Quit"
                    elif event.key in player_actions.keys():
                        player_actions[event.key]["start_action"]()
                elif event.type == pygame.KEYUP:
                    if event.key in player_actions.keys():
                        player_actions[event.key]["stop_action"]()

            self.update()
            pygame.display.update()

            pygame.time.delay(10)

            if self.players_die():
                _run = False
                self.game.status = "Lose"
                self.game.lives -= 1

            if self.players_win():
                _run = False
                self.game.status = "Win"
                self.game.won_levels += 1
        return self.game


class Level1(Level):
    def __init__(self, game):
        super(Level1, self).__init__(game, "gfx/background.png")

    def create_sprites(self):
        super(Level1, self).create_sprites()
        self.create_ennemy()
        self.create_platform(300, 350)
        self.create_goal(500, 400)


class Level0(Level):
    def __init__(self, game):
        super(Level0, self).__init__(game, "gfx/background.png")

    def create_sprites(self):
        super(Level0, self).create_sprites()
        self.create_ennemy()
        self.create_platform(350, 50)
        self.create_platform(350, 100)
        self.create_goal(400, 400)


def select_level(game):
    lvls = {0: Level0,
            1: Level1}
    _Level = lvls.get(game.won_levels, Level1)
    level = _Level(game)
    level.create_sprites()
    return level

