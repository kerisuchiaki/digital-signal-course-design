import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import cv2
import numpy as np


class ImageProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("图像处理程序")

        # 创建一个Frame用于放置滑块
        self.control_frame = ttk.Frame(self.root)
        self.control_frame.pack(side=tk.LEFT, padx=5, pady=5)

        # 创建一个Frame用于放置图片
        self.image_frame = ttk.Frame(self.root)
        self.image_frame.pack(side=tk.LEFT, padx=5, pady=5)

        # 创建显示图片的画布
        self.canvas = tk.Canvas(self.image_frame, width=400, height=400)
        self.canvas.pack(side=tk.TOP)
        self.image_label = tk.Label(self.image_frame, text="原图")
        self.image_label.pack(side=tk.TOP)

        # 创建色温调节滑块
        self.temperature_scale_var = tk.DoubleVar()
        self.temperature_scale = ttk.Scale(self.control_frame, from_=2000, to=12000,
                                           orient=tk.HORIZONTAL, variable=self.temperature_scale_var,
                                           command=self.adjust_temperature)
        self.temperature_scale.set(6500)  # 初始色温值
        self.temperature_scale.pack(side=tk.TOP, padx=5, pady=5)

        # 加载示例图片
        self.image_path = "../image/sakura.jpg"
        self.image = Image.open(self.image_path)
        self.display_image()

    def adjust_temperature(self, evt=None):
        if hasattr(self, 'image'):
            temperature_value = self.temperature_scale.get()
            adjusted_img = self.color_temperature(np.array(self.image), temperature_value)
            self.image = Image.fromarray(adjusted_img)
            self.display_image()

    @staticmethod
    def color_temperature(img, temperature):
        min_temperature = 2000
        max_temperature = 12000
        normalized_temperature = (temperature - min_temperature) / (max_temperature - min_temperature)

        blue_curve = np.array([0, 0.03951, 0.07592, 0.13793, 0.20915, 0.29977, 0.40986, 0.53903, 0.68698, 0.85445, 1.0])
        new_blue = np.interp(normalized_temperature, np.linspace(0, 1, len(blue_curve)), blue_curve)
        new_red = np.interp(normalized_temperature, np.linspace(0, 1, len(blue_curve)), blue_curve[::-1])
        new_green = 1 - (new_blue + new_red)

        color_adjustment_matrix = np.column_stack([new_blue, new_green, new_red])

        # 使用cv2.warpAffine进行仿射变换
        adjusted_img = cv2.warpAffine(img, color_adjustment_matrix[:, :2], (img.shape[1], img.shape[0]))

        # 将调整后的图像值限制在 [0, 255] 范围内
        adjusted_img = np.clip(adjusted_img, 0, 255).astype(np.uint8)

        return adjusted_img

    def display_image(self):
        if hasattr(self, 'image'):
            img = cv2.cvtColor(np.array(self.image), cv2.COLOR_BGR2RGB)
            img = Image.fromarray(img)
            photo = ImageTk.PhotoImage(img)
            self.canvas.config(width=img.width, height=img.height)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
            self.canvas.image = photo


# 创建主窗口
root = tk.Tk()
app = ImageProcessorApp(root)

# 运行主循环
root.mainloop()
