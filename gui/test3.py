import tkinter as tk

def on_mouse_press(event):
    global start_x, start_y, rectangle
    start_x = event.x
    start_y = event.y
    canvas.delete("reg")

    rectangle = canvas.create_rectangle(start_x, start_y, start_x, start_y,tags="reg")  # 创建初始矩形框

def on_mouse_motion(event):
    canvas.coords(rectangle, start_x, start_y, event.x, event.y)  # 更新矩形框的坐标

root = tk.Tk()

canvas = tk.Canvas(root, width=1000, height=800)
canvas.pack()

canvas.bind("<ButtonPress>", on_mouse_press)
canvas.bind("<B1-Motion>", on_mouse_motion)

root.mainloop()