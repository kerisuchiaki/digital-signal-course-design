import tkinter as tk


def on_mouse_press(event):
    global start_x, start_y
    start_x = event.x
    start_y = event.y


def on_mouse_release(event):
    canvas.delete("aa")
    canvas.delete("bb")
    canvas.delete("cc")
    canvas.delete("dd")
    canvas.create_line(start_x, start_y, event.x, start_y, tags="aa", smooth=True)  # 绘制水平直线
    canvas.create_line(start_x, event.y, event.x, event.y, tags="aa", smooth=True)  # 绘制水平直线
    canvas.create_line(event.x, start_y, event.x, event.y, tags="bb", smooth=True)  # 绘制垂直直线
    canvas.create_line(start_x, start_y, start_x, event.y, tags="bb", smooth=True)  # 绘制垂直直线


root = tk.Tk()
canvas = tk.Canvas(root, width=1000, height=900)
canvas.pack()
canvas.bind("<ButtonPress>", on_mouse_press)
canvas.bind("<B1-Motion>", on_mouse_release)

root.mainloop()
