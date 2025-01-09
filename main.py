import pygame

from data import *

# компоненты
from tetris_game import TetrisGame
from additionally import Score, Previous

class Main:
    def __init__(self):

        # основное
        pygame.init()
        self.main_surface = pygame.display.set_mode((WINDOW_SIZE))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption('Tetris')

        # компоненты
        self.tetris_game = TetrisGame(self.main_surface)
        self.score = Score(self.main_surface)
        self.previous = Previous(self.main_surface)

        self.change_y = 0
        self.change_x = 0
        self.v = 1
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            pressed = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.change_x += 1
                        pressed = True
                    if event.key == pygame.K_LEFT:
                        self.change_x -= 1
                        pressed = True

            self.main_surface.fill(BACKGROUND_COLOR)
            self.tetris_game.run(self.change_y, self.change_x, pressed)
            self.score.run()
            self.previous.run()

            self.change_y += self.v * self.clock.tick() / 1000

            pygame.display.update()

if __name__ == '__main__':
    main = Main()
    main.run()