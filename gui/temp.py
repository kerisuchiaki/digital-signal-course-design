from PIL import Image
import numpy as np

def hsl_to_rgb(h, s, l):
    # 规范化色相到[0, 360)
    h = h % 360

    # 如果饱和度为0，灰度色彩
    if s == 0:
        r = g = b = int(l * 255)
    else:
        # 计算辅助变量
        if l < 0.5:
            temp2 = l * (1.0 + s)
        else:
            temp2 = l + s - l * s

        temp1 = 2.0 * l - temp2

        # 计算RGB的每个分量
        h /= 360.0
        rgb = [0, 0, 0]
        for i in range(3):
            t = h + 1.0 / 3.0 * -(i - 1)
            if t < 0:
                t += 1
            elif t > 1:
                t -= 1

            if 6.0 * t < 1.0:
                rgb[i] = int((temp1 + (temp2 - temp1) * 6.0 * t) * 255)
            elif 2.0 * t < 1.0:
                rgb[i] = int(temp2 * 255)
            elif 3.0 * t < 2.0:
                rgb[i] = int((temp1 + (temp2 - temp1) * (2.0 / 3.0 - t) * 6.0) * 255)
            else:
                rgb[i] = int(temp1 * 255)

    return tuple(rgb)


def rgb_to_hsl(rgb):
    # 将RGB值归一化到[0, 1]范围
    r, g, b = rgb
    r /= 255.0
    g /= 255.0
    b /= 255.0

    # 计算max和min
    max_val = max(r, g, b)
    min_val = min(r, g, b)

    # 计算亮度（l）
    l = (max_val + min_val) / 2.0

    # 如果max和min相等，灰度色调
    if max_val == min_val:
        h = 0.0
        s = 0.0
    else:
        # 计算饱和度（s）
        s = (max_val - min_val) / (1 - abs(2 * l - 1))

        # 计算色相（h）
        if max_val == r:
            h = 60 * ((g - b) / (max_val - min_val) % 6)
        elif max_val == g:
            h = 60 * ((b - r) / (max_val - min_val) + 2)
        elif max_val == b:
            h = 60 * ((r - g) / (max_val - min_val) + 4)

    # 规范化色相到[0, 360)
    h = (h + 360) % 360

    return h, s, l

# 将PIL Image从RGB转HSL
def pil_image_rgb_to_hsl(image):
    image_array = np.array(image)
    hsl_data = np.apply_along_axis(rgb_to_hsl, 2, image_array)
    hsl_image = Image.fromarray((hsl_data * 255).astype(np.uint8), mode='RGB')
    return hsl_image

# 将PIL Image从HSL转RGB
def pil_image_hsl_to_rgb(hsl_image):
    hsl_array = np.array(hsl_image) / 255.0
    rgb_data = np.apply_along_axis(hsl_to_rgb, 2, hsl_array)
    rgb_image = Image.fromarray((rgb_data * 255).astype(np.uint8), mode='RGB')
    return rgb_image

# 读取RGB图像
rgb_image_path = "../image/miku.jpg"  # 替换为实际路径
rgb_image = Image.open(rgb_image_path)

# RGB to HSL
hsl_image = pil_image_rgb_to_hsl(rgb_image)
hsl_image.show(title="HSL Image")

# HSL to RGB
rgb_image_after_conversion = pil_image_hsl_to_rgb(hsl_image)
rgb_image_after_conversion.show(title="RGB Image After Conversion")
