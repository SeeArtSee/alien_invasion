import sys
import pygame
from settings import Settings
from ship import Ship
from ship2 import Ship2
from bullet import Bullet
from alien import Alien
from bullet2 import Bullet2
from time import sleep
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from raindrops import Drop
from random import randint


class AlienInvasion:
    """Класс для управления ресурсами и поведением игры"""
    def __init__(self):
        """Инициализирует игру и создаёт игровые ресурсы"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))
        pygame.display.set_caption("Стрельба по мишеням")
        self.ship = Ship(self)
        self.ship2 = Ship2(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.drops = pygame.sprite.Group()
        self.create_drops()
        self._create_fleet()

    def run_game(self):
        """Запуск основного цикла"""
        while True:
            self._check_event()
            self.ship2.update()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()
            self._update_drops()

    def _check_event(self):
        """Обрабатывает нажатие клавиш и события мыши"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Функция обрабатывает нажатие клавиш"""
        if event.key == pygame.K_KP4:
            self.ship2.moving_left = True
        elif event.key == pygame.K_KP6:
            self.ship2.moving_right = True
        elif event.key == pygame.K_a:
            self.ship.moving_left = True
        elif event.key == pygame.K_d:
            self.ship.moving_right = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_DOWN:
            self._fire_bullet2()
            """Калавиша Q для выхода"""
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Функция обрабатывает отпускание клавиш"""
        if event.key == pygame.K_KP4:
            self.ship2.moving_left = False
        elif event.key == pygame.K_KP6:
            self.ship2.moving_right = False
        elif event.key == pygame.K_a:
            self.ship.moving_left = False
        elif event.key == pygame.K_d:
            self.ship.moving_right = False

    def _update_bullets(self):
        """Уничтожение снарядов, вышедших за край экрана"""
        self.bullets.update()
        for b in self.bullets.copy():
            if b.rect.bottom <= 0:
                self.bullets.remove(b)

    def _update_aliens(self):
        """Обновляет позиции пришельцев"""
        self._chek_fleet_edges()
        self.aliens.update()

    def _update_drops(self):
        """Обновляет позиции всех капель."""
        self.drops.update()

    def _update_screen(self):
        """Обновляет экран"""
        self.screen.blit(self.settings.screen_image, (0, 0))
        self.ship.blitme()
        self.ship2.blitme()
        for bull in self.bullets.sprites():
            bull.draw_bullet()
        self.aliens.draw(self.screen)
        self.drops.draw(self.screen)
        pygame.display.flip()

    def _fire_bullet(self):
        """Создание нового снаряда и включение его в группу bullets"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _fire_bullet2(self):
        """Создание нового снаряда для второго корабля"""
        new_bullet2 = Bullet2(self)
        self.bullets.add(new_bullet2)

    def _create_fleet(self):
        """Создаёт пришельцев"""
        alien = Alien(self)
        self.aliens.add(alien)

    def _chek_fleet_edges(self):
        """Реагирует на достижение пришельцем края"""
        for alien in self.aliens.sprites():
            if alien.check_edges:
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Опускает весь флот и меняет направление движения"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def create_drops(self):
        """Создание капель дождя"""
        drop = Drop(self)
        random_number = randint(-10, 10)
        drop_width, drop_height = drop.rect.size
        available_space_x = (self.settings.screen_width - (2 * drop_width))
        number_drops_x = available_space_x // (2 * drop_width)
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * drop_height) - ship_height)
        number_rows = available_space_y // (2 * drop_height)
        for row_number in range(number_rows+random_number):
            for drop_number in range(number_drops_x+random_number):
                self.create_drop(drop_number, row_number)

    def create_drop(self, drop_number, row_number):
        drop = Drop(self)
        random_number = randint(-30, 50)
        drop_width = drop.rect.width
        drop_width, drop_height = drop.rect.size
        drop.x = drop_width + 2 * drop_width * drop_number
        drop.rect.x = drop.x + random_number
        drop.rect.y = (drop.rect.height + 2 * drop.rect.height * row_number) + random_number
        self.drops.add(drop)


if __name__ == '__main__':
    """Создание экземпляра и запуск игры."""
    ai = AlienInvasion()
    ai.run_game()
