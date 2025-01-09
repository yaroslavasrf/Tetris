import random

import pygame.key

from timer import Timer
from data import *

class TetrisGame:
    def __init__(self, main_surface):
        self.tetris_game_surface = pygame.Surface(TETRIS_GAME_SIZE)
        self.main_surface = main_surface

        self.all_sprites = pygame.sprite.Group()

        self.shape = Shape(random.choice(list(SHAPES.keys())), self.all_sprites)






    def run(self, change_y):
        self.main_surface.blit(self.tetris_game_surface, (INDENT, INDENT))

        self.tetris_game_surface.fill(BACKGROUND_COLOR)
        self.field_display()
        self.pressed()

        self.all_sprites.draw(self.tetris_game_surface)
        self.free_fall(change_y)

    def free_fall(self, change_y):
        self.shape.free_fall(change_y)

    def pressed(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.shape.move_side(-1)
        if keys[pygame.K_RIGHT]:
            self.shape.move_side(1)

    def field_display(self):
        for col in range(COLUMNS):
            for row in range(ROWS):
                coords = (col * CELL_SIZE, row * CELL_SIZE,
                          CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(self.tetris_game_surface, WHITE, coords, 1)
        pygame.draw.rect(self.tetris_game_surface, WHITE, (0, 0, TETRIS_GAME_WIDTH, TETRIS_GAME_HEIGHT), 1)

class Shape:
    def __init__(self, shape, group):
        self.positions = SHAPES[shape]['shape']
        self.color = random.choice(COLORS)
        self.group = group
        self.create_shape()

    def create_shape(self):
        self.blocks = []
        for pos in self.positions:
            self.blocks.append(Block(self.group, pos, self.color))


    def free_fall(self, change_y):
        for block in self.blocks:
            block.update_y(change_y)

    def move_side(self, change_x):
        for block in self.blocks:
            block.x += change_x






class Block(pygame.sprite.Sprite):
    def __init__(self, group, pos, color):
        super().__init__(group)
        self.image = pygame.Surface((CELL_SIZE + 2, CELL_SIZE + 2))
        self.image.fill(color)

        self.x = (pos[0] + START_POS_BLOCK_X) * CELL_SIZE - 1
        self.y = (pos[1] + START_POS_BLOCK_Y) * CELL_SIZE - 1
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def update_y(self, change_y):
        self.rect = self.image.get_rect(topleft=(self.x, self.y + change_y * CELL_SIZE))


