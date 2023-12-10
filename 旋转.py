import numpy as np

import matplotlib.pyplot as plt

import cv2


def rotate(img, yaw):
    rows, cols, channels = img.shape
    # getRotationMatrix2D有三个参数，第一个为旋转中心，第二个为旋转角度，第三个为缩放比例
    M = cv2.getRotationMatrix2D((cols / 2, rows / 2), yaw, 1)
    dst = cv2.warpAffine(img, M, (cols, rows))
    return dst


# 读取图像
img = cv2.imread('./image/img2.jpg')

# 旋转图像
rotated_img = rotate(img, 90)

# 显示原图和旋转后的图像
cv2.imshow('Original Image', img)
cv2.imshow('Rotated Image', rotated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
