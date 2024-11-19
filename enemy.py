import pygame
from settings import WHITE, SCREEN_WIDTH
import random


class Enemy:

    def __init__(self, screen, direction) -> None:
        self.screen = screen
        self.pos = pygame.Vector2(random.randrange(0, SCREEN_WIDTH), random.choice([100, 200, 300]))
        self.direction = direction
        self.speed = 2
        self.health = 100
        self.color = (255, 0, 0)

    def render(self):
        if self.pos.x + 60 > SCREEN_WIDTH or self.pos.x < 0:
            self.direction *= -1

        player = pygame.Rect(self.pos.x, self.pos.y, 60, 60)
        pygame.draw.rect(self.screen, self.color, player, 0)
        self.color = (255, 0, 0)

    def move(self):
        if self.direction == 1:
            self.pos.x += self.speed
        else:
            self.pos.x -= self.speed

    def get_damage(self, damage):

        self.health -= damage
        self.color = (255, 255, 255)
