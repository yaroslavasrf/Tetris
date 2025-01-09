from data import *

class Score:
	def __init__(self, main_surface):
		self.score_surface = pygame.Surface((ADDITIONALLY_WIDTH, TETRIS_GAME_HEIGHT * SCORE_HEIGHT - INDENT))
		self.main_surface = main_surface

	def run(self):
		self.main_surface.blit(self.score_surface, (INDENT * 2 + TETRIS_GAME_WIDTH, INDENT))
		self.score_surface.fill(BACKGROUND_COLOR)


class Previous:
	def __init__(self, main_surface):
		self.previous_surface = pygame.Surface((ADDITIONALLY_WIDTH, TETRIS_GAME_HEIGHT * PREVIEW_HEIGHT - INDENT))
		self.main_surface = main_surface

	def run(self):
		self.main_surface.blit(self.previous_surface, (INDENT * 2 + TETRIS_GAME_WIDTH, INDENT * 2 + SCORE_HEIGHT * TETRIS_GAME_HEIGHT))
		self.previous_surface.fill(BACKGROUND_COLOR)
