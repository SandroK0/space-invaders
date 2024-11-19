import pygame
from settings import WHITE, SCREEN_WIDTH
from bullet import Bullet, DoubleBullet


class Player:

    def __init__(self, screen) -> None:
        self.screen = screen
        self.pos = pygame.Vector2(SCREEN_WIDTH / 2, 600)
        self.last_shot_time = pygame.time.get_ticks()  # Track time of the last shot
        self.shooting_delay = 10
        self.health = 500

    def render(self):

        player = pygame.Rect(self.pos.x, self.pos.y, 60, 60)
        pygame.draw.rect(self.screen, WHITE, player, 0)

    def shoot(self, game_self):

        current_time = pygame.time.get_ticks()

        if current_time - self.last_shot_time >= self.shooting_delay:
            game_self.shooted_bullets.append(DoubleBullet(self.screen, self.pos))
            self.last_shot_time = current_time
