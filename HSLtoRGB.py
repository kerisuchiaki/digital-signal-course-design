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

# 示例
h, s, l = 120, 1, 0.75  # 红色
rgb = hsl_to_rgb(h, s, l)
print(f"HSL({h:.2f}°, {s:.2f}, {l:.2f}) 转换为 RGB: ({rgb[0]}, {rgb[1]}, {rgb[2]})")
