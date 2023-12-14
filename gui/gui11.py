"""
本代码由[Tkinter布局助手]生成
官网:https://www.pytk.net
QQ交流群:788392508
"""
import inspect
from tkinter import *
from tkinter import filedialog
# from tkinter.ttk import *
# del Scale
import tkinter as tk
from tkinter.ttk import Notebook

from PIL import Image, ImageTk, ImageEnhance


class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.tk_button_open_image = self.__tk_button_open_image(self)
        self.tk_button_cancel = self.__tk_button_cancel(self)
        self.tk_button_modify = self.__tk_button_modify(self)
        self.tk_button_save = self.__tk_button_save(self)
        self.tk_tabs_option = self.__tk_tabs_option(self)
        self.tk_frame_container0 = self.__tk_frame_container0(self.tk_tabs_option_1)
        self.tk_scale_slider1 = self.__tk_scale_slider1(self.tk_frame_container0)
        # self.tk_scale_slider1 =
        self.tk_label_brightness = self.__tk_label_brightness(self.tk_frame_container0)
        self.tk_scale_slider2 = self.__tk_scale_slider2(self.tk_frame_container0)
        self.tk_label_exposure = self.__tk_label_exposure(self.tk_frame_container0)
        self.tk_scale_slider3 = self.__tk_scale_slider3(self.tk_frame_container0)
        self.tk_label_pome = self.__tk_label_pome(self.tk_frame_container0)
        self.tk_scale_slider4 = self.__tk_scale_slider4(self.tk_frame_container0)
        self.tk_button_Sharpen = self.__tk_button_Sharpen(self.tk_frame_container0)
        self.tk_button_Smooth = self.__tk_button_Smooth(self.tk_frame_container0)
        self.tk_button_Histogram_equalization = self.__tk_button_Histogram_equalization(self.tk_frame_container0)
        self.tk_label_saturation = self.__tk_label_saturation(self.tk_frame_container0)
        self.tk_scale_slider5 = self.__tk_scale_slider5(self.tk_frame_container0)
        self.tk_label_contrast = self.__tk_label_contrast(self.tk_frame_container0)
        self.tk_frame_container1 = self.__tk_frame_container1(self.tk_tabs_option_2)
        self.tk_scale_Saturation = self.__tk_scale_Saturation(self.tk_frame_container1)
        self.tk_label_Hue = self.__tk_label_Hue(self.tk_frame_container1)
        self.tk_scale_slider6 = self.__tk_scale_slider6(self.tk_frame_container1)
        self.tk_label_Saturation = self.__tk_label_Saturation(self.tk_frame_container1)
        self.tk_scale_slider7 = self.__tk_scale_slider7(self.tk_frame_container1)
        self.tk_label_lightness = self.__tk_label_lightness(self.tk_frame_container1)
        self.tk_button_rotate = self.__tk_button_rotate(self.tk_tabs_option_0)
        self.tk_button_trim = self.__tk_button_trim(self.tk_tabs_option_0)
        self.tk_input_text = self.__tk_input_text(self.tk_tabs_option_3)
        self.tk_button_add = self.__tk_button_add(self.tk_tabs_option_3)
        self.tk_label_text_label = self.__tk_label_text_label(self.tk_tabs_option_3)
        self.tk_canvas_watermark = self.__tk_canvas_watermark(self.tk_tabs_option_3)
        self.tk_button_open_watermark = self.__tk_button_open_watermark(self.tk_tabs_option_3)
        self.tk_button_add_watermark = self.__tk_button_add_watermark(self.tk_tabs_option_3)
        self.canvas = self.__tk_canvas_image(self)

    def load_image(self, evt=None):
        # 弹出文件选择对话框
        file_path = filedialog.askopenfilename()

        if file_path:
            # 打开并调整图片大小以适应画布
            self.image_stack = []
            self.image = Image.open(file_path)
            self.init_img = self.image.copy()  # 保持原图不变
            self.adjust_image_size()
            self.image_stack.append(self.image.copy())
            self.show_image()

    def show_image(self, flag=0):
        # 显示调整后的图片
        if flag == 0:
            self.image_back = self.image
        self.photo = ImageTk.PhotoImage(self.image)
        self.init_photo = ImageTk.PhotoImage(self.init_img)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

    def adjust_image_size(self):
        # 获取画布的大小
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()

        # 获取图像的原始大小
        original_width, original_height = self.image.size

        # 计算调整后的大小，保持纵横比
        if original_width > original_height:
            new_width = canvas_width
            new_height = int((canvas_width / original_width) * original_height)
        else:
            new_height = canvas_height
            new_width = int((canvas_height / original_height) * original_width)

        # 使用thumbnail方法调整图像大小
        self.image.thumbnail((new_width, new_height), Image.LANCZOS)

    def __win(self):
        self.title("Tkinter布局助手")
        # 设置窗口大小、居中
        width = 1360
        height = 681
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
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

    def __tk_scale_slider1(self, parent):
        # scale = Scale(parent, orient=HORIZONTAL, )
        scale = Scale(parent, from_=0, to=200, orient=tk.HORIZONTAL, length=200,
                      )
        scale.set(100)
        scale.place(x=0, y=42, width=150, height=50)
        return scale

    def __tk_label_brightness(self, parent):
        label = Label(parent, text="亮度调节", anchor="center", )
        label.place(x=26, y=82, width=87, height=30)
        return label

    def __tk_scale_slider2(self, parent):
        scale = Scale(parent, orient=HORIZONTAL, )
        scale.place(x=0, y=125, width=150, height=30)
        return scale

    def __tk_label_exposure(self, parent):
        label = Label(parent, text="曝光", anchor="center", )
        label.place(x=1, y=180, width=146, height=30)
        return label

    def __tk_scale_slider3(self, parent):
        scale = Scale(parent, orient=HORIZONTAL, )
        scale.place(x=0, y=231, width=150, height=30)
        return scale

    def __tk_label_pome(self, parent):
        label = Label(parent, text="光感", anchor="center", )
        label.place(x=53, y=276, width=50, height=30)
        return label

    def __tk_scale_slider4(self, parent):
        scale = Scale(parent, orient=HORIZONTAL, )
        scale.place(x=0, y=329, width=150, height=30)
        return scale

    def __tk_button_Sharpen(self, parent):
        btn = Button(parent, text="锐化", takefocus=False, )
        btn.place(x=252, y=238, width=50, height=30)
        return btn

    def __tk_button_Smooth(self, parent):
        btn = Button(parent, text="平滑", takefocus=False, )
        btn.place(x=255, y=328, width=50, height=30)
        return btn

    def __tk_button_Histogram_equalization(self, parent):
        btn = Button(parent, text="直方图均衡化", takefocus=False, )
        btn.place(x=239, y=131, width=88, height=30)
        return btn

    def __tk_label_saturation(self, parent):
        label = Label(parent, text="饱和度调整", anchor="center", )
        label.place(x=43, y=383, width=92, height=30)
        return label

    def __tk_scale_slider5(self, parent):
        scale = Scale(parent, orient=HORIZONTAL, )
        scale.place(x=0, y=452, width=150, height=30)
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
        scale.place(x=13, y=342, width=150, height=30)
        return scale

    def __tk_label_Hue(self, parent):
        label = Label(parent, text="H", anchor="center", )
        label.place(x=62, y=0, width=50, height=30)
        return label

    def __tk_scale_slider6(self, parent):
        scale = Scale(parent, orient=HORIZONTAL, )
        scale.place(x=13, y=56, width=143, height=30)
        return scale

    def __tk_label_Saturation(self, parent):
        label = Label(parent, text="S", anchor="center", )
        label.place(x=62, y=127, width=50, height=30)
        return label

    def __tk_scale_slider7(self, parent):
        scale = Scale(parent, orient=HORIZONTAL, )
        scale.place(x=11, y=189, width=150, height=30)
        return scale

    def __tk_label_lightness(self, parent):
        label = Label(parent, text="L", anchor="center", )
        label.place(x=64, y=271, width=50, height=30)
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
        canvas = Canvas(parent, bg="#aaa")
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
        menu.add_command(label="撤销", command=self.cancel)
        menu.add_command(label="反撤销", command=self.uncancel)
        menu.add_command(label="重做", command=self.init_image)
        menu.add_command(label="关于", command=self.about_me)
        return menu

    def menu_lq4uzrg8(self, parent):
        menu = Menu(parent, tearoff=False)
        menu.add_command(label="打开", command=self.load_image_wrapper)
        menu.add_command(label="保存", command=self.save)
        return menu

    def load_image_wrapper(self):
        # 弹出文件选择对话框
        file_path = filedialog.askopenfilename()

        if file_path:
            # 打开并调整图片大小以适应画布
            self.image_stack = []
            self.image = Image.open(file_path)
            self.init_img = self.image.copy()  # 保持原图不变
            self.adjust_image_size()
            self.image_stack.append(self.image.copy())
            self.show_image()

    def save(self):
        print("点击了菜单")

    def cancel(self):
        print("点击了菜单")

    def uncancel(self):
        print("点击了菜单")

    def init_image(self):
        print("点击了菜单")

    def about_me(self):
        print("点击了菜单")

        # def adjust_contrast(self, event=None):
        #     if self.last_op != inspect.currentframe().f_code.co_name:
        #         self.image_back = self.image

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

    def adjust_brightness(self, evt):
        print("<Configure>事件未处理:", evt)

    def adjust_exposure(self, evt):
        print("<Configure>事件未处理:", evt)

    def adjust_light_sense(self, evt):
        print("<Configure>事件未处理:", evt)

    def sharpen(self, evt):
        print("<Button-1>事件未处理:", evt)

    def smooth(self, evt):
        print("<Button-1>事件未处理:", evt)

    def adjust_equalize(self, evt):
        print("<Button-1>事件未处理:", evt)

    def adjust_saturation(self, evt):
        print("<Configure>事件未处理:", evt)

    def adjust_L(self, evt):
        print("<Configure>事件未处理:", evt)

    def adjust_H(self, evt):
        print("<Configure>事件未处理:", evt)

    def adjust_S(self, evt):
        print("<Configure>事件未处理:", evt)

    def rotate_image(self, evt=None):
        # 旋转图片功能
        if hasattr(self, 'image'):
            rotation_angle = 90
            rotated_image = self.image.rotate(rotation_angle, expand=True)

            # 显示旋转后的图片
            self.image = rotated_image
            self.image_stack.append(self.image.copy())
            self.show_image()

    def crop_image(self, evt=None):
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
            self.show_image()

    def adjust_contrast(self, event=None):
        if self.last_op != inspect.currentframe().f_code.co_name:
            self.image_back = self.image

        # 调整对比度功能
        if hasattr(self, 'image_back') and self.image is not None:
            contrast_factor = self.tk_scale_slider1.get() / 100.0
            # 在增强对比度之前检查 self.image 是否不为 None
            contrast_adjusted = ImageEnhance.Contrast(self.image_back).enhance(contrast_factor)

            # 显示调整对比度后的图片
            self.image = contrast_adjusted
            self.show_image(1)
            # 获取当前函数的名称
            self.last_op = inspect.currentframe().f_code.co_name

    def adjust_contrast(self, event=None):
        if self.last_op != inspect.currentframe().f_code.co_name:
            self.image_back = self.image

        # 调整对比度功能
        if hasattr(self, 'image_back') and self.image is not None:
            contrast_factor = self.tk_scale_slider1.get() / 50.0  # Adjust the scaling factor
            # 在增强对比度之前检查 self.image 是否不为 None
            contrast_adjusted = ImageEnhance.Contrast(self.image_back).enhance(contrast_factor)

            # 显示调整对比度后的图片
            self.image = contrast_adjusted
            self.show_image(1)
            # 获取当前函数的名称
            self.last_op = inspect.currentframe().f_code.co_name

    def add_text(self, evt):
        print("<Button-1>事件未处理:", evt)

    def watermark(self, evt):
        print("<Button-1>事件未处理:", evt)

    def hint(self, evt):
        print("<Enter>事件未处理:", evt)

    def __event_bind(self):
        self.tk_button_open_image.bind('<Button-1>', self.load_image)
        self.tk_scale_slider1.bind('<B1-Motion>', self.adjust_contrast)
        self.tk_scale_slider2.bind('<Configure>', self.adjust_brightness)
        self.tk_scale_slider3.bind('<Configure>', self.adjust_exposure)
        self.tk_scale_slider4.bind('<Configure>', self.adjust_light_sense)
        self.tk_button_Sharpen.bind('<Button-1>', self.sharpen)
        self.tk_button_Smooth.bind('<Button-1>', self.smooth)
        self.tk_button_Histogram_equalization.bind('<Button-1>', self.adjust_equalize)
        self.tk_scale_slider5.bind('<Configure>', self.adjust_saturation)
        self.tk_scale_Saturation.bind('<Configure>', self.adjust_L)
        self.tk_scale_slider6.bind('<Configure>', self.adjust_H)
        self.tk_scale_slider7.bind('<Configure>', self.adjust_S)
        self.tk_button_rotate.bind('<Button-1>', self.rotate_image)
        self.tk_button_trim.bind('<Button-1>', self.crop_image)
        self.tk_button_add.bind('<Button-1>', self.add_text)
        self.tk_button_open_watermark.bind('<Button-1>', self.load_image)
        self.tk_button_add_watermark.bind('<Button-1>', self.watermark)
        self.canvas.bind('<Enter>', self.hint)
        pass


if __name__ == "__main__":
    win = Win()
    win.mainloop()
