import tkinter as tk
from tkinter import filedialog

from PIL import Image, ImageTk

root = tk.Tk()
# 创建画布1
canvas = tk.Canvas(root, bg="red")
canvas.place(x=384, y=78, width=960, height=960)
canvas.pack()
file_path = filedialog.askopenfilename()
if file_path:
    image = Image.open(file_path)
    photo = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)

canvas2 = tk.Canvas(root, bg="red")
canvas2.place(x=384, y=78, width=960, height=960)

canvas2.pack()
file_path = filedialog.askopenfilename()
canvas.pack_forget()

if file_path:
    image = Image.open(file_path)
    photo = ImageTk.PhotoImage(image)
    canvas2.create_image(0, 0, anchor=tk.NW, image=photo)
root.mainloop()
