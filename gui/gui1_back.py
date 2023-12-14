from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
import tkinter as tk

from PIL import Image, ImageTk


class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()

    def __win(self):
        self.title("Tkinter布局助手")


if __name__ == "__main__":
    win = WinGUI()
    win.mainloop()
