import time
import numpy as np

from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog, colorchooser
import colorsys

# 方法1：使用嵌套循环遍历像素


img = Image.open('../image/color.png')
# 创建选择颜色按钮

root = tk.Tk()

# 创建画布
canvas = tk.Canvas(root, width=400, height=400)
canvas.place(x=384, y=78, width=960, height=960)

photo = ImageTk.PhotoImage(img)
canvas.create_image(0, 0, anchor=tk.NW, image=photo)
canvas.image = photo


def method1(img, color):
    img_array = np.array(img)
    rr, gg, bb = color[0], color[1], color[2]

    # 创建图像副本
    modified_img = img_array.copy()

    # 获取图像的宽度和高度
    width, height, _ = modified_img.shape

    start_time = time.time()

    # 遍历图像的每个像素
    for i in range(width):
        for j in range(height):
            r, g, b = modified_img[i, j]

            # 检查是否与选定颜色匹配
            if r == rr and g == gg and b == bb:
                # 将匹配的像素点设为白色
                modified_img[i, j] = [255, 0, 255]

    end_time = time.time()
    elapsed_time = end_time - start_time

    return modified_img, elapsed_time


# 方法2：使用向量化操作
def method2(img, color):
    start_time = time.time()

    # 将图像转换为numpy数组
    img_array = np.array(img)
    # 将选定的颜色转换为HSL

    rr, gg, bb = [int(color[i:i + 2], 16) for i in range(1, 7, 2)]
    print(rr, gg, bb)

    img_array = np.array(img)
    dst = np.zeros_like(img_array)
    dst = np.zeros_like(img_array)

    # 将图像数组归一化到0-1范围
    img_array_norm = img_array / 255.0

    # 获取纯红像素点的条件
    red_condition = (img_array[:, :, 0] == rr) & (img_array[:, :, 1] == gg) & (img_array[:, :, 2] == bb)

    # 将纯红像素点变为白色
    img_array[red_condition] = [255, 0, 255]

    # 将修改后的numpy数组转换回Image对象
    modified_img = Image.fromarray(img_array)

    end_time = time.time()
    elapsed_time = end_time - start_time

    return modified_img, elapsed_time

    # 将调整后的图像显示在画布上
    photo = ImageTk.PhotoImage(modified_img)
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)
    canvas.image = photo


# 选定颜色
color = (255, 0, 0)  # 红色

# 测试方法1
modified_img1, elapsed_time1 = method1(img, color)
print(f"Method 1: Elapsed Time = {elapsed_time1:.6f} seconds")


# 创建画布
def select_color():
    color = colorchooser.askcolor()[1]
    print(color)
    if color:
        modified_img2, elapsed_time2 = method2(img, color)
        print(f"Method 2: Elapsed Time = {elapsed_time2:.6f} seconds")


# 创建选择颜色按钮

img = Image.open('../image/color.png')
select_color_button = tk.Button(root, text='Select Color', command=select_color)
select_color_button.pack()
# 运行主循环
root.mainloop()

# 测试方法2
# modified_img2, elapsed_time2 = method2(img, color)
# print(f"Method 2: Elapsed Time = {elapsed_time2:.6f} seconds")
