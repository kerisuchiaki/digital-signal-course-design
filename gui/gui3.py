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
        self.tk_button_lq3wd5dc = self.__tk_button_lq3wd5dc(self)
        self.tk_button_lq3wd6vd = self.__tk_button_lq3wd6vd(self)
        self.tk_button_lq3wdh0h = self.__tk_button_lq3wdh0h(self)
        self.tk_button_lq3wdimy = self.__tk_button_lq3wdimy(self)
        self.tk_canvas_lq3wewj2 = self.__tk_canvas_lq3wewj2(self)
        self.tk_button_lq3wf5g5 = self.__tk_button_lq3wf5g5(self)
        self.tk_scale_lq3wfk1b = self.__tk_scale_lq3wfk1b(self)

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
        btn = Button(parent, text="打开", takefocus=False, )
        btn.place(x=0, y=0, width=50, height=30)
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

    def __tk_canvas_lq3wewj2(self, parent):
        canvas = Canvas(parent, bg="#aaa")
        canvas.place(x=0, y=65, width=368, height=279)
        return canvas

    def __tk_button_lq3wf5g5(self, parent):
        btn = Button(parent, text="旋转", takefocus=False, )
        btn.place(x=441, y=70, width=50, height=30)
        return btn

    def __tk_scale_lq3wfk1b(self, parent):
        scale = Scale(parent, orient=HORIZONTAL, )
        scale.place(x=405, y=205, width=150, height=30)
        return scale


class Win(WinGUI):
    def __init__(self):
        super().__init__()
        self.__event_bind()

    def __event_bind(self):
        pass


if __name__ == "__main__":
    win = Win()
    win.mainloop()