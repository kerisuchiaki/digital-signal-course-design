from PIL import Image
from colorsys import rgb_to_hls, hls_to_rgb


def adjust_hsl(image_path, target_rgb):
    image = Image.open(image_path)
    width, height = image.size

    target_hls = rgb_to_hls(target_rgb[0] / 255, target_rgb[1] / 255, target_rgb[2] / 255)

    adjusted_image = Image.new("RGB", (width, height))

    for x in range(width):
        for y in range(height):
            r, g, b = image.getpixel((x, y))
            h, l, s = rgb_to_hls(r / 255, g / 255, b / 255)

            new_r, new_g, new_b = hls_to_rgb(target_hls[0], l, s)

            adjusted_image.putpixel((x, y), (int(new_r * 255), int(new_g * 255), int(new_b * 255)))

    adjusted_image.save("adjusted_image.jpg")


# 调整纯红色图像到 RGB(51, 204, 255)
adjust_hsl("../image/red.png", (51, 204, 255))

# python图像处理HSL调整，要求有三个滑块控制HSL的分量