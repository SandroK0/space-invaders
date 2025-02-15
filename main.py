import pygame
from game import Game
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Space Invaders")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 18)

    game = Game(screen)

    while game.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.running = False

        game.update()
        game.render()
        fps = clock.get_fps()
        fps_text = font.render(f"FPS: {fps:.2f}", True, pygame.Color('white'))
        screen.blit(fps_text, (10, 10))
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
