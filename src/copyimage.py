def update_image(self, color=None):
    print("debug")
    color = self.color
    hsl_image = self.image.copy()
    # 将图像转换为HSL颜色空间

    # 获取滑块的值
    hue = self.tk_scale_Hue.get()  # 将0-100的值转换为0-360的角度
    saturation = self.tk_scale_Saturation.get() / 100.0
    lightness = self.tk_scale_lightness.get() / 100.0
    print(hue, saturation, lightness)

    # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
    # 针对每个像素进行HSL调整

    # ------------

    if color:
        # 将选定的颜色转换为HSL
        rr, gg, bb = [int(color[i:i + 2], 16) for i in range(1, 7, 2)]
        print(rr, gg, bb)

        img_array = np.array(self.image)
        dst = np.zeros_like(img_array)

        # 将图像数组归一化到0-1范围
        img_array_norm = img_array / 255.0

        # 将选定颜色转换为HSL
        h_tmp, l_tmp, s_tmp = colorsys.rgb_to_hls(rr / 255.0, gg / 255.0, bb / 255.0)

        for channel in range(3):
            # 提取当前通道的像素值
            channel_pixels = img_array_norm[:, :, channel]

            # 创建一个布尔掩码，指示与选定颜色匹配的像素
            mask = np.logical_and.reduce(
                (img_array[:, :, 0] == rr, img_array[:, :, 1] == gg, img_array[:, :, 2] == bb))

            # 对满足条件的像素进行批量处理
            h, l, s = np.where(mask, h_tmp, channel_pixels), np.where(mask, l_tmp, channel_pixels), np.where(mask,
                                                                                                             s_tmp,
                                                                                                             channel_pixels)


            # 进行HSL调整
            adjusted_h = (hue / 360.0 + h) % 1.0
            adjusted_s = np.clip(saturation + s, 0, 1)
            adjusted_l = np.clip(lightness + l, 0, 1)

            # 将调整后的HSL转换为RGB
            hls_to_rgb_vectorized = np.vectorize(colorsys.hls_to_rgb)
            adjusted_r, adjusted_g, adjusted_b = hls_to_rgb_vectorized(adjusted_h, adjusted_l, adjusted_s)

            # 将处理后的像素值放回图像数组
            img_array[:, :, channel] = np.where(mask, adjusted_r, img_array[:, :, channel])
            dst[:, :, channel] = img_array[:, :, channel]

    img2 = Image.fromarray(np.uint8(dst * 255))
    self.image = img2
    self.show_image()
    return

    # --------

    # &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&