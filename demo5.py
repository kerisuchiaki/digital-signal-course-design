"""
本代码由[Tkinter布局助手]生成
官网:https://www.pytk.net
QQ交流群:788392508
"""
from tkinter import filedialog
from tkinter.ttk import *

from PIL import Image


class WinGUI(Tk):
    def __init__(self):
        super().__init__()
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
        self.tk_canvas_lq3wx1wz = self.__tk_canvas_lq3wx1wz(self.tk_frame_lq3wwwnm)
        self.tk_frame_lq3wxf80 = self.__tk_frame_lq3wxf80(self.tk_tabs_lq3wrrpn_1)
        self.tk_scale_lq3wxmuy = self.__tk_scale_lq3wxmuy(self.tk_frame_lq3wxf80)
        self.tk_label_lq3wxrk2 = self.__tk_label_lq3wxrk2(self.tk_frame_lq3wxf80)
        self.tk_label_lq3xdc9w = self.__tk_label_lq3xdc9w(self.tk_frame_lq3wxf80)
        self.tk_scale_lq3xdkzk = self.__tk_scale_lq3xdkzk(self.tk_frame_lq3wxf80)
        self.tk_label_lq3xe8ky = self.__tk_label_lq3xe8ky(self.tk_frame_lq3wxf80)
        self.tk_scale_lq3xehli = self.__tk_scale_lq3xehli(self.tk_frame_lq3wxf80)
        self.tk_frame_lq3x26vp = self.__tk_frame_lq3x26vp(self.tk_tabs_lq3wrrpn_2)
        self.tk_scale_lq3x2a9t = self.__tk_scale_lq3x2a9t(self.tk_frame_lq3x26vp)
        self.tk_label_lq3x2d8a = self.__tk_label_lq3x2d8a(self.tk_frame_lq3x26vp)
        self.tk_label_lq3x2nid = self.__tk_label_lq3x2nid(self.tk_frame_lq3x26vp)
        self.tk_scale_lq3x2s3y = self.__tk_scale_lq3x2s3y(self.tk_frame_lq3x26vp)
        self.tk_label_lq3x2w8i = self.__tk_label_lq3x2w8i(self.tk_frame_lq3x26vp)
        self.tk_scale_lq3x36rq = self.__tk_scale_lq3x36rq(self.tk_frame_lq3x26vp)
        self.tk_frame_lq3x843y = self.__tk_frame_lq3x843y(self.tk_tabs_lq3wrrpn_1)
        self.tk_canvas_lq3x87yu = self.__tk_canvas_lq3x87yu(self.tk_frame_lq3x843y)
        self.tk_frame_lq3x8k0a = self.__tk_frame_lq3x8k0a(self.tk_tabs_lq3wrrpn_2)
        self.tk_canvas_lq3x8q9u = self.__tk_canvas_lq3x8q9u(self.tk_frame_lq3x8k0a)

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
        frame.place(x=0, y=45, width=586, height=245)
        return frame

    def __tk_frame_lq3wrrpn_0(self, parent):
        frame = Frame(parent)
        frame.place(x=0, y=45, width=586, height=245)
        return frame

    def __tk_frame_lq3wrrpn_1(self, parent):
        frame = Frame(parent)
        frame.place(x=0, y=45, width=586, height=245)
        return frame

    def __tk_frame_lq3wrrpn_2(self, parent):
        frame = Frame(parent)
        frame.place(x=0, y=45, width=586, height=245)
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

    def __tk_frame_lq3wxf80(self, parent):
        frame = Frame(parent, )
        frame.place(x=366, y=0, width=216, height=245)
        return frame

    def __tk_scale_lq3wxmuy(self, parent):
        scale = Scale(parent, orient=HORIZONTAL, )
        scale.place(x=0, y=38, width=150, height=30)
        return scale

    def __tk_label_lq3wxrk2(self, parent):
        label = Label(parent, text="亮度调整", anchor="center", )
        label.place(x=50, y=0, width=50, height=30)
        return label

    def __tk_label_lq3xdc9w(self, parent):
        label = Label(parent, text="光感", anchor="center", )
        label.place(x=47, y=77, width=50, height=30)
        return label

    def __tk_scale_lq3xdkzk(self, parent):
        scale = Scale(parent, orient=HORIZONTAL, )
        scale.place(x=0, y=116, width=150, height=30)
        return scale

    def __tk_label_lq3xe8ky(self, parent):
        label = Label(parent, text="对比度", anchor="center", )
        label.place(x=49, y=156, width=50, height=30)
        return label

    def __tk_scale_lq3xehli(self, parent):
        scale = Scale(parent, orient=HORIZONTAL, )
        scale.place(x=0, y=195, width=150, height=30)
        return scale

    def __tk_frame_lq3x26vp(self, parent):
        frame = Frame(parent, )
        frame.place(x=374, y=0, width=200, height=245)
        return frame

    def __tk_scale_lq3x2a9t(self, parent):
        scale = Scale(parent, orient=HORIZONTAL, )
        scale.place(x=27, y=40, width=150, height=30)
        return scale

    def __tk_label_lq3x2d8a(self, parent):
        label = Label(parent, text="H", anchor="center", )
        label.place(x=75, y=0, width=50, height=30)
        return label

    def __tk_label_lq3x2nid(self, parent):
        label = Label(parent, text="S", anchor="center", )
        label.place(x=77, y=76, width=50, height=30)
        return label

    def __tk_scale_lq3x2s3y(self, parent):
        scale = Scale(parent, orient=HORIZONTAL, )
        scale.place(x=27, y=111, width=150, height=30)
        return scale

    def __tk_label_lq3x2w8i(self, parent):
        label = Label(parent, text="L", anchor="center", )
        label.place(x=77, y=146, width=50, height=30)
        return label

    def __tk_scale_lq3x36rq(self, parent):
        scale = Scale(parent, orient=HORIZONTAL, )
        scale.place(x=29, y=186, width=150, height=30)
        return scale

    def __tk_frame_lq3x843y(self, parent):
        frame = Frame(parent, )
        frame.place(x=0, y=0, width=308, height=241)
        return frame

    def __tk_canvas_lq3x87yu(self, parent):
        canvas = Canvas(parent, bg="#aaa")
        canvas.place(x=0, y=0, width=307, height=241)
        return canvas

    def __tk_frame_lq3x8k0a(self, parent):
        frame = Frame(parent, )
        frame.place(x=0, y=0, width=287, height=245)
        return frame

    def __tk_canvas_lq3x8q9u(self, parent):
        canvas = Canvas(parent, bg="#aaa")
        canvas.place(x=0, y=0, width=286, height=245)
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

            # self.display_image()
            self.show_image()

            # 更新显示图片路径的Label
            # self.image_path_label.config(text="当前图片路径：" + file_path)


class Win(WinGUI):
    def __init__(self):
        super().__init__()
        self.__event_bind()

    def __event_bind(self):
        pass


if __name__ == "__main__":
    win = Win()
    win.mainloop()
