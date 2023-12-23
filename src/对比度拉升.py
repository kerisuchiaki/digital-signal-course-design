import cv2
import imutils
import numpy as np

image = cv2.imread('../image/sakura.jpg')
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 在灰度图进行分段线性对比度拉伸
# 此种方式变换函数把灰度级由原来的线性拉伸到整个范围[0, 255]
r_min, r_max = 255, 0
for i in range(gray_img.shape[0]):
    for j in range(gray_img.shape[1]):
        if gray_img[i, j] > r_max:
            r_max = gray_img[i, j]
        if gray_img[i, j] < r_min:
            r_min = gray_img[i, j]
r1, s1 = r_min, 0
r2, s2 = r_max, 255
print(r1, s1, r2, s2)

precewise_img = np.zeros((gray_img.shape[0], gray_img.shape[1]), dtype=np.uint8)
k1 = s1 / r1
if r2 != 255:
    k3 = (255 - s2) / (255 - r2)
k2 = (s2 - s1) / (r2 - r1)
for i in range(gray_img.shape[0]):
    for j in range(gray_img.shape[1]):
        if r1 <= gray_img[i, j] <= r2:
            precewise_img[i, j] = k2 * (gray_img[i, j] - r1)
        elif gray_img[i, j] < r1:
            precewise_img[i, j] = k1 * gray_img[i, j]
        elif gray_img[i, j] > r2:
            precewise_img[i, j] = k3 * (gray_img[i, j] - r2)

cv2.imshow('origin image', imutils.resize(image, 480))
cv2.imshow('precewise image', imutils.resize(precewise_img, 480))
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()
