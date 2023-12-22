"""
本代码由[Tkinter布局助手]生成
官网:https://www.pytk.net
QQ交流群:788392508
在线反馈:https://support.qq.com/product/618914
"""
from tkinter import *
from tkinter.ttk import *
class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.tk_list_box_lqerfds4 = self.__tk_list_box_lqerfds4(self)
        self.tk_select_box_lqerfnpt = self.__tk_select_box_lqerfnpt(self)
        self.tk_canvas_lqergjqd = self.__tk_canvas_lqergjqd(self)
        self.tk_scale_lqerhjgi = self.__tk_scale_lqerhjgi(self)
        self.tk_scale_lqerhlex = self.__tk_scale_lqerhlex(self)
        self.tk_scale_lqerhn25 = self.__tk_scale_lqerhn25(self)
        self.tk_button_lqerhyed = self.__tk_button_lqerhyed(self)
        self.tk_label_lqerkz1q = self.__tk_label_lqerkz1q(self)
        self.tk_label_lqerl35d = self.__tk_label_lqerl35d(self)
        self.tk_label_lqerl6uc = self.__tk_label_lqerl6uc(self)
        self.tk_label_lqerlc5s = self.__tk_label_lqerlc5s(self)
        self.tk_input_lqerlxw6 = self.__tk_input_lqerlxw6(self)
        self.tk_button_lqerm2f7 = self.__tk_button_lqerm2f7(self)
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


clc;
clear;
img = imread('autumn.tif');
subplot(2, 2, 1), imshow(img);
title('原图像');

%将低频移动到图像的中心
s = fftshift(fft2(img));
subplot(2, 2, 3), imshow(log(abs(s)), []);
title('图像傅里叶变换取对数所得频谱');

[a, b] = size(img);
low_filter = zeros(a, b);
D0 = min(a, b) / 12; %截止频率

for u = 1:a
for v = 1:b
%计算频率平面上的距离
dist = sqrt((u - a / 2) ^ 2 + (v - b / 2) ^ 2);
%判断是否要截止
if dist <= D0
    low_filter(u, v) = 1;
end
end
end

subplot(2, 2, 4), imshow(log(abs(low_filter)), []);
title('低通滤波频谱');

new_img = uint8(real(ifft2(ifftshift(low_filter. * s))));
subplot(2, 2, 2), imshow(new_img, []);
title('低通滤波后的图像');


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
    def __tk_list_box_lqerfds4(self,parent):
        lb = Listbox(parent)

        lb.insert(END, "列表框")

        lb.insert(END, "Python")

        lb.insert(END, "Tkinter Helper")

        lb.place(x=158, y=70, width=150, height=100)
        return lb
    def __tk_select_box_lqerfnpt(self,parent):
        cb = Combobox(parent, state="readonly", )
        cb['values'] = ("列表框","Python","Tkinter Helper")
        cb.place(x=159, y=211, width=150, height=30)
        return cb
    def __tk_canvas_lqergjqd(self,parent):
        canvas = Canvas(parent,bg="#aaa")
        canvas.place(x=335, y=51, width=265, height=246)
        return canvas
    def __tk_scale_lqerhjgi(self,parent):
        scale = Scale(parent, orient=HORIZONTAL, )
        scale.place(x=0, y=81, width=150, height=30)
        return scale
    def __tk_scale_lqerhlex(self,parent):
        scale = Scale(parent, orient=HORIZONTAL, )
        scale.place(x=0, y=160, width=150, height=30)
        return scale
    def __tk_scale_lqerhn25(self,parent):
        scale = Scale(parent, orient=HORIZONTAL, )
        scale.place(x=0, y=227, width=150, height=30)
        return scale
    def __tk_button_lqerhyed(self,parent):
        btn = Button(parent, text="按钮", takefocus=False,)
        btn.place(x=54, y=289, width=50, height=30)
        return btn
    def __tk_label_lqerkz1q(self,parent):
        label = Label(parent,text="标签",anchor="center", )
        label.place(x=0, y=1, width=50, height=30)
        return label
    def __tk_label_lqerl35d(self,parent):
        label = Label(parent,text="标签",anchor="center", )
        label.place(x=55, y=0, width=50, height=30)
        return label
    def __tk_label_lqerl6uc(self,parent):
        label = Label(parent,text="标签",anchor="center", )
        label.place(x=112, y=0, width=50, height=30)
        return label
    def __tk_label_lqerlc5s(self,parent):
        label = Label(parent,text="标签",anchor="center", )
        label.place(x=170, y=0, width=50, height=30)
        return label
    def __tk_input_lqerlxw6(self,parent):
        ipt = Entry(parent, )
        ipt.place(x=13, y=367, width=150, height=30)
        return ipt
    def __tk_button_lqerm2f7(self,parent):
        btn = Button(parent, text="按钮", takefocus=False,)
        btn.place(x=52, y=421, width=50, height=30)
        return btn
class Win(WinGUI):
    def __init__(self, controller):
        self.ctl = controller
        super().__init__()
        self.__event_bind()
        self.ctl.init(self)
    def __event_bind(self):
        pass
if __name__ == "__main__":
    win = WinGUI()
    win.mainloop()