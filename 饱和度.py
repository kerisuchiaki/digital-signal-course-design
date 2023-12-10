import cv2
import numpy as np


# 饱和度调整算法，输入参数 increment: [-100, 100] 归一化为 [-1, 1]
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


# 读取图像
image = cv2.imread('./image/img2.jpg')

# 饱和度调整，参数 increment: [-100, 100] 归一化为 [-1, 1]，这里设置为增加饱和度 30
saturated_image = saturation(image, 30)

# 显示原图和饱和度调整后的图像
cv2.imshow('Original Image', image)
cv2.imshow('Saturated Image', saturated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
