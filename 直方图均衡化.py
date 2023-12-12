import cv2
import matplotlib.pyplot as plt

# 读取图像
image_path = "./image/img2.jpg"
im_mat = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# 进行直方图均衡化
equ = cv2.equalizeHist(im_mat)

# 绘制原始图像和直方图均衡化后的图像
plt.subplot(2, 1, 1)
plt.imshow(im_mat, cmap='gray')
plt.title('Original Image')

plt.subplot(2, 1, 2)
plt.imshow(equ, cmap='gray')
plt.title('Equalized Image')

# 绘制直方图
plt.figure()
plt.hist(im_mat.reshape([im_mat.size]), bins=256, density=True, color='blue', alpha=0.7, label='Original Image')
plt.hist(equ.reshape([equ.size]), bins=256, density=True, color='red', alpha=0.7, label='Equalized Image')
plt.title('Histogram')
plt.legend()

# 显示图像和直方图
plt.show()
