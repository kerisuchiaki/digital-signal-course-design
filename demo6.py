"""
本代码由[Tkinter布局助手]生成
官网:https://www.pytk.net
QQ交流群:788392508
"""
from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
import tkinter as tk

from PIL import Image, ImageTk


class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.photo = None
        self.init_photo = None
        self.image_back = None
        self.init_img = None
        self.image = None
        self.image_stack = None
        self.__win()
        self.tk_button_lq3wd5dc = self.__tk_button_lq3wd5dc(self)
        self.tk_button_lq3wd6vd = self.__tk_button_lq3wd6vd(self)
        self.tk_button_lq3wdh0h = self.__tk_button_lq3wdh0h(self)
        self.tk_button_lq3wdimy = self.__tk_button_lq3wdimy(self)
        self.tk_tabs_lq3wrrpn = self.__tk_tabs_lq3wrrpn(self)
        self.tk_frame_lq3ww73l = self.__tk_frame_lq3ww73l(self.tk_tabs_lq3wrrpn_0)
        self.tk_button_lq3wwibn = self.__tk_button_lq3wwibn(self.tk_frame_lq3ww73l)
        self.tk_button_lq3xbrg6 = self.__tk_button_lq3xbrg6(self.tk_frame_lq3ww73l)
        self.tk_frame_lq3wwwnm = self.__tk_frame_lq3wwwnm(self.tk_tabs_lq3wrrpn_0)
        self.canvas = self.__tk_canvas_lq3wx1wz(self.tk_frame_lq3wwwnm)

    def __win(self):
        self.title("Tkinter布局助手")
        # 设置窗口大小、居中
        width = 600
        height = 500
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)

        self.resizable(width=False, height=False)

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

    def __tk_button_lq3wd5dc(self, parent):
        btn = Button(parent, text="打开", takefocus=False, command=self.load_image)
        btn.place(x=0, y=1, width=50, height=30)
        return btn

    def __tk_button_lq3wd6vd(self, parent):
        btn = Button(parent, text="撤销", takefocus=False, )
        btn.place(x=78, y=0, width=50, height=30)
        return btn

    def __tk_button_lq3wdh0h(self, parent):
        btn = Button(parent, text="修改", takefocus=False, )
        btn.place(x=159, y=0, width=50, height=30)
        return btn

    def __tk_button_lq3wdimy(self, parent):
        btn = Button(parent, text="保存", takefocus=False, )
        btn.place(x=234, y=1, width=50, height=30)
        return btn

    def __tk_tabs_lq3wrrpn(self, parent):
        frame = Notebook(parent)
        self.tk_tabs_lq3wrrpn_0 = self.__tk_frame_lq3wrrpn_0(frame)
        frame.add(self.tk_tabs_lq3wrrpn_0, text="几何变换")
        self.tk_tabs_lq3wrrpn_1 = self.__tk_frame_lq3wrrpn_1(frame)
        frame.add(self.tk_tabs_lq3wrrpn_1, text="图像增强")
        self.tk_tabs_lq3wrrpn_2 = self.__tk_frame_lq3wrrpn_2(frame)
        frame.add(self.tk_tabs_lq3wrrpn_2, text="HSL调整")
        frame.place(x=0, y=44, width=586, height=245)
        return frame

    def __tk_frame_lq3wrrpn_0(self, parent):
        frame = Frame(parent)
        frame.place(x=0, y=44, width=586, height=245)
        return frame

    def __tk_frame_lq3wrrpn_1(self, parent):
        frame = Frame(parent)
        frame.place(x=0, y=44, width=586, height=245)
        return frame

    def __tk_frame_lq3wrrpn_2(self, parent):
        frame = Frame(parent)
        frame.place(x=0, y=44, width=586, height=245)
        return frame

    def __tk_frame_lq3ww73l(self, parent):
        frame = Frame(parent, )
        frame.place(x=385, y=0, width=200, height=150)
        return frame

    def __tk_button_lq3wwibn(self, parent):
        btn = Button(parent, text="裁剪", takefocus=False, )
        btn.place(x=0, y=0, width=50, height=30)
        return btn

    def __tk_button_lq3xbrg6(self, parent):
        btn = Button(parent, text="旋转", takefocus=False, )
        btn.place(x=0, y=30, width=50, height=30)
        return btn

    def __tk_frame_lq3wwwnm(self, parent):
        frame = Frame(parent, )
        frame.place(x=0, y=0, width=336, height=245)
        return frame

    def __tk_canvas_lq3wx1wz(self, parent):
        canvas = Canvas(parent, bg="#aaa")
        canvas.place(x=0, y=0, width=334, height=245)
        return canvas

    def load_image(self):
        # 弹出文件选择对话框
        file_path = filedialog.askopenfilename()

        if file_path:
            # 打开并调整图片大小以适应画布
            self.image_stack = []
            self.image = Image.open(file_path)
            self.init_img = self.image  # 这里这样写也能保持原图不变奇怪
            # self.adjust_image_size()
            # self.image_stack.append(self.image.copy())
            #
            self.show_image()

            # 更新显示图片路径的Label
            # self.image_path_label.config(text="当前图片路径：" + file_path)

    def show_image(self,flag=0):
            # 显示调整后的图片
            if flag == 0:
                self.image_back = self.image
            self.photo = ImageTk.PhotoImage(self.image)
            self.init_photo = ImageTk.PhotoImage(self.init_img)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

class Win(WinGUI):
    def __init__(self):
        super().__init__()
        self.__event_bind()

    def __event_bind(self):
        pass


if __name__ == "__main__":
    win = Win()
    win.mainloop()
