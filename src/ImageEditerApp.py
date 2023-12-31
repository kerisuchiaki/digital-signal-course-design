
import inspect
from tkinter import *
from tkinter import filedialog
# from tkinter.ttk import *
# del Scale
import tkinter as tk
from tkinter.ttk import Notebook, Button

import cv2
import numpy as np
from PIL import Image, ImageTk, ImageEnhance, ImageOps, ImageGrab

from Utils.color_temperature import change_temperature


class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.file_path = None
        self.image_back = None
        self.image_back_last = None
        self.__win()
        self.tk_button_open_image = self.__tk_button_open_image(self)
        self.tk_button_cancel = self.__tk_button_cancel(self)
        self.tk_button_modify = self.__tk_button_modify(self)
        self.tk_button_save = self.__tk_button_save(self)
        self.image_path_label = Label(self)
        self.image_path_label.config(text="当前图片路径：")
        self.image_path_label.place(x=376, y=1)
        self.tk_tabs_option = self.__tk_tabs_option(self)
        self.tk_frame_container0 = self.__tk_frame_container0(self.tk_tabs_option_1)
        self.tk_label_contrast = self.__tk_label_contrast(self.tk_frame_container0)  # 对比度
        self.tk_scale_contrast = self.__tk_scale_contrast(self.tk_frame_container0)
        self.tk_label_brightness = self.__tk_label_brightness(self.tk_frame_container0)  # 亮度
        self.tk_scale_brightness = self.__tk_scale_brightness(self.tk_frame_container0)
        self.tk_label_exposure = self.__tk_label_exposure(self.tk_frame_container0)
        self.tk_scale_exposure = self.__tk_scale_exposure(self.tk_frame_container0)
        self.tk_label_pome = self.__tk_label_pome(self.tk_frame_container0)
        self.tk_scale_pome = self.__tk_scale_pome(self.tk_frame_container0)
        self.tk_label_sharpen = Label(self.tk_frame_container0, text="锐化", anchor="center", )
        self.tk_label_sharpen.place(x=252, y=208, width=50, height=30)
        self.tk_scale_Sharpen = self.__tk_scale_Sharpen(self.tk_frame_container0)  # 锐化，考虑做成滑块
        self.tk_label_smooth = Label(self.tk_frame_container0, text="平滑", anchor="center", )
        self.tk_label_smooth.place(x=252, y=298, width=50, height=30)
        self.tk_scale_Smooth = self.__tk_scale_Smooth(self.tk_frame_container0)  # 平滑，同上

        self.temperature_slider = Scale(self.tk_frame_container0, from_=0, to=200, orient=tk.HORIZONTAL, label="色温",
                                        command=self.adjust_temperature, length=200, )
        self.temperature_slider.set(100)
        self.temperature_slider.place(x=202, y=8, width=150, height=80)

        self.label_hue_slider = Label(self.tk_frame_container0, text="色调", anchor="center", )
        self.label_hue_slider.place(x=252, y=80, width=50, height=30)
        self.hue_slider = Scale(self.tk_frame_container0, from_=0, to=200, orient=tk.HORIZONTAL, length=200,
                                command=self.adjust_hue
                                )
        self.hue_slider.place(x=202, y=108, width=150, height=50)

        self.tk_button_Histogram_equalization = self.__tk_button_Histogram_equalization(self.tk_frame_container0)
        self.tk_label_saturation = self.__tk_label_saturation(self.tk_frame_container0)
        self.tk_scale_saturation = self.__tk_scale_saturation(self.tk_frame_container0)
        self.tk_frame_container1 = self.__tk_frame_container1(self.tk_tabs_option_2)
        self.tk_label_Hue = self.__tk_label_Hue(self.tk_frame_container1)
        self.tk_scale_Hue = self.__tk_scale_Hue(self.tk_frame_container1)
        self.tk_label_Saturation = self.__tk_label_Saturation(self.tk_frame_container1)
        self.tk_scale_Saturation = self.__tk_scale_Saturation(self.tk_frame_container1)
        self.tk_label_lightness = self.__tk_label_lightness(self.tk_frame_container1)
        self.tk_scale_lightness = self.__tk_scale_lightness(self.tk_frame_container1)
        self.tk_button_rotate = self.__tk_button_rotate(self.tk_tabs_option_0)
        self.tk_button_trim = self.__tk_button_trim(self.tk_tabs_option_0)
        self.tk_input_text = self.__tk_input_text(self.tk_tabs_option_3)
        self.tk_button_add = self.__tk_button_add(self.tk_tabs_option_3)
        self.tk_label_text_label = self.__tk_label_text_label(self.tk_tabs_option_3)
        self.tk_canvas_watermark = self.__tk_canvas_watermark(self.tk_tabs_option_3)
        self.tk_button_open_watermark = self.__tk_button_open_watermark(self.tk_tabs_option_3)
        self.tk_button_add_watermark = self.__tk_button_add_watermark(self.tk_tabs_option_3)
        self.crop_canvas = Canvas(self)
        self.crop_canvas.place(x=384, y=78, width=960, height=960)
        self.crop_canvas.pack_forget()
        self.canvas = self.__tk_canvas_image(self)
        self.init_canvas = self.canvas

    def adjust_temperature_1(self, temperature):
        original_image = self.image_back.convert("RGB")
        r, g, b = original_image.split()
        print(temperature)

        # 避免除以零错误
        adjusted_b = b.point(lambda p: p * (1 / temperature) if temperature != 0 else p)

        # 调整红色通道
        adjusted_r = r.point(lambda p: p * temperature)

        # 合并通道
        adjusted_image = Image.merge("RGB", (adjusted_r, g, adjusted_b))

        return adjusted_image

    def adjust_temperature(self, value, evt=None):
        if self.last_op != inspect.currentframe().f_code.co_name:
            self.image_back = self.image
        if hasattr(self, 'image_back') and self.image is not None:
            temperature = float(value) / 100.0

            # 避免除以零错误
            temperature = max(temperature, 0.001)

            self.image = self.adjust_temperature_1(temperature)
            self.show_image(flag=1)
            self.last_op = inspect.currentframe().f_code.co_name

    def adjust_hue(self, evt=None):
        if self.last_op != inspect.currentframe().f_code.co_name:
            self.image_back = self.image
        # 调整亮度功能
        if hasattr(self, 'image_back') and self.image is not None:
            hue_value = self.hue_slider.get()
            print(hue_value)

            origin_image = cv2.imread(self.file_path)

            # 转换图片颜色空间为HSV
            hsv_image = cv2.cvtColor(origin_image, cv2.COLOR_BGR2HSV)

            # 调整色调
            hsv_image[:, :, 0] += hue_value

            # 调整色温
            hsv_image[:, :, 1] = np.clip(hsv_image[:, :, 1] + 0, 0, 255)

            # 转换回BGR颜色空间
            bgr_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)

            # 将OpenCV图像转换为PIL图像
            self.image = Image.fromarray(cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB))
            self.adjust_image_size()

            # 将PIL图像转换为Tkinter图像
            self.show_image(flag=1)
            self.last_op = inspect.currentframe().f_code.co_name

    def load_image(self, evt=None, flag=0):
        self.crop_canvas.place(x=384, y=78, width=960, height=960)
        self.canvas.place(x=384, y=78, width=960, height=960)

        # 弹出文件选择对话框
        self.file_path = filedialog.askopenfilename()

        if self.file_path:
            if flag == 0:
                # 打开并调整图片大小以适应画布
                self.image_stack = []
                self.image = Image.open(self.file_path)
                self.adjust_image_size()
                self.init_img = self.image  # 保持原图不变
                self.image_stack.append(self.image)
                self.show_image()
            else:
                self.watermark_image = Image.open(self.file_path)
                self.watermark_image_back = self.watermark_image.copy()
                self.adjust_image_size(flag=1)
                self.watermark_photo = ImageTk.PhotoImage(self.watermark_image)
                self.tk_canvas_watermark.create_image(0, 0, anchor=tk.NW, image=self.watermark_photo)
                self.tk_canvas_watermark.create_image(0, 0, anchor=tk.NW, image=self.watermark_photo)
            self.image_path_label.config(text="当前图片路径：" + self.file_path)

    def show_image(self, evt=None, flag=0, refresh=0):
        print("sqa")
        if hasattr(self, 'image_back') and hasattr(self, 'image'):
            # 清除之前的内容
            self.canvas.delete("all")
            # 显示调整后的图片
            if flag == 0:
                self.image_back = self.image
                print("000000000000")
            if refresh == 1:
                self.photo = ImageTk.PhotoImage(self.image_back)
                print("bug")
            else:
                self.photo = ImageTk.PhotoImage(self.image)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)
            self.crop_canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

    def adjust_image_size(self, flag=0):
        # 获取画布的大小
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        original_width, original_height = self.image.size

        if flag == 1:
            canvas_width = self.tk_canvas_watermark.winfo_width()
            canvas_height = self.tk_canvas_watermark.winfo_height()
            # 获取图像的原始大小
            original_width, original_height = self.watermark_image.size

        # 计算调整后的大小，保持纵横比
        if original_width > original_height:
            self.new_width = canvas_width
            self.new_height = int((canvas_width / original_width) * original_height)
        else:
            self.new_height = canvas_height
            self.new_width = int((canvas_height / original_height) * original_width)

        # 使用thumbnail方法调整图像大小
        if flag == 1:
            self.watermark_image.thumbnail((self.new_width, self.new_height), Image.LANCZOS)
        else:
            self.image.thumbnail((self.new_width, self.new_height), Image.LANCZOS)

    def __win(self):
        self.title("Tkinter")
        # 设置窗口大小、居中
        width = 1360
        height = 681
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        # self.config(bg="black")
        self.geometry(geometry)

        # self.resizable(width=False, height=False)

    def scrollbar_autohide(self, vbar, hbar, widget):
        """自动隐藏滚动条"""

        def show():
            if vbar: vbar.lift(widget)
            if hbar: hbar.lift(widget)

        def hide():
            if vbar: vbar.lower(widget)
            if hbar: hbar.lower(widget)

        hide()
        widget.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Leave>", lambda e: hide())
        if hbar: hbar.bind("<Enter>", lambda e: show())
        if hbar: hbar.bind("<Leave>", lambda e: hide())
        widget.bind("<Leave>", lambda e: hide())

    def v_scrollbar(self, vbar, widget, x, y, w, h, pw, ph):
        widget.configure(yscrollcommand=vbar.set)
        vbar.config(command=widget.yview)
        vbar.place(relx=(w + x) / pw, rely=y / ph, relheight=h / ph, anchor='ne')

    def h_scrollbar(self, hbar, widget, x, y, w, h, pw, ph):
        widget.configure(xscrollcommand=hbar.set)
        hbar.config(command=widget.xview)
        hbar.place(relx=x / pw, rely=(y + h) / ph, relwidth=w / pw, anchor='sw')

    def create_bar(self, master, widget, is_vbar, is_hbar, x, y, w, h, pw, ph):
        vbar, hbar = None, None
        if is_vbar:
            vbar = Scrollbar(master)
            self.v_scrollbar(vbar, widget, x, y, w, h, pw, ph)
        if is_hbar:
            hbar = Scrollbar(master, orient="horizontal")
            self.h_scrollbar(hbar, widget, x, y, w, h, pw, ph)
        self.scrollbar_autohide(vbar, hbar, widget)

    def __tk_button_open_image(self, parent):
        btn = Button(parent, text="打开", takefocus=False, command=self.load_image)
        btn.place(x=0, y=1, width=50, height=30)
        return btn

    def __tk_button_cancel(self, parent):
        btn = Button(parent, text="撤销", takefocus=False, )
        btn.place(x=78, y=0, width=50, height=30)
        return btn

    def __tk_button_modify(self, parent):
        btn = Button(parent, text="修改", takefocus=False, )
        btn.place(x=158, y=0, width=50, height=30)
        return btn

    def __tk_button_save(self, parent):
        btn = Button(parent, text="保存", takefocus=False, )
        btn.place(x=234, y=1, width=50, height=30)
        return btn

    def __tk_tabs_option(self, parent):
        frame = Notebook(parent)
        self.tk_tabs_option_0 = self.__tk_frame_option_0(frame)
        frame.add(self.tk_tabs_option_0, text="几何变换 ")
        self.tk_tabs_option_1 = self.__tk_frame_option_1(frame)
        frame.add(self.tk_tabs_option_1, text="图像增强 ")
        self.tk_tabs_option_2 = self.__tk_frame_option_2(frame)
        frame.add(self.tk_tabs_option_2, text="HSL调整 ")
        self.tk_tabs_option_3 = self.__tk_frame_option_3(frame)
        frame.add(self.tk_tabs_option_3, text="拓展")
        frame.place(x=1, y=53, width=361, height=1080)
        return frame

    def __tk_frame_option_0(self, parent):
        frame = Frame(parent)
        frame.place(x=1, y=53, width=361, height=511)
        return frame

    def __tk_frame_option_1(self, parent):
        frame = Frame(parent)
        frame.place(x=1, y=53, width=361, height=511)
        return frame

    def __tk_frame_option_2(self, parent):
        frame = Frame(parent)
        frame.place(x=1, y=53, width=361, height=511)
        return frame

    def __tk_frame_option_3(self, parent):
        frame = Frame(parent)
        frame.place(x=1, y=53, width=361, height=511)
        return frame

    def __tk_frame_container0(self, parent):
        frame = Frame(parent, )
        frame.place(x=0, y=0, width=349, height=480)
        return frame

    def __tk_scale_contrast(self, parent):
        scale = Scale(parent, from_=0, to=200, orient=tk.HORIZONTAL, length=200,
                      )
        scale.set(100)
        scale.place(x=0, y=42, width=150, height=50)
        return scale

    def __tk_label_brightness(self, parent):
        label = Label(parent, text="亮度调节", anchor="center", )
        label.place(x=26, y=102, width=87, height=30)
        return label

    def __tk_scale_brightness(self, parent):
        scale = Scale(parent, from_=0, to=200, orient=tk.HORIZONTAL, length=200,
                      )
        scale = Scale(parent, from_=0, to=200, orient=HORIZONTAL, length=200, )
        scale.place(x=0, y=125, width=150, height=50)
        scale.set(100)
        return scale

    def __tk_label_exposure(self, parent):
        label = Label(parent, text="曝光", anchor="center", )
        label.place(x=1, y=210, width=146, height=30)
        return label

    def __tk_scale_exposure(self, parent):
        scale = Scale(parent, from_=0, to=100, orient=tk.HORIZONTAL, length=200,
                      )
        scale.set(50)
        scale.place(x=0, y=231, width=150, height=50)
        return scale

    def __tk_label_pome(self, parent):
        label = Label(parent, text="光感", anchor="center", )
        label.place(x=53, y=276, width=50, height=30)
        return label

    def __tk_scale_pome(self, parent):
        scale = Scale(parent, from_=0, to=100, orient=tk.HORIZONTAL, length=200,
                      )
        scale.set(50)
        scale.place(x=0, y=309, width=150, height=50)
        return scale

    def __tk_scale_Sharpen(self, parent):
        scale = Scale(parent, from_=0, to=100, orient=tk.HORIZONTAL, length=200,
                      )
        scale.place(x=202, y=238, width=150, height=60)
        return scale

    def __tk_scale_Smooth(self, parent):
        scale = Scale(parent, from_=0, to=10, orient=tk.HORIZONTAL, length=200,
                      )
        scale.place(x=202, y=328, width=150, height=50)
        return scale

    def __tk_button_Histogram_equalization(self, parent):
        btn = Button(parent, text="直方图均衡化", takefocus=False, )
        btn.place(x=239, y=181, width=88, height=30)
        return btn

    def __tk_label_saturation(self, parent):
        label = Label(parent, text="饱和度调整", anchor="center", )
        label.place(x=43, y=383, width=92, height=30)
        return label

    def __tk_scale_saturation(self, parent):
        scale = Scale(parent, from_=0, to=200, orient=tk.HORIZONTAL, length=200,
                      )
        scale.set(100)
        scale.place(x=0, y=412, width=150, height=50)
        return scale

    def __tk_label_contrast(self, parent):
        label = Label(parent, text="对比度", anchor="center", )
        label.place(x=35, y=0, width=67, height=30)
        return label

    def __tk_frame_container1(self, parent):
        frame = Frame(parent, )
        frame.place(x=0, y=0, width=347, height=482)
        return frame

    def __tk_scale_Saturation(self, parent):
        scale = Scale(parent, orient=HORIZONTAL, )
        scale.place(x=13, y=342, width=150, height=50)
        scale.set(100)
        return scale

    def __tk_label_Hue(self, parent):
        label = Label(parent, text="H", anchor="center", )
        label.place(x=62, y=0, width=50, height=30)
        return label

    def __tk_scale_Hue(self, parent):
        scale = Scale(parent, from_=0, to=360, orient=tk.HORIZONTAL, length=200,
                      )
        scale.place(x=13, y=56, width=143, height=50)
        return scale

    def __tk_label_Saturation(self, parent):
        label = Label(parent, text="S", anchor="center", )
        label.place(x=62, y=127, width=50, height=30)
        return label

    def __tk_scale_lightness(self, parent):
        scale = Scale(parent, orient=HORIZONTAL, )
        scale.place(x=11, y=189, width=150, height=50)
        scale.set(100)
        return scale

    def __tk_label_lightness(self, parent):
        label = Label(parent, text="L", anchor="center", )
        label.place(x=64, y=251, width=50, height=50)
        return label

    def __tk_button_rotate(self, parent):
        btn = Button(parent, text="旋转", takefocus=False, )
        btn.place(x=1, y=47, width=50, height=30)
        return btn

    def __tk_button_trim(self, parent):
        btn = Button(parent, text="裁剪", takefocus=False, )
        btn.place(x=0, y=2, width=50, height=30)
        return btn

    def __tk_input_text(self, parent):
        ipt = Entry(parent, )
        ipt.place(x=0, y=35, width=150, height=30)
        return ipt

    def __tk_button_add(self, parent):
        btn = Button(parent, text="添加", takefocus=False, )
        btn.place(x=164, y=34, width=50, height=30)
        return btn

    def __tk_label_text_label(self, parent):
        label = Label(parent, text="添加文字", anchor="center", )
        label.place(x=0, y=0, width=148, height=30)
        return label

    def __tk_canvas_watermark(self, parent):
        canvas = Canvas(parent, )
        canvas.place(x=176, y=273, width=182, height=196)
        return canvas

    def __tk_button_open_watermark(self, parent):
        btn = Button(parent, text="选择水印图片", takefocus=False, )
        btn.place(x=1, y=282, width=146, height=30)
        return btn

    def __tk_button_add_watermark(self, parent):
        btn = Button(parent, text="添加水印", takefocus=False, )
        btn.place(x=11, y=343, width=107, height=30)
        return btn

    def __tk_canvas_image(self, parent):
        canvas = Canvas(parent)
        canvas.place(x=384, y=78, width=960, height=960)
        return canvas


class Win(WinGUI):
    def __init__(self):
        super().__init__()
        self.last_op = None
        self.__event_bind()
        self.config(menu=self.create_menu())

    def create_menu(self):
        menu = Menu(self, tearoff=False)
        menu.add_cascade(label="文件", menu=self.menu_lq4uzrg8(menu))
        menu.add_command(label="打开", command=self.load_image)
        menu.add_command(label="撤销", command=self.undo_image)
        menu.add_command(label="重做", command=self.init_image)
        menu.add_command(label="保存", command=self.save)
        menu.add_command(label="关于", command=self.about_me)
        return menu

    def menu_lq4uzrg8(self, parent):
        menu = Menu(parent, tearoff=False)
        menu.add_command(label="打开", command=self.load_image_wrapper)
        menu.add_command(label="保存", command=self.save)
        return menu

    def load_image_wrapper(self, evt=None):
        # 弹出文件选择对话框
        file_path = filedialog.askopenfilename()

        if file_path:
            # 打开并调整图片大小以适应画布
            self.image_stack = []
            self.image = Image.open(file_path)
            self.adjust_image_size()
            self.init_img = self.image  # 保持原图不变
            self.image_stack.append(self.image)
            self.show_image()

    def load_watermark_image(self, evt=None):
        self.load_image(flag=1)

    def save(self):
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

    def undo_image(self, evt=None):
        if hasattr(self, 'image_stack') and self.image is not None:
            # 撤销按钮的处理方法
            if len(self.image_stack) >= 1:
                # 弹出当前图像

                # 恢复到上一个状态
                self.image = self.image_stack[-1]

                # 当只剩下最初的原图时不能再出栈了，不然后面入栈其他的再撤销会找不到原图的
                if len(self.image_stack) > 1:
                    self.image_stack.pop()
                # 显示图像
                self.show_image()

    def uncancel(self):
        print("点击了菜单")

    def init_image(self):
        self.image = self.image_stack[0].copy()
        self.show_image()

    def about_me(self):
        print("点击了菜单")

    def adjust_brightness(self, evt=None):
        if self.last_op != inspect.currentframe().f_code.co_name:
            self.image_back = self.image
        # 调整亮度功能
        if hasattr(self, 'image_back') and self.image is not None:
            brightness_factor = self.tk_scale_brightness.get() / 100.0
            # 在增强亮度之前检查 self.image 是否不为 None
            brightness_adjusted = ImageEnhance.Brightness(self.image_back).enhance(brightness_factor)

            # 显示调整亮度后的图片
            self.image = brightness_adjusted
            self.show_image(flag=1)
            # 获取当前函数的名称
            self.last_op = inspect.currentframe().f_code.co_name

    def _adjust_exposure(self, img, b):
        # 曝光度调整 参数 b: 0~100
        print("pre", b)
        b = np.float32(b - 50) / 20.0
        print("pro", b)
        res = img.astype(np.float32)
        print(pow(2, b))
        res = res * pow(2, b)
        res = np.where(res > 255, 255, res)
        res = res.astype(np.uint8)
        return res

    def adjust_exposure(self, event=None):
        if self.last_op != inspect.currentframe().f_code.co_name:
            self.image_back = self.image
        # 调整曝光度功能
        if hasattr(self, 'image'):
            exposure_factor = self.tk_scale_exposure.get()
            exposure_adjusted = self._adjust_exposure(np.array(self.image_back), exposure_factor)
            self.image = Image.fromarray(exposure_adjusted)
            self.show_image(flag=1)
            self.last_op = inspect.currentframe().f_code.co_name

    def lightSense(self, img, a):
        a = np.float32(a - 50) / 80.0
        a = a * 255
        res = img.astype(np.float32)
        res = res + a * res / 255.0
        res = np.where(res > 255, 255, res)
        res = np.where(res < 0, 0, res)
        res = res.astype(np.uint8)
        return res

    def adjust_light_sense(self, evt):
        if self.last_op != inspect.currentframe().f_code.co_name:
            self.image_back = self.image
        # 调整光感功能
        if hasattr(self, 'image'):
            light_sense_factor = self.tk_scale_pome.get()
            print("光感系数", light_sense_factor)
            light_sense_adjusted = self.lightSense(np.array(self.image_back), light_sense_factor)

            # 将 NumPy 数组转换回 PIL 图像
            self.image = Image.fromarray(light_sense_adjusted)

            # 显示调整光感后的图片
            self.show_image(flag=1)
            self.last_op = inspect.currentframe().f_code.co_name

    def sharpen(self, evt):
        if self.last_op != inspect.currentframe().f_code.co_name:
            self.image_back = self.image
        if hasattr(self, 'image'):
            # Convert to OpenCV format
            img_np = np.array(self.image_back)
            img_cv2 = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)

            # 获取滑块值
            sharpen_value = self.tk_scale_Sharpen.get()
            # 当滑块的值为0时不调整
            print(sharpen_value)

            if sharpen_value < 0.1:
                self.image=self.image_back
                self.show_image(flag=1)
                self.last_op = inspect.currentframe().f_code.co_name
                return
            sharpen_value = max(sharpen_value, 0) / 100.0  # 将取值截断到 0 到 1 之间
            print(sharpen_value)

            # Apply sharpening filter based on slider value
            kernel = np.array([[-1, -1, -1],
                               [-1, 9 + sharpen_value, -1],
                               [-1, -1, -1]])
            sharpened_img = cv2.filter2D(img_cv2, -1, kernel)

            # Convert back to PIL format
            self.image = Image.fromarray(cv2.cvtColor(sharpened_img, cv2.COLOR_BGR2RGB))
            self.show_image(flag=1)
            self.last_op = inspect.currentframe().f_code.co_name

    def smooth(self, evt=None):
        if self.last_op != inspect.currentframe().f_code.co_name:
            self.image_back = self.image
        if hasattr(self, 'image'):
            # Convert to OpenCV format
            img_np = np.array(self.image_back)
            img_cv2 = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)

            # 获取滑块值，并确保是正奇数
            smooth_value = self.tk_scale_Smooth.get()
            if smooth_value % 2 == 0:
                smooth_value += 1
            smooth_value = smooth_value if smooth_value % 2 != 0 else smooth_value + 1  #
            print(smooth_value)

            # Apply smoothing filter based on slider value
            smoothed_img = cv2.GaussianBlur(img_cv2, (smooth_value, smooth_value), 0)

            # Convert back to PIL format
            self.image = Image.fromarray(cv2.cvtColor(smoothed_img, cv2.COLOR_BGR2RGB))
            self.show_image(flag=1)
            self.last_op = inspect.currentframe().f_code.co_name

    def adjust_equalize(self, evt):
        # 直方图均衡化功能
        if hasattr(self, 'image'):
            equalize_adjusted = ImageOps.equalize(self.image)
            self.image = equalize_adjusted
            self.show_image()
            self.image_stack.append(self.image.copy())

    def adjust_saturation(self, evt):
        if self.last_op != inspect.currentframe().f_code.co_name:
            self.image_back = self.image
        # 饱和度调整功能
        if hasattr(self, 'image'):
            saturation_factor = self.tk_scale_saturation.get() / 100.0
            saturation_adjusted = ImageEnhance.Color(self.init_img).enhance(saturation_factor)
            self.image = saturation_adjusted
            self.show_image(flag=1)
            self.last_op = inspect.currentframe().f_code.co_name

    def adjust_L(self, evt):
        print("<Configure>事件未处理:", evt)

    def adjust_H(self, evt):
        print("HHHHH")

    def adjust_S(self, evt):
        print("<Configure>事件未处理:", evt)

    def rotate_image(self, evt=None):
        # 旋转图片功能
        if hasattr(self, 'image'):
            rotation_angle = 90
            rotated_image = self.image.rotate(rotation_angle, expand=True)

            # 显示旋转后的图片
            self.image = rotated_image
            self.image_stack.append(self.image)
            self.show_image()

    def crop_image(self, parent, evt=None):
        print("sdsada")
        # 裁剪图片功能
        if hasattr(self, 'image'):
            print("裁剪")
            self.canvas.place(x=0, y=0, width=0, height=0)
            self.photo = ImageTk.PhotoImage(self.image)
            self.crop_canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)
            # self.crop_canvas.place(x=384, y=78, width=960, height=960)
            # crop_percent = 0.8
            # width, height = self.image.size
            # left = (1 - crop_percent) * width / 2
            # top = (1 - crop_percent) * height / 2
            # right = (1 + crop_percent) * width / 2
            # bottom = (1 + crop_percent) * height / 2
            # cropped_image = self.image.crop((left, top, right, bottom))
            #
            # # 显示裁剪后的图片
            # self.image = cropped_image
            self.show_image()

    def adjust_contrast(self, event=None):
        if self.last_op != inspect.currentframe().f_code.co_name:
            self.image_back = self.image

        # 调整对比度功能
        if hasattr(self, 'image_back') and self.image is not None:
            contrast_factor = self.tk_scale_contrast.get() / 100.0
            # 在增强对比度之前检查 self.image 是否不为 None
            contrast_adjusted = ImageEnhance.Contrast(self.image_back).enhance(contrast_factor)

            # 显示调整对比度后的图片
            self.image = contrast_adjusted
            self.show_image(flag=1)
            # 获取当前函数的名称
            self.last_op = inspect.currentframe().f_code.co_name

    def add_text(self, evt):
        text = self.tk_input_text.get()
        draggable_text = DraggableText(self.canvas, text, self.canvas.winfo_x(), self.canvas.winfo_y())
        self.last_op = self.add_text.__name__

    def watermark(self, evt=None):
        # 打开背景图和水印图
        background = self.image.convert('RGBA')
        watermark = self.watermark_image_back.convert('RGBA')
        # 调整水印大小以适应背景图
        alpha = 0.1
        # background = self.watermark_image_back.convert('RGBA')
        # watermark = self.image.convert('RGBA')
        # # 调整水印大小以适应背景图
        # alpha = 0.9
        watermark = watermark.resize(background.size, Image.LANCZOS)

        # 将水印叠加到背景图上
        result = Image.blend(background, watermark, alpha)
        self.image = result
        self.show_image()

        # 保存结果
        # result.save(output_path, format='PNG')

    def enter(self, evt=None):
        if self.last_op == self.add_text.__name__:
            return
        print("enter")
        # 显示调整后的图片
        if hasattr(self, 'init_img'):
            self.init_img = self.image_stack[-1]
            self.init_photo = ImageTk.PhotoImage(self.init_img)
            self.canvas.delete("all")
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.init_photo)

    def refresh_img(self, evt=None):
        if self.last_op == self.add_text.__name__:
            self.last_op = self.refresh_img.__name__
            return
        print("refresh")
        if hasattr(self, 'image_back') and hasattr(self, 'image'):
            # 逆天BUG
            # self.image_back = self.image写成self.image=self.image_back  导致定位BUG到这边但是逻辑检查一直都没问题
            # 原本以为经过图像增强的图像会改变在self.image_back上实际上是self.image
            self.image_back = self.image  # 这对于从滑块切到其它选项卡时会起作用
            # ------
            if self.image != self.image_stack[-1]:
                self.image_stack.append(self.image)  # 入栈及时保存
            self.photo = ImageTk.PhotoImage(self.image_back)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)
            # 查询当前选项卡的名称
            # 如果是HSL调整
            # 则将self.image转hsl

            # 查询当前选项卡的名称
            current_tab = self.tk_tabs_option.tab(self.tk_tabs_option.select(), "text")

            # 查询当前选项卡的名称
            current_tab = self.tk_tabs_option.tab(self.tk_tabs_option.select(), "text")

            if current_tab == "HSL调整":
                # 获取图像的宽度和高度
                width, height = self.image_back.size

                # 遍历图像的每个像素
                for x in range(width):
                    for y in range(height):
                        # 获取当前像素的 RGB 值
                        r, g, b = self.image_back.getpixel((x, y))

                        # 将 RGB 转换为 HSL
                        h, s, l = self.rgb_to_hsl(r, g, b)

                        # 根据 HSL 调整，这里需要根据你的调整算法修改
                        # 这里只是一个示例，你需要根据你的需求进行调整
                        h = (h + 0.1) % 1.0
                        s = min(1.0, s * 1.1)
                        l = min(1.0, l * 1.1)

                        # 将 HSL 转换回 RGB
                        new_r, new_g, new_b = self.hsl_to_rgb(h, s, l)

                        # 更新图像的当前像素
                        self.image_back.putpixel((x, y), (int(new_r), int(new_g), int(new_b)))

            if self.image != self.image_stack[-1]:
                self.image_stack.append(self.image)  # 入栈及时保存
            self.photo = ImageTk.PhotoImage(self.image_back)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

    def leave(self, evt=None):
        if self.last_op == self.add_text.__name__:
            # 获取画布内容
            print("text")
            x = self.winfo_rootx() + self.canvas.winfo_x() + 2
            print(x)
            y = self.winfo_rooty() + self.canvas.winfo_y() + 2
            print(y)
            x1 = x + self.new_width - 4
            print(self.canvas.winfo_width())
            y1 = y + self.new_height - 2
            print(self.canvas.winfo_height())
            image = ImageGrab.grab((x, y, x1, y1))

            # 保存画布内容为图像文件
            save_path = "../image/canvas_snapshot.png"
            image.save(save_path)
            self.image = Image.open(save_path)
            print("保存成功:", save_path)
            return
        print("leave")
        if hasattr(self, 'image_back') and hasattr(self, 'image'):
            self.canvas.delete("all")
            # 当photo改变时要即使create_image才能显示正常图像
            self.photo = ImageTk.PhotoImage(self.image)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)
        else:
            print("bug")

    def rgb_to_hsl(self, r, g, b):
        # 将RGB值归一化到[0, 1]范围
        r /= 255.0
        g /= 255.0
        b /= 255.0

        # 计算max和min
        max_val = max(r, g, b)
        min_val = min(r, g, b)

        # 计算亮度（l）
        l = (max_val + min_val) / 2.0

        # 如果max和min相等，灰度色调
        if max_val == min_val:
            h = 0.0
            s = 0.0
        else:
            # 计算饱和度（s）
            s = (max_val - min_val) / (1 - abs(2 * l - 1))

            # 计算色相（h）
            if max_val == r:
                h = 60 * ((g - b) / (max_val - min_val) % 6)
            elif max_val == g:
                h = 60 * ((b - r) / (max_val - min_val) + 2)
            elif max_val == b:
                h = 60 * ((r - g) / (max_val - min_val) + 4)

        # 规范化色相到[0, 360)
        h = (h + 360) % 360

        return h, s, l

    def hsl_to_rgb(self, h, s, l):
        # 规范化色相到[0, 360)
        h = h % 360

        # 如果饱和度为0，灰度色彩
        if s == 0:
            r = g = b = int(l * 255)
        else:
            # 计算辅助变量
            if l < 0.5:
                temp2 = l * (1.0 + s)
            else:
                temp2 = l + s - l * s

            temp1 = 2.0 * l - temp2

            # 计算RGB的每个分量
            h /= 360.0
            rgb = [0, 0, 0]
            for i in range(3):
                t = h + 1.0 / 3.0 * -(i - 1)
                if t < 0:
                    t += 1
                elif t > 1:
                    t -= 1

                if 6.0 * t < 1.0:
                    rgb[i] = int((temp1 + (temp2 - temp1) * 6.0 * t) * 255)
                elif 2.0 * t < 1.0:
                    rgb[i] = int(temp2 * 255)
                elif 3.0 * t < 2.0:
                    rgb[i] = int((temp1 + (temp2 - temp1) * (2.0 / 3.0 - t) * 6.0) * 255)
                else:
                    rgb[i] = int(temp1 * 255)
        return tuple(rgb)

    def on_mouse_press(self, event):
        global start_x, start_y
        start_x = event.x
        start_y = event.y

    def on_mouse_click(self, event):
        self.crop_canvas.delete("aa")
        self.crop_canvas.delete("bb")
        self.crop_canvas.delete("cc")
        self.crop_canvas.delete("dd")
        self.crop_canvas.create_line(start_x, start_y, event.x, start_y, fill="white", tags="aa", smooth=True)  # 绘制水平直线
        self.crop_canvas.create_line(start_x, event.y, event.x, event.y, fill="white", tags="aa", smooth=True)  # 绘制水平直线
        self.crop_canvas.create_line(event.x, start_y, event.x, event.y, fill="white", tags="bb", smooth=True)  # 绘制垂直直线
        self.crop_canvas.create_line(start_x, start_y, start_x, event.y, fill="white", tags="bb", smooth=True)  # 绘制垂直直线

    def on_mouse_release(self, evt=None):
        def display_cro():
            # 实现图像裁剪根据两点坐标裁剪
            self.image = self.image.crop((start_x, start_y, evt.x, evt.y))

        self.crop_canvas.place(x=384, y=78, width=960, height=960)
        self.canvas.place(x=384, y=78, width=960, height=960)
        display_cro()
        self.photo = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

    def __event_bind(self):
        self.tk_button_open_image.bind('<Button-1>', self.load_image)
        self.tk_scale_contrast.bind('<B1-Motion>', self.adjust_contrast)
        self.tk_scale_brightness.bind('<B1-Motion>', self.adjust_brightness)
        self.tk_scale_exposure.bind('<B1-Motion>', self.adjust_exposure)
        self.tk_scale_pome.bind('<B1-Motion>', self.adjust_light_sense)
        self.tk_scale_Sharpen.bind('<B1-Motion>', self.sharpen)
        self.tk_scale_Smooth.bind('<B1-Motion>', self.smooth)
        self.tk_button_Histogram_equalization.bind('<Button-1>', self.adjust_equalize)
        self.tk_scale_saturation.bind('<B1-Motion>', self.adjust_saturation)
        self.tk_scale_Saturation.bind('<Configure>', self.adjust_L)
        self.tk_scale_Hue.bind('<B1-Motion>', self.adjust_H)
        self.tk_scale_lightness.bind('<Configure>', self.adjust_S)
        self.tk_button_rotate.bind('<Button-1>', self.rotate_image)
        self.tk_button_trim.bind('<Button-1>', self.crop_image)
        self.tk_button_add.bind('<Button-1>', self.add_text)
        self.tk_button_open_watermark.bind('<Button-1>', self.load_watermark_image)
        self.tk_button_add_watermark.bind('<Button-1>', self.watermark)
        self.canvas.bind('<Enter>', self.enter)
        self.canvas.bind('<Leave>', self.leave)  # 服了我直接调用show_image(flag=1,refusre=1)时这个事件会失效
        self.crop_canvas.bind("<ButtonPress>", self.on_mouse_press)
        self.crop_canvas.bind('<B1-Motion>', self.on_mouse_click)
        self.crop_canvas.bind("<ButtonRelease-1>", self.on_mouse_release)

        self.tk_tabs_option.bind('<<NotebookTabChanged>>', self.refresh_img)
        self.tk_button_cancel.bind('<Button-1>', self.undo_image)
        pass


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


if __name__ == "__main__":
    win = Win()
    win.mainloop()
