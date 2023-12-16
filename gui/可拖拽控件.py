from PIL import Image, ImageDraw, ImageFont, ImageTk
import tkinter as tk


class MyApp:
    def __init__(self):
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root)
        self.canvas.pack()

        self.image = Image.open("../image/sakura.jpg")  # 假设有一个初始的self.image

        # 将self.image添加到画布中
        self.photo = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

        # 在画布上添加文字
        self.add_text_to_canvas("Hello, World!", (100, 100))

        # 将带有文字的画布内容赋值给self.image
        # self.update_image()

    def add_text_to_canvas(self, text, position, font_name, font_size, color):
        # 创建一个可绘制对象
        draw = ImageDraw.Draw(self.image)

        # 创建字体对象
        font = ImageFont.truetype(font_name, font_size)

        # 在画布上添加文字
        draw.text(position, text, fill=color, font=font)

    def update_image(self):
        # 显示更新后的self.image
        self.photo = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)


app = MyApp()
app.root.mainloop()
