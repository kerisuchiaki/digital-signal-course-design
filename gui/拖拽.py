import tkinter as tk
from PIL import Image, ImageTk, ImageGrab


class DraggableText:
    def __init__(self, canvas, text, x, y):
        self.canvas = canvas
        self.text = text
        self.x = x
        self.y = y
        self.drag_data = {"x": 0, "y": 0}
        self.create_text()

    def create_text(self):
        self.text_widget = self.canvas.create_text(self.x, self.y, text=self.text, font=("Arial", 12), tags="draggable")

        self.canvas.tag_bind(self.text_widget, "<ButtonPress-1>", self.on_press)
        self.canvas.tag_bind(self.text_widget, "<B1-Motion>", self.on_drag)
        self.canvas.tag_bind(self.text_widget, "<ButtonRelease-1>", self.on_release)

    def on_press(self, event):
        self.drag_data["x"] = event.x
        self.drag_data["y"] = event.y

    def on_drag(self, event):
        dx = event.x - self.drag_data["x"]
        dy = event.y - self.drag_data["y"]
        self.canvas.move(self.text_widget, dx, dy)
        self.drag_data["x"] = event.x
        self.drag_data["y"] = event.y

    def on_release(self, event):
        pass


def save_canvas():
    # 获取画布内容
    x = root.winfo_rootx() + canvas.winfo_x()+2
    print(root.winfo_rootx())
    print(canvas.winfo_x())
    y = root.winfo_rooty() + canvas.winfo_y()+2
    print(root.winfo_rooty())
    print(canvas.winfo_y())

    x1 = x + canvas.winfo_width()-4
    y1 = y + canvas.winfo_height()-4
    image = ImageGrab.grab((x, y, x1, y1))

    # 保存画布内容为图像文件
    save_path = "../image/canvas_snapshot.png"
    image.save(save_path)
    print("保存成功:", save_path)


root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# 展示图片
image_path = "../image/sakura.jpg"
pil_image = Image.open(image_path)
image = ImageTk.PhotoImage(pil_image)
canvas.create_image(0, 0, anchor="nw", image=image)

# 创建可拖拽的文本
draggable_text = DraggableText(canvas, "Drag me", 100, 100)

# 保存按钮
save_button = tk.Button(root, text="Save Canvas", command=save_canvas)
save_button.pack()

root.mainloop()
