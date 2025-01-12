import pygame
from settings import SCREEN_WIDTH
from bullet import Bullet, DoubleBullet


class Player:

    def __init__(self, screen) -> None:

        self.font = pygame.font.Font(None, 48)
        self.title_font = pygame.font.Font(None, 64)  # Font for the title text
        self.screen = screen
        self.pos = pygame.Vector2(SCREEN_WIDTH / 2, 800)
        self.last_shot_time = pygame.time.get_ticks()  # Track time of the last shot
        self.shooting_delay = 100
        self.health = 100
        self.color = "white"

    def render(self):

        player = pygame.Rect(self.pos.x, self.pos.y, 60, 60)
        pygame.draw.rect(self.screen, self.color, player, 0)
        self.color = "white"

        text_surface = self.font.render(str(self.health), True, "black")
        text_rect = text_surface.get_rect(center=player.center)
        self.screen.blit(text_surface, text_rect)

    def shoot(self, game_self):

        current_time = pygame.time.get_ticks()

        if current_time - self.last_shot_time >= self.shooting_delay:
            game_self.player_bullets.append(
                Bullet(self.screen, self.pos))
            game_self.player_bullets.append(
                Bullet(self.screen, self.pos))
            self.last_shot_time = current_time

    def take_damage(self, damage):
        self.health -= damage
        self.color = "red"
