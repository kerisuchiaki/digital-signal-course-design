import cv2
import numpy as np
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


def modify_color_temperature(img, temperature):
    imgB = img[:, :, 0]
    imgG = img[:, :, 1]
    imgR = img[:, :, 2]

    bAve = cv2.mean(imgB)[0]
    gAve = cv2.mean(imgG)[0] + temperature
    rAve = cv2.mean(imgR)[0] + temperature
    aveGray = (int)(bAve + gAve + rAve) / 3

    bCoef = aveGray / bAve
    gCoef = aveGray / gAve
    rCoef = aveGray / rAve

    imgB = np.floor((imgB * bCoef))
    imgG = np.floor((imgG * gCoef))
    imgR = np.floor((imgR * rCoef))

    imgB[imgB > 255] = 255
    imgG[imgG > 255] = 255
    imgR[imgR > 255] = 255

    cold_rgb = np.dstack((imgB, imgG, imgR)).astype(np.uint8)

    return cold_rgb


class ImageProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Processor")

        self.init_img = cv2.imread("../image/sakura_1.png")
        self.image = Image.fromarray(cv2.cvtColor(self.init_img, cv2.COLOR_BGR2RGB))

        self.temperature_scale_var = tk.DoubleVar()
        self.create_widgets()

    def create_widgets(self):
        self.image_label = ttk.Label(self.root)
        self.image_label.pack()

        self.temperature_scale = ttk.Scale(self.root, from_=-50, to=50, orient="horizontal",
                                           variable=self.temperature_scale_var, command=self.adjust_temperature)
        self.temperature_scale.pack()

        self.display_image()

    def display_image(self):
        img = ImageTk.PhotoImage(self.image)
        self.image_label.config(image=img)
        self.image_label.image = img

    def adjust_temperature(self, evt=None):
        temperature_value = self.temperature_scale_var.get()
        adjusted_img = modify_color_temperature(np.array(self.init_img), temperature_value)
        self.image = Image.fromarray(cv2.cvtColor(adjusted_img, cv2.COLOR_BGR2RGB))
        self.display_image()


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageProcessorApp(root)
    root.mainloop()
