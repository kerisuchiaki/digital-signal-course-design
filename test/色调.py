from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog


def adjust_temperature(image_path, temperature):
    original_image = Image.open(image_path).convert("RGB")
    r, g, b = original_image.split()
    print(temperature)

    # 避免除以零错误
    adjusted_b = b.point(lambda p: p * (1 / temperature) if temperature != 0 else p)

    # 调整红色通道
    adjusted_r = r.point(lambda p: p * temperature)

    # 合并通道
    adjusted_image = Image.merge("RGB", (adjusted_r, g, adjusted_b))

    return adjusted_image


def update_temperature(value):
    temperature = float(value) / 100.0
    print(value)

    # 避免除以零错误
    temperature = max(temperature, 0.001)

    adjusted_image = adjust_temperature(image_path, temperature)
    updated_photo = ImageTk.PhotoImage(adjusted_image)
    canvas.itemconfig(image_item, image=updated_photo)
    canvas.image = updated_photo


def open_image():
    global image_path
    image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp")])

    if image_path:
        original_image = Image.open(image_path).convert("RGB")
        photo = ImageTk.PhotoImage(original_image)
        canvas.config(width=original_image.width, height=original_image.height)
        canvas.itemconfig(image_item, image=photo)
        canvas.image = photo
        scale.config(state=tk.NORMAL)
    else:
        scale.config(state=tk.DISABLED)


# 创建主窗口
root = tk.Tk()
root.title("Image Temperature Adjustment")

# 打开图像按钮
open_button = tk.Button(root, text="Open Image", command=open_image)
open_button.pack(pady=10)

# 创建Canvas用于显示图像
canvas = tk.Canvas(root)
canvas.pack()

# 创建滑块用于调节色温
scale = tk.Scale(root, from_=0, to=200, orient=tk.HORIZONTAL, label="Temperature", command=update_temperature,
                 state=tk.DISABLED)
scale.pack(pady=10)

# 初始图像路径
image_path = None

# 图像显示项
image_item = canvas.create_image(0, 0, anchor=tk.NW)

# 运行主循环
root.mainloop()
