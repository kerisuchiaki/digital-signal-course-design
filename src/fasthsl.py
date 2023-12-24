import colorsys
import numpy as np
from PIL import Image


def adjust_color_and_neighbors(img, color, hue_shift, saturation_shift, lightness_shift):
    # 将图像转换为numpy数组
    img_array = np.array(img)

    # 将选定的颜色转换为RGB表示
    rr, gg, bb = color

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


# 示例用法
selected_color = (0, 255, 255)  # 选定的颜色为红色
hue_shift = 30  # 色相调整值
saturation_shift = -0.2  # 饱和度调整值
lightness_shift = 0.3  # 亮度调整值
tolerance = 10  # 匹配容差
weight = 0.5  # 相邻颜色调整权重

# 假设有一个名为"image"的图像对象
adjusted_image = adjust_color_and_neighbors(image, selected_color, hue_shift, saturation_shift, lightness_shift)
