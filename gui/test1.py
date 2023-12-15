import tkinter as tk

def on_mouse_press(event):
    global start_x, start_y
    start_x = event.x
    start_y = event.y

def on_mouse_release(event):
    canvas.create_line(start_x, start_y, event.x, event.y)

root = tk.Tk()

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()
canvas.bind("<ButtonPress>", on_mouse_press)
canvas.bind("<ButtonRelease>", on_mouse_release)

root.mainloop()