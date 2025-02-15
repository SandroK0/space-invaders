import pygame
from player import Player
from settings import SCREEN_WIDTH, SCREEN_HEIGHT
from enemy import EnemyWave


class Game:

    def __init__(self, screen) -> None:

        pygame.font.init()

        self.running = True
        self.screen = screen
        self.font = pygame.font.Font(None, 74)
        self.mode = None
        self.player = Player(screen)
        self.enemy_wave = EnemyWave(screen)
        self.enemies = self.enemy_wave.enemies
        self.score = 0
        self.enemy_bullets = []
        self.player_bullets = []

    def handle_events(self, event, state):
        pass

    def update(self):

        if len(self.enemy_wave) == 0:
            print("You Won!")
            self.running = False

        keys = pygame.key.get_pressed()
        self.enemy_wave.shoot(self, self.player.pos)
        self.handle_press(keys)
        self.check_hits()

    def render(self):

        self.screen.fill("black")
        self.render_enemy_bullets()
        self.render_player_bullets()
        self.enemy_wave.render_wave()
        self.player.render()

    def render_enemy_bullets(self):
        for bullet in self.enemy_bullets:
            if bullet.pos.y > 900:
                self.enemy_bullets.remove(bullet)
            else:
                bullet.render()

    def render_player_bullets(self):


        for bullet in self.player_bullets:
            if (bullet.pos.x < 0 or bullet.pos.x > SCREEN_WIDTH or bullet.pos.y < 0 or bullet.pos.y > SCREEN_HEIGHT):
                self.player_bullets.remove(bullet)
            else:
                bullet.render()

    def handle_press(self, keys):
        if keys[pygame.K_a]:
            if not self.player.pos.x <= 0:
                self.player.pos.x -= self.player.speed
        if keys[pygame.K_d]:
            if not self.player.pos.x + 60 >= SCREEN_WIDTH:
                self.player.pos.x += self.player.speed
        if keys[pygame.K_w]:
            if not self.player.pos.y <= 0:
                self.player.pos.y -= self.player.speed
        if keys[pygame.K_s]:
            if not self.player.pos.y + 60 >= SCREEN_HEIGHT:
                self.player.pos.y += self.player.speed
        if keys[pygame.K_SPACE]:
            self.player.shoot(self)
        
        mouse_buttons = pygame.mouse.get_pressed() 
        if mouse_buttons[0]:
            self.player.shoot(self)


    def check_hits(self):
        for bullet in self.player_bullets:
            for enemy in self.enemies:
                if (
                    enemy.pos.x <= bullet.pos.x <= enemy.pos.x + 60
                    and enemy.pos.y <= bullet.pos.y <= enemy.pos.y + 60
                ):

                    enemy.take_damage(bullet.damage)
                    if bullet in self.player_bullets:
                        self.player_bullets.remove(bullet)
                    if enemy.health <= 0:
                        self.enemies.remove(enemy)

        for bullet in self.enemy_bullets:
            if (
                self.player.pos.x <= bullet.pos.x <= self.player.pos.x + 60
                and self.player.pos.y <= bullet.pos.y <= self.player.pos.y + 60
            ):

                self.player.take_damage(bullet.damage)
                self.enemy_bullets.remove(bullet)
                if self.player.health <= 0:
                    print("You died!")
                    self.running = False
