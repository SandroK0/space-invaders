import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT
import random
from bullet import Bullet, EnemyBullet



class Enemy:
    
    shooting_delay = 100

    def __init__(self, screen, direction, position) -> None:
        self.screen = screen
        self.pos = position
        self.direction = direction
        self.speed = 2
        self.health = 100
        self.color = (255, 0, 0)
        self.last_shot_time = pygame.time.get_ticks()
        self.font = pygame.font.Font(None, 48)
        self.title_font = pygame.font.Font(None, 64)  # Font for the title text

    def render(self):
        player = pygame.Rect(self.pos.x, self.pos.y, 60, 60)
        pygame.draw.rect(self.screen, self.color, player, 0)
        self.color = (255, 0, 0)

        text_surface = self.font.render(str(self.health), True, "white")
        text_rect = text_surface.get_rect(center=player.center)
        self.screen.blit(text_surface, text_rect)

    def check_collisions(self):

        if self.pos.x + 60 >= SCREEN_WIDTH + 2500:
            self.direction *= -1
        if self.pos.x <= -2500:
            self.direction *= -1

    def move(self):

        self.check_collisions()

        if self.direction == 1:
            self.pos.x += self.speed
        else:
            self.pos.x -= self.speed

    def take_damage(self, damage):

        self.health -= damage
        self.color = (255, 255, 255)

    def shoot(self, game_self, direction):

        current_time = pygame.time.get_ticks()

        if current_time - self.last_shot_time >= Enemy.shooting_delay:
            game_self.enemy_bullets.append(
                EnemyBullet(self.screen, self.pos, direction))
            self.last_shot_time = current_time


class EnemyWave:
    def __init__(self, screen) -> None:
        self.screen = screen
        self.enemies = self.get_wave(screen)
        self.last_shot_time = pygame.time.get_ticks()
        self.current_shooter = 0

    def get_wave(self, screen):

        enemies = []
        for i in range(500):
            pos_x = random.randint(-2000, SCREEN_WIDTH + 2000)
            pos_y = random.randint(0, SCREEN_HEIGHT - 60)
            enemies.append(
                Enemy(screen, random.choice([1, -1]), pygame.Vector2(pos_x, pos_y)))

        return enemies

    def shoot(self, game_self, player_pos):
        current_time = pygame.time.get_ticks()  # Get the current time

        if current_time - self.last_shot_time > Enemy.shooting_delay:

            current_shooter = self.enemies[self.current_shooter]

            bullet_direction = pygame.Vector2(
                player_pos.x - current_shooter.pos.x, player_pos.y - current_shooter.pos.y)
            if bullet_direction.length() != 0:
                bullet_direction = bullet_direction.normalize()

            current_shooter.shoot(game_self, bullet_direction)
            self.current_shooter += 1
            self.last_shot_time = current_time

        if self.current_shooter >= len(self.enemies):
            self.current_shooter = 0

    def render_wave(self):

        for enemy in self.enemies:
            enemy.move()
            enemy.render()

    def __len__(self):

        return len(self.enemies)
