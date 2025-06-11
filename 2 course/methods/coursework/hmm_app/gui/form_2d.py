import tkinter as tk
from tkinter import ttk, messagebox
import math
import colorsys


class Object2DForm(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("2D Ker(|a+b| - |a-b|)")
        self.geometry("900x700")
        self.bind('<F1>', lambda event: self.show_about())

        # цветовая схема
        self.bg_color = "#1e1e1e"
        self.panel_color = "#252526"
        self.button_color = "#333333"
        self.text_color = "#d4d4d4"
        self.highlight_color = "#3e3e42"

        self.configure(bg=self.bg_color)
        self.style = ttk.Style()
        self.style.theme_use('clam')

        # настройка стилей
        self.setup_styles()

        self.aspect_ratio = 6
        self.x_min = -10
        self.x_max = 10
        self.y_min = -10
        self.y_max = 10
        self.a_param = 100
        self.b_param = 4
        self.colors_size = 100
        self.visualization_type = "Ker(|a+b|-|a-b|)"
        self.palette = []

        # создание интерфейса
        self.create_widgets()
        self.generate_palette()
        self.update_render()

    def setup_styles(self):
        self.style.configure(".", background=self.panel_color, foreground=self.text_color, font=('Segoe UI', 10))
        self.style.configure("TFrame", background=self.panel_color)
        self.style.configure("TLabel", background=self.panel_color, foreground=self.text_color)
        self.style.configure("TButton", background=self.button_color, borderwidth=1, relief="flat", padding=6)
        self.style.map("TButton", background=[("active", self.highlight_color)], relief=[("pressed", "sunken")])
        self.style.configure("TCombobox", fieldbackground=self.button_color, selectbackground=self.highlight_color)
        self.style.configure("TCheckbutton", background=self.panel_color)
        self.style.configure("TEntry", fieldbackground=self.button_color)
        self.style.configure("TLabelframe", background=self.panel_color, foreground=self.text_color)
        self.style.configure("TLabelframe.Label", background=self.panel_color, foreground=self.text_color)

    def create_widgets(self):
        main_frame = ttk.Frame(self)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # панель управления
        control_frame = ttk.Frame(main_frame, width=220)
        control_frame.pack(side="left", fill="y", padx=(0, 10))

        # заголовок
        title = ttk.Label(control_frame, text="2D Ker(|a+b| - |a-b|)", font=('Segoe UI', 12, 'bold'))
        title.pack(pady=(10, 20))

        # выбор типа визуализации
        ttk.Label(control_frame, text="Тип визуализации:").pack(anchor="w", pady=(0, 5))
        self.vis_combobox = ttk.Combobox(
            control_frame,
            values=["Ker(|a+b|-|a-b|)", "LenNOD(a,b)", "LenCH(a,b)"],
            state="readonly"
        )
        self.vis_combobox.set(self.visualization_type)
        self.vis_combobox.bind("<<ComboboxSelected>>", self.vis_type_changed)
        self.vis_combobox.pack(fill="x", pady=(0, 15))

        ttk.Label(control_frame, text="Количество цветов (2-200):").pack(anchor="w", pady=(0, 5))
        self.colors_entry = ttk.Entry(control_frame)
        self.colors_entry.insert(0, str(self.colors_size))
        self.colors_entry.pack(fill="x", pady=(0, 15))

        ttk.Label(control_frame, text="Параметр A:").pack(anchor="w", pady=(0, 5))
        self.a_entry = ttk.Entry(control_frame)
        self.a_entry.insert(0, str(self.a_param))
        self.a_entry.pack(fill="x", pady=(0, 5))

        ttk.Label(control_frame, text="Параметр B:").pack(anchor="w", pady=(0, 5))
        self.b_entry = ttk.Entry(control_frame)
        self.b_entry.insert(0, str(self.b_param))
        self.b_entry.pack(fill="x", pady=(0, 15))

        # Aspect
        ttk.Label(control_frame, text="Aspect:").pack(anchor="w", pady=(0, 5))
        self.aspect_entry = ttk.Entry(control_frame)
        self.aspect_entry.insert(0, str(self.aspect_ratio))
        self.aspect_entry.pack(fill="x", pady=(0, 15))

        # Диапазоны осей
        ttk.Label(control_frame, text="Диапазон осей:").pack(anchor="w", pady=(0, 5))

        frame_x = ttk.Frame(control_frame)
        frame_x.pack(fill="x", pady=(0, 5))
        ttk.Label(frame_x, text="X min:").pack(side="left")
        self.x_min_entry = ttk.Entry(frame_x, width=8)
        self.x_min_entry.insert(0, str(self.x_min))
        self.x_min_entry.pack(side="left", padx=(5, 0))

        ttk.Label(frame_x, text="max:").pack(side="left", padx=(5, 0))
        self.x_max_entry = ttk.Entry(frame_x, width=8)
        self.x_max_entry.insert(0, str(self.x_max))
        self.x_max_entry.pack(side="left")

        frame_y = ttk.Frame(control_frame)
        frame_y.pack(fill="x", pady=(0, 15))
        ttk.Label(frame_y, text="Y min:").pack(side="left")
        self.y_min_entry = ttk.Entry(frame_y, width=8)
        self.y_min_entry.insert(0, str(self.y_min))
        self.y_min_entry.pack(side="left", padx=(5, 0))

        ttk.Label(frame_y, text="max:").pack(side="left", padx=(5, 0))
        self.y_max_entry = ttk.Entry(frame_y, width=8)
        self.y_max_entry.insert(0, str(self.y_max))
        self.y_max_entry.pack(side="left")

        # Кнопки
        ttk.Button(control_frame, text="Обновить визуализацию", command=self.calculate).pack(fill="x", pady=5)
        ttk.Button(control_frame, text="Справка", command=self.show_about).pack(fill="x", pady=5)

        # Область визуализации
        vis_frame = ttk.Frame(main_frame)
        vis_frame.pack(side="right", fill="both", expand=True)

        # Шкала цветов
        self.color_scale = tk.Canvas(vis_frame, height=30, bg=self.panel_color, bd=0, highlightthickness=0)
        self.color_scale.pack(fill="x", pady=(0, 10))

        # Основной холст
        self.canvas = tk.Canvas(vis_frame, bg=self.bg_color, bd=0, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

    def generate_palette(self):
        self.palette = []
        for i in range(self.colors_size):
            hue = i / self.colors_size
            r, g, b = colorsys.hsv_to_rgb(hue, 0.9, 0.9)
            self.palette.append(f'#{int(r * 255):02x}{int(g * 255):02x}{int(b * 255):02x}')

    def update_render(self):
        self.update_color_scale()
        self.draw_points()

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

    def draw_points(self):
        self.canvas.delete("all")
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()

        if width <= 1 or height <= 1:
            return

        step_x = (self.x_max - self.x_min) / (width / self.aspect_ratio)
        step_y = (self.y_max - self.y_min) / (height / self.aspect_ratio)

        y = self.y_min
        while y <= self.y_max:
            x = self.x_min
            while x <= self.x_max:
                color = self.get_color_for_point(x, y)
                x_pixel = self.logical_x_to_pixel(x, width)
                y_pixel = self.logical_y_to_pixel(y, height)

                self.canvas.create_oval(
                    x_pixel - 3, y_pixel - 3,
                    x_pixel + 3, y_pixel + 3,
                    fill=color, outline=color
                )
                x += step_x
            y += step_y

        # Отрисовка осей
        self.render_axes(width, height)

    def render_axes(self, width, height):
        # Ось X
        y_pos = self.logical_y_to_pixel(0, height)
        self.canvas.create_line(0, y_pos, width, y_pos, fill=self.text_color, width=2)

        # Ось Y
        x_pos = self.logical_x_to_pixel(0, width)
        self.canvas.create_line(x_pos, 0, x_pos, height, fill=self.text_color, width=2)

        # Метки на оси X
        label_step_x = (self.x_max - self.x_min) / 10
        x = self.x_min
        while x <= self.x_max:
            if abs(x) < 1e-6:
                x += label_step_x
                continue

            x_pixel = self.logical_x_to_pixel(x, width)
            self.canvas.create_line(x_pixel, y_pos - 5, x_pixel, y_pos + 5, fill=self.text_color, width=1)

            # Текст метки
            text = f"{x:.1f}"
            self.canvas.create_text(
                x_pixel, y_pos + 10,
                text=text, fill=self.text_color,
                anchor=tk.CENTER
            )
            x += label_step_x

        # Метки на оси Y
        label_step_y = (self.y_max - self.y_min) / 10
        y = self.y_min
        x_pos = self.logical_x_to_pixel(0, width)
        while y <= self.y_max:
            if abs(y) < 1e-6:
                y += label_step_y
                continue

            y_pixel = self.logical_y_to_pixel(y, height)
            self.canvas.create_line(x_pos - 5, y_pixel, x_pos + 5, y_pixel, fill=self.text_color, width=1)

            # Текст метки
            text = f"{y:.1f}"
            self.canvas.create_text(
                x_pos - 10, y_pixel,
                text=text, fill=self.text_color,
                anchor=tk.E
            )
            y += label_step_y

    def logical_x_to_pixel(self, x, width):
        return int((x - self.x_min) / (self.x_max - self.x_min) * width)

    def logical_y_to_pixel(self, y, height):
        return int(height - (y - self.y_min) / (self.y_max - self.y_min) * height)

    def calculate(self):
        """Обновляет параметры и перерисовывает график на основе введенных данных."""
        try:
            # Обновляем параметры из полей ввода
            self.aspect_ratio = int(self.aspect_entry.get())
            self.a_param = float(self.a_entry.get())
            self.b_param = float(self.b_entry.get())
            self.colors_size = int(self.colors_entry.get())

            # Проверка допустимости значений
            if self.colors_size < 2 or self.colors_size > 200:
                raise ValueError("Количество цветов должно быть от 2 до 200")

            # Обновляем диапазоны осей
            self.x_min = float(self.x_min_entry.get())
            self.x_max = float(self.x_max_entry.get())
            self.y_min = float(self.y_min_entry.get())
            self.y_max = float(self.y_max_entry.get())

            if self.x_min >= self.x_max or self.y_min >= self.y_max:
                raise ValueError("Минимальное значение оси должно быть меньше максимального")

            # Перегенерируем палитру и обновляем визуализацию
            self.generate_palette()
            self.update_render()

        except ValueError as e:
            messagebox.showerror("Ошибка", f"Некорректный ввод: {str(e)}")

    def get_color_for_point(self, x, y):
        """Возвращает цвет для точки (x, y) в зависимости от выбранной визуализации."""
        if self.visualization_type == "Ker(|a+b|-|a-b|)":
            value = abs(x + y) - abs(x - y)  # This ranges between -2max to +2max
            
            # Normalize value to [0,1] range first
            max_val = max(abs(x), abs(y)) if max(abs(x), abs(y)) != 0 else 1
            normalized = (value / (2 * max_val) + 1) / 2  # maps to [0,1]
            
            # Then apply parameters
            scaled_value = (normalized * self.a_param + self.b_param) % self.colors_size
        elif self.visualization_type == "LenNOD(a,b)":
            value = math.gcd(abs(int(x)), abs(int(y))) if x != 0 or y != 0 else 0
            scaled_value = (value * self.a_param) % self.colors_size
        elif self.visualization_type == "LenCH(a,b)":
            value = max(abs(x), abs(y))
            scaled_value = (value * self.a_param) % self.colors_size
        else:
            value = 0
            scaled_value = 0

        # Нормализация значения для выбора цвета из палитры
        if self.colors_size == 0:
            return "#000000"

        color_index = int(scaled_value) % len(self.palette)
        return self.palette[color_index]

    def vis_type_changed(self, event):
        """Обработчик изменения типа визуализации."""
        self.visualization_type = self.vis_combobox.get()
        self.update_render()

    def show_about(self):
        """Показывает окно 'О программе'."""
        about_text = (
            "2D Ker(|a+b| - |a-b|)\n\n"
            "Визуализация математических функций:\n"
            "1. Ker(|a+b| - |a-b|) — ядро разности модулей\n"
            "2. LenNOD(a,b) — наибольший общий делитель\n"
            "3. LenCH(a,b) — чебышёвская норма\n\n"
            "Управление:\n"
            "- Измените параметры и нажмите 'Обновить'.\n"
            "- F1 — справка."
        )
        messagebox.showinfo("О программе", about_text)