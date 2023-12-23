from PIL import Image
import numpy as np

from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog, colorchooser
import colorsys

# 使用PIL的Image模块加载图像
img = Image.open('../image/color.png')
# 创建选择颜色按钮

root = tk.Tk()

# 创建画布
canvas = tk.Canvas(root, width=400, height=400)
canvas.place(x=384, y=78, width=960, height=960)

photo = ImageTk.PhotoImage(img)
canvas.create_image(0, 0, anchor=tk.NW, image=photo)
canvas.image = photo



def update_image(img, color):
    if color:
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
        h,l,s=colorsys.rgb_to_hls(rr/255,gg/255,bb/255)
        adjusted_h = hue / 360.0 + h
        if adjusted_h <= 0: adjusted_h += 1
        if adjusted_h >= 1: adjusted_h -= 1
        adjusted_s = saturation + s
        if adjusted_s <= 0: adjusted_s = 0
        if adjusted_s >= 1: adjusted_s = 1
        adjusted_l = lightness + l
        if adjusted_l <= 0: adjusted_l = 0
        if adjusted_l >= 1: adjusted_l = 1
        adjusted_r, adjusted_g, adjusted_b = colorsys.hls_to_rgb(adjusted_h, adjusted_l, adjusted_s)


        # 将纯红像素点变为白色
        img_array[red_condition] = [adjusted_r, adjusted_g, adjusted_b]

        # 将修改后的numpy数组转换回Image对象
        modified_img = Image.fromarray(img_array)

        # 将调整后的图像显示在画布上
        photo = ImageTk.PhotoImage(modified_img)
        canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        canvas.image = photo



def select_color():
    # 打开颜色选择器对话框
    color = colorchooser.askcolor()[1]

    print(color)

    if color:
        update_image(img,color)


# 创建画布
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# 创建选择颜色按钮
select_color_button = tk.Button(root, text='Select Color', command=select_color)
select_color_button.pack()

# 运行主循环
root.mainloop()
