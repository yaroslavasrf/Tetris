import pygame
from settings import *

class Game:
    def __init__(self):
        # Инициализация библиотеки pygame
        pygame.init()

        # Создание окна игры
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

        # Установка заголовка окна
        pygame.display.set_caption("Tetris")

        # Создание объекта для управления временем
        self.clock = pygame.time.Clock()

        # Флаг для управления циклом игры
        self.running = True

    def handle_events(self):
        # Обработка событий игры
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False


    def run(self):
        """Запуск игрового цикла."""

        while self.running:
            self.handle_events()  # Обработка событий
            self.clock.tick(60)  # Ограничение FPS (60 кадров в секунду)