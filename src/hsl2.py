import tkinter as tk
from tkinter import colorchooser
import colorsys


def update_color(value):
    # 获取滑块的值
    hue = hue_scale.get() / 100.0
    saturation = saturation_scale.get() / 100.0
    lightness = lightness_scale.get() / 100.0

    # 将HSL转换为RGB颜色
    rgb = colorsys.hls_to_rgb(hue, lightness, saturation)
    r, g, b = [int(x * 255) for x in rgb]

    # 更新颜色预览标签的背景颜色
    color_preview.config(bg='#%02x%02x%02x' % (r, g, b))


def select_color():
    # 打开颜色选择器对话框
    color = colorchooser.askcolor()[1]

    print(color)

    if color:
        # 将选定的颜色转换为HSL
        r, g, b = [int(color[i:i + 2], 16) for i in range(1, 7, 2)]
        print(r,g,b)
        h, l, s = colorsys.rgb_to_hls(r / 255.0, g / 255.0, b / 255.0)

        # 更新滑块的值
        hue_scale.set(h * 100)
        saturation_scale.set(s * 100)
        lightness_scale.set(l * 100)
        update_color(None)


# 创建主窗口
root = tk.Tk()

# 创建颜色预览标签
color_preview = tk.Label(root, width=20, height=10)
color_preview.pack()

# 创建滑块和标签
hue_label = tk.Label(root, text='Hue')
hue_label.pack()
hue_scale = tk.Scale(root, from_=0, to=100, orient='horizontal', command=update_color)
hue_scale.pack()

saturation_label = tk.Label(root, text='Saturation')
saturation_label.pack()
saturation_scale = tk.Scale(root, from_=0, to=100, orient='horizontal', command=update_color)
saturation_scale.pack()

lightness_label = tk.Label(root, text='Lightness')
lightness_label.pack()
lightness_scale = tk.Scale(root, from_=0, to=100, orient='horizontal', command=update_color)
lightness_scale.pack()

# 创建选择颜色按钮
select_color_button = tk.Button(root, text='Select Color', command=select_color)
select_color_button.pack()

# 运行主循环
root.mainloop()