import tkinter as tk
from tkinter import ttk, filedialog, Scale
import cv2
import numpy as np
from PIL import Image, ImageTk


class ImageProcessor:
    def __init__(self):
        self.image = None
        self.original_image = None
        self.crop_coords = None

    def load_image(self, file_path):
        self.image = cv2.imread(file_path)
        self.original_image = self.image.copy()
        return self.image

    def rotate(self, angle):
        rows, cols, _ = self.image.shape
        M = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
        self.image = cv2.warpAffine(self.image, M, (cols, rows))
        return self.image

    def crop(self, x_lt, y_lt, x_rb, y_rb):
        self.image = self.original_image[y_lt:y_rb, x_lt:x_rb]
        return self.image

    def resize(self, scale):
        scale_factor = scale / 50.0
        if scale_factor < 1:
            self.image = cv2.resize(self.original_image, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_AREA)
        else:
            self.image = cv2.resize(self.original_image, None, fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_LINEAR)
        return self.image

    def adjust_contrast(self, factor):
        factor = (factor + 20) / 50.0
        table = np.array([(i - 74) * factor + 74 for i in range(256)]).clip(0, 255).astype('uint8')
        self.image = cv2.LUT(self.image, table)
        return self.image

    def adjust_brightness(self, factor):
        factor = (factor - 50) / 180.0
        factor *= 255
        self.image = self.original_image.astype(np.float32) + factor
        self.image = np.where(self.image > 255, 255, self.image)
        self.image = np.where(self.image < 0, 0, self.image)
        self.image = self.image.astype(np.uint8)
        return self.image

    def adjust_lightness(self, factor):
        factor = (factor - 50) / 80.0
        factor *= 255
        self.image = self.original_image.astype(np.float32) + factor * self.image / 255.0
        self.image = np.where(self.image > 255, 255, self.image)
        self.image = np.where(self.image < 0, 0, self.image)
        self.image = self.image.astype(np.uint8)
        return self.image

    def adjust_light_sense(self, factor):
        factor = (factor - 50) / 80.0
        factor *= 255
        self.image = self.original_image.astype(np.float32) + factor * self.image / 255.0
        self.image = np.where(self.image > 255, 255, self.image)
        self.image = np.where(self.image < 0, 0, self.image)
        self.image = self.image.astype(np.uint8)
        return self.image

    def adjust_exposure(self, factor):
        factor = (factor - 50) / 20.0
        self.image = self.original_image.astype(np.float32) * pow(2, factor)
        self.image = np.where(self.image > 255, 255, self.image)
        self.image = self.image.astype(np.uint8)
        return self.image

    def adjust_saturation(self, factor):
        factor = (factor - 50) / 50.0
        hsv_image = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2HSV)
        hsv_image[:, :, 1] = np.clip(hsv_image[:, :, 1] + factor * hsv_image[:, :, 1], 0, 255)
        self.image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)
        return self.image

    def equalize_histogram(self):
        hsv_image = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2HSV)
        hsv_image[:, :, 2] = cv2.equalizeHist(hsv_image[:, :, 2])
        self.image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)
        return self.image

    def adjust_hsl(self, h_factor, s_factor, l_factor):
        h_factor = (h_factor + 10) / 100.0
        s_factor = (s_factor + 10) / 100.0
        l_factor = (l_factor + 20) / 100.0
        hsl_image = self.rgb_to_hsl(self.original_image)
        hsl_image[:, :, 0] *= h_factor
        hsl_image[:, :, 1] *= s_factor
        hsl_image[:, :, 2] *= l_factor
        self.image = self.hsl_to_rgb(hsl_image)
        return self.image

    def rgb_to_hsl(self, rgb_image):
        hsl_image = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2HLS)
        hsl_image[:, :, 0] *= 2  # Scale H channel to match the original range [0, 360]
        hsl_image[:, :, 1:] /= 255.0  # Normalize S and L channels to [0, 1]
        return hsl_image

    def hsl_to_rgb(self, hsl_image):
        hsl_image[:, :, 0] /= 2  # Scale back H channel to the original range [0, 180]
        hsl_image[:, :, 1:] *= 255.0  # Denormalize S and L channels
        return cv2.cvtColor(hsl_image, cv2.COLOR_HLS2BGR)

    def set_crop_coords(self, coords):
        self.crop_coords = coords

    def perform_crop(self):
        if self.crop_coords is not None:
            x_lt, y_lt, x_rb, y_rb = self.crop_coords
            self.image = self.crop(x_lt, y_lt, x_rb, y_rb)
            self.original_image = self.image.copy()
            self.crop_coords = None
            return True
        return False


class ImageProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("图像处理程序")

        self.image_processor = ImageProcessor()

        self.load_button = ttk.Button(self.root, text="加载图片", command=self.load_image)
        self.load_button.pack()

        self.canvas = tk.Canvas(self.root, width=400, height=400)
        self.canvas.pack()

        self.create_slider("旋转角度", self.image_processor.rotate, -180, 180)
        self.create_slider("图像缩放", self.image_processor.resize, 0, 200)
        self.create_slider("对比度调整", self.image_processor.adjust_contrast, -20, 180)
        self.create_slider("亮度调整", self.image_processor.adjust_brightness, -50, 150)
        self.create_slider("光感调整", self.image_processor.adjust_light_sense, -50, 150)
        self.create_slider("曝光度调整", self.image_processor.adjust_exposure, -50, 150)
        self.create_slider("饱和度调整", self.image_processor.adjust_saturation, -50, 150)
        self.create_button("直方图均衡化", self.image_processor.equalize_histogram)
        self.create_slider("HSL调整-Hue", self.image_processor.adjust_hsl, -10, 190, axis=0)
        self.create_slider("HSL调整-Saturation", self.image_processor.adjust_hsl, -10, 190, axis=1)
        self.create_slider("HSL调整-Lightness", self.image_processor.adjust_hsl, -20, 180, axis=2)
        self.create_button("剪切图像", self.init_crop_mode)

        self.process_button = ttk.Button(self.root, text="处理图片", command=self.process_image)
        self.process_button.pack()

        self.crop_mode = False
        self.crop_coords = None
        self.bind_mouse_events()

    def load_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image_processor.load_image(file_path)
            self.display_image()

    def display_image(self):
        if hasattr(self, 'photo'):
            self.canvas.delete(self.photo)

        image = Image.fromarray(cv2.cvtColor(self.image_processor.image, cv2.COLOR_BGR2RGB))
        photo = ImageTk.PhotoImage(image)
        self.photo = self.canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        self.canvas.image = photo

    def process_image(self):
        # 根据用户选择的功能进行图像处理
        if hasattr(self, 'current_function'):
            if self.current_function['type'] == 'slider':
                value = self.slider.get()
                self.current_function['function'](value)
            elif self.current_function['type'] == 'button':
                self.current_function['function']()

            # 显示处理后的图片
            self.display_image()

    def create_slider(self, label_text, processing_function, from_value, to_value, axis=None, position=None):
        # 创建滑动条
        label = tk.Label(self.root, text=label_text)
        label.pack()
        self.slider = Scale(self.root, from_=from_value, to=to_value, orient=tk.HORIZONTAL, length=200)
        self.slider.pack()

        # 添加事件处理函数
        self.slider.bind("<ButtonRelease-1>", self.on_slider_release)
        self.current_function = {'type': 'slider', 'function': processing_function}

    def create_button(self, label_text, processing_function):
        # 创建处理按钮
        button = ttk.Button(self.root, text=label_text, command=self.process_image)
        button.pack()

        # 更新当前处理函数
        self.current_function = {'type': 'button', 'function': processing_function}

    def init_crop_mode(self):
        self.crop_mode = True
        self.canvas.bind("<Button-1>", self.on_crop_start)

    def on_crop_start(self, event):
        self.crop_coords = [event.x, event.y]
        self.canvas.bind("<B1-Motion>", self.on_cropping)
        self.canvas.bind("<ButtonRelease-1>", self.on_crop_end)

    def on_cropping(self, event):
        self.canvas.delete("crop_line")
        x, y = self.crop_coords
        self.canvas.create_rectangle(x, y, event.x, event.y, outline="red", tags="crop_line")

    def on_crop_end(self, event):
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
        x, y = self.crop_coords
        self.crop_coords.extend([event.x, event.y])
        self.image_processor.set_crop_coords(self.crop_coords)
        self.crop_mode = False
        self.canvas.delete("crop_line")

        if self.image_processor.perform_crop():
            # 如果执行了剪切操作，更新显示
            self.display_image()

    def bind_mouse_events(self):
        self.canvas.bind("<Button-3>", self.on_right_click)

    def on_right_click(self, event):
        # 右键单击时，取消剪切模式
        if self.crop_mode:
            self.crop_mode = False
            self.canvas.unbind("<B1-Motion>")
            self.canvas.unbind("<ButtonRelease-1>")
            self.canvas.delete("crop_line")

    def on_slider_release(self, event):
        # 滑动条释放时触发处理图片事件
        self.process_image()


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageProcessorApp(root)
    root.mainloop()
