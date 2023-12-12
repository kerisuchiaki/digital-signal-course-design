import cv2
import numpy as np

img = cv2.imread("./image/miku.jpg")

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

theta = 45
curvature = theta / 180 * np.pi

x = np.zeros_like(img, dtype=np.float32)
y = np.zeros_like(img, dtype=np.float32)

for row in range(img.shape[0]):
    for col in range(img.shape[1]):
        x[row, col] = round(row * np.cos(curvature) - col * np.sin(curvature))
        y[row, col] = round(row * np.sin(curvature) + col * np.cos(curvature))

x = x - x.min()
y = y - y.min()

dst = np.zeros((int(y.max()) + 1, int(x.max()) + 1), dtype=np.uint8)
flag = np.zeros_like(dst, dtype=np.uint8)

for row in range(gray_img.shape[0]):
    for col in range(gray_img.shape[1]):
        i = int(x[row, col])
        j = int(y[row, col])

        dst[i, j] = gray_img[row, col]
        flag[i, j] = 1

for row in range(1, dst.shape[0] - 1):
    for col in range(1, dst.shape[1] - 1):
        if (flag[row, col - 1] == 1 and flag[row, col + 1] == 1 and
                flag[row - 1, col] == 1 and flag[row + 1, col] == 1 and
                flag[row, col] == 0):
            dst[row, col] = np.uint8((dst[row, col - 1] + dst[row, col + 1] +
                                      dst[row - 1, col] + dst[row + 1, col]) / 4)

cv2.imshow("input", gray_img)
cv2.imshow("output", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
