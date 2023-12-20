from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog, colorchooser
import colorsys

def update_color():
    # 将图像转换为HSL颜色空间
    hsl_image = original_image.convert("HSV")

    # 获取滑块的值
    hue = hue_scale.get() * 3.6  # 将0-100的值转换为0-360的角度
    saturation = saturation_scale.get() / 100.0
    lightness = lightness_scale.get() / 100.0

    # 针对每个像素进行HSL调整
    pixels = hsl_image.load()
    width, height = hsl_image.size
    for x in range(width):
        for y in range(height):
            h, s, v = pixels[x, y]
            adjusted_h = hue if hue_checkbox_var.get() else h
            adjusted_s = saturation if saturation_checkbox_var.get() else s / 255.0
            adjusted_l = lightness if lightness_checkbox_var.get() else v / 255.0

            adjusted_r, adjusted_g, adjusted_b = colorsys.hsv_to_rgb(adjusted_h / 360.0, adjusted_s, adjusted_l)
            pixels[x, y] = (int(adjusted_h), int(adjusted_s * 255), int(adjusted_b * 255))

    # 将图像转换回RGB颜色空间
    adjusted_image = hsl_image.convert("RGB")

    # 将调整后的图像显示在画布上
    photo = ImageTk.PhotoImage(adjusted_image)
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)
    canvas.image = photo

def load_image():
    # 打开文件对话框选择图像文件
    file_path = filedialog.askopenfilename()
    if file_path:
        # 加载图像并显示在画布上
        global original_image
        original_image = Image.open(file_path)
        photo = ImageTk.PhotoImage(original_image)
        canvas.create_image(0, 0, anchor=tk.NW, image=photo)
        canvas.image = photo


def select_color():
    # 打开颜色选择器对话框
    color = colorchooser.askcolor()[1]

    print(color)

    if color:
        update_color(color)

# 创建主窗口
root = tk.Tk()

# 创建画布
canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

# 创建滑块和标签
hue_label = tk.Label(root, text='Hue')
hue_label.pack()
hue_scale = tk.Scale(root, from_=0, to=100, orient='horizontal')
hue_scale.pack()

saturation_label = tk.Label(root, text='Saturation')
saturation_label.pack()
saturation_scale = tk.Scale(root, from_=0, to=100, orient='horizontal')
saturation_scale.pack()

lightness_label = tk.Label(root, text='Lightness')
lightness_label.pack()
lightness_scale = tk.Scale(root, from_=0, to=100, orient='horizontal')
lightness_scale.pack()

# 创建复选框
hue_checkbox_var = tk.BooleanVar()
hue_checkbox = tk.Checkbutton(root, text="Hue", variable=hue_checkbox_var)
hue_checkbox.pack()

saturation_checkbox_var = tk.BooleanVar()
saturation_checkbox = tk.Checkbutton(root, text="Saturation", variable=saturation_checkbox_var)
saturation_checkbox.pack()

lightness_checkbox_var = tk.BooleanVar()
lightness_checkbox = tk.Checkbutton(root, text="Lightness", variable=lightness_checkbox_var)
lightness_checkbox.pack()

# 创建加载图像按钮
load_button = tk.Button(root, text='Load Image', command=load_image)
load_button.pack()

# 创建选择颜色按钮
select_color_button = tk.Button(root, text='Select Color', command=select_color)
select_color_button.pack()

# 创建应用按钮
apply_button = tk.Button(root, text='Apply', command=update_color)
apply_button.pack()

# 运行主循环
root.mainloop()