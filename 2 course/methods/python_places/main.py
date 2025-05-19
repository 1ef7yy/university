import os
import sqlite3
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk


class AmDBMSFApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Фонд AmDBMSF")
        self.root.geometry("1000x600")

        self.db_path = 'places.db'
        self.records = self.load_data()
        self.current_index = 0

        self.frame = tk.Frame(self.root)
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.listbox = tk.Listbox(self.frame, height=20, width=30)
        self.listbox.pack(side=tk.LEFT, padx=20, pady=20)

        scrollbar = tk.Scrollbar(self.frame, orient=tk.VERTICAL, command=self.listbox.yview)
        scrollbar.pack(side=tk.LEFT, fill=tk.Y)
        self.listbox.config(yscrollcommand=scrollbar.set)

        self.image_label = tk.Label(self.frame)
        self.image_label.pack(side=tk.LEFT, padx=20)

        self.description_text = tk.Text(self.frame, wrap=tk.WORD, height=10, width=60)
        self.description_text.pack(side=tk.LEFT, padx=20)

        self.populate_listbox()

        self.show_record(0)  # select first index on startup

        self.listbox.bind('<<ListboxSelect>>', self.on_select_place)

        self.help_button = tk.Button(self.root, text="Справка", command=self.show_help)
        self.help_button.pack(side=tk.LEFT, padx=20)

        self.about_button = tk.Button(self.root, text="О программе", command=self.show_about)
        self.about_button.pack(side=tk.LEFT, padx=20)

        self.setup_shortcuts()

    def setup_shortcuts(self):
        self.root.bind("<F1>", self.show_credits)

    def load_data(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, description, image_path FROM places")
        rows = cursor.fetchall()
        conn.close()

        records = []
        for row in rows:
            records.append({
                'id': row[0],
                'name': row[1],
                'description': row[2],
                'image_path': row[3]
            })
        return records

    def populate_listbox(self):
        for record in self.records:
            self.listbox.insert(tk.END, record['name'])

    def show_record(self, index):
        if index < 0 or index >= len(self.records):
            return
        record = self.records[index]

        self.description_text.delete(1.0, tk.END)
        self.description_text.insert(tk.END, record['description'])

        image_path = record['image_path']
        if os.path.exists(image_path):
            image = Image.open(image_path)
            image.thumbnail((300, 300))
            photo = ImageTk.PhotoImage(image)
            self.image_label.config(image=photo)
            self.image_label.image = photo

    def on_select_place(self, event):
        selection = self.listbox.curselection()
        if selection:
            selected_index = selection[0]
            self.show_record(selected_index)

    def show_credits(self, event=None):
        credits = """
Большое спасибо моим родителям:
Устьянцеву Дмитрию Аркадьевичу и
Устьянцевой Маргарите Шамсумовной
за их поддержку и любовь!
"""
        messagebox.showinfo("Благодарность", credits)

    def show_help(self):
        content = """
Известные исторические места России

Возможности программы:
1. Просмотр списка исторических мест России
2. Просмотр фотографий этих мест
3. Получение информации и исторической справки
"""
        messagebox.showinfo("Содержание", content)

    def show_about(self):
        about = """
Известные исторические места России

Версия 1.0

©Ustyantsev, Moscow, 2025
"""
        messagebox.showinfo("О программе", about)

if __name__ == "__main__":
    root = tk.Tk()
    app = AmDBMSFApp(root)
    root.mainloop()
