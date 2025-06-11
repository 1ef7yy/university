import tkinter as tk
from tkinter import messagebox
from gui.form_1d import PoliteNumbersVisualizer
from gui.form_2d import Object2DForm

class MainApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("Главное окно")
        self.root.geometry("505x505")
        self.root.resizable(False, False)

        self.form_1d = None
        self.form_2d = None

        self.child_windows = {
            '1d': None,
            '2d': None
        }
        self.create_menu()
        self.create_bindings()

    def create_menu(self):
        menubar = tk.Menu(self.root)

        # Меню "Файл"
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Выход", command=self.root.quit)
        menubar.add_cascade(label="Файл", menu=file_menu)

        # Меню "Визуализация"
        vis_menu = tk.Menu(menubar, tearoff=0)
        vis_menu.add_command(label="1D", command=self.open_1d)
        vis_menu.add_command(label="2D", command=self.open_2d)
        menubar.add_cascade(label="Визуализация", menu=vis_menu)

        # Меню "Справка"
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="Справка", command=self.show_help)
        help_menu.add_command(label="О программе", command=self.show_about)
        menubar.add_cascade(label="Справка", menu=help_menu)

        self.root.config(menu=menubar)

    def create_bindings(self):
        self.root.bind('<F1>', lambda e: self.show_help())
        self.root.bind('<F4>', lambda e: self.open_1d())
        self.root.bind('<F5>', lambda e: self.open_2d())


    def open_1d(self):
        PoliteNumbersVisualizer(self.root)

    def open_2d(self):
        Object2DForm(self.root)

    def show_help(self):
        help_window = tk.Toplevel(self.root)
        help_window.title("Справка")
        help_window.geometry("400x300")
        help_window.resizable(False, False)

        text_frame = tk.Frame(help_window)
        text_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        scrollbar = tk.Scrollbar(text_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        help_text = tk.Text(
            text_frame,
            wrap=tk.WORD,
            yscrollcommand=scrollbar.set,
            font=('Arial', 10),
            padx=10,
            pady=10
        )
        help_text.pack(fill=tk.BOTH, expand=True)

        scrollbar.config(command=help_text.yview)

        help_content = """
                                        Справка

        Визуализация данных:
           - F4 - Вызов визуализации 1D
           - F5 - Вызов визуализации 2D

        Использование:
           - Выберите нужный режим визуализации из меню
           - Работайте с открывшимися формами
           - Для выхода используйте меню Файл -> Выход
           - F1 - Вызов справки

        """

        help_text.insert(tk.END, help_content)
        help_text.config(state=tk.DISABLED)

        close_btn = tk.Button(
            help_window,
            text="Закрыть",
            command=help_window.destroy,
            width=10
        )
        close_btn.pack(pady=10)

    def show_about(self):
        about_text = (
            "Хромоматематическое моделирование\n\n"
            "Версия: 1.0\n"
            "Разработчик: Устьянцев М. Д.\n"
            "2025, Moscow, Russia\n"
            "Спасибо Устьянцевой М.Ш. и Устьянцеву Д.А. за поддержку во всех моих начинаниях!"
        )
        messagebox.showinfo("О программе", about_text)


if __name__ == "__main__":
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()
