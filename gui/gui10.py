"""
本代码由[Tkinter布局助手]生成
官网:https://www.pytk.net
QQ交流群:788392508
"""
from tkinter import *
from tkinter.ttk import *
class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.tk_button_open_image = self.__tk_button_open_image(self)
        self.tk_button_cancel = self.__tk_button_cancel(self)
        self.tk_button_modify = self.__tk_button_modify(self)
        self.tk_button_save = self.__tk_button_save(self)
        self.tk_tabs_option = self.__tk_tabs_option(self)
        self.tk_frame_container0 = self.__tk_frame_container0( self.tk_tabs_option_1)
        self.tk_scale_slider1 = self.__tk_scale_slider1( self.tk_frame_container0)
        self.tk_label_brightness = self.__tk_label_brightness( self.tk_frame_container0)
        self.tk_scale_slider2 = self.__tk_scale_slider2( self.tk_frame_container0)
        self.tk_label_exposure = self.__tk_label_exposure( self.tk_frame_container0)
        self.tk_scale_slider3 = self.__tk_scale_slider3( self.tk_frame_container0)
        self.tk_label_pome = self.__tk_label_pome( self.tk_frame_container0)
        self.tk_scale_slider4 = self.__tk_scale_slider4( self.tk_frame_container0)
        self.tk_button_Sharpen = self.__tk_button_Sharpen( self.tk_frame_container0)
        self.tk_button_Smooth = self.__tk_button_Smooth( self.tk_frame_container0)
        self.tk_button_Histogram_equalization = self.__tk_button_Histogram_equalization( self.tk_frame_container0)
        self.tk_label_saturation = self.__tk_label_saturation( self.tk_frame_container0)
        self.tk_scale_slider5 = self.__tk_scale_slider5( self.tk_frame_container0)
        self.tk_label_contrast = self.__tk_label_contrast( self.tk_frame_container0)
        self.tk_frame_container1 = self.__tk_frame_container1( self.tk_tabs_option_2)
        self.tk_scale_Saturation = self.__tk_scale_Saturation( self.tk_frame_container1)
        self.tk_label_Hue = self.__tk_label_Hue( self.tk_frame_container1)
        self.tk_scale_slider6 = self.__tk_scale_slider6( self.tk_frame_container1)
        self.tk_label_Saturation = self.__tk_label_Saturation( self.tk_frame_container1)
        self.tk_scale_slider7 = self.__tk_scale_slider7( self.tk_frame_container1)
        self.tk_label_lightness = self.__tk_label_lightness( self.tk_frame_container1)
        self.tk_button_rotate = self.__tk_button_rotate( self.tk_tabs_option_0)
        self.tk_button_trim = self.__tk_button_trim( self.tk_tabs_option_0)
        self.tk_input_text = self.__tk_input_text( self.tk_tabs_option_3)
        self.tk_button_add = self.__tk_button_add( self.tk_tabs_option_3)
        self.tk_label_text_label = self.__tk_label_text_label( self.tk_tabs_option_3)
        self.tk_canvas_watermark = self.__tk_canvas_watermark( self.tk_tabs_option_3)
        self.tk_button_open_watermark = self.__tk_button_open_watermark( self.tk_tabs_option_3)
        self.tk_button_add_watermark = self.__tk_button_add_watermark( self.tk_tabs_option_3)
        self.tk_canvas_image = self.__tk_canvas_image(self)
    def __win(self):
        self.title("Tkinter布局助手")
        # 设置窗口大小、居中
        width = 831
        height = 681
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)

        self.resizable(width=False, height=False)

    def scrollbar_autohide(self,vbar, hbar, widget):
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

    def v_scrollbar(self,vbar, widget, x, y, w, h, pw, ph):
        widget.configure(yscrollcommand=vbar.set)
        vbar.config(command=widget.yview)
        vbar.place(relx=(w + x) / pw, rely=y / ph, relheight=h / ph, anchor='ne')
    def h_scrollbar(self,hbar, widget, x, y, w, h, pw, ph):
        widget.configure(xscrollcommand=hbar.set)
        hbar.config(command=widget.xview)
        hbar.place(relx=x / pw, rely=(y + h) / ph, relwidth=w / pw, anchor='sw')
    def create_bar(self,master, widget,is_vbar,is_hbar, x, y, w, h, pw, ph):
        vbar, hbar = None, None
        if is_vbar:
            vbar = Scrollbar(master)
            self.v_scrollbar(vbar, widget, x, y, w, h, pw, ph)
        if is_hbar:
            hbar = Scrollbar(master, orient="horizontal")
            self.h_scrollbar(hbar, widget, x, y, w, h, pw, ph)
        self.scrollbar_autohide(vbar, hbar, widget)
    def __tk_button_open_image(self,parent):
        btn = Button(parent, text="打开", takefocus=False,)
        btn.place(x=0, y=1, width=50, height=30)
        return btn
    def __tk_button_cancel(self,parent):
        btn = Button(parent, text="撤销", takefocus=False,)
        btn.place(x=78, y=0, width=50, height=30)
        return btn
    def __tk_button_modify(self,parent):
        btn = Button(parent, text="修改", takefocus=False,)
        btn.place(x=158, y=0, width=50, height=30)
        return btn
    def __tk_button_save(self,parent):
        btn = Button(parent, text="保存", takefocus=False,)
        btn.place(x=234, y=1, width=50, height=30)
        return btn
    def __tk_tabs_option(self,parent):
        frame = Notebook(parent)
        self.tk_tabs_option_0 = self.__tk_frame_option_0(frame)
        frame.add(self.tk_tabs_option_0, text="几何变换")
        self.tk_tabs_option_1 = self.__tk_frame_option_1(frame)
        frame.add(self.tk_tabs_option_1, text="图像增强")
        self.tk_tabs_option_2 = self.__tk_frame_option_2(frame)
        frame.add(self.tk_tabs_option_2, text="HSL调整")
        self.tk_tabs_option_3 = self.__tk_frame_option_3(frame)
        frame.add(self.tk_tabs_option_3, text="拓展")
        frame.place(x=3, y=54, width=361, height=511)
        return frame
    def __tk_frame_option_0(self,parent):
        frame = Frame(parent)
        frame.place(x=3, y=54, width=361, height=511)
        return frame
    def __tk_frame_option_1(self,parent):
        frame = Frame(parent)
        frame.place(x=3, y=54, width=361, height=511)
        return frame
    def __tk_frame_option_2(self,parent):
        frame = Frame(parent)
        frame.place(x=3, y=54, width=361, height=511)
        return frame
    def __tk_frame_option_3(self,parent):
        frame = Frame(parent)
        frame.place(x=3, y=54, width=361, height=511)
        return frame
    def __tk_frame_container0(self,parent):
        frame = Frame(parent,)
        frame.place(x=0, y=0, width=349, height=533)
        return frame
    def __tk_scale_slider1(self,parent):
        scale = Scale(parent, orient=HORIZONTAL, )
        scale.place(x=0, y=42, width=150, height=30)
        return scale
    def __tk_label_brightness(self,parent):
        label = Label(parent,text="亮度调节",anchor="center", )
        label.place(x=26, y=82, width=87, height=30)
        return label
    def __tk_scale_slider2(self,parent):
        scale = Scale(parent, orient=HORIZONTAL, )
        scale.place(x=0, y=125, width=150, height=30)
        return scale
    def __tk_label_exposure(self,parent):
        label = Label(parent,text="谱光",anchor="center", )
        label.place(x=1, y=180, width=146, height=30)
        return label
    def __tk_scale_slider3(self,parent):
        scale = Scale(parent, orient=HORIZONTAL, )
        scale.place(x=0, y=231, width=150, height=30)
        return scale
    def __tk_label_pome(self,parent):
        label = Label(parent,text="光感",anchor="center", )
        label.place(x=53, y=276, width=50, height=30)
        return label
    def __tk_scale_slider4(self,parent):
        scale = Scale(parent, orient=HORIZONTAL, )
        scale.place(x=0, y=328, width=150, height=30)
        return scale
    def __tk_button_Sharpen(self,parent):
        btn = Button(parent, text="锐化", takefocus=False,)
        btn.place(x=252, y=238, width=50, height=30)
        return btn
    def __tk_button_Smooth(self,parent):
        btn = Button(parent, text="平滑", takefocus=False,)
        btn.place(x=256, y=328, width=50, height=30)
        return btn
    def __tk_button_Histogram_equalization(self,parent):
        btn = Button(parent, text="直方图均衡化", takefocus=False,)
        btn.place(x=217, y=130, width=120, height=30)
        return btn
    def __tk_label_saturation(self,parent):
        label = Label(parent,text="饱和度调整",anchor="center", )
        label.place(x=44, y=383, width=92, height=30)
        return label
    def __tk_scale_slider5(self,parent):
        scale = Scale(parent, orient=HORIZONTAL, )
        scale.place(x=0, y=452, width=150, height=30)
        return scale
    def __tk_label_contrast(self,parent):
        label = Label(parent,text="对比度",anchor="center", )
        label.place(x=35, y=0, width=67, height=30)
        return label
    def __tk_frame_container1(self,parent):
        frame = Frame(parent,)
        frame.place(x=0, y=0, width=347, height=482)
        return frame
    def __tk_scale_Saturation(self,parent):
        scale = Scale(parent, orient=HORIZONTAL, )
        scale.place(x=13, y=342, width=150, height=30)
        return scale
    def __tk_label_Hue(self,parent):
        label = Label(parent,text="H",anchor="center", )
        label.place(x=62, y=0, width=50, height=30)
        return label
    def __tk_scale_slider6(self,parent):
        scale = Scale(parent, orient=HORIZONTAL, )
        scale.place(x=13, y=56, width=143, height=30)
        return scale
    def __tk_label_Saturation(self,parent):
        label = Label(parent,text="S",anchor="center", )
        label.place(x=62, y=127, width=50, height=30)
        return label
    def __tk_scale_slider7(self,parent):
        scale = Scale(parent, orient=HORIZONTAL, )
        scale.place(x=11, y=189, width=150, height=30)
        return scale
    def __tk_label_lightness(self,parent):
        label = Label(parent,text="L",anchor="center", )
        label.place(x=64, y=271, width=50, height=30)
        return label
    def __tk_button_rotate(self,parent):
        btn = Button(parent, text="旋转", takefocus=False,)
        btn.place(x=0, y=46, width=50, height=30)
        return btn
    def __tk_button_trim(self,parent):
        btn = Button(parent, text="裁剪", takefocus=False,)
        btn.place(x=0, y=0, width=50, height=30)
        return btn
    def __tk_input_text(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=0, y=35, width=150, height=30)
        return ipt
    def __tk_button_add(self,parent):
        btn = Button(parent, text="添加", takefocus=False,)
        btn.place(x=165, y=34, width=50, height=30)
        return btn
    def __tk_label_text_label(self,parent):
        label = Label(parent,text="添加文字",anchor="center", )
        label.place(x=0, y=0, width=148, height=30)
        return label
    def __tk_canvas_watermark(self,parent):
        canvas = Canvas(parent,bg="#aaa")
        canvas.place(x=176, y=273, width=182, height=196)
        return canvas
    def __tk_button_open_watermark(self,parent):
        btn = Button(parent, text="选择水印图片", takefocus=False,)
        btn.place(x=1, y=282, width=146, height=30)
        return btn
    def __tk_button_add_watermark(self,parent):
        btn = Button(parent, text="添加水印", takefocus=False,)
        btn.place(x=11, y=343, width=107, height=30)
        return btn
    def __tk_canvas_image(self,parent):
        canvas = Canvas(parent,bg="#aaa")
        canvas.place(x=384, y=79, width=447, height=473)
        return canvas
class Win(WinGUI):
    def __init__(self):
        super().__init__()
        self.__event_bind()
        self.config(menu=self.create_menu())
    def create_menu(self):
        menu = Menu(self,tearoff=False)
        menu.add_cascade(label="文件",menu=self.menu_lq4uzrg8(menu))
        menu.add_command(label="撤销",command=self.cancel)
        menu.add_command(label="反撤销",command=self.uncancel)
        menu.add_command(label="重做",command=self.init_image)
        return menu
    def menu_lq4uzrg8(self,parent):
        menu = Menu(parent,tearoff=False)
        menu.add_command(label="打开",command=self.load_image)
        menu.add_command(label="保存",command=self.save)
        return menu
    def load_image(self):
        print("点击了菜单")
    def save(self):
        print("点击了菜单")
    def cancel(self):
        print("点击了菜单")
    def uncancel(self):
        print("点击了菜单")
    def init_image(self):
        print("点击了菜单")
    def load_image(self,evt):
        print("<Button-1>事件未处理:",evt)
    def __event_bind(self):
        self.tk_button_open_image.bind('<Button-1>',self.load_image)
        pass
if __name__ == "__main__":
    win = Win()
    win.mainloop()