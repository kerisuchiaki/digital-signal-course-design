import numpy as np
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import colorchooser

# 使用PIL的Image模块加载图像
img = Image.open('../image/color.png')

root = tk.Tk()

# 创建画布
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

photo = ImageTk.PhotoImage(img)
image_item = canvas.create_image(0, 0, anchor=tk.NW, image=photo)


def update_image(color):
    if color:
        # 将图像转换为numpy数组
        img_array = np.array(img)

        rr, gg, bb = [int(color[i:i + 2], 16) for i in range(1, 7, 2)]
        print(rr, gg, bb)

        # 获取纯红像素点的条件
        red_condition = (img_array[:, :, 0] == rr) & (img_array[:, :, 1] == gg) & (img_array[:, :, 2] == bb)

        # 将纯红像素点变为橙色（255, 127.5, 0）
        img_array[red_condition] = [255, 127.5, 0]

        # 将修改后的numpy数组转换回Image对象
        modified_img = Image.fromarray(img_array)

        global img
        # python的特点就是可以不声明而赋值，或者说赋值即声明，导致函数内部不知道内部出现的和外面的同名变量是同一个，会将内部的同名变量认为是新定义的
        #
        img = modified_img

        # 更新画布上的图片
        photo = ImageTk.PhotoImage(modified_img)
        canvas.itemconfig(image_item, image=photo)
        canvas.image = photo


def select_color():
    # 打开颜色选择器对话框
    _, color = colorchooser.askcolor()

    if color:
        update_image(color)


# 创建选择颜色按钮
select_color_button = tk.Button(root, text='Select Color', command=select_color)
select_color_button.pack()

# 运行主循环
root.mainloop()
