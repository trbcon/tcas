from functools import partial
import readline
import tkinter as tk
from tkinter.colorchooser import askcolor

class App(tk.Tk):
    def __init__(self):
        self.set_color("fg")

    def set_color(self, option):
        color = askcolor()[1]
        print("Выбрать цвет:", color)
        file = open("cfg.txt", "r")
        file.readline();bg = file.readline()
        file.close()
        file = open("cfg.txt", "w")
        file.write(color + "\n" + bg)
        file.close()

if __name__ == "__main__":
    app = App()
    app.mainloop()