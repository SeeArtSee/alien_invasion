import pygame

class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self) -> object:
        """Инициализирует статические настройки игры."""
        """Параметры экрана."""
        self.screen_width = 1700
        self.screen_height = 900
        self.bg_color = (20, 200, 200)
        self.screen_image = pygame.image.load('images/sky5.jpg')
        """Настройки корабля"""
        self.ship_speed = 1.5
        self.ship_limit = 1
        """Параметры снаряда"""
        self.bullet_speed = 3
        self.bullet_width = 5
        self.bullet_height = 20
        self.bullet_color = (25, 0, 0)
        self.bullet2_width = 15
        self.bullet2_height = 3
        """Настройки пришельцев"""
        self.alien_speed = 1.0
        self.fleet_drop_speed = 1
        # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = 1
        # Темп ускорения игры
        self.speedup_scale = 1.1
        """Настройки капель"""
        self.speed_drop = 1

        # Темп роста стоимости пришельцев
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся в ходе игры."""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0
        # fleet_direction = 1 обозначает движение вправо; а -1 - влево.
        self.fleet_direction = 1
        # Подсчет очков
        self.alien_points = 50

    def increase_speed(self):
        """Увеличивает настройки стоимости и скорости."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)


