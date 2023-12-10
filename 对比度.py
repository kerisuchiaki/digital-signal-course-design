import cv2
import numpy as np


# 对比度调节，参数 contrast_factor: -20~30
def adjust_contrast(img, contrast_factor):
    contrast_factor = np.float32(contrast_factor + 20) / 50.0
    table = np.array([(i - 74) * contrast_factor + 74 for i in range(0, 256)]).clip(0, 255).astype('uint8')
    if img.shape[2] == 1:
        return cv2.LUT(img, table)[:, :, np.newaxis]
    else:
        return cv2.LUT(img, table)


# 读取图像
image = cv2.imread('./image/img2.jpg')

# 图像对比度调节，参数 contrast_factor: -20~30，这里设置为增加对比度 10
contrasted_image = adjust_contrast(image, 10)

# 显示原图和对比度调节后的图像
cv2.imshow('Original Image', image)
cv2.imshow('Contrasted Image', contrasted_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
