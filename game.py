import pygame
import random
import json
from level import Level
from tetromino import Tetromino
from settings import *
from start_screen import StartScreen


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

        # Создание объекта уровня игры
        self.level = Level()

        # Выбор случайной фигуры
        self.falling_tetromino = Tetromino(random.choice(list(SHAPES.keys())))

        # Начальный счёт
        self.score = 0

        # Начальное количество очищенных линий
        self.lines_cleared = 0

        # Начальный уровень игрока
        self.player_level = 1

        # Начальная скорость падения
        self.fall_speed = 500

        # Время последнего падения фигуры
        self.last_fall_time = pygame.time.get_ticks()

        # Флаг для управления циклом игры
        self.running = True

        # Загрузка сохранённой игры
        self.load_game()

        # Отображаем заголовок игры
        start_screen = StartScreen(self.screen)
        start_screen.display()

    def save_game(self, score, grid, level, lines_cleared):
        """Сохраняет текущее состояние игры."""

        # Создание словаря с данными
        data = {
            "score": score,  # Текущий счёт
            "grid": grid,  # Состояние сетки
            "level": level,  # Текущий уровень
            "lines_cleared": lines_cleared  # Количество очищенных линий
        }

        # Запись данных в файл
        with open("data.txt", "w") as file:
            json.dump(data, file)

    def load_game(self):
        """Загружает сохранённое состояние игры, если файл существует."""

        try:
            # Чтение данных из файла
            with open("data.txt", "r") as file:
                data = json.load(file)

                # Восстановление состояния игры
                self.score = data["score"]
                self.level.grid = data["grid"]
                self.player_level = data.get("level", 1)
                self.lines_cleared = data.get("lines_cleared", 0)
                self.fall_speed = max(500 - (self.player_level - 1) * 50, 100)

        except (FileNotFoundError, json.JSONDecodeError):
            # Если файл не найден или повреждён, начинаем игру с начальных значений
            self.score = 0
            self.lines_cleared = 0
            self.player_level = 1
            self.fall_speed = 500
            self.level.grid = [[None for _ in range(COLUMNS)] for _ in range(ROWS)]

    def handle_events(self):
        # Обработка событий игры
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Сохранение состояния игры при выходе
                self.save_game(self.score, self.level.grid, self.player_level, self.lines_cleared)
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

    def move_tetromino(self, dx):
        # Перемещение фигуры по горизонтали
        self.falling_tetromino.x += dx
        if self.level.check_collision(self.falling_tetromino):
            # Если есть столкновение, откатываем движение
            self.falling_tetromino.x -= dx

    def rotate_tetromino(self):
        # Поворот фигуры
        self.falling_tetromino.rotate()
        if self.level.check_collision(self.falling_tetromino):
            # Если есть столкновение после поворота, откатываем поворот
            self.falling_tetromino.rotate_back()

    def soft_drop(self):
        """Одноразовое ускорение вниз."""
        # Ускорение падения фигуры
        self.falling_tetromino.y += 1
        if self.level.check_collision(self.falling_tetromino):
            # Если есть столкновение, откатываем движение и фиксируем фигуру
            self.falling_tetromino.y -= 1
            self.lock_tetromino()

    def drop_tetromino(self):
        """Регулярное падение фигуры."""
        # Падение фигуры на один шаг вниз
        self.falling_tetromino.y += 1
        if self.level.check_collision(self.falling_tetromino):
            # Если есть столкновение, откатываем движение и фиксируем фигуру
            self.falling_tetromino.y -= 1
            self.lock_tetromino()

    def lock_tetromino(self):
        """Фиксирует фигуру на месте, добавляет её в сетку и проверяет линии."""

        # Добавляем фигуру в сетку
        self.level.add_tetromino(self.falling_tetromino)

        # Создаём новую случайную фигуру
        self.falling_tetromino = Tetromino(random.choice(list(SHAPES.keys())))

        # Очищаем полные строки и обновляем счёт
        rows_cleared = self.level.clear_full_rows()
        self.score += rows_cleared * 10
        self.lines_cleared += rows_cleared

        # Вызов обновления уровня
        self.update_level()

        # Проверка на окончание игры
        if self.level.check_collision(self.falling_tetromino):
            self.show_game_over_window()
            self.save_game(0, [[None for _ in range(COLUMNS)] for _ in range(ROWS)], 1, 0)
            self.running = False

    def update_level(self):
        # Обновляет уровень игрока на основе количества очищенных линий
        self.player_level = self.score // 10

        # Расчёт нового уровня
        new_level = self.lines_cleared // 10 + 1
        if new_level > self.player_level:
            self.player_level = new_level
            self.fall_speed = max(270 - (self.player_level - 1) * 50, 100)  # Ускоряем падение

    def show_game_over_window(self):
        """Отображает окно окончания игры."""

        # Заполнение экрана чёрным цветом
        self.screen.fill(BLACK)

        # Отображение текста "Game Over"
        font = pygame.font.Font("HowardFatRegular.ttf", 72)
        text = font.render("Game Over!", True, WHITE)
        self.screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - 50))

        # Отображение финального счёта
        font = pygame.font.Font("HowardFatRegular.ttf", 36)
        score_text = font.render(f"Final Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, SCREEN_HEIGHT // 2 + 20))

        # Обновление экрана
        pygame.display.flip()

        # Задержка на 3 секунды
        pygame.time.wait(3000)

    def update_game(self):
        """Обновление игры с учётом текущего времени."""

        # Получаем текущее время
        now = pygame.time.get_ticks()

        # Если прошло достаточно времени, падаем на один шаг
        if now - self.last_fall_time > self.fall_speed:
            self.drop_tetromino()
            self.last_fall_time = now

    def draw_grid(self):
        """Рисует сетку поля."""

        # Рисуем сетку на экране
        for y in range(ROWS):
            for x in range(COLUMNS):
                rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
                pygame.draw.rect(self.screen, GREY, rect, 1)

    def draw_tetromino(self, tetromino):
        """Рисует падающую фигуру."""

        # Рисуем каждый блок фигуры
        for x, y in tetromino.get_positions():
            if y >= 0:  # Игнорируем блоки, которые за пределами экрана
                rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
                pygame.draw.rect(self.screen, tetromino.color, rect)

    def draw_level(self):
        """Рисует текущие зафиксированные блоки."""

        # Рисуем блоки на экране
        for y in range(ROWS):
            for x in range(COLUMNS):
                if self.level.grid[y][x]:
                    rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
                    pygame.draw.rect(self.screen, self.level.grid[y][x], rect)

    def render(self):
        """Отображает всю информацию на экране."""

        # Заполнение экрана чёрным цветом
        self.screen.fill(BLACK)

        # Рисуем сетку, зафиксированные блоки и текущую падающую фигуру
        self.draw_grid()
        self.draw_level()
        self.draw_tetromino(self.falling_tetromino)

        # Отображение счёта
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))

        # Отображение уровня
        level_text = font.render(f"Level: {self.player_level}", True, WHITE)
        self.screen.blit(level_text, (SCREEN_WIDTH - level_text.get_width() - 10, 10))

        # Обновление экрана
        pygame.display.flip()

    def run(self):
        """Запуск игрового цикла."""

        while self.running:
            self.handle_events()  # Обработка событий
            self.update_game()  # Обновление игры
            self.render()  # Отображение на экране
            self.clock.tick(60)  # Ограничение FPS (60 кадров в секунду)
