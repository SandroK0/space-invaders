import pygame
from settings import SCREEN_WIDTH
import random
from bullet import Bullet, EnemyBullet
import asyncio


class Enemy:

    def __init__(self, screen, direction, position) -> None:
        self.screen = screen
        self.pos = position
        self.direction = direction
        self.speed = 2
        self.health = 100
        self.color = (255, 0, 0)
        self.last_shot_time = pygame.time.get_ticks()
        self.shooting_delay = 2500
        self.font = pygame.font.Font(None, 48)
        self.title_font = pygame.font.Font(None, 64)  # Font for the title text

    def render(self):
        player = pygame.Rect(self.pos.x, self.pos.y, 60, 60)
        pygame.draw.rect(self.screen, self.color, player, 0)
        self.color = (255, 0, 0)

        text_surface = self.font.render(str(self.health), True, "white")
        text_rect = text_surface.get_rect(center=player.center)
        self.screen.blit(text_surface, text_rect)

    def move(self):
        if self.direction == 1:
            self.pos.x += self.speed
        else:
            self.pos.x -= self.speed

    def take_damage(self, damage):

        self.health -= damage
        self.color = (255, 255, 255)

    def shoot(self, game_self):

        current_time = pygame.time.get_ticks()

        if current_time - self.last_shot_time >= self.shooting_delay:
            game_self.enemy_bullets.append(
                EnemyBullet(self.screen, self.pos))
            self.last_shot_time = current_time


class EnemyWave:
    def __init__(self, screen) -> None:
        self.screen = screen
        self.enemies = self.get_wave(screen)
        self.last_shot_time = pygame.time.get_ticks()
        self.shooting_delay = 2500
        self.current_shooter = 0

    def get_wave(self, screen):

        enemies = []
        pos_x = 100
        pos_y = 100
        for i in range(2):
            for i in range(5):
                enemies.append(
                    Enemy(screen, 1, pygame.Vector2(pos_x, pos_y)))
                pos_x += 100
            pos_y += 100
            pos_x = 100

        return enemies

    def change_wave_direction(self):
        if self.enemies[-1].pos.x + 60 >= SCREEN_WIDTH:
            for enemy in self.enemies:
                enemy.direction *= -1
        if self.enemies[0].pos.x <= 0:
            for enemy in self.enemies:
                enemy.direction *= -1

    def shoot(self, game_self):
        current_time = pygame.time.get_ticks()  # Get the current time

        if current_time - self.last_shot_time > 500:
            self.enemies[self.current_shooter].shoot(game_self)
            self.current_shooter += 1
            self.last_shot_time = current_time

        if self.current_shooter >= len(self.enemies):
            self.current_shooter = 0

    def render_wave(self):

        for enemy in self.enemies:
            enemy.move()
            enemy.render()

        self.change_wave_direction()
