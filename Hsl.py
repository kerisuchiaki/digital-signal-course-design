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
