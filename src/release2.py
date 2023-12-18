import tkinter as tk
from tkinter import ttk, filedialog, Scale, IntVar

import cv2
import numpy as np
from PIL import Image, ImageTk, ImageEnhance, ImageOps, ImageDraw, ImageFont


class ImageProcessorApp:
    def __init__(self, root):
        self.light_sense_scale = None
        self.root = root
        self.root.title("图像处理程序")

        # 创建一个Frame用于放置按钮
        self.button_frame = ttk.Frame(self.root)
        self.button_frame.pack(side=tk.LEFT, padx=5, pady=5)

        # 创建一个Frame用于放置图片
        self.image_frame = ttk.Frame(self.root)
        self.image_frame.pack(side=tk.LEFT, padx=5, pady=5)

        self.ProgressBar_frame = ttk.Frame(self.root)
        self.ProgressBar_frame.pack(side=tk.LEFT, padx=5, pady=5)

        # 创建显示图片的画布
        self.canvas = tk.Canvas(self.image_frame, width=400, height=400)
        self.canvas.pack(side=tk.TOP)
        self.image_target_label = tk.Label(self.image_frame, text="目标图")
        self.image_target_label.pack(side=tk.TOP)

        # 原始图片的画布
        self.canvas1 = tk.Canvas(self.image_frame, width=400, height=400)
        self.canvas1.pack(side=tk.TOP)
        self.image_init_label = tk.Label(self.image_frame, text="原图")
        self.image_init_label.pack(side=tk.TOP)

        # 创建用于显示图片路径的Label
        self.image_path_label = tk.Label(self.image_frame, text="当前图片路径：")
        self.image_path_label.pack(side=tk.TOP, padx=5, pady=5)

        # 创建加载图片按钮
        self.load_button = ttk.Button(self.button_frame, text="加载图片", command=self.load_image)
        self.load_button.pack(side=tk.TOP, padx=5, pady=5)

        # 创建处理图片按钮
        self.process_button = ttk.Button(self.button_frame, text="处理图片", command=self.process_image)
        self.process_button.pack(side=tk.TOP, padx=5, pady=5)

        # 创建功能按钮
        self.crop_button = ttk.Button(self.button_frame, text="裁剪", command=self.crop_image)
        self.crop_button.pack(side=tk.TOP, padx=5, pady=5)

        self.rotate_button = ttk.Button(self.button_frame, text="旋转", command=self.rotate_image)
        self.rotate_button.pack(side=tk.TOP, padx=5, pady=5)

        # 创建HSL、锐化、平滑按钮
        self.hsl_button = ttk.Button(self.button_frame, text="HSL调整", command=self.adjust_hsl)
        self.hsl_button.pack(side=tk.TOP, padx=5, pady=5)

        self.sharpen_button = ttk.Button(self.button_frame, text="锐化", command=self.sharpen)
        self.sharpen_button.pack(side=tk.TOP, padx=5, pady=5)

        self.smooth_button = ttk.Button(self.button_frame, text="平滑", command=self.smooth)
        self.smooth_button.pack(side=tk.TOP, padx=5, pady=5)

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
        self.contrast_scale.set(100)
        self.contrast_scale.pack(side=tk.TOP)

        # 创建光感调节控件
        self.light_sense_label = tk.Label(self.ProgressBar_frame, text="光感调节（实时）")
        self.light_sense_label.pack(side=tk.TOP)
        self.light_sense_scale = Scale(self.ProgressBar_frame, from_=0, to=200, orient=tk.HORIZONTAL, length=200,
                                       command=self.adjust_light_sense)
        self.light_sense_scale.set(100)
        self.light_sense_scale.pack(side=tk.TOP)

        # 创建曝光度调整控件
        self.exposure_label = tk.Label(self.ProgressBar_frame, text="曝光度调整（实时）")
        self.exposure_label.pack(side=tk.TOP)
        self.exposure_scale = Scale(self.ProgressBar_frame, from_=0, to=200, orient=tk.HORIZONTAL, length=200,
                                    command=self.adjust_exposure)
        self.exposure_scale.set(100)
        self.exposure_scale.pack(side=tk.TOP)

        self.equalize_button = ttk.Button(self.button_frame, text="直方图均衡化", command=self.adjust_equalize)
        self.equalize_button.pack(side=tk.TOP, padx=5, pady=5)

        # 创建饱和度调整控件
        self.saturation_label = tk.Label(self.ProgressBar_frame, text="饱和度调整（实时）")
        self.saturation_label.pack(side=tk.TOP)
        self.saturation_scale = Scale(self.ProgressBar_frame, from_=0, to=200, orient=tk.HORIZONTAL, length=200,
                                      command=self.adjust_saturation)
        self.saturation_scale.set(100)
        self.saturation_scale.pack(side=tk.TOP)

        # 创建曲线调色控件
        self.curve_color_label = tk.Label(self.ProgressBar_frame, text="曲线调色（实时）")
        self.curve_color_label.pack(side=tk.TOP)
        self.curve_color_scale = Scale(self.ProgressBar_frame, from_=0, to=200, orient=tk.HORIZONTAL, length=200,
                                       command=self.adjust_curve_color)
        self.curve_color_scale.set(100)
        self.curve_color_scale.pack(side=tk.TOP)

        self.image_stack = []  # 用于保存图像状态的堆栈

        # 创建撤销按钮
        self.undo_button = ttk.Button(self.button_frame, text="撤销", command=self.undo_image)
        self.undo_button.pack(side=tk.TOP, padx=5, pady=5)

        # 创建曲线调整控件
        self.curve_label = tk.Label(self.ProgressBar_frame, text="曲线调整（实时）")
        self.curve_label.pack(side=tk.TOP)
        self.curve_scale = Scale(self.ProgressBar_frame, from_=0, to=200, orient=tk.HORIZONTAL, length=200,
                                 command=self.adjust_curve)
        self.curve_scale.set(100)
        self.curve_scale.pack(side=tk.TOP)

        # 创建色温调整控件
        self.temperature_label = tk.Label(self.ProgressBar_frame, text="色温调整（实时）")
        self.temperature_label.pack(side=tk.TOP)
        self.temperature_scale = Scale(self.ProgressBar_frame, from_=0, to=200, orient=tk.HORIZONTAL, length=200,
                                       command=self.adjust_temperature)
        self.temperature_scale.set(100)
        self.temperature_scale.pack(side=tk.TOP)

        # 创建色调调整控件
        self.hue_label = tk.Label(self.ProgressBar_frame, text="色调调整（实时）")
        self.hue_label.pack(side=tk.TOP)
        self.hue_scale = Scale(self.ProgressBar_frame, from_=0, to=200, orient=tk.HORIZONTAL, length=200,
                               command=self.adjust_hue)
        self.hue_scale.set(100)
        self.hue_scale.pack(side=tk.TOP)

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





    # ... (之前的其他方法)

    def load_image(self):
        # 弹出文件选择对话框
        file_path = filedialog.askopenfilename()

        if file_path:
            # 打开并调整图片大小以适应画布
            self.image = Image.open(file_path)
            self.init_img = self.image
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

        # self.image = self.image.resize((new_width, new_height), Image.ANTIALIAS)

        self.image = self.image.resize((new_width, new_height), Image.LANCZOS)

        width1, height1 = self.init_img.size
        aspect_ratio1 = width1 / height1

        if aspect_ratio1 > 1:
            new_width1 = canvas_width
            new_height1 = int(canvas_width / aspect_ratio1)
        else:
            new_height1 = canvas_height
            new_width1 = int(canvas_height * aspect_ratio1)

        # self.init_img = self.image.resize((new_width1, new_height1), Image.ANTIALIAS)
        self.init_img = self.image.resize((new_width1, new_height1), Image.LANCZOS)

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
            rotation_angle = 90
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
            contrast_adjusted = ImageEnhance.Contrast(self.init_img).enhance(contrast_factor)

            # 显示调整对比度后的图片
            self.image = contrast_adjusted
            self.display_image()

    def lightSense(self, img, a):
        a = np.float32(a - 50) / 80.0
        a = a * 255
        res = img.astype(np.float32)
        res = res + a * res / 255.0
        res = np.where(res > 255, 255, res)
        res = np.where(res < 0, 0, res)
        res = res.astype(np.uint8)
        return res

    def adjust_light_sense(self, event=None):
        # 调整光感功能
        if hasattr(self, 'image'):
            light_sense_factor = self.light_sense_scale.get() / 10.0
            light_sense_adjusted = self.lightSense(np.array(self.init_img), light_sense_factor)

            # 将 NumPy 数组转换回 PIL 图像
            self.image = Image.fromarray(light_sense_adjusted)

            # 显示调整光感后的图片
            self.display_image()

    def adjust_exposure(self, event=None):
        # 调整曝光度功能
        if hasattr(self, 'image'):
            exposure_factor = self.exposure_scale.get() / 100.0
            exposure_adjusted = self._adjust_exposure(np.array(self.init_img), exposure_factor)
            self.image = Image.fromarray(exposure_adjusted)
            self.display_image()

    def _adjust_exposure(self, img, b):
        # 曝光度调整 参数 b: 0~100
        b = np.float32(b - 50) / 20.0
        res = img.astype(np.float32)
        res = res * pow(2, b)
        res = np.where(res > 255, 255, res)
        res = res.astype(np.uint8)
        return res

    def adjust_curve(self, event=None):
        # 调整曲线功能
        if hasattr(self, 'image'):
            curve_factor = self.curve_scale.get() / 100.0
            curve_adjusted = ImageEnhance.Contrast(self.init_img).enhance(curve_factor)
            self.image = curve_adjusted
            self.display_image()

    def adjust_equalize(self):
        # 直方图均衡化功能
        if hasattr(self, 'image'):
            equalize_adjusted = ImageOps.equalize(self.init_img)
            self.image = equalize_adjusted
            self.display_image()

    def adjust_saturation(self, event=None):
        # 饱和度调整功能
        if hasattr(self, 'image'):
            saturation_factor = self.saturation_scale.get() / 100.0
            saturation_adjusted = ImageEnhance.Color(self.init_img).enhance(saturation_factor)
            self.image = saturation_adjusted
            self.display_image()

    def adjust_curve_color(self, event=None):
        # 曲线调色功能
        if hasattr(self, 'image'):
            curve_color_factor = self.curve_color_scale.get() / 100.0
            curve_color_adjusted = ImageEnhance.Contrast(self.init_img).enhance(curve_color_factor)
            self.image = curve_color_adjusted
            self.display_image()

    def sharpen(self):
        if hasattr(self, 'image'):
            # Convert to OpenCV format
            img_np = np.array(self.init_img)
            img_cv2 = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)

            # Apply sharpening filter
            kernel = np.array([[-1, -1, -1],
                               [-1, 9, -1],
                               [-1, -1, -1]])
            sharpened_img = cv2.filter2D(img_cv2, -1, kernel)

            # Convert back to PIL format
            self.image = Image.fromarray(cv2.cvtColor(sharpened_img, cv2.COLOR_BGR2RGB))
            self.display_image()
            # 添加当前图像到堆栈
            self.image_stack.append(self.image.copy())

    def smooth(self):
        if hasattr(self, 'image'):
            # Convert to OpenCV format
            img_np = np.array(self.init_img)
            img_cv2 = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)

            # Apply smoothing filter
            smoothed_img = cv2.GaussianBlur(img_cv2, (5, 5), 0)

            # Convert back to PIL format
            self.image = Image.fromarray(cv2.cvtColor(smoothed_img, cv2.COLOR_BGR2RGB))
            self.display_image()
            # 添加当前图像到堆栈
            self.image_stack.append(self.image.copy())

    def adjust_hsl(self):
        if hasattr(self, 'image'):
            # 示例：增加对 HSL 调整的参数，可以根据需要调整
            cf_h = 20
            cf_s = 20
            cf_l = 20

            # 调用 HSL 调整函数
            hsl_img = self.HSL(self.init_img, cf_h, cf_s, cf_l)

            # 显示调整后的图片
            self.image = self.convertToBGR(hsl_img)
            self.display_image()
            # 添加当前图像到堆栈
            self.image_stack.append(self.image.copy())

    # ... (之前的其他方法)

    # 图像HSL调节
    # cf_h 范围[0, 200] 对应[0, 2]
    # cf_s, cf_l 范围[0, 200] 对应 [0, 2]
    # 整个调用过程：
    # 对于一个img
    #   1. hslImg = convertToHSL(img)
    #   2. dst = HSL(hslImg, cf_h, cf_s, cf_l)
    #   3. dst = convertToBGR(dst)
    def HSL(self, img, cf_h, cf_s, cf_l):
        # cf_h 范围[0, 200] 对应[0, 2]
        # cf_s, cf_l 范围[0, 200] 对应 [0, 2]
        # h_new = h * cf_h
        cf_h = (cf_h + 10) / 100.0
        cf_s = (cf_s + 10) / 100.0
        cf_l = (cf_l + 20) / 100.0
        rows, cols, channels = img.shape
        res = np.zeros(img.shape)
        for i in range(rows):
            for j in range(cols):
                res[i, j, 0] = np.float32(cf_h) * img[i, j, 0]
                if res[i, j, 0] > 360.0:
                    res[i, j, 0] = 360.0
                res[i, j, 1] = np.float32(cf_s) * img[i, j, 1]
                if res[i, j, 1] > 1.0:
                    res[i, j, 1] = 1.0
                res[i, j, 2] = np.float32(cf_l) * img[i, j, 2]
                if res[i, j, 2] > 1.0:
                    res[i, j, 2] = 1.0

        return res

    # 图像RGB空间转HSL
    def convertToHSL(self, img):
        rows, cols, channels = img.shape
        res = np.zeros(img.shape)
        for i in range(rows):
            for j in range(cols):
                b_val = np.float32(img[i, j, 0]) / 255.0
                g_val = np.float32(img[i, j, 1]) / 255.0
                r_val = np.float32(img[i, j, 2]) / 255.0
                max_val = max(b_val, max(g_val, r_val))
                min_val = min(b_val, min(g_val, r_val))
                # H [0, 360)
                H = 0
                S = 0
                L = 0
                if max_val == min_val:
                    H = 0
                elif max_val == r_val and g_val >= b_val:
                    H = np.float32(60) * (g_val - b_val) / (max_val - min_val)
                elif max_val == r_val and g_val < b_val:
                    H = np.float32(60) * (g_val - b_val) / (max_val - min_val) + 360
                elif max_val == g_val:
                    H = np.float32(60) * (b_val - r_val) / (max_val - min_val) + 120
                elif max_val == b_val:
                    H = np.float32(60) * (r_val - g_val) / (max_val - min_val) + 240

                # L [0, 1]
                L = np.float32(0.5) * (max_val + min_val)

                # S [0, 1]
                if L == 0 or max_val == min_val:
                    S = 0
                elif 0 < L <= 0.5:
                    S = (max_val - min_val) / (2.0 * L)
                elif L > 0.5:
                    S = (max_val - min_val) / (2.0 - 2.0 * L)

                res[i, j, 0] = H
                res[i, j, 1] = S
                res[i, j, 2] = L
        return res

    # 图像HSL空间转RGB
    def convertToBGR(self, img):
        rows, cols, channels = img.shape
        res = np.zeros(img.shape, dtype=np.float32)
        for i in range(rows):
            for j in range(cols):
                h, s, l = img[i, j, :]
                if s == 0:
                    res[i, j, 0] = l
                    res[i, j, 1] = l
                    res[i, j, 2] = l
                    continue
                if l < 0.5:
                    q = l * (1.0 + s)
                else:
                    q = l + s - (l * s)
                p = 2 * l - q
                hk = h / 360.0
                tC = np.array([hk - 1.0 / 3.0, hk, hk + 1.0 / 3.0], dtype=np.float32)
                tC = np.where(tC < 0, tC + 1.0, tC)
                tC = np.where(tC > 1, tC - 1.0, tC)
                for tt in range(3):
                    if tC[tt] < 1.0 / 6.0:
                        temp_val = p + ((q - p) * 6.0 * tC[tt])
                    elif tC[tt] < 1.0 / 2.0:
                        temp_val = q
                    elif tC[tt] < 2.0 / 3.0:
                        temp_val = p + ((q - p) * 6.0 * (2.0 / 3.0 - tC[tt]))
                    else:
                        temp_val = p
                    res[i, j, tt] = temp_val

        res = res * np.float32(255.0)
        res = res.astype(np.uint8)
        return res

    def adjust_temperature(self, event=None):
        # 色温调整功能
        if hasattr(self, 'image'):
            temperature_factor = self.temperature_scale.get() / 100.0
            temperature_adjusted = self.adjust_image_temperature(self.init_img, temperature_factor)

            # 显示调整色温后的图片
            self.image = temperature_adjusted
            self.display_image()

    def adjust_hue(self, event=None):
        # 色调调整功能
        if hasattr(self, 'image'):
            hue_factor = self.hue_scale.get() / 100.0
            hue_adjusted = self.adjust_image_hue(self.init_img, hue_factor)

            # 显示调整色调后的图片
            self.image = hue_adjusted
            self.display_image()

    def adjust_image_temperature(self, image, factor):
        # 调整图片色温
        r, g, b = image.split()
        r = r.point(lambda i: i * factor)
        return Image.merge('RGB', (r, g, b))

    def adjust_image_hue(self, image, factor):
        # 调整图片色调
        hsl_image = image.convert('HSV')
        h, s, v = hsl_image.split()
        h = h.point(lambda i: i + int(factor * 255))
        return Image.merge('HSV', (h, s, v)).convert('RGB')

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

    def show_image(self, image_path):
        # 打开图像并在画布上显示
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        self.canvas.image = photo  # 保持引用以避免被垃圾回收


# 添加水印的函数（与之前提供的相同）
def add_watermark(input_image_path, output_image_path, watermark_text):
    original_image = Image.open(input_image_path)

    # 创建一个绘图对象
    draw = ImageDraw.Draw(original_image)

    # 获取水印文本的包围框
    font = ImageFont.load_default()  # 使用默认字体
    text_bbox = draw.textbbox((0, 0), watermark_text, font=font)

    # 计算水印文本的宽度和高度
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    # 计算水印文本的位置
    text_position = (original_image.width - text_width, original_image.height - text_height)

    # 在图片上绘制水印
    draw.text(text_position, watermark_text, font=font)

    # 保存带有水印的图片
    original_image.save(output_image_path)


# 你的 HSL 转 RGB 函数
# ...

# 其他部分保持不变

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageProcessorApp(root)
    root.mainloop()
