import cv2
import numpy as np


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

# 图像曝光度调节，参数 b: 0~100，这里设置为增加曝光度 30
exposed_image = exposure(image, 30)

# 显示原图和曝光度调节后的图像
cv2.imshow('Original Image', image)
cv2.imshow('Exposed Image', exposed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
