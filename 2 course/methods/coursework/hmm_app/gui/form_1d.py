import tkinter as tk
from tkinter import ttk, messagebox, IntVar, Canvas
import colorsys

class PoliteNumbersVisualizer(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Вежливые цифры: визуализация")
        self.geometry("900x700")
        self.configure(bg="#1e1e1e")
        self.parent = parent
        
        # Настройки по умолчанию
        self.colors_size = 100
        self.square_size = 25
        self.render_type = tk.StringVar(value="Замощение плоскости")
        self.show_values = IntVar(value=1)
        self.color_mode = tk.StringVar(value="Радуга")

        # Фиксированные размеры области визуализации
        self.vis_width = 650
        self.vis_height = 550

        # Цветовая схема
        self.bg_color = "#1e1e1e"
        self.panel_color = "#252526"
        self.button_color = "#333333"
        self.text_color = "#d4d4d4"
        self.highlight_color = "#3e3e42"

        self.setup_styles()
        self.init_ui()
        self.generate_palette()
        self.update_render()


    def setup_styles(self):
        self.style = ttk.Style()
        self.style.theme_use('clam')

        self.style.configure(".", background=self.panel_color,
                            foreground=self.text_color,
                            font=('Segoe UI', 10))

        self.style.configure("TFrame", background=self.panel_color)
        self.style.configure("TLabel", background=self.panel_color, 
                           foreground=self.text_color)
        self.style.configure("TButton", background=self.button_color,
                            borderwidth=1, relief="flat", padding=6)
        self.style.map("TButton",
                      background=[("active", self.highlight_color)],
                      relief=[("pressed", "sunken")])

        self.style.configure("TCombobox", fieldbackground=self.button_color,
                           selectbackground=self.highlight_color)
        self.style.configure("TCheckbutton", background=self.panel_color)
        self.style.configure("TEntry", fieldbackground=self.button_color)

    def init_ui(self):
        # Основной контейнер
        main_frame = ttk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Панель управления
        control_frame = ttk.Frame(main_frame, width=220)
        control_frame.pack(side="left", fill="y", padx=(0, 10))

        # Заголовок
        title = ttk.Label(control_frame, text="Вежливые цифры",
                         font=('Segoe UI', 12, 'bold'))
        title.pack(pady=(10, 20))

        # Элементы управления
        ttk.Label(control_frame, text="Тип визуализации").pack(anchor="w", pady=(0, 5))
        types = ttk.Combobox(control_frame,
                            values=["Замощение плоскости", "Квадратная спираль", "Диагональная спираль"],
                            textvariable=self.render_type)
        types.pack(fill="x", pady=(0, 15))

        ttk.Label(control_frame, text="Цветовая схема").pack(anchor="w", pady=(0, 5))
        ttk.Combobox(control_frame,
                    values=["Радуга", "Земляные тона", "Черно-белый", "Зеленый градиент"],
                    textvariable=self.color_mode).pack(fill="x", pady=(0, 15))

        ttk.Label(control_frame, text="Количество цветов (2-200)").pack(anchor="w", pady=(0, 5))
        self.colors_entry = ttk.Entry(control_frame)
        self.colors_entry.insert(0, str(self.colors_size))
        self.colors_entry.pack(fill="x", pady=(0, 15))

        ttk.Label(control_frame, text="Размер квадрата (10-40)").pack(anchor="w", pady=(0, 5))
        self.size_entry = ttk.Entry(control_frame)
        self.size_entry.insert(0, str(self.square_size))
        self.size_entry.pack(fill="x", pady=(0, 15))

        ttk.Checkbutton(control_frame, text="Показать значения",
                       variable=self.show_values).pack(anchor="w", pady=(0, 20))

        ttk.Button(control_frame, text="Обновить визуализацию",
                  command=self.update_render).pack(fill="x", pady=5)

        ttk.Button(control_frame, text="Справка",
                  command=self.about_app).pack(fill="x", pady=5)

        ttk.Button(control_frame, text="Выход",
                  command=self.destroy).pack(fill="x", pady=(5, 0))

        # Область визуализации
        vis_frame = ttk.Frame(main_frame)
        vis_frame.pack(side="right", fill="both", expand=True)

        # Шкала цветов
        self.color_scale = Canvas(vis_frame, height=30, bg=self.panel_color,
                                bd=0, highlightthickness=0)
        self.color_scale.pack(fill="x", pady=(0, 10))

        self.canvas = Canvas(vis_frame, width=self.vis_width, height=self.vis_height,
                           bg=self.bg_color, bd=0, highlightthickness=0)
        self.canvas.pack()

    def about_app(self):
        about_window = tk.Toplevel(self)
        about_window.title("О программе")
        about_window.geometry("500x480")
        about_window.resizable(False, False)
        about_window.configure(bg=self.panel_color)

        title_label = ttk.Label(about_window,
                                text="Вежливые цифры: визуализация",
                                font=('Segoe UI', 14, 'bold'))
        title_label.pack(pady=(15, 10))

        version_label = ttk.Label(about_window,
                                  text="         Версия 1.0\nАвтор: [Устьянцев Макар]",
                                  font=('Segoe UI', 10))
        version_label.pack(pady=(0, 20))

        desc_text = """Эта программа визуализирует вежливые цифры (полиморфные числа)
различными способами с использованием цветовых схем.

Вежливые цифры - это числа, которые можно представить в виде суммы
последовательных натуральных чисел. Например:
5 = 2 + 3
9 = 4 + 5 или 2 + 3 + 4

Доступные типы визуализации:
1. Замощение плоскости - числа заполняются слева направо,
сверху вниз (последовательно)
2. Квадратная спираль - классическая спираль, растущая из центра
3. Диагональная спираль - спираль, растущая по диагонали

Цветовые схемы:
- Радуга: яркие цвета спектра
- Земляные тона: природные оттенки
- Черно-белый: градации серого
- Зеленый градиент: плавные зеленые оттенки"""

        desc_label = ttk.Label(about_window,
                               text=desc_text,
                               justify=tk.LEFT)
        desc_label.pack(pady=(0, 20), padx=20, anchor="w")

        close_button = ttk.Button(about_window,
                                  text="Закрыть",
                                  command=about_window.destroy)
        close_button.pack(pady=(10, 15))

    def generate_palette(self):
        self.palette = []
        color_mode = self.color_mode.get()

        if color_mode == "Черно-белый":
            for i in range(self.colors_size):
                value = int(255 * (i / (self.colors_size - 1)))
                self.palette.append(f'#{value:02x}{value:02x}{value:02x}')
        elif color_mode == "Земляные тона":
            for i in range(self.colors_size):
                hue = 0.1 + 0.15 * (i / self.colors_size)
                saturation = 0.5 + 0.3 * (i / self.colors_size)
                value = 0.4 + 0.5 * (i / self.colors_size)
                r, g, b = colorsys.hsv_to_rgb(hue, saturation, value)
                self.palette.append(f'#{int(r * 255):02x}{int(g * 255):02x}{int(b * 255):02x}')
        elif color_mode == "Зеленый градиент":
            for i in range(self.colors_size):
                intensity = i / self.colors_size
                r, g, b = 0, int(100 + 155 * intensity), int(200 * intensity)
                self.palette.append(f'#{r:02x}{g:02x}{b:02x}')
        else:  # Радуга
            for i in range(self.colors_size):
                hue = i / self.colors_size
                r, g, b = colorsys.hsv_to_rgb(hue, 0.9, 0.9)
                self.palette.append(f'#{int(r * 255):02x}{int(g * 255):02x}{int(b * 255):02x}')

        self.update_color_scale()

    def update_color_scale(self):
        self.color_scale.delete("all")
        width = self.color_scale.winfo_width()
        if width < 2 or not self.palette:
            return

        color_width = width / len(self.palette)
        for i, color in enumerate(self.palette):
            x0 = i * color_width
            x1 = x0 + color_width
            self.color_scale.create_rectangle(x0, 0, x1, 30, fill=color, outline="")

    def is_polite_number(self, n):
        if n == 0:
            return False
        # число является вежливым, если оно не является степенью двойки
        return (n & (n - 1)) != 0

    def get_color_for_number(self, num):
        if self.is_polite_number(num):
            index = num % self.colors_size
            return self.palette[index]
        else:
            return "#000000"  # черный цвет для "грубых" чисел

    def update_render(self):
        try:
            self.colors_size = int(self.colors_entry.get())
            self.square_size = int(self.size_entry.get())

            if not (2 <= self.colors_size <= 200):
                raise ValueError("Количество цветов должно быть от 2 до 200")
            if not (10 <= self.square_size <= 40):
                raise ValueError("Размер квадрата должен быть от 10 до 40")
        except ValueError as e:
            messagebox.showerror("Ошибка", str(e))
            return

        self.generate_palette()
        self.canvas.delete("all")

        render_type = self.render_type.get()
        if render_type == "Замощение плоскости":
            self.render_sequence()
        elif render_type == "Квадратная спираль":
            self.render_square_spiral()
        elif render_type == "Диагональная спираль":
            self.render_diagonal_spiral()

    def render_sequence(self):
        scaled_size = self.square_size
        cols = int(self.vis_width / scaled_size)
        rows = int(self.vis_height / scaled_size)
        total = cols * rows
        x, y = 0, 0

        for i in range(1, total + 1):
            color = self.get_color_for_number(i)
            self.canvas.create_rectangle(x, y, x + scaled_size, y + scaled_size,
                                         fill=color, outline=self.panel_color, width=1)
            if self.show_values.get():
                self.canvas.create_text(x + scaled_size / 2, y + scaled_size / 2,
                                        text=str(i), fill="white" if self.is_dark(color) else "black",
                                        font=("Segoe UI", max(8, int(scaled_size / 4))))
            x += scaled_size
            if x + scaled_size > self.vis_width:
                x = 0
                y += scaled_size

    def render_square_spiral(self):
        scaled_size = self.square_size
        center_x = self.vis_width // 2
        center_y = self.vis_height // 2

        x, y = center_x, center_y
        step = 1
        direction = 0  # 0 - вправо, 1 - вверх, 2 - влево, 3 - вниз
        steps_in_direction = 1
        direction_changes = 0
        max_squares = (self.vis_width * self.vis_height) // (scaled_size * scaled_size)

        for n in range(1, max_squares):
            color = self.get_color_for_number(n)

            if (0 <= x < self.vis_width - scaled_size and
                    0 <= y < self.vis_height - scaled_size):
                self.canvas.create_rectangle(x, y, x + scaled_size, y + scaled_size,
                                             fill=color, outline=self.panel_color, width=1)
                if self.show_values.get():
                    self.canvas.create_text(x + scaled_size / 2, y + scaled_size / 2,
                                            text=str(n),
                                            fill="white" if self.is_dark(color) else "black",
                                            font=("Segoe UI", max(8, int(scaled_size / 4))))

            # Движение по спирали
            if direction == 0:
                x += scaled_size
            elif direction == 1:
                y -= scaled_size
            elif direction == 2:
                x -= scaled_size
            elif direction == 3:
                y += scaled_size

            step += 1

            if step > steps_in_direction:
                step = 1
                direction = (direction + 1) % 4
                direction_changes += 1

                if direction_changes % 2 == 0:
                    steps_in_direction += 1

    def render_diagonal_spiral(self):
        scaled_size = self.square_size
        center_x = self.vis_width // 2
        center_y = self.vis_height // 2

        x, y = center_x, center_y
        step = 1
        direction = 0  # 0 - вправо-вниз, 1 - влево-вниз, 2 - влево-вверх, 3 - вправо-вверх
        steps_in_direction = 1
        direction_changes = 0
        max_squares = (self.vis_width * self.vis_height) // (scaled_size * scaled_size)

        for n in range(1, max_squares):
            color = self.get_color_for_number(n)

            if (0 <= x < self.vis_width - scaled_size and
                    0 <= y < self.vis_height - scaled_size):
                self.canvas.create_rectangle(x, y, x + scaled_size, y + scaled_size,
                                             fill=color, outline=self.panel_color, width=1)
                if self.show_values.get():
                    self.canvas.create_text(x + scaled_size / 2, y + scaled_size / 2,
                                            text=str(n),
                                            fill="white" if self.is_dark(color) else "black",
                                            font=("Segoe UI", max(8, int(scaled_size / 4))))

            # движение по диагональной спирали
            if direction == 0:
                x += scaled_size
                y += scaled_size
            elif direction == 1:
                x -= scaled_size
                y += scaled_size
            elif direction == 2:
                x -= scaled_size
                y -= scaled_size
            elif direction == 3:
                x += scaled_size
                y -= scaled_size

            step += 1

            if step > steps_in_direction:
                step = 1
                direction = (direction + 1) % 4
                direction_changes += 1

                if direction_changes % 2 == 0:
                    steps_in_direction += 1

    def is_dark(self, color):
        if len(color) == 7:
            r = int(color[1:3], 16)
            g = int(color[3:5], 16)
            b = int(color[5:7], 16)
            return (r * 0.299 + g * 0.587 + b * 0.114) < 128
        return False


if __name__ == "__main__":
    app = PoliteNumbersVisualizer()
    app.mainloop()


