from settings import *

class Level:
    def __init__(self):
        # Инициализация уровня (сетка для хранения блоков)
        self.grid = [[None for _ in range(COLUMNS)] for _ in range(ROWS)]

    def add_tetromino(self, tetromino):
        # Добавляет тетромино в сетку
        for x, y in tetromino.get_positions():
            if 0 <= y < ROWS and 0 <= x < COLUMNS:
                self.grid[y][x] = tetromino.color

    def is_row_full(self, row):
        # Проверяет, заполнена ли строка
        return all(self.grid[row])

    def clear_full_rows(self):
        # Очищает полные строки и возвращает количество очищенных строк
        cleared = 0
        for y in range(ROWS):
            if self.is_row_full(y):
                # Удаление строки и добавление новой пустой в начало
                self.grid.pop(y)
                self.grid.insert(0, [None for _ in range(COLUMNS)])
                cleared += 1
        return cleared

    def check_collision(self, tetromino):
        # Проверяет столкновение тетромино с другими блоками или границами
        for x, y in tetromino.get_positions():
            if x < 0 or x >= COLUMNS or y >= ROWS or (y >= 0 and self.grid[y][x]):
                return True
        return False