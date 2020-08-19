import pygame
from game import Game

if __name__ == '__main__':

    pygame.init()
    font = pygame.font.SysFont("Arial, Times New Roman ", 50)
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption('2048')
    done = False
    game = Game()
    game.start_pygame(pygame)
    clock = pygame.time.Clock()
    game.show(screen, font)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True
                elif event.key == pygame.K_UP:
                    game.move_up()
                elif event.key == pygame.K_DOWN:
                    game.move_down()
                elif event.key == pygame.K_LEFT:
                    game.move_left()
                elif event.key == pygame.K_RIGHT:
                    game.move_right()
                game.show(screen)
        pygame.display.flip()
        clock.tick(60)