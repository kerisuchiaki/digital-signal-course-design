import tkinter as tk

def on_mouse_press(event):
    global start_x, start_y
    start_x = event.x
    start_y = event.y

def on_mouse_motion(event):
    canvas.coords("line_aa", start_x, start_y, event.x, start_y)  # 更新水平直线的坐标
    canvas.coords("line_cc", start_x, event.y, event.x, event.y)  # 更新水平直线的坐标
    canvas.coords("line_bb", event.x, start_y, event.x, event.y)  # 更新垂直直线的坐标
    canvas.coords("line_dd", start_x, start_y, start_x, event.y)  # 更新垂直直线的坐标

root = tk.Tk()

canvas = tk.Canvas(root, width=1000, height=900)
canvas.pack()

# 创建水平直线和垂直直线，并设置smooth选项为True
canvas.create_line(0, 0, 0, 0, tags="line_aa", smooth=True)
canvas.create_line(0, 0, 0, 0, tags="line_cc", smooth=True)
canvas.create_line(0, 0, 0, 0, tags="line_bb", smooth=True)
canvas.create_line(0, 0, 0, 0, tags="line_dd", smooth=True)

canvas.bind("<ButtonPress>", on_mouse_press)
canvas.bind("<B1-Motion>", on_mouse_motion)

root.mainloop()