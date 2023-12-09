import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


class ImageProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("图像处理程序")

        self.load_button = tk.Button(self.root, text="加载图片", command=self.load_image)
        self.load_button.pack()

        self.canvas = tk.Canvas(self.root, width=400, height=400)
        self.canvas.pack()

        self.process_button = tk.Button(self.root, text="处理图片", command=self.process_image)
        self.process_button.pack()

    def load_image(self):
        file_path = filedialog.askopenfilename()
        self.image = Image.open(file_path)
        self.photo = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

    def process_image(self):
        # 在这里添加图像处理功能的代码，例如裁剪、调整亮度、对比度等

        # 更新处理后的图片到界面上
        self.photo = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageProcessorApp(root)
    root.mainloop()
