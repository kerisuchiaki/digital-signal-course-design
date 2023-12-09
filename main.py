

import cv2
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


# 图像旋转
def rotate(img, yaw):
    rows, cols, channels = img.shape
    # getRotationMatrix2D有三个参数，第一个为旋转中心，第二个为旋转角度，第三个为缩放比例
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), yaw, 1)
    dst = cv2.warpAffine(img, M, (cols, rows))
    return dst


# 1.3图像剪切
def cut(img, x_lt, y_lt, x_rb, y_rb):
    return img[x_lt:x_rb, y_lt:y_rb]


# 1.4图像缩放
# 缩放系数 k ∈ [0, 2]
def imgScale(img, k):
    # 输入k [0, 100]
    k = k / 50
    if k < 1:
        # 缩小
        dst = cv2.resize(img, (int(k * img.shape[1]), int(k * img.shape[0])), interpolation=cv2.INTER_AREA)
    else:
        # 放大
        dst = cv2.resize(img, (int(k * img.shape[1]), int(k * img.shape[0])), interpolation=cv2.INTER_LINEAR)
    return dst


# 2.1对比度调节
def adjust_contrast(img, contrast_factor):
    contrast_factor = np.float32(contrast_factor + 20) / 50.0
    table = np.array([(i - 74) * contrast_factor + 74 for i in range(0, 256)]).clip(0, 255).astype('uint8')
    if img.shape[2] == 1:
        return cv2.LUT(img, table)[:, :, np.newaxis]
    else:
        return cv2.LUT(img, table)


# 2.2亮度调节
# 亮度调节 参数 b: 0~100
def lightness(img, b):
    # b ∈ [0, 100] -> [-1.0, 1.0]
    b = np.float32(b - 50) / 180.0
    b = b * 255
    res = img.astype(np.float32)
    res = res + b
    res = np.where(res > 255, 255, res)
    res = np.where(res < 0, 0, res)
    res = res.astype(np.uint8)
    return res


# 图像光感调节 参数 a: 0~100
# a ∈ [0, 100] ->
def lightSense(img, a):
    a = np.float32(a - 50) / 80.0
    a = a * 255
    res = img.astype(np.float32)
    res = res + a * res / 255.0
    res = np.where(res > 255, 255, res)
    res = np.where(res < 0, 0, res)
    res = res.astype(np.uint8)
    return res


# 曝光度调节 参数 b: 0~100
def exposure(img, b):
    # b ∈ [0, 100] -> [-2.5, 2.5]
    b = np.float32(b - 50) / 20.0
    print('b = %.2f' % b)
    res = img.astype(np.float32)
    res = res * pow(2, b)
    res = np.where(res > 255, 255, res)
    res = res.astype(np.uint8)
    return res


# 饱和度调整算法 输入参数increment,[-100,100] 归一化为 [-1,1]
@jit
def saturation(img, increment):
    increment = np.float32(increment - 50) / 50.0
    res = img.astype(np.float64)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            val_max = max(res[i, j, 0], max(res[i, j, 1], res[i, j, 2]))
            val_min = min(res[i, j, 0], min(res[i, j, 1], res[i, j, 2]))
            delta = (val_max - val_min) / 255
            if delta == 0:
                continue
            val = (val_max + val_min) / 255
            L = val / 2
            if L < 0.5:
                S = delta / val
            else:
                S = delta / (2 - val)

            if increment >= 0:
                if increment + S > 1:
                    alpha = S
                else:
                    alpha = 1 - increment
                alpha = 1 / alpha - 1
                res[i, j, 2] = res[i, j, 2] + (res[i, j, 2] - L * 255) * alpha
                res[i, j, 1] = res[i, j, 1] + (res[i, j, 1] - L * 255) * alpha
                res[i, j, 0] = res[i, j, 0] + (res[i, j, 0] - L * 255) * alpha
            else:
                alpha = increment
                res[i, j, 2] = L * 255 + (res[i, j, 2] - L * 255) * (1 + alpha)
                res[i, j, 1] = L * 255 + (res[i, j, 1] - L * 255) * (1 + alpha)
                res[i, j, 0] = L * 255 + (res[i, j, 0] - L * 255) * (1 + alpha)
    res = res.astype(np.uint8)
    return res


# 直方图均衡化
def equalize(img):
    dst = img.copy()
    rows, cols, channels = dst.shape
    for i in range(channels):
        dst[:, :, i] = cv2.equalizeHist(dst[:, :, i])
    return dst


# 图像HSL调节
# cf_h 范围[0, 200] 对应[0, 2]
# cf_s, cf_l 范围[0, 200] 对应 [0, 2]
# 整个调用过程：
# 对于一个img
#   1. hslImg = convertToHSL(img)
#   2. dst = HSL(hslImg, cf_h, cf_s, cf_l)
#   3. dst = convertToBGR(dst)
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
@jit
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
@jit
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

# 补充完整代码
