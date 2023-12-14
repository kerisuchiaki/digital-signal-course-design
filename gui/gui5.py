from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
import tkinter as tk
from PIL import Image, ImageTk

class ImageEditorApp(Tk):
    def __init__(self):
        super().__init__()
        self.fullscreen = False
        self.photo = None
        self.init_photo = None
        self.image_back = None
        self.init_img = None
        self.image = None
        self.image_stack = None
        self.__win()
        self.tk_button_open_image = self.__tk_button_open_image(self)
        self.tk_button_cancel = self.__tk_button_cancel(self)
        self.tk_button_modify = self.__tk_button_modify(self)
        self.tk_button_save = self.__tk_button_save(self)
        self.tk_tabs_option = self.__tk_tabs_option(self)
        self.tk_frame_container1 = self.__tk_frame_container1(self.tk_tabs_option_0)
        self.tk_button_trim = self.__tk_button_trim(self.tk_frame_container1)
        self.tk_button_rotate = self.__tk_button_rotate(self.tk_frame_container1)
        self.tk_canvas_canvas2 = self.__tk_canvas_canvas2(self.tk_tabs_option_1)
        self.tk_frame_container2 = self.__tk_frame_container2(self.tk_tabs_option_1)
        self.tk_scale_slider1 = self.__tk_scale_slider1(self.tk_frame_container2)
        self.tk_label_brightness = self.__tk_label_brightness(self.tk_frame_container2)
        self.tk_label_saturation = self.__tk_label_saturation(self.tk_frame_container2)
        self.tk_scale_slider2 = self.__tk_scale_slider2(self.tk_frame_container2)
        self.tk_label_exposure = self.__tk_label_exposure(self.tk_frame_container2)
        self.tk_scale_slider3 = self.__tk_scale_slider3(self.tk_frame_container2)
        self.tk_label_pome = self.__tk_label_pome(self.tk_frame_container2)
        self.tk_scale_slider4 = self.__tk_scale_slider4(self.tk_frame_container2)
        self.tk_button_Sharpen = self.__tk_button_Sharpen(self.tk_frame_container2)
        self.tk_button_Smooth = self.__tk_button_Smooth(self.tk_frame_container2)
        self.tk_button_Histogram_equalization = self.__tk_button_Histogram_equalization(self.tk_frame_container2)
        self.tk_label_saturation = self.__tk_label_saturation(self.tk_frame_container2)
        self.tk_scale_slider5 = self.__tk_scale_slider5(self.tk_frame_container2)
        self.canvas = self.__tk_canvas_canvas1(self.tk_tabs_option_0)
        self.tk_canvas_canvas3 = self.__tk_canvas_canvas3(self.tk_tabs_option_2)
        self.tk_frame_container3 = self.__tk_frame_container3(self.tk_tabs_option_2)
        self.tk_scale_Saturation = self.__tk_scale_Saturation(self.tk_frame_container3)
        self.tk_label_Hue = self.__tk_label_Hue(self.tk_frame_container3)
        self.tk_scale_slider6 = self.__tk_scale_slider6(self.tk_frame_container3)
        self.tk_label_Saturation = self.__tk_label_Saturation(self.tk_frame_container3)
        self.tk_scale_slider7 = self.__tk_scale_slider7(self.tk_frame_container3)
        self.tk_label_lightness = self.__tk_label_lightness(self.tk_frame_container3)

    def __win(self):
        self.title("Tkinter Image Editor")
        self.geometry("800x600")  # Set initial window size
        self.resizable(True, True)  # Allow window resizing
        self.bind("<F11>", self.toggle_fullscreen)  # Bind F11 key to toggle fullscreen
        self.bind("<Escape>", self.exit_fullscreen)  # Bind Escape key to exit fullscreen

    def toggle_fullscreen(self, event=None):
        self.fullscreen = not self.fullscreen
        self.attributes("-fullscreen", self.fullscreen)

    def exit_fullscreen(self, event=None):
        self.fullscreen = False
        self.attributes("-fullscreen", False)

    def scrollbar_autohide(self, vbar, hbar, widget):
        """Automatically hide scrollbars"""
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

    # ... (remaining code remains unchanged)
