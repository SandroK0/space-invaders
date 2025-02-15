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
        self.shooting_delay = 10
        self.health = 1000
        self.color = "white"
        self.speed = 15

    def render(self):

        player = pygame.Rect(self.pos.x, self.pos.y, 60, 60)
        pygame.draw.rect(self.screen, self.color, player, 0)
        self.color = "white"

        text_surface = self.font.render(str(self.health), True, "black")
        text_rect = text_surface.get_rect(center=player.center)
        self.screen.blit(text_surface, text_rect)

    def shoot(self, game_self):
        current_time = pygame.time.get_ticks()
        mouse_x, mouse_y = pygame.mouse.get_pos()
        direction = pygame.Vector2(mouse_x - self.pos.x, mouse_y - self.pos.y)
        if direction.length() != 0:
            direction = direction.normalize()  # Normalize direction

        if current_time - self.last_shot_time >= self.shooting_delay:
            game_self.player_bullets.append(
                Bullet(self.screen, self.pos, direction)
            )
            self.last_shot_time = current_time

    def take_damage(self, damage):
        self.health -= damage
        self.color = "red"
