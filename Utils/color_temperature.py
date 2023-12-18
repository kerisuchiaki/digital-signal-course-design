from PIL import Image, ImageTk


def change_temperature(pil_image, temperature):
    r, g, b = pil_image.split()
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
    pil_image=None
    adjusted_image = change_temperature(pil_image, temperature)

