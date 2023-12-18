import cv2
import numpy as np
import tkinter as tk
from PIL import Image, ImageTk

def adjust_image(image_path):
    def update_image(_):
        hue_value = hue_slider.get()
        temperature_value = temperature_slider.get()

        # 转换图片颜色空间为HSV
        hsv_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2HSV)

        # 调整色调
        hsv_image[:, :, 0] += hue_value % 360

        # 调整色温
        hsv_image[:, :, 1] = np.clip(hsv_image[:, :, 1] + temperature_value, 0, 255)

        # 转换回BGR颜色空间
        bgr_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)

        # 将OpenCV图像转换为PIL图像
        pil_image = Image.fromarray(cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB))

        # 将PIL图像转换为Tkinter图像
        tk_image = ImageTk.PhotoImage(pil_image)

        # 更新标签图像
        label.config(image=tk_image)
        label.image = tk_image

    # 读取图片
    original_image = cv2.imread(image_path)

    # 创建Tkinter窗口
    window = tk.Tk()
    window.title("Adjust Image")

    # 将OpenCV图像转换为PIL图像
    pil_image = Image.fromarray(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))

    # 将PIL图像转换为Tkinter图像
    tk_image = ImageTk.PhotoImage(pil_image)

    # 创建标签并显示图像
    label = tk.Label(window, image=tk_image)
    label.pack()

    # 创建滑块用于调整色调
    hue_slider = tk.Scale(window, from_=0, to=360, label="Hue", orient=tk.HORIZONTAL, length=200, command=update_image)
    hue_slider.pack()

    # 创建滑块用于调整色温
    temperature_slider = tk.Scale(window, from_=-50, to=50, label="Temperature", orient=tk.HORIZONTAL, length=200, command=update_image)
    temperature_slider.pack()

    # 运行Tkinter窗口
    window.mainloop()

# 调用函数进行图片调节
adjust_image("../image/kagome.png")
