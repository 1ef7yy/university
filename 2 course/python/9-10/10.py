import pygame
import random
import sys
from abc import ABC, abstractmethod

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Гонки - Лабораторная работа №10")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (100, 100, 100)
YELLOW = (255, 255, 0)

class GameObject(ABC):
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    @abstractmethod
    def draw(self, screen):
        pass

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

class Car(GameObject):
    def __init__(self):
        super().__init__(
            x=SCREEN_WIDTH // 2 - 25,
            y=SCREEN_HEIGHT - 100,
            width=50,
            height=80,
            color=BLUE
        )
        self.speed = 5

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        # Рисуем "окна" машины
        pygame.draw.rect(screen, WHITE, (self.x + 5, self.y + 15, self.width - 10, 20))
        pygame.draw.rect(screen, WHITE, (self.x + 5, self.y + 45, self.width - 10, 20))

    def move(self, direction):
        if direction == "left" and self.x > 50:
            self.x -= self.speed
        if direction == "right" and self.x < SCREEN_WIDTH - self.width - 50:
            self.x += self.speed
        if direction == "up" and self.y > 0:
            self.y -= self.speed
        if direction == "down" and self.y < SCREEN_HEIGHT - self.height:
            self.y += self.speed

class Obstacle(GameObject):
    def __init__(self, x, y, width, height, color, speed):
        super().__init__(x, y, width, height, color)
        self.speed = speed

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def move(self):
        self.y += self.speed

    def is_off_screen(self):
        return self.y > SCREEN_HEIGHT

class Rock(Obstacle):
    def __init__(self, x, y):
        super().__init__(x, y, 60, 60, GRAY, 4)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x + self.width//2, self.y + self.height//2), self.width//2)

class OilPuddle(Obstacle):
    def __init__(self, x, y):
        super().__init__(x, y, 80, 40, BLACK, 2)

    def draw(self, screen):
        pygame.draw.ellipse(screen, self.color, (self.x, self.y, self.width, self.height))

class Cone(Obstacle):
    def __init__(self, x, y):
        super().__init__(x, y, 30, 50, YELLOW, 3)

    def draw(self, screen):
        pygame.draw.polygon(screen, self.color, [
            (self.x + self.width//2, self.y),
            (self.x, self.y + self.height),
            (self.x + self.width, self.y + self.height)
        ])

class FinishLine(GameObject):
    def __init__(self):
        super().__init__(50, -1000, SCREEN_WIDTH - 100, 20, GREEN)
        self.speed = 3

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        # шахматный рисунок на финише
        for i in range(0, int(self.width), 40):
            for j in range(0, int(self.height), 20):
                if (i//40 + j//20) % 2 == 0:
                    pygame.draw.rect(screen, WHITE, (self.x + i, self.y + j, 20, 10))

    def move(self):
        self.y += self.speed

    def is_reached(self, car):
        return car.y < self.y

class Menu:
    def __init__(self):
        self.font = pygame.font.SysFont('Arial', 36)
        self.options = ["Начать игру", "Инструкция", "Выход"]
        self.selected = 0

    def draw(self, screen):
        screen.fill(BLACK)
        title = self.font.render("ГОНКИ - Лабораторная работа №10", True, WHITE)
        screen.blit(title, (SCREEN_WIDTH//2 - title.get_width()//2, 100))

        for i, option in enumerate(self.options):
            color = RED if i == self.selected else WHITE
            text = self.font.render(option, True, color)
            screen.blit(text, (SCREEN_WIDTH//2 - text.get_width()//2, 200 + i * 50))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "exit"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    self.selected = (self.selected + 1) % len(self.options)
                if event.key == pygame.K_UP:
                    self.selected = (self.selected - 1) % len(self.options)
                if event.key == pygame.K_RETURN:
                    return self.options[self.selected].lower()
        return None

class RacingGame:
    def __init__(self):
        self.car = Car()
        self.obstacles = []
        self.finish_line = FinishLine()
        self.score = 0
        self.game_over = False
        self.font = pygame.font.SysFont('Arial', 36)
        self.clock = pygame.time.Clock()
        self.obstacle_types = [Rock, OilPuddle, Cone]
        self.spawn_timer = 0
        self.road_offset = 0

    def spawn_obstacle(self):
        x = random.randint(50, SCREEN_WIDTH - 110)
        obstacle_class = random.choice(self.obstacle_types)
        self.obstacles.append(obstacle_class(x, -100))

    def update(self):
        if self.game_over:
            return

        self.road_offset = (self.road_offset + 3) % 40

        self.finish_line.move()

        # спавн препятствий
        self.spawn_timer += 1
        if self.spawn_timer >= 60:
            self.spawn_obstacle()
            self.spawn_timer = 0

        # движение препятствий
        for obstacle in self.obstacles[:]:
            obstacle.move()
            if obstacle.is_off_screen():
                self.obstacles.remove(obstacle)
                self.score += 1

            # Проверка столкновений
            if self.car.get_rect().colliderect(obstacle.get_rect()):
                self.game_over = True

        # проверка достижения финиша
        if self.finish_line.is_reached(self.car):
            self.game_over = True
            self.score += 100

    def draw(self, screen):
        screen.fill(WHITE)

        # рисуем дорогу с эффектом движения
        pygame.draw.rect(screen, (100, 100, 100), (50, 0, SCREEN_WIDTH - 100, SCREEN_HEIGHT))
        for i in range(-40, SCREEN_HEIGHT, 40):
            pygame.draw.rect(screen, (150, 150, 150), (SCREEN_WIDTH//2 - 5, i + self.road_offset, 10, 20))

        self.car.draw(screen)

        for obstacle in self.obstacles:
            obstacle.draw(screen)

        self.finish_line.draw(screen)

        score_text = self.font.render(f"Очки: {self.score}", True, BLACK)
        screen.blit(score_text, (10, 10))

        if self.game_over:
            if self.finish_line.is_reached(self.car):
                message = "Победа! Нажмите R для рестарта"
            else:
                message = "Авария! Нажмите R для рестарта"

            game_over_text = self.font.render(message, True, RED)
            screen.blit(game_over_text, (SCREEN_WIDTH//2 - game_over_text.get_width()//2, SCREEN_HEIGHT//2))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and self.game_over:
                    self.__init__()  # Рестарт игры

        if not self.game_over:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.car.move("left")
            if keys[pygame.K_RIGHT]:
                self.car.move("right")
            if keys[pygame.K_UP]:
                self.car.move("up")
            if keys[pygame.K_DOWN]:
                self.car.move("down")

        return True

    def show_instructions(self):
        running = True
        while running:
            screen.fill(BLACK)

            title = self.font.render("Инструкция", True, WHITE)
            screen.blit(title, (SCREEN_WIDTH//2 - title.get_width()//2, 50))

            lines = [
                "Управление:",
                "← → - движение влево/вправо",
                "↑ ↓ - движение вверх/вниз",
                "",
                "Цель игры:",
                "Доехать до финиша (зеленая полоса),",
                "избегая столкновений с препятствиями.",
                "",
                "Нажмите ESC для возврата в меню"
            ]

            for i, line in enumerate(lines):
                text = self.font.render(line, True, WHITE)
                screen.blit(text, (SCREEN_WIDTH//2 - text.get_width()//2, 120 + i * 40))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "exit"
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

        return None

    def run(self):
        menu = Menu()
        current_screen = "menu"

        running = True
        while running:
            if current_screen == "menu":
                menu_result = menu.handle_events()
                if menu_result == "начать игру":
                    current_screen = "game"
                    self.__init__()
                elif menu_result == "инструкция":
                    current_screen = "instructions"
                elif menu_result == "выход" or menu_result == "exit":
                    running = False

                menu.draw(screen)

            elif current_screen == "instructions":
                result = self.show_instructions()
                if result == "exit":
                    running = False
                else:
                    current_screen = "menu"

            elif current_screen == "game":
                if not self.handle_events():
                    running = False
                self.update()
                self.draw(screen)

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = RacingGame()
    game.run()
