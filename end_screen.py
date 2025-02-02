# Импортируем pygame для создания экрана окончания игры

import pygame

# Класс экрана окончания игры
class EndScreen:
    def __init__(self, screen, score):
        # Инициализация экрана
        self.screen = screen
        self.score = score
    def display(self):

        # Заливаем экран черным цветом
        self.screen.fill((0, 0, 0))
        # Создаем шрифт для текста
        font = pygame.font.Font("HowardFatRegular.ttf", 36)
        # Рисуем сообщение об окончании игры и текущий счет
        end_text = font.render(f"Game Over! Score: {self.score}", True, (255, 255, 255))
        # Рисуем инструкции для пользователя (перезапуск или выход)
        restart_text_1 = font.render("Press R to restart", True, (255, 255, 255))
        restart_text_2 = font.render("or Q to quit", True, (255, 255, 255))
        # Отображаем тексты на экране
        self.screen.blit(end_text, (15, 200))
        self.screen.blit(restart_text_1, (20, 300))
        self.screen.blit(restart_text_2, (20, 350))
        # Обновляем экран
        pygame.display.flip()

        # Ожидаем нажатие клавиш от пользователя
        while True:
            for event in pygame.event.get():
                # Закрытие игры
                if event.type == pygame.QUIT:
                    return False
                # Перезапуск игры при нажатии 'R'
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        with open("data.txt", "w") as file:
                            file.write('')
                        return 'restart'


                    # Выход из игры при нажатии 'Q'
                    elif event.key == pygame.K_q:
                        return False
