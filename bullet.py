import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

class Bullet:

    def __init__(self, screen, pos) -> None:
        self.screen = screen
        self.pos = pygame.Vector2(pos.x + 30, pos.y)
        self.speed = 10
        self.isActive = True

    def render(self):
        self.update()
        pygame.draw.circle(self.screen, "white", self.pos, 10)

    def reset(self, pos):
        self.pos = pygame.Vector2(pos.x + 10, pos.y)

    def update(self):
        self.pos.y -= 10


class DoubleBullet(Bullet):

    def __init__(self, screen, pos) -> None:
        self.screen = screen
        self.pos1 = pygame.Vector2(pos.x, pos.y)
        self.pos2 = pygame.Vector2(pos.x + 50, pos.y)
        self.speed = 10
        self.isActive = True

    def render(self):
        self.update()
        pygame.draw.circle(self.screen, "white", self.pos1, 10)
        pygame.draw.circle(self.screen, "white", self.pos2, 10)

    def update(self):
        self.pos1.y -= 10
        self.pos2.y -= 10