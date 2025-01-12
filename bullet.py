import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT


class Bullet:

    def __init__(self, screen, pos) -> None:
        self.screen = screen
        self.pos = pygame.Vector2(pos.x + 30, pos.y)
        self.speed = 10
        self.isActive = True
        self.damage = 10

    def render(self):
        self.update()
        bullet = pygame.Rect(self.pos.x, self.pos.y, 5, 20)
        pygame.draw.rect(self.screen, "white", bullet, 10)

    def update(self):
        self.pos.y -= self.speed


class EnemyBullet(Bullet):

    def __init__(self, screen, pos) -> None:
        self.screen = screen
        self.pos = pygame.Vector2(pos.x + 30, pos.y)
        self.speed = 3
        self.isActive = True
        self.damage = 10

    def render(self):
        self.update()
        bullet = pygame.Rect(self.pos.x, self.pos.y, 5, 20)
        pygame.draw.rect(self.screen, "red", bullet, 10)

    def update(self):
        self.pos.y += self.speed


class DoubleBullet(Bullet):

    def __init__(self, screen, pos) -> None:
        self.screen = screen
        self.pos1 = pygame.Vector2(pos.x, pos.y)
        self.pos2 = pygame.Vector2(pos.x + 50, pos.y)
        self.speed = 10
        self.isActive = True

    def render(self):
        self.update()
        bullet1 = pygame.Rect(self.pos.x, self.pos.y, 5, 20)
        pygame.draw.rect(self.screen, "red", bullet1, 10)
        bullet2 = pygame.Rect(self.pos.x, self.pos.y, 5, 20)
        pygame.draw.rect(self.screen, "red", bullet2, 10)

    def update(self):
        self.pos1.y -= self.speed
        self.pos2.y -= self.speed
