import cv2
import numpy as np


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


# 读取图像
image = cv2.imread('./image/img2.jpg')

# 图像光感调节，参数 a: 0~100，这里设置为增加光感 20
sensed_image = lightSense(image, 20)

# 显示原图和光感调节后的图像
cv2.imshow('Original Image', image)
cv2.imshow('Sensed Image', sensed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
