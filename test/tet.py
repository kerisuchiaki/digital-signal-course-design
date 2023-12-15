from tkinter import Tk, Scale, Label
from PIL import Image, ImageTk, ImageOps


class ImageEditor:
    def __init__(self, image_path):
        # 创建 Tkinter 窗口
        self.root = Tk()
        self.root.title("Image Editor")

        # 打开图像并进行初始化
        self.image = Image.open(image_path).convert("RGB")
        self.edited_image = self.image.copy()

        # 创建调整 HSL 的滑块
        self.hue_scale = Scale(self.root, from_=0, to=360, orient="horizontal", command=self.update_image)
        self.hue_scale.set(0)
        self.hue_scale.pack()

        self.saturation_scale = Scale(self.root, from_=0, to=200, orient="horizontal", command=self.update_image)
        self.saturation_scale.set(100)
        self.saturation_scale.pack()

        self.lightness_scale = Scale(self.root, from_=0, to=200, orient="horizontal", command=self.update_image)
        self.lightness_scale.set(100)
        self.lightness_scale.pack()

        # 创建用于显示图像的 Label
        self.image_label = Label(self.root)
        self.image_label.pack()

        # 初始化时更新图像
        self.update_image()

    def update_image(self, event=None):
        # 获取当前滑块的值
        hue = self.hue_scale.get()
        saturation = self.saturation_scale.get() / 100.0
        lightness = self.lightness_scale.get() / 100.0

        # 将图像转换为灰度图
        edited_image = self.image.convert("L")

        # 使用 ImageOps.colorize 方法调整图像的 HSL
        edited_image = ImageOps.colorize(edited_image, (hue, saturation, lightness), (0, 0, 0))

        # 将图像转换回 RGB 模式
        edited_image = edited_image.convert("RGB")

        # 更新编辑后的图像
        self.edited_image = edited_image

        # 在 GUI 中显示处理后的图像
        photo = ImageTk.PhotoImage(edited_image)
        self.image_label.configure(image=photo)
        self.image_label.image = photo

    def run(self):
        # 启动 Tkinter 主循环
        self.root.mainloop()


# 创建 ImageEditor 对象并运行图像编辑器
image_editor = ImageEditor("../image/miku.jpg")
image_editor.run()
