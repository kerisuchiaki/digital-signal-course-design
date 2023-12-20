import inspect
import tkinter as tk
from tkinter import ttk, filedialog, Scale, IntVar

import cv2
import numpy as np
from PIL import Image, ImageTk, ImageEnhance, ImageOps, ImageDraw, ImageFont

from release2 import add_watermark


class ImageProcessorApp:
    def __init__(self, root):
        self.last_op = None
        self.image_back = None
        self.photo = None
        self.init_canvas = None
        self.init_photo = None
        self.image = None
        self.init_img = None
        self.light_sense_scale = None
        self.root = root
        self.root.title("图像处理程序")

        # 创建一个Frame用于放置按钮
        self.button_frame = ttk.Frame(self.root)
        self.button_frame.pack(side=tk.LEFT, padx=5, pady=5)

        # 创建一个Frame用于放置图片
        self.image_frame = ttk.Frame(self.root)
        self.image_frame.pack(side=tk.LEFT, padx=5, pady=5)

        # 创建一个Frame用来防止滑块
        self.ProgressBar_frame = ttk.Frame(self.root)
        self.ProgressBar_frame.pack(side=tk.LEFT, padx=5, pady=5)



        # 创建显示图片的画布
        self.canvas = tk.Canvas(self.image_frame, width=400, height=400)
        self.canvas.pack(side=tk.TOP)
        self.image_target_label = tk.Label(self.image_frame, text="目标图")
        self.image_target_label.pack(side=tk.TOP)

        # 原始图片的画布
        self.init_canvas = tk.Canvas(self.image_frame, width=400, height=400)
        self.init_canvas.pack(side=tk.TOP)
        self.image_init_label = tk.Label(self.image_frame, text="原图")
        self.image_init_label.pack(side=tk.TOP)

        # 创建用于显示图片路径的Label
        self.image_path_label = tk.Label(self.image_frame, text="当前图片路径：")
        self.image_path_label.pack(side=tk.TOP, padx=5, pady=5)

        # 创建加载图片按钮
        self.load_button = ttk.Button(self.button_frame, text="加载图片", command=self.load_image)
        self.load_button.pack(side=tk.TOP, padx=5, pady=5)

        # 创建处理图片按钮
        self.process_button = ttk.Button(self.button_frame, text="保存处理", command=self.process_image)
        self.process_button.pack(side=tk.TOP, padx=5, pady=5)

        # 创建功能按钮
        self.crop_button = ttk.Button(self.button_frame, text="裁剪", command=self.crop_image)
        self.crop_button.pack(side=tk.TOP, padx=5, pady=5)

        self.rotate_button = ttk.Button(self.button_frame, text="旋转", command=self.rotate_image)
        self.rotate_button.pack(side=tk.TOP, padx=5, pady=5)

        # 创建HSL、锐化、平滑按钮
        self.sharpen_button = ttk.Button(self.button_frame, text="锐化", command=self.sharpen)
        self.sharpen_button.pack(side=tk.TOP, padx=5, pady=5)

        self.smooth_button = ttk.Button(self.button_frame, text="平滑", command=self.smooth)
        self.smooth_button.pack(side=tk.TOP, padx=5, pady=5)

        self.equalize_button = ttk.Button(self.button_frame, text="直方图均衡化", command=self.adjust_equalize)
        self.equalize_button.pack(side=tk.TOP, padx=5, pady=5)

        # 创建HSL、锐化、平滑按钮
        self.hsl_button = ttk.Button(self.button_frame, text="HSL调整")
        self.hsl_button.pack(side=tk.TOP, padx=5, pady=5)


        # 创建文字输入框和按钮
        self.text_entry = ttk.Entry(self.button_frame)
        self.text_entry.pack(side=tk.TOP, pady=5)
        self.add_text_button = ttk.Button(self.button_frame, text="添加文字", command=self.add_text_to_image)
        self.add_text_button.pack(side=tk.TOP, pady=5)

        # 创建水印输入框和按钮
        self.watermark_entry = ttk.Entry(self.button_frame)
        self.watermark_entry.pack(side=tk.TOP, pady=5)
        self.add_watermark_button = ttk.Button(self.button_frame, text="添加水印", command=self.add_watermark_to_image)
        self.add_watermark_button.pack(side=tk.TOP, pady=5)

        # 创建亮度调整控件
        self.brightness_label = tk.Label(self.ProgressBar_frame, text="亮度调整（实时）")
        self.brightness_label.pack(side=tk.TOP)
        self.brightness_scale = Scale(self.ProgressBar_frame, from_=0, to=200, orient=tk.HORIZONTAL, length=200,
                                      command=self.adjust_brightness)
        self.brightness_scale.set(100)
        self.brightness_scale.pack(side=tk.TOP)

        # 创建对比度调整控件
        self.contrast_label = tk.Label(self.ProgressBar_frame, text="对比度调整（实时）")
        self.contrast_label.pack(side=tk.TOP)
        self.contrast_scale = Scale(self.ProgressBar_frame, from_=0, to=200, orient=tk.HORIZONTAL, length=200,
                                    command=self.adjust_contrast)
        # self.contrast_scale.set(100)
        self.contrast_scale.pack(side=tk.TOP)

        self.image_stack = []  # 用于保存图像状态的堆栈

        # 创建撤销按钮
        self.undo_button = ttk.Button(self.button_frame, text="撤销", command=self.undo_image)
        self.undo_button.pack(side=tk.TOP, padx=5, pady=5)

        # 创建文字输入框和按钮
        self.text_entry = ttk.Entry(self.button_frame)
        self.text_entry.pack(side=tk.TOP, pady=5)
        self.add_text_button = ttk.Button(self.button_frame, text="添加文字", command=self.add_text_to_image)
        self.add_text_button.pack(side=tk.TOP, pady=5)

        # 创建取消按钮
        self.cancel_button = ttk.Button(self.button_frame, text="取消处理", command=self.cancel_process)
        self.cancel_button.pack(side=tk.TOP, padx=5, pady=5)

        # 创建保存按钮
        self.save_button = ttk.Button(self.button_frame, text="保存图片", command=self.save_image)
        self.save_button.pack(side=tk.TOP, padx=5, pady=5)


    def add_watermark_to_image(self):
        # 获取水印文本
        watermark_text = self.watermark_entry.get()

        if watermark_text:
            # 获取当前显示图像的路径并去除前缀
            current_image_path = self.image_path_label["text"].replace('当前图片路径：', '')

            # 生成保存水印图像的路径
            output_image_path = current_image_path.replace(".jpg", "_with_watermark.jpg")

            # 添加水印
            add_watermark(current_image_path, output_image_path, watermark_text)

            # 更新图像显示
            self.show_image(output_image_path)

    def adjust_equalize(self):
        # 直方图均衡化功能
        if hasattr(self, 'image'):
            equalize_adjusted = ImageOps.equalize(self.image)
            self.image = equalize_adjusted
            self.display_image()

    def cancel_process(self):
        if hasattr(self, 'init_img'):
            self.image = self.init_img
            # 显示图像
            self.display_image()

    def load_image(self):
        # 弹出文件选择对话框
        file_path = filedialog.askopenfilename()

        if file_path:
            # 打开并调整图片大小以适应画布
            self.image_stack = []
            self.image = Image.open(file_path)
            self.init_img = self.image  # 这里这样写也能保持原图不变奇怪
            self.adjust_image_size()
            self.image_stack.append(self.image.copy())

            self.display_image()

            # 更新显示图片路径的Label
            self.image_path_label.config(text="当前图片路径：" + file_path)

    def undo_image(self):
        # 撤销按钮的处理方法
        if len(self.image_stack) >= 1:
            # 弹出当前图像

            # 恢复到上一个状态
            self.image = self.image_stack[-1].copy()

            # 当只剩下最初的原图时不能再出栈了，不然后面入栈其他的再撤销会找不到原图的
            if len(self.image_stack) > 1:
                self.image_stack.pop()

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

        self.image = self.image.resize((new_width, new_height), Image.LANCZOS)

        # 下面是原图
        width1, height1 = self.init_img.size
        aspect_ratio1 = width1 / height1

        if aspect_ratio1 > 1:
            new_width1 = canvas_width
            new_height1 = int(canvas_width / aspect_ratio1)
        else:
            new_height1 = canvas_height
            new_width1 = int(canvas_height * aspect_ratio1)

        # self.image = self.image.resize((new_width1, new_height1), Image.ANTIALIAS)
        self.init_img = self.image.resize((new_width1, new_height1), Image.LANCZOS)

    def process_image(self):
        # 处理图片的默认功能
        if hasattr(self, 'image'):
            # 显示处理后的图片
            self.display_image()
            # 添加当前图像到堆栈
            self.image_stack.append(self.image.copy())

    def display_image(self, flag=0):
        # 显示调整后的图片
        if flag == 0:
            self.image_back = self.image
        self.photo = ImageTk.PhotoImage(self.image)
        self.init_photo = ImageTk.PhotoImage(self.init_img)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)
        self.init_canvas.create_image(0, 0, anchor=tk.NW, image=self.init_photo)

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
            rotation_angle = 90
            rotated_image = self.image.rotate(rotation_angle, expand=True)

            # 显示旋转后的图片
            self.image = rotated_image
            self.display_image()

    def adjust_brightness(self, event=None):
        if self.last_op != inspect.currentframe().f_code.co_name:
            self.image_back = self.image
        # 调整亮度功能
        if hasattr(self, 'image_back') and self.image is not None:
            brightness_factor = self.brightness_scale.get() / 100.0
            # 在增强亮度之前检查 self.image 是否不为 None
            brightness_adjusted = ImageEnhance.Brightness(self.image_back).enhance(brightness_factor)

            # 显示调整亮度后的图片
            self.image = brightness_adjusted
            self.display_image(1)
            # 获取当前函数的名称
            self.last_op = inspect.currentframe().f_code.co_name

    def adjust_contrast(self, event=None):
        if self.last_op != inspect.currentframe().f_code.co_name:
            self.image_back = self.image

        # 调整对比度功能
        if hasattr(self, 'image_back') and self.image is not None:
            contrast_factor = self.contrast_scale.get() / 100.0
            # 在增强对比度之前检查 self.image 是否不为 None
            contrast_adjusted = ImageEnhance.Contrast(self.image_back).enhance(contrast_factor)

            # 显示调整对比度后的图片
            self.image = contrast_adjusted
            self.display_image(1)
            # 获取当前函数的名称
            self.last_op = inspect.currentframe().f_code.co_name

    def sharpen(self):
        if hasattr(self, 'image'):
            # Convert to OpenCV format
            img_np = np.array(self.image)
            img_cv2 = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)

            # Apply sharpening filter
            kernel = np.array([[-1, -1, -1],
                               [-1, 9, -1],
                               [-1, -1, -1]])
            sharpened_img = cv2.filter2D(img_cv2, -1, kernel)

            # Convert back to PIL format
            self.image = Image.fromarray(cv2.cvtColor(sharpened_img, cv2.COLOR_BGR2RGB))

            self.display_image(1)

    def smooth(self):
        if hasattr(self, 'image'):
            # Convert to OpenCV format
            img_np = np.array(self.image)
            img_cv2 = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)

            # Apply smoothing filter
            smoothed_img = cv2.GaussianBlur(img_cv2, (5, 5), 0)

            # Convert back to PIL format
            self.image = Image.fromarray(cv2.cvtColor(smoothed_img, cv2.COLOR_BGR2RGB))
            self.display_image()
            # 添加当前图像到堆栈

    def add_text_to_image(self):
        # 添加文本到图片
        if hasattr(self, 'image'):
            text_to_add = self.text_entry.get()

            if text_to_add:
                # 使用PIL的ImageDraw模块在图片上绘制文本
                draw = ImageDraw.Draw(self.image)
                draw.text((10, 10), text_to_add, fill="white")

                # 显示带有文本的图片
                self.display_image()

    def save_image(self):
        # 保存图片功能
        if hasattr(self, 'image'):
            # 弹出文件选择对话框
            file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                     filetypes=[("PNG files", "*.png"),
                                                                ("JPEG files", "*.jpg"),
                                                                ("All files", "*.*")])

            if file_path:
                # 保存图片
                self.image.save(file_path)

    def show_image(self, image_path):
        # 打开图像并在画布上显示
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        self.canvas.image = photo  # 保持引用以避免被垃圾回收


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageProcessorApp(root)
    root.mainloop()

