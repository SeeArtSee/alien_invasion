import pygame
from pygame.sprite import Sprite
from random import randint


class Drop(Sprite):
    """Класс представляющий одну каплю"""
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        """ Загрузка изображения капли"""
        self.image = pygame.image.load('images/dropwater.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width + randint(-10, 100)
        self.rect.y = self.rect.height + randint(-10, 500)
        self.x = float(self.rect.x)

    def update(self):
        """Перемещает каплю вправо."""
        self.x += self.settings.speed_drop+randint(-8, 7)
        self.rect.x = self.x


