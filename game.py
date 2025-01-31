import pygame
import random
from settings import *
from level import Level
from tetromino import Tetromino


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

        # Начальный счёт
        self.score = 0

        # Начальное количество очищенных линий
        self.lines_cleared = 0

        # Создание объекта уровня игры
        self.level = Level()

        # Выбор случайной фигуры
        self.falling_tetromino = Tetromino(random.choice(list(SHAPES.keys())))

        # Флаг для управления циклом игры
        self.running = True

    def lock_tetromino(self):
        """Фиксирует фигуру на месте, добавляет её в сетку и проверяет линии."""

        # Добавляем фигуру в сетку
        self.level.add_tetromino(self.falling_tetromino)

        # Создаём новую случайную фигуру
        self.falling_tetromino = Tetromino(random.choice(list(SHAPES.keys())))

        # Очищаем полные строки и обновляем счёт
        rows_cleared = self.level.clear_full_rows()
        self.lines_cleared += rows_cleared

        # Вызов обновления уровня
        self.update_level()

        # Проверка на окончание игры
        if self.level.check_collision(self.falling_tetromino):
            #self.show_game_over_window()
            #self.save_game(0, [[None for _ in range(COLUMNS)] for _ in range(ROWS)], 1, 0)
            self.running = False

    def handle_events(self):
        # Обработка событий игры
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    # Перемещение фигуры влево
                    self.move_tetromino(-1)
                elif event.key == pygame.K_RIGHT:
                    # Перемещение фигуры вправо
                    self.move_tetromino(1)
                elif event.key == pygame.K_DOWN:
                    # Мгновенное падение фигуры
                    self.soft_drop()
                elif event.key == pygame.K_UP:
                    # Поворот фигуры
                    self.rotate_tetromino()

    def draw_grid(self):
        """Рисует сетку поля."""

        # Рисуем сетку на экране
        for y in range(ROWS):
            for x in range(COLUMNS):
                rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
                pygame.draw.rect(self.screen, GREY, rect, 1)

    def move_tetromino(self, dx):
        # Перемещение фигуры по горизонтали
        self.falling_tetromino.x += dx
        if self.level.check_collision(self.falling_tetromino):
            # Если есть столкновение, откатываем движение
            self.falling_tetromino.x -= dx

    def soft_drop(self):
        """Одноразовое ускорение вниз."""
        # Ускорение падения фигуры
        self.falling_tetromino.y += 1
        if self.level.check_collision(self.falling_tetromino):
            # Если есть столкновение, откатываем движение и фиксируем фигуру
            self.falling_tetromino.y -= 1
            self.lock_tetromino()

    def rotate_tetromino(self):
        # Поворот фигуры
        self.falling_tetromino.rotate()
        if self.level.check_collision(self.falling_tetromino):
            # Если есть столкновение после поворота, откатываем поворот
            self.falling_tetromino.rotate_back()

    def update_level(self):
        # Обновляет уровень игрока на основе количества очищенных линий
        self.player_level = self.score // 10

        # Расчёт нового уровня
        new_level = self.lines_cleared // 10 + 1
        if new_level > self.player_level:
            self.player_level = new_level
            self.fall_speed = max(270 - (self.player_level - 1) * 50, 100)  # Ускоряем падение

    def draw_tetromino(self, tetromino):
        """Рисует падающую фигуру."""

        # Рисуем каждый блок фигуры
        for x, y in tetromino.get_positions():
            if y >= 0:  # Игнорируем блоки, которые за пределами экрана
                rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
                pygame.draw.rect(self.screen, tetromino.color, rect)

    def render(self):
        """Отображает всю информацию на экране."""

        # Заполнение экрана чёрным цветом
        self.screen.fill(BLACK)

        # Рисуем сетку, зафиксированные блоки и текущую падающую фигуру
        self.draw_grid()
        self.draw_tetromino(self.falling_tetromino)

        # Обновление экрана
        pygame.display.flip()

    def run(self):
        """Запуск игрового цикла."""

        while self.running:
            self.handle_events()  # Обработка событий
            self.render()  # Отображение на экране
            self.clock.tick(60)  # Ограничение FPS (60 кадров в секунду)