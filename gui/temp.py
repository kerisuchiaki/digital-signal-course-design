from tkinter import *
import tkinter as tk
from tkinter.ttk import *

class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.scale = Scale(self, from_=0, to=200, orient=tk.HORIZONTAL, length=200)
        self.scale.set(100)
        self.scale.pack(side=tk.TOP)

        self.ttk_scale = tkinter.ttk.Scale(self, from_=0, to=200, orient=tk.HORIZONTAL, length=200)
        self.ttk_scale.set(100)
        self.ttk_scale.pack(side=tk.TOP)

if __name__ == "__main__":
    win = WinGUI()
    win.mainloop()
