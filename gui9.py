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
        self.tk_frame_container1 = self.__tk_frame_container1( self.tk_tabs_option_0)
        self.tk_button_trim = self.__tk_button_trim( self.tk_frame_container1)
        self.tk_button_rotate = self.__tk_button_rotate( self.tk_frame_container1)
        self.tk_canvas_canvas2 = self.__tk_canvas_canvas2( self.tk_tabs_option_1)
        self.tk_frame_container2 = self.__tk_frame_container2( self.tk_tabs_option_1)
        self.tk_scale_slider1 = self.__tk_scale_slider1( self.tk_frame_container2)
        self.tk_label_brightness = self.__tk_label_brightness( self.tk_frame_container2)
        self.tk_scale_slider2 = self.__tk_scale_slider2( self.tk_frame_container2)
        self.tk_label_exposure = self.__tk_label_exposure( self.tk_frame_container2)
        self.tk_scale_slider3 = self.__tk_scale_slider3( self.tk_frame_container2)
        self.tk_label_pome = self.__tk_label_pome( self.tk_frame_container2)
        self.tk_scale_slider4 = self.__tk_scale_slider4( self.tk_frame_container2)
        self.tk_button_Sharpen = self.__tk_button_Sharpen( self.tk_frame_container2)
        self.tk_button_Smooth = self.__tk_button_Smooth( self.tk_frame_container2)
        self.tk_button_Histogram_equalization = self.__tk_button_Histogram_equalization( self.tk_frame_container2)
        self.tk_label_saturation = self.__tk_label_saturation( self.tk_frame_container2)
        self.tk_scale_slider5 = self.__tk_scale_slider5( self.tk_frame_container2)
        self.tk_label_lq4n9yq9 = self.__tk_label_lq4n9yq9( self.tk_frame_container2)
        self.tk_canvas_canvas1 = self.__tk_canvas_canvas1( self.tk_tabs_option_0)
        self.tk_canvas_canvas3 = self.__tk_canvas_canvas3( self.tk_tabs_option_2)
        self.tk_frame_container3 = self.__tk_frame_container3( self.tk_tabs_option_2)
        self.tk_scale_Saturation = self.__tk_scale_Saturation( self.tk_frame_container3)
        self.tk_label_Hue = self.__tk_label_Hue( self.tk_frame_container3)
        self.tk_scale_slider6 = self.__tk_scale_slider6( self.tk_frame_container3)
        self.tk_label_Saturation = self.__tk_label_Saturation( self.tk_frame_container3)
        self.tk_scale_slider7 = self.__tk_scale_slider7( self.tk_frame_container3)
        self.tk_label_lightness = self.__tk_label_lightness( self.tk_frame_container3)
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
        btn.place(x=159, y=0, width=50, height=30)
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
        frame.place(x=0, y=47, width=827, height=536)
        return frame
    def __tk_frame_option_0(self,parent):
        frame = Frame(parent)
        frame.place(x=0, y=47, width=827, height=536)
        return frame
    def __tk_frame_option_1(self,parent):
        frame = Frame(parent)
        frame.place(x=0, y=47, width=827, height=536)
        return frame
    def __tk_frame_option_2(self,parent):
        frame = Frame(parent)
        frame.place(x=0, y=47, width=827, height=536)
        return frame
    def __tk_frame_container1(self,parent):
        frame = Frame(parent,)
        frame.place(x=626, y=0, width=200, height=535)
        return frame
    def __tk_button_trim(self,parent):
        btn = Button(parent, text="裁剪", takefocus=False,)
        btn.place(x=0, y=0, width=50, height=30)
        return btn
    def __tk_button_rotate(self,parent):
        btn = Button(parent, text="旋转", takefocus=False,)
        btn.place(x=0, y=56, width=50, height=30)
        return btn
    def __tk_canvas_canvas2(self,parent):
        canvas = Canvas(parent,bg="#aaa")
        canvas.place(x=0, y=0, width=465, height=499)
        return canvas
    def __tk_frame_container2(self,parent):
        frame = Frame(parent,)
        frame.place(x=469, y=1, width=358, height=533)
        return frame
    def __tk_scale_slider1(self,parent):
        scale = Scale(parent, orient=HORIZONTAL, )
        scale.place(x=0, y=43, width=150, height=30)
        return scale
    def __tk_label_brightness(self,parent):
        label = Label(parent,text="亮度调节",anchor="center", )
        label.place(x=21, y=83, width=87, height=30)
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
        btn.place(x=285, y=51, width=50, height=30)
        return btn
    def __tk_button_Smooth(self,parent):
        btn = Button(parent, text="平滑", takefocus=False,)
        btn.place(x=286, y=115, width=50, height=30)
        return btn
    def __tk_button_Histogram_equalization(self,parent):
        btn = Button(parent, text="直方图均衡化", takefocus=False,)
        btn.place(x=238, y=0, width=120, height=30)
        return btn
    def __tk_label_saturation(self,parent):
        label = Label(parent,text="饱和度调整",anchor="center", )
        label.place(x=46, y=380, width=92, height=30)
        return label
    def __tk_scale_slider5(self,parent):
        scale = Scale(parent, orient=HORIZONTAL, )
        scale.place(x=0, y=452, width=150, height=30)
        return scale
    def __tk_label_lq4n9yq9(self,parent):
        label = Label(parent,text="对比度",anchor="center", )
        label.place(x=23, y=0, width=67, height=30)
        return label
    def __tk_canvas_canvas1(self,parent):
        canvas = Canvas(parent,bg="#aaa")
        canvas.place(x=0, y=1, width=511, height=533)
        return canvas
    def __tk_canvas_canvas3(self,parent):
        canvas = Canvas(parent,bg="#aaa")
        canvas.place(x=1, y=0, width=465, height=535)
        return canvas
    def __tk_frame_container3(self,parent):
        frame = Frame(parent,)
        frame.place(x=467, y=0, width=356, height=536)
        return frame
    def __tk_scale_Saturation(self,parent):
        scale = Scale(parent, orient=HORIZONTAL, )
        scale.place(x=206, y=92, width=150, height=30)
        return scale
    def __tk_label_Hue(self,parent):
        label = Label(parent,text="H",anchor="center", )
        label.place(x=253, y=37, width=50, height=30)
        return label
    def __tk_scale_slider6(self,parent):
        scale = Scale(parent, orient=HORIZONTAL, )
        scale.place(x=206, y=200, width=150, height=30)
        return scale
    def __tk_label_Saturation(self,parent):
        label = Label(parent,text="S",anchor="center", )
        label.place(x=256, y=147, width=50, height=30)
        return label
    def __tk_scale_slider7(self,parent):
        scale = Scale(parent, orient=HORIZONTAL, )
        scale.place(x=206, y=311, width=150, height=30)
        return scale
    def __tk_label_lightness(self,parent):
        label = Label(parent,text="L",anchor="center", )
        label.place(x=253, y=251, width=50, height=30)
        return label
class Win(WinGUI):
    def __init__(self):
        super().__init__()
        self.__event_bind()
        self.config(menu=self.create_menu())
    def create_menu(self):
        menu = Menu(self,tearoff=False)
        menu.add_cascade(label="menu",menu=self.menu_lq4qgs6a(menu))
        menu.add_command(label="menu2",command=self.menu2)
        return menu
    def menu_lq4qgs6a(self,parent):
        menu = Menu(parent,tearoff=False)
        menu.add_command(label="mune2",command=self.menu2)
        return menu
    def menu2(self):
        print("点击了菜单")
    def menu2(self):
        print("点击了菜单")
    def load_image(self,evt):
        print("<Button-1>事件未处理:",evt)
    def rotate_image(self,evt):
        print("<Button-1>事件未处理:",evt)
    def __event_bind(self):
        self.tk_button_open_image.bind('<Button-1>',self.load_image)
        self.tk_button_rotate.bind('<Button-1>',self.rotate_image)
        pass
if __name__ == "__main__":
    win = Win()
    win.mainloop()