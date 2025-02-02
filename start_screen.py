# Импортируем pygame для создания экрана начала игры
import pygame

# Класс экрана начала игры
class StartScreen:
    def __init__(self, screen):
        # Инициализация экрана
        self.screen = screen

    def display(self):
        # Заливаем экран черным цветом
        self.screen.fill((0, 0, 0))
        # Создаем шрифт для текста
        font = pygame.font.Font("HowardFatRegular.ttf", 36)
        # Рисуем заголовок игры
        title_text = font.render("TETRIS", True, (255, 255, 255))
        # Рисуем сообщение о начале игры
        start_text = font.render("Press any key to start", True, (255, 255, 255))
        # Отображаем текст на экране
        self.screen.blit(title_text, (100, 200))
        self.screen.blit(start_text, (20, 300))
        # Обновляем экран
        pygame.display.flip()

        # Ожидаем события от пользователя
        while True:
            for event in pygame.event.get():
                # Закрытие игры
                if event.type == pygame.QUIT:
                    return False
                # Начало игры по нажатию любой клавиши
                if event.type == pygame.KEYDOWN:
                    return True
