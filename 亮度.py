import cv2
import numpy as np


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


# 读取图像
image = cv2.imread('./image/img2.jpg')

# 亮度调节，参数 b: 0~100，这里设置为增加亮度 30
brightened_image = lightness(image, 100)

# 显示原图和亮度调节后的图像
cv2.imshow('Original Image', image)
cv2.imshow('Brightened Image', brightened_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
