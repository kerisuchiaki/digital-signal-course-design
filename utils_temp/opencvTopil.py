from PIL import Image
import cv2
import numpy as np

# 打开OpenCV Image
opencv_image = cv2.imread("../image/miku.jpg")

# 转换为RGB模式
opencv_image_rgb = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2RGB)

# 转换为PIL Image
pil_image = Image.fromarray(opencv_image_rgb)
