import tkinter as tk
from gui.main_window import MainApplication

def main():
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()

if __name__ == '__main__':
    main()
