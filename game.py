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

    def draw_grid(self):
        """Рисует сетку поля."""

        # Рисуем сетку на экране
        for y in range(ROWS):
            for x in range(COLUMNS):
                rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
                pygame.draw.rect(self.screen, GREY, rect, 1)
    def render(self):
        """Отображает всю информацию на экране."""

        # Заполнение экрана чёрным цветом
        self.screen.fill(BLACK)

        # Рисуем сетку, зафиксированные блоки и текущую падающую фигуру
        self.draw_grid()

        # Обновление экрана
        pygame.display.flip()

    def run(self):
        """Запуск игрового цикла."""

        while self.running:
            self.handle_events()  # Обработка событий
            self.render()  # Отображение на экране
            self.clock.tick(60)  # Ограничение FPS (60 кадров в секунду)