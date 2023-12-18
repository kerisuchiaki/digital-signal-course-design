from PIL import Image
import cv2
import numpy as np

# 打开PIL Image
pil_image = Image.open("../image/miku.jpg")

# 转换为NumPy数组
numpy_image = np.array(pil_image)

# 转换为OpenCV Image
opencv_image = cv2.cvtColor(numpy_image, cv2.COLOR_RGB2BGR)
cv2.imshow("opencv", opencv_image)
cv2.waitKey(0)
