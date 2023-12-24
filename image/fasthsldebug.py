import colorsys

import numpy as np
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import colorchooser

# 使用PIL的Image模块加载图像
img = Image.open('../image/aa.png')

root = tk.Tk()
weight = 0.5
# 创建画布
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()
print("dqwda")

photo = ImageTk.PhotoImage(img)
image_item = canvas.create_image(0, 0, anchor=tk.NW, image=photo)


def update_image(color):
    global img

    if color:
        # 将图像转换为numpy数组
        img_array = np.array(img)

        rr, gg, bb = [int(color[i:i + 2], 16) for i in range(1, 7, 2)]
        print(rr, gg, bb)

        # 获取纯红像素点的条件
        red_condition = (rr - 50 <= img_array[:, :, 0] <= rr + 50) & (gg - 50 <= img_array[:, :, 1] <= 50 + gg) & (
                    bb - 50 <=
                    img_array[:, :, 2] <= 50 + bb)

        # 将纯红像素点变为橙色（255, 127.5, 0）
        img_array[red_condition] = [255, 127.5, 0]

        # 将修改后的numpy数组转换回Image对象
        modified_img = Image.fromarray(img_array)

        img = modified_img

        # 更新画布上的图片
        photo = ImageTk.PhotoImage(modified_img)
        canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        canvas.image = photo


def adjust_color_and_neighbors(img, color, hue_shift, saturation_shift, lightness_shift):
    # 将图像转换为numpy数组
    img_array = np.array(img)

    # 将选定的颜色转换为RGB表示
    rr, gg, bb = [int(color[i:i + 2], 16) for i in range(1, 7, 2)]

    # 获取纯色像素点的条件
    red_condition = (img_array[:, :, 0] == rr) & (img_array[:, :, 1] == gg) & (img_array[:, :, 2] == bb)

    # 将选定颜色及相邻颜色进行调整
    h, l, s = colorsys.rgb_to_hls(rr / 255, gg / 255, bb / 255)
    adjusted_h = hue_shift / 360.0 + h
    if adjusted_h <= 0: adjusted_h += 1
    if adjusted_h >= 1: adjusted_h -= 1
    adjusted_s = saturation_shift + s
    if adjusted_s <= 0: adjusted_s = 0
    if adjusted_s >= 1: adjusted_s = 1
    adjusted_l = lightness_shift + l
    if adjusted_l <= 0: adjusted_l = 0
    if adjusted_l >= 1: adjusted_l = 1
    adjusted_r, adjusted_g, adjusted_b = colorsys.hls_to_rgb(adjusted_h, adjusted_l, adjusted_s)
    img_array[red_condition] = [adjusted_r * 255, adjusted_g * 255, adjusted_b * 255]

    # 创建一个掩码以标识相邻像素
    mask = np.zeros_like(img_array)
    mask[red_condition] = 1

    # 获取相邻像素
    neighbors = np.zeros_like(mask)
    neighbors[:-1] += mask[1:]
    neighbors[1:] += mask[:-1]
    neighbors[:, :-1] += mask[:, 1:]
    neighbors[:, 1:] += mask[:, :-1]

    # 将相邻像素进行调整
    adjusted_neighbors = img_array * neighbors
    adjusted_img_array = img_array + weight * adjusted_neighbors

    # 将修改后的numpy数组转换回Image对象
    modified_img = Image.fromarray(adjusted_img_array.astype(np.uint8))

    return modified_img


def select_color():
    # 打开颜色选择器对话框
    _, color = colorchooser.askcolor()

    if color:
        global img
        img = adjust_color_and_neighbors(img, color, 30, -0.2, 0.3)
        # 更新画布上的图片
        global photo
        print("dw")
        photo = ImageTk.PhotoImage(img)
        canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        canvas.image = photo
        # update_image(color)


# 创建选择颜色按钮
select_color_button = tk.Button(root, text='Select Color', command=select_color)
select_color_button.pack()

# 运行主循环
root.mainloop()
