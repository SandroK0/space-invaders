import pygame
from player import Player
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, PLAYER_SPEED, BALL_SPEED
from bullet import Bullet
from enemy import Enemy
import random


class Game:

    def __init__(self, screen) -> None:

        pygame.font.init()

        self.screen = screen
        self.font = pygame.font.Font(None, 74)
        self.mode = None
        self.enemies = []
        self.player = Player(screen)
        self.score = 0
        self.enemy_bullets = []
        self.player_bullets = []
        self.enemy_wave()

    def update(self):

        keys = pygame.key.get_pressed()
        self.handle_press(keys)
        self.player.shoot(self)
        self.check_hits()

    def handle_events(self, event, state):
        pass

    def render(self):

        self.screen.fill("black")
        self.render_bullets()
        self.render_enemies()
        self.player.render()

    def render_bullets(self):
        for bullet in self.enemy_bullets:
            # if bullet.pos.y < 0:
            #     self.shooted_bullets.remove(bullet)
            # else:
            bullet.render()

    def render_enemies(self):
        for enemy in self.enemies:
            enemy.move()
            enemy.render()

    def handle_press(self, keys):
        if keys[pygame.K_a]:
            if not self.player.pos.x <= 0:
                self.player.pos.x -= PLAYER_SPEED
        if keys[pygame.K_d]:
            if not self.player.pos.x + 60 >= SCREEN_WIDTH:
                self.player.pos.x += PLAYER_SPEED

    def enemy_wave(self):

        for i in range(10):
            self.spawn_enemy()

    def spawn_enemy(self):
        direction = random.choice([-1, 1])
        self.enemies.append(Enemy(self.screen, direction))

    def check_hits(self):
        return
        for bullet in self.shooted_bullets:
            for enemy in self.enemies:
                if (
                    enemy.pos.x <= bullet.pos.x <= enemy.pos.x + 60
                    and enemy.pos.y <= bullet.pos.y <= enemy.pos.y + 60
                ):
                    if bullet.isActive:
                        enemy.get_damage(10)
                        print("Hit")
                        bullet.isActive = False
                        if enemy.health <= 0:
                            self.enemies.remove(enemy)
