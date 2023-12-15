from colorsys import rgb_to_hls, hls_to_rgb
from tkinter import Tk, Scale, Label

import numpy as np
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

        self.saturation_scale = Scale(self.root, from_=0, to=100, orient="horizontal", command=self.update_image)
        self.saturation_scale.set(0)
        self.saturation_scale.pack()

        self.lightness_scale = Scale(self.root, from_=0, to=100, orient="horizontal", command=self.update_image)
        self.lightness_scale.set(0)
        self.lightness_scale.pack()

        # 创建用于显示图像的 Label
        self.image_label = Label(self.root)
        self.image_label.pack()
        self.pre()

        # 初始化时更新图像
        self.update_image()

    def pre(self):
        width, height = self.image.size
        h_total = 0
        s_total = 0
        l_total = 0

        for x in range(width):
            for y in range(height):
                r, g, b = self.image.getpixel((x, y))
                h, l, s = rgb_to_hls(r / 255, g / 255, b / 255)
                # print("h:", h)
                # print("s:", s)
                # print("l:", l)
                h_total += h
                l_total += l
                s_total += s
        print("h:", h_total)
        print("s:", s_total)
        print("l:", l_total)
        h_total = h_total / (height * width)*360
        self.hue_scale.set(h_total)
        s_total = s_total / (height * width)*100
        self.saturation_scale.set(s_total)
        l_total = l_total / (height * width)*100
        self.lightness_scale.set(l_total)
        print("h:", h_total)
        print("s:", s_total)
        print("l:", l_total)


    def update_image(self, event=None):
        # 获取当前滑块的值
        hue = self.hue_scale.get()
        saturation = self.saturation_scale.get()
        lightness = self.lightness_scale.get()

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

    # 图像HSL调节
    # cf_h 范围[0, 200] 对应[0, 2]
    # cf_s, cf_l 范围[0, 200] 对应 [0, 2]
    # 整个调用过程：
    # 对于一个img
    #   1. hslImg = convertToHSL(img)
    #   2. dst = HSL(hslImg, cf_h, cf_s, cf_l)
    #   3. dst = convertToBGR(dst)
    import numpy as np

    @jit
    def HSL(img, cf_h, cf_s, cf_l):
        # cf_h 范围[0, 200] 对应[0, 2]
        # cf_s, cf_l 范围[0, 200] 对应 [0, 2]
        # h_new = h * cf_h
        cf_h = (cf_h + 10) / 100.0
        cf_s = (cf_s + 10) / 100.0
        cf_l = (cf_l + 20) / 100.0
        rows, cols, channels = img.shape
        res = np.zeros(img.shape)
        for i in range(rows):
            for j in range(cols):
                res[i, j, 0] = np.float32(cf_h) * img[i, j, 0]
                if res[i, j, 0] > 360.0:
                    res[i, j, 0] = 360.0
                res[i, j, 1] = np.float32(cf_s) * img[i, j, 1]
                if res[i, j, 1] > 1.0:
                    res[i, j, 1] = 1.0
                res[i, j, 2] = np.float32(cf_l) * img[i, j, 2]
                if res[i, j, 2] > 1.0:
                    res[i, j, 2] = 1.0

        return res

    # 图像RGB空间转HSL
    def convertToHSL(img):
        rows, cols, channels = img.shape
        res = np.zeros(img.shape)
        for i in range(rows):
            for j in range(cols):
                b_val = np.float32(img[i, j, 0]) / 255.0
                g_val = np.float32(img[i, j, 1]) / 255.0
                r_val = np.float32(img[i, j, 2]) / 255.0
                max_val = max(b_val, max(g_val, r_val))
                min_val = min(b_val, min(g_val, r_val))
                # H [0, 360)
                H = 0
                S = 0
                L = 0
                if max_val == min_val:
                    H = 0
                elif max_val == r_val and g_val >= b_val:
                    H = np.float32(60) * (g_val - b_val) / (max_val - min_val)
                elif max_val == r_val and g_val < b_val:
                    H = np.float32(60) * (g_val - b_val) / (max_val - min_val) + 360
                elif max_val == g_val:
                    H = np.float32(60) * (b_val - r_val) / (max_val - min_val) + 120
                elif max_val == b_val:
                    H = np.float32(60) * (r_val - g_val) / (max_val - min_val) + 240

                # L [0, 1]
                L = np.float32(0.5) * (max_val + min_val)

                # S [0, 1]
                if L == 0 or max_val == min_val:
                    S = 0
                elif 0 < L <= 0.5:
                    S = (max_val - min_val) / (2.0 * L)
                elif L > 0.5:
                    S = (max_val - min_val) / (2.0 - 2.0 * L)

                res[i, j, 0] = H
                res[i, j, 1] = S
                res[i, j, 2] = L
        return res

    # 图像HSL空间转RGB
    def convertToBGR(img):
        rows, cols, channels = img.shape
        res = np.zeros(img.shape, dtype=np.float32)
        for i in range(rows):
            for j in range(cols):
                h, s, l = img[i, j, :]
                if s == 0:
                    res[i, j, 0] = l
                    res[i, j, 1] = l
                    res[i, j, 2] = l
                    continue
                if l < 0.5:
                    q = l * (1.0 + s)
                else:
                    q = l + s - (l * s)
                p = 2 * l - q
                hk = h / 360.0
                tC = np.array([hk - 1.0 / 3.0, hk, hk + 1.0 / 3.0], dtype=np.float32)
                tC = np.where(tC < 0, tC + 1.0, tC)
                tC = np.where(tC > 1, tC - 1.0, tC)
                for tt in range(3):
                    if tC[tt] < 1.0 / 6.0:
                        temp_val = p + ((q - p) * 6.0 * tC[tt])
                    elif tC[tt] < 1.0 / 2.0:
                        temp_val = q
                    elif tC[tt] < 2.0 / 3.0:
                        temp_val = p + ((q - p) * 6.0 * (2.0 / 3.0 - tC[tt]))
                    else:
                        temp_val = p
                    res[i, j, tt] = temp_val

        res = res * np.float32(255.0)
        res = res.astype(np.uint8)
        return res


# 创建 ImageEditor 对象并运行图像编辑器
image_editor = ImageEditor("../image/shuiyin.png")
image_editor.run()
