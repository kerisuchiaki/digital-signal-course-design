import cv2
import imutils
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk

MAX_VALUE = 100


def s_and_b(arg):
    lsImg = np.zeros(image.shape, np.float32)
    hlsCopy = np.copy(hlsImg)
    hsvCopy = np.copy(hsvImg)
    l = l_scale.get()
    s = s_scale.get()
    h = h_scale.get()
    hlsCopy[:, :, 1] = (1.0 + l / float(MAX_VALUE)) * hlsCopy[:, :, 1]
    hlsCopy[:, :, 1][hlsCopy[:, :, 1] > 1] = 1
    hlsCopy[:, :, 2] = (1.0 + s / float(MAX_VALUE)) * hlsCopy[:, :, 2]
    hlsCopy[:, :, 2][hlsCopy[:, :, 2] > 1] = 1
    lsImg = cv2.cvtColor(hlsCopy, cv2.COLOR_HLS2BGR)

    hsvCopy[:, :, 0] = (h / float(MAX_VALUE)) * hsvCopy[:, :, 0]
    hsvCopy[:, :, 0][hsvCopy[:, :, 0] > 179] = 179

    bgrImg = cv2.cvtColor(hsvCopy, cv2.COLOR_HSV2BGR)

    bgrImg = (bgrImg * 255).astype(np.uint8)

    img = Image.fromarray(cv2.cvtColor(bgrImg, cv2.COLOR_BGR2RGB))
    img = ImageTk.PhotoImage(image=img)

    panel.config(image=img)
    panel.image = img


def load_image():
    global image, fImg, hlsImg, hsvImg

    image = cv2.imread('../image/miku.jpg', 1)
    fImg = image.astype(np.float32)
    fImg = fImg / 255.0
    hlsImg = cv2.cvtColor(fImg, cv2.COLOR_BGR2HLS)
    hsvImg = cv2.cvtColor(fImg, cv2.COLOR_BGR2HSV)

    s_and_b(0)


window = tk.Tk()
window.title("Image Adjustments")

l_scale = tk.Scale(window, from_=0, to=MAX_VALUE, orient=tk.HORIZONTAL, label="Lightness", command=s_and_b)
s_scale = tk.Scale(window, from_=0, to=MAX_VALUE, orient=tk.HORIZONTAL, label="Saturation", command=s_and_b)
h_scale = tk.Scale(window, from_=0, to=MAX_VALUE, orient=tk.HORIZONTAL, label="Hue", command=s_and_b)
l_scale.pack()
s_scale.pack()
h_scale.pack()

panel = tk.Label(window)
panel.pack()

load_image()

load_button = tk.Button(window, text="Load Image", command=load_image)
load_button.pack()

quit_button = tk.Button(window, text="Quit", command=window.quit)
quit_button.pack()

window.mainloop()
