import numpy as np
import cv2 as cv

# 以灰度图的形式读取图像
img = cv.imread('./image/img2.jpg', 0)
cv.imshow('window', img)


def cut(img, x_lt, y_lt, x_rb, y_rb):
    return img[y_lt:y_rb, x_lt:x_rb]  # 修正参数顺序


cv.waitKey(0)
img2 = cut(img, 1000, 200, 2000, 700)
cv.imshow('window2', img2)

cv.waitKey(0)
cv.destroyAllWindows()
