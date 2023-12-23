import cv2
import imutils
import numpy as np

image = cv2.imread('../image/Lena.tif')
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#阈值处理函数：当r1=r2, s1=0, s2=L-1时，此时分段线性函数便是阈值处理函数
plist = []
for i in range(gray_img.shape[0]):
    for j in range(gray_img.shape[1]):
        plist.append(gray_img[i, j])
r_avg = int(sum(plist)/len(plist))
thresh_img = np.zeros((gray_img.shape[0], gray_img.shape[1]), dtype=np.uint8)
for i in range(gray_img.shape[0]):
    for j in range(gray_img.shape[1]):
        if gray_img[i, j] < r_avg:
            thresh_img[i, j] = 0
        else:
            thresh_img[i, j] = 255


for i in range(gray_img.shape[0]):
    for j in range(gray_img.shape[1]):
        print(thresh_img[i, j])

cv2.imshow('origin image', imutils.resize(image, 600))
cv2.imshow('thresh image', imutils.resize(thresh_img, 600))
if cv2.waitKey(0) == 27:
    cv2.destroyAllWindows()