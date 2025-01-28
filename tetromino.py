import random
from settings import *

class Tetromino:
    def __init__(self, shape):
        # Инициализация фигуры
        self.shape = shape  # Форма фигуры
        self.rotation = 0  # Начальный угол поворота
        self.x = COLUMNS // 2 - 2  # Начальная позиция по горизонтали
        self.y = 0  # Начальная позиция по вертикали
        self.color = random.choice(COLORS)  # Случайный выбор цвета

    def get_positions(self):
        # Возвращает список позиций блоков фигуры
        return [(self.x + x, self.y + y) for x, y in SHAPES[self.shape][self.rotation]]

