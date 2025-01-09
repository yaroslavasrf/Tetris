import pygame

#параметры клетчатого поля
COLUMNS = 10
ROWS = 20
CELL_SIZE = 40

# ширина поверхностей с доп информацией
ADDITIONALLY_WIDTH = 200

# отступы между поверхностями
INDENT = 20

# параметры игры
TETRIS_GAME_SIZE = COLUMNS * CELL_SIZE, ROWS * CELL_SIZE
TETRIS_GAME_WIDTH = COLUMNS * CELL_SIZE
TETRIS_GAME_HEIGHT = ROWS * CELL_SIZE

# параметры окна
WINDOW_SIZE = TETRIS_GAME_WIDTH + ADDITIONALLY_WIDTH + INDENT * 3, TETRIS_GAME_HEIGHT + INDENT * 2
WINDOW_WIDTH = TETRIS_GAME_WIDTH + ADDITIONALLY_WIDTH + INDENT * 3
WINDOW_HEIGHT = TETRIS_GAME_HEIGHT + INDENT * 2

PREVIEW_HEIGHT = 0.6
SCORE_HEIGHT = 1 - PREVIEW_HEIGHT

# смещение
START_POS_BLOCK_X = 4
START_POS_BLOCK_Y = 1

# цвета
BACKGROUND_COLOR = '#49423d'

YELLOW = '#FFDB8B'
PINK = '#E4717A'
PURPLE = '#A18594'
BLUE = '#5D9B9B'

WHITE = '#ffffff'


COLORS = [YELLOW, PINK, PURPLE, BLUE]
SHAPES = {
    'T': {'shape': [(0, 0), (-1, 0), (1, 0), (0, -1)]},
    'O': {'shape': [(0, 0), (0, -1), (1, 0), (1, -1)]},
    'J': {'shape': [(0, 0), (0, -1), (0, 1), (-1, 1)]},
    'L': {'shape': [(0, 0), (0, -1), (0, 1), (1, 1)]},
    'I': {'shape': [(0, 0), (0, -1), (0, -2), (0, 1)]},
    'S': {'shape': [(0, 0), (-1, 0), (0, -1), (1, -1)]},
    'Z': {'shape': [(0, 0), (1, 0), (0, -1), (-1, -1)]}
}


SCORE_DATA = {1: 40, 2: 100, 3: 300, 4: 1200}

