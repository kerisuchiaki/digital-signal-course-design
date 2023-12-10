import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


class ImageProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("图像处理程序")

        # 创建加载图片按钮
        self.load_button = tk.Button(self.root, text="加载图片", command=self.load_image)
        self.load_button.pack()

        # 创建显示图片的画布
        self.canvas = tk.Canvas(self.root, width=400, height=400)
        self.canvas.pack()

        # 创建处理图片按钮
        self.process_button = tk.Button(self.root, text="处理图片", command=self.process_image)
        self.process_button.pack()

    def load_image(self):
        # 弹出文件选择对话框
        file_path = filedialog.askopenfilename()

        # 打开并显示图片
        self.image = Image.open(file_path)
        self.display_image()

    def process_image(self):
        if hasattr(self, 'image'):
            # 示例: 裁剪图片（将图像裁剪为正方形）
            width, height = self.image.size
            min_dim = min(width, height)
            cropped_image = self.image.crop((0, 0, min_dim, min_dim))

            # 示例: 调整亮度
            brightness_factor = 1.5
            brightness_adjusted = cropped_image.point(lambda p: p * brightness_factor)

            # 示例: 调整对比度
            contrast_factor = 1.5
            contrast_adjusted = brightness_adjusted.point(lambda p: (p - 128) * contrast_factor + 128)

            # 显示处理后的图片
            self.image = contrast_adjusted
            self.display_image()

    def display_image(self):
        # 调整图片大小以适应画布
        resized_image = self.image.resize((400, 400), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(resized_image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageProcessorApp(root)
    root.mainloop()