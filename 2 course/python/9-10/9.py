class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

class MazeSolver:
    def __init__(self, maze):
        self.maze = maze
        self.rows = len(maze)
        self.cols = len(maze[0]) if self.rows > 0 else 0
        self.visited = [[False for _ in range(self.cols)] for _ in range(self.rows)]
        self.stack = Stack()
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Вверх, вниз, влево, вправо

    def is_valid(self, row, col):
        return (0 <= row < self.rows and
                0 <= col < self.cols and
                self.maze[row][col] == 1 and
                not self.visited[row][col])

    def solve_maze(self, start_row, start_col, end_row, end_col):
        if not self.is_valid(start_row, start_col) or not self.is_valid(end_row, end_col):
            return None

        self.stack.push((start_row, start_col))
        self.visited[start_row][start_col] = True

        while not self.stack.is_empty():
            current = self.stack.peek()
            if current == (end_row, end_col):
                return list(self.stack.items)

            found = False
            for dr, dc in self.directions:
                next_row, next_col = current[0] + dr, current[1] + dc
                if self.is_valid(next_row, next_col):
                    self.stack.push((next_row, next_col))
                    self.visited[next_row][next_col] = True
                    found = True
                    break

            if not found:
                self.stack.pop()

        return None

def print_maze(maze):
    for row in maze:
        print(' '.join(str(cell) for cell in row))

def main():
    # 1 - проходимый квадрат, 0 - непроходимый
    maze = [
        [1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1],
        [1, 0, 0, 1, 0],
        [1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1]
    ]

    print("Лабиринт:")
    print_maze(maze)

    solver = MazeSolver(maze)
    start = (0, 0)  # начальная точка
    end = (4, 4)     # конечная точка

    path = solver.solve_maze(*start, *end)

    if path:
        print("\nНайденный путь:")
        for step in path:
            print(step)
    else:
        print("\nПуть не найден")

if __name__ == "__main__":
    main()
