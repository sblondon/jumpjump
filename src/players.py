import pygame.display
import pygame.image
import pygame.sprite

import engine


class Player(pygame.sprite.Sprite):
    def __init__(self, image_path, x):
        super(Player, self).__init__()
        self._screen = pygame.display.get_surface()

        self.image = pygame.image.load(image_path).convert_alpha()
        y = self._screen.get_height() - 70
        self.rect = self.image.get_rect().move(x, y)
        self.mask = pygame.mask.from_surface(self.image)
        self.on_goal_previous_loop = False
        
        self._change_x = 0
        self._change_y = 0
        self.level = None

    def update(self):
        self._gravity_effect()
        self._move()

    def _move(self):
        self.rect.x += self._change_x

        block_hits = pygame.sprite.spritecollide(self, self.level.platform_sprites, False)
        for block in block_hits:
            if self._change_x > 0:
                self.rect.right = block.rect.left
            elif self._change_x < 0:
                self.rect.left = block.rect.right

        self.rect.y += self._change_y

        block_hits = pygame.sprite.spritecollide(self, self.level.platform_sprites, False)
        for block in block_hits:
            if self._change_y > 0:
                self.rect.bottom = block.rect.top
            elif self._change_y < 0:
                self.rect.top = block.rect.bottom

            self._change_y = 0

        if self.rect.left < 0 or self.rect.right > self._screen.get_width():
            self._change_x = 0

    def go_to_right(self):
        self._change_x = 1

    def go_to_left(self):
        self._change_x = -1

    def jump(self):
        if self._is_on_floor() or self._is_on_platform():
            self._change_y = -10

    def _is_on_floor(self):
        return self.rect.bottom >= self._screen.get_height() 

    def _is_on_platform(self):
        self.rect.y += 2
        platform_hits = pygame.sprite.spritecollide(self, self.level.platform_sprites, False)
        self.rect.y -= 2
        return platform_hits

    def stop_go_to_left(self):
        if self._change_x < 0:
            self._change_x = 0

    def stop_go_to_right(self):
        if self._change_x > 0:
            self._change_x = 0

    def _gravity_effect(self):
        if self._change_y == 0:
            self._change_y = 1
        else:
            self._change_y += .35

        if self.rect.y >= self._screen.get_height() - self.rect.height and self._change_y >= 0:
            self._change_y = 0
            self.rect.y = self._screen.get_height() - self.rect.height


class Red(Player):
    def __init__(self):
        super(Red, self).__init__(engine.image_path("person-red.png"), x=50)

    def __unicode__(self):
        return "Red player"


class Blue(Player):

    def __init__(self):
        super(Blue, self).__init__(engine.image_path("person-blue.png"), x=600)

    def __unicode__(self):
        return "Blue player"

