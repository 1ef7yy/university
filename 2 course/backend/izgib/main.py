import pygame
import random
import sys


class GameObject:
    def __init__(self, position=(0, 0)):
        self.position = position
        self.body_color = None

    def draw(self, surface):
        pass


class Apple(GameObject):
    def __init__(self, position=(0, 0)):
        super().__init__(position)
        self.body_color = (255, 0, 0)
        self.randomize_position()

    def randomize_position(self):
        self.position = (
            random.randint(0, 31) * 20,
            random.randint(0, 23) * 20
        )

    def draw(self, surface):
        rect = pygame.Rect(
            (self.position[0], self.position[1]),
            (20, 20)
        )
        pygame.draw.rect(surface, self.body_color, rect)
        pygame.draw.rect(surface, (0, 0, 0), rect, 1)


class Snake(GameObject):
    def __init__(self, position=(320, 240)):
        super().__init__(position)
        self.body_color = (0, 255, 0)
        self.length = 1
        self.positions = [position]
        self.direction = (20, 0)
        self.next_direction = None

    def update_direction(self):
        if self.next_direction:
            self.direction = self.next_direction
            self.next_direction = None

    def move(self):
        head_x, head_y = self.get_head_position()
        dir_x, dir_y = self.direction
        new_x = (head_x + dir_x) % 640
        new_y = (head_y + dir_y) % 480

        self.positions.insert(0, (new_x, new_y))

        if len(self.positions) > self.length:
            self.positions.pop()

    def get_head_position(self):
        return self.positions[0]

    def reset(self):
        self.length = 1
        self.positions = [(320, 240)]
        self.direction = (20, 0)
        self.next_direction = None

    def draw(self, surface):
        for position in self.positions:
            rect = pygame.Rect(
                (position[0], position[1]),
                (20, 20)
            )
            pygame.draw.rect(surface, self.body_color, rect)
            pygame.draw.rect(surface, (0, 0, 0), rect, 1)


def handle_keys(snake):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.direction != (0, 20):
                snake.next_direction = (0, -20)
            elif event.key == pygame.K_DOWN and snake.direction != (0, -20):
                snake.next_direction = (0, 20)
            elif event.key == pygame.K_LEFT and snake.direction != (20, 0):
                snake.next_direction = (-20, 0)
            elif event.key == pygame.K_RIGHT and snake.direction != (-20, 0):
                snake.next_direction = (20, 0)


def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('Изгиб Питона')
    clock = pygame.time.Clock()

    snake = Snake()
    apple = Apple()

    while True:
        handle_keys(snake)
        snake.update_direction()
        snake.move()

        if snake.get_head_position() == apple.position:
            snake.length += 1
            apple.randomize_position()
            while apple.position in snake.positions:
                apple.randomize_position()

        head = snake.get_head_position()
        if head in snake.positions[1:]:
            snake.reset()

        screen.fill((0, 0, 0))
        snake.draw(screen)
        apple.draw(screen)

        pygame.display.update()
        clock.tick(10)


if __name__ == "__main__":
    main()
