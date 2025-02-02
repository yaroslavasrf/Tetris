import pygame

class Score:
    def __init__(self):
        # Инициализация счётчика очков
        self.score = 0

    def add_score(self, lines_cleared):
        # Добавление очков за очищенные строки
        self.score += lines_cleared * 100

    def draw(self, screen):
        # Отображение счёта на экране
        font = pygame.font.Font("HowardFatRegular.ttf", 36)  # Шрифт для текста
        score_text = font.render(f"Score: {self.score}", True, (255, 255, 255))  # Рендеринг текста
        screen.blit(score_text, (10, 10))  # Отображение текста на экране

    def save_score(self):
        # Сохранение счёта в файл
        with open('data.txt', 'a') as f:
            f.write(f"Score: {self.score}\n")
