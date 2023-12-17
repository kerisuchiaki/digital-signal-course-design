from tkinter import ttk, Scale, IntVar, filedialog
import tkinter as tk
import cv2
import numpy as np
from PIL import Image, ImageTk, ImageOps, ImageEnhance


class ImageProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("图像处理程序")

        # 创建一个Frame用于放置按钮和滑块
        self.control_frame = ttk.Frame(self.root)
        self.control_frame.pack(side=tk.LEFT, padx=5, pady=5)

        # 创建一个Frame用于放置图片
        self.image_frame = ttk.Frame(self.root)
        self.image_frame.pack(side=tk.LEFT, padx=5, pady=5)

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

        # 创建加载图片按钮
        self.load_button = ttk.Button(self.control_frame, text="加载图片", command=self.load_image)
        self.load_button.pack(side=tk.TOP, padx=5, pady=5)

        # 创建处理图片按钮
        self.process_button = ttk.Button(self.control_frame, text="处理图片", command=self.process_image)
        self.process_button.pack(side=tk.TOP, padx=5, pady=5)

        # 创建平滑滑块
        self.smooth_scale_var = IntVar()
        self.smooth_scale = Scale(self.control_frame, label="平滑程度", from_=1, to=10, orient=tk.HORIZONTAL,
                                  variable=self.smooth_scale_var,
                                  command=self.smooth)
        self.smooth_scale.set(5)
        self.smooth_scale.pack(side=tk.TOP, padx=5, pady=5)

        # 创建锐化滑块
        self.sharpen_scale = Scale(self.control_frame, label="锐化程度", from_=1, to=10, orient=tk.HORIZONTAL,
                                   command=self.sharpen)
        self.sharpen_scale.set(5)
        self.sharpen_scale.pack(side=tk.TOP, padx=5, pady=5)

        # 创建色温滑块
        self.temperature_scale_var = IntVar()
        self.temperature_scale = Scale(self.control_frame, label="色温调节", from_=2000, to=8000, orient=tk.HORIZONTAL,
                                       variable=self.temperature_scale_var, command=self.adjust_temperature)
        self.temperature_scale.set(5000)  # 设置一个默认值
        self.temperature_scale.pack(side=tk.TOP, padx=5, pady=5)

        # 创建色调滑块
        self.tint_scale_var = IntVar()
        self.tint_scale = Scale(self.control_frame, label="色调调节", from_=-100, to=100, orient=tk.HORIZONTAL,
                                variable=self.tint_scale_var, command=self.adjust_tint)
        self.tint_scale.set(0)  # 设置一个默认值
        self.tint_scale.pack(side=tk.TOP, padx=5, pady=5)

        # 创建显示图片路径的Label
        self.image_path_label = ttk.Label(self.control_frame, text="当前图片路径：")
        self.image_path_label.pack(side=tk.TOP, padx=5, pady=5)

        self.image_stack = []  # 用于保存图像状态的堆栈

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

        width1, height1 = self.init_img.size
        aspect_ratio1 = width1 / height1

        self.canvas.config(width=new_width, height=new_height)
        # self.canvas1.config(width=new_width1, height=new_height1)

        if aspect_ratio1 > 1:
            new_width1 = canvas_width
            new_height1 = int(canvas_width / aspect_ratio1)
        else:
            new_height1 = canvas_height
            new_width1 = int(canvas_height * aspect_ratio1)

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

    def smooth(self, evt=None):
        if not hasattr(self, 'init_img'):
            return
        if hasattr(self, 'image'):
            # Convert to OpenCV format
            img_np = np.array(self.init_img)
            img_cv2 = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)

            # 获取滑块值，并确保是正奇数
            smooth_value = self.smooth_scale.get()
            if smooth_value % 2 == 0:
                smooth_value += 1
            smooth_value = smooth_value if smooth_value % 2 != 0 else smooth_value + 1

            # Apply smoothing filter based on slider value
            smoothed_img = cv2.GaussianBlur(img_cv2, (smooth_value, smooth_value), 0)

            # Convert back to PIL format
            self.image = Image.fromarray(cv2.cvtColor(smoothed_img, cv2.COLOR_BGR2RGB))
            self.display_image()
            # 添加当前图像到堆栈
            self.image_stack.append(self.image.copy())

    def sharpen(self, evt=None):
        if not hasattr(self, 'init_img'):
            return
        if hasattr(self, 'image'):
            # Convert to OpenCV format
            img_np = np.array(self.init_img)
            img_cv2 = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)

            # 获取滑块值
            sharpen_value = self.sharpen_scale.get()
            print(sharpen_value)
            sharpen_value = max(sharpen_value, 0) / 10.0  # 将取值截断到 0 到 1 之间
            print(sharpen_value)

            # Apply sharpening filter based on slider value
            kernel = np.array([[-1, -1, -1],
                               [-1, 8 + sharpen_value, -1],
                               [-1, -1, -1]])
            sharpened_img = cv2.filter2D(img_cv2, -1, kernel)

            # Convert back to PIL format
            self.image = Image.fromarray(cv2.cvtColor(sharpened_img, cv2.COLOR_BGR2RGB))
            self.display_image()
            # 添加当前图像到堆栈
            self.image_stack.append(self.image.copy())

    def adjust_temperature(self, evt=None):
        if not hasattr(self, 'init_img'):
            return
        if hasattr(self, 'image'):
            # Convert to OpenCV format
            img_np = np.array(self.init_img)
            img_cv2 = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)

            # 获取滑块值
            temperature_value = self.temperature_scale.get()

            # 调整色温
            temperature_matrix = np.float32([[1.0, 0.0, 0.0],
                                             [0.0, 1.0, 0.0]])

            temperature_matrix[0, 2] = (temperature_value - 5000) / 5000.0
            temperature_matrix[1, 2] = (temperature_value - 5000) / 5000.0

            # Apply warpAffine using the transformation matrix
            adjusted_img = cv2.warpAffine(img_cv2, temperature_matrix, img_cv2.shape[:2][::-1])

            # Convert back to PIL format
            self.image = Image.fromarray(cv2.cvtColor(adjusted_img, cv2.COLOR_BGR2RGB))
            self.display_image()
            # 添加当前图像到堆栈
            self.image_stack.append(self.image.copy())

    def adjust_tint(self, evt=None):
        if hasattr(self, 'image'):
            # Convert to OpenCV format
            img_np = np.array(self.init_img)
            img_cv2 = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)

            # 获取滑块值
            tint_value = self.tint_scale.get()

            # 调整色调
            tint_matrix = np.float32([[1.0, 0.0, 0.0],
                                      [0.0, 1.0, 0.0]])

            tint_matrix[0, 2] = tint_value / 100.0

            # Apply warpAffine using the transformation matrix
            adjusted_img = cv2.warpAffine(img_cv2, tint_matrix, img_cv2.shape[:2][::-1])

            # Convert back to PIL format
            self.image = Image.fromarray(cv2.cvtColor(adjusted_img, cv2.COLOR_BGR2RGB))
            self.display_image()
            # 添加当前图像到堆栈
            self.image_stack.append(self.image.copy())


# 创建主窗口
root = tk.Tk()
app = ImageProcessorApp(root)

# 运行主循环
root.mainloop()
