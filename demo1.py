import tkinter as tk
from tkinter import ttk, filedialog, Scale, IntVar
from PIL import Image, ImageTk, ImageEnhance, ImageOps


class ImageProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("图像处理程序")

        # 创建加载图片按钮
        self.load_button = ttk.Button(self.root, text="加载图片", command=self.load_image)
        self.load_button.pack(side=tk.LEFT, padx=5, pady=5)

        # 创建处理图片按钮
        self.process_button = ttk.Button(self.root, text="处理图片", command=self.process_image)
        self.process_button.pack(side=tk.RIGHT, padx=5, pady=5)

        # 创建显示图片的画布
        self.canvas = tk.Canvas(self.root, width=400, height=400)
        self.canvas.pack()
        self.canvas1 = tk.Canvas(self.root, width=400, height=400)
        self.canvas1.pack()

        # 创建用于显示图片路径的Label
        self.image_path_label = tk.Label(self.root, text="当前图片路径：")
        self.image_path_label.pack(side=tk.TOP, padx=5, pady=5)

        # 创建功能按钮
        self.crop_button = ttk.Button(self.root, text="裁剪", command=self.crop_image)
        self.crop_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.rotate_button = ttk.Button(self.root, text="旋转", command=self.rotate_image)
        self.rotate_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.brightness_label = tk.Label(self.root, text="亮度调整")
        self.brightness_label.pack(side=tk.TOP)
        self.brightness_scale = Scale(self.root, from_=0, to=200, orient=tk.HORIZONTAL, length=200)
        self.brightness_scale.set(100)
        self.brightness_scale.pack(side=tk.TOP)

        self.contrast_label = tk.Label(self.root, text="对比度调整")
        self.contrast_label.pack(side=tk.TOP)
        self.contrast_scale = Scale(self.root, from_=0, to=200, orient=tk.HORIZONTAL, length=200)
        self.contrast_scale.set(100)
        self.contrast_scale.pack(side=tk.TOP)



        # 创建亮度调整控件
        self.brightness_label = tk.Label(self.root, text="亮度调整")
        self.brightness_label.pack(side=tk.TOP)
        self.brightness_scale = Scale(self.root, from_=0, to=200, orient=tk.HORIZONTAL, length=200,command=self.adjust_brightness)
        self.brightness_scale.set(100)
        self.brightness_scale.pack(side=tk.TOP)

        # 创建对比度调整控件
        self.contrast_label = tk.Label(self.root, text="对比度调整")
        self.contrast_label.pack(side=tk.TOP)
        self.contrast_scale = Scale(self.root, from_=0, to=200, orient=tk.HORIZONTAL, length=200,
                                    command=self.adjust_contrast)
        self.contrast_scale.set(100)
        self.contrast_scale.pack(side=tk.TOP)

        self.image_stack = []  # 用于保存图像状态的堆栈

        # ... (之前的初始化代码)

        # 创建撤销按钮
        self.undo_button = ttk.Button(self.root, text="撤销", command=self.undo_image)
        self.undo_button.pack(side=tk.TOP, padx=5, pady=5)

    # ... (之前的其他方法)

    def load_image(self):
        # 弹出文件选择对话框
        file_path = filedialog.askopenfilename()

        if file_path:
            # 打开并调整图片大小以适应画布
            self.image = Image.open(file_path)
            self.init_img=self.image
            self.adjust_image_size()
            self.display_image()

            # 更新显示图片路径的Label
            self.image_path_label.config(text="当前图片路径：" + file_path)

            # 添加当前图像到堆栈
            self.image_stack.append(self.image.copy())

    def undo_image(self):
        # 撤销按钮的处理方法
        if len(self.image_stack) > 1:
            # 弹出当前图像
            self.image_stack.pop()
            # 恢复到上一个状态
            self.image = self.image_stack[-1].copy()
            # 显示图像
            self.display_image()
    def adjust_image_size(self):
        # 调整图片大小以适应画布并保持其纵横比
        canvas_width = 400
        canvas_height = 400
        width, height = self.image.size
        aspect_ratio = width / height

        if aspect_ratio > 1:
            new_width = canvas_width
            new_height = int(canvas_width / aspect_ratio)
        else:
            new_height = canvas_height
            new_width = int(canvas_height * aspect_ratio)

        self.image = self.image.resize((new_width, new_height), Image.ANTIALIAS)

        width1, height1 = self.init_img.size
        aspect_ratio1 = width1 / height1

        if aspect_ratio1 > 1:
            new_width1 = canvas_width
            new_height1 = int(canvas_width / aspect_ratio1)
        else:
            new_height1 = canvas_height
            new_width1 = int(canvas_height * aspect_ratio1)

        self.init_img = self.image.resize((new_width1, new_height1), Image.ANTIALIAS)

    def process_image(self):
        # 处理图片的默认功能
        if hasattr(self, 'image'):
            # 示例: 曲线调整
            curve_adjusted = ImageOps.autocontrast(self.image)

            # 示例: 直方图均衡化
            equalized_image = ImageOps.equalize(curve_adjusted)

            # 示例: 饱和度调整
            saturation_factor = 1.5
            saturation_adjusted = ImageEnhance.Color(equalized_image).enhance(saturation_factor)

            # 显示处理后的图片
            self.image = saturation_adjusted
            self.display_image()
            # 添加当前图像到堆栈
            self.image_stack.append(self.image.copy())

    def display_image(self):
        # 显示调整后的图片
        self.photo = ImageTk.PhotoImage(self.image)
        self.photo1 = ImageTk.PhotoImage(self.init_img)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)
        self.canvas1.create_image(0, 0, anchor=tk.NW, image=self.photo1)

    def crop_image(self):
        # 裁剪图片功能
        if hasattr(self, 'image'):
            crop_percent = 0.8
            width, height = self.image.size
            left = (1 - crop_percent) * width / 2
            top = (1 - crop_percent) * height / 2
            right = (1 + crop_percent) * width / 2
            bottom = (1 + crop_percent) * height / 2
            cropped_image = self.image.crop((left, top, right, bottom))

            # 显示裁剪后的图片
            self.image = cropped_image
            self.display_image()

    def rotate_image(self):
        # 旋转图片功能
        if hasattr(self, 'image'):
            rotation_angle = 45
            rotated_image = self.image.rotate(rotation_angle, expand=True)

            # 显示旋转后的图片
            self.image = rotated_image
            self.display_image()

    def adjust_brightness(self):
        # 调整亮度功能
        if hasattr(self, 'image'):
            print("hello")
            brightness_factor = self.brightness_scale.get() / 100.0
            brightness_adjusted = ImageEnhance.Brightness(self.image).enhance(brightness_factor)

            # 显示调整亮度后的图片
            self.image = brightness_adjusted
            self.display_image()

    def adjust_contrast(self):
        # 调整对比度功能
        if hasattr(self, 'image'):
            print("hello")

            contrast_factor = self.contrast_scale.get() / 100.0
            contrast_adjusted = ImageEnhance.Contrast(self.image).enhance(contrast_factor)

            # 显示调整对比度后的图片
            self.image = contrast_adjusted
            self.display_image()

    def rotate_image(self):
        # 旋转图片功能
        if hasattr(self, 'image'):
            rotation_angle = 45
            rotated_image = self.image.rotate(rotation_angle, expand=True)

            # 显示旋转后的图片
            self.image = rotated_image
            self.display_image()

    def adjust_brightness(self, event=None):
        # 调整亮度功能
        if hasattr(self, 'image'):
            brightness_factor = self.brightness_scale.get() / 100.0
            # 将这里的self.image改成self.init_img为什么显示的图片不完全，init_img是最初的图片
            brightness_adjusted = ImageEnhance.Brightness(self.init_img).enhance(brightness_factor)

            # 显示调整亮度后的图片
            self.image = brightness_adjusted
            self.display_image()

    def adjust_contrast(self, event=None):
        # 调整对比度功能
        if hasattr(self, 'image'):
            contrast_factor = self.contrast_scale.get() / 100.0
            contrast_adjusted = ImageEnhance.Contrast(self.image).enhance(contrast_factor)

            # 显示调整对比度后的图片
            self.image = contrast_adjusted
            self.display_image()


# 其他部分保持不变

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageProcessorApp(root)
    root.mainloop()
