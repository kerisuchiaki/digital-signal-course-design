import cv2
import numpy as np

# 读取图像
image = cv2.imread('input_image.jpg')

# 构图（裁剪）
crop_start_x, crop_start_y, crop_end_x, crop_end_y = 100, 100, 300, 300
cropped_image = image[crop_start_y:crop_end_y, crop_start_x:crop_end_x]

# 旋转
angle = 45
rows, cols = image.shape[:2]
rotation_matrix = cv2.getRotationMatrix2D((cols / 2, rows / 2), angle, 1)
rotated_image = cv2.warpAffine(image, rotation_matrix, (cols, rows))

# 光感
gamma = 1.5
gamma_corrected = np.power(image / 255.0, gamma) * 255.0
gamma_corrected = np.clip(gamma_corrected, 0, 255).astype(np.uint8)

# 亮度
brightness_factor = 1.5
brightness_adjusted = cv2.convertScaleAbs(image, alpha=brightness_factor, beta=0)

# 曝光
exposure_factor = 2.0
exposure_adjusted = np.clip(image * exposure_factor, 0, 255).astype(np.uint8)

# 对比度
contrast_factor = 1.5
contrast_adjusted = cv2.convertScaleAbs(image, alpha=contrast_factor, beta=0)

# 曲线调整、直方图均衡化、饱和度调整等功能可以根据具体需求使用OpenCV或其他图像处理库的相关函数进行实现。

# 选项模块
option_module = "beauty_filter"  # 可选项： "defog", "watermark", "beauty_filter"

if option_module == "defog":
    # 图像去雾功能
    defogged_image = cv2.ximgproc.createFastLineDetector().detect(image)
    # 实现去雾功能的具体代码

elif option_module == "watermark":
    # 为修图后的图像添加水印
    watermark = cv2.putText(image, 'Watermark', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
    # 实现添加水印的具体代码

elif option_module == "beauty_filter":
    # 人脸检测（使用OpenCV的人脸检测器）
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # 美颜滤镜（假设美颜滤镜效果是通过图像模糊实现的）
    for (x, y, w, h) in faces:
        face_roi = image[y:y+h, x:x+w]
        blurred_face = cv2.GaussianBlur(face_roi, (25, 25), 0)
        image[y:y+h, x:x+w] = blurred_face

# 显示结果
cv2.imshow('Original Image', image)
cv2.imshow('Cropped Image', cropped_image)
cv2.imshow('Rotated Image', rotated_image)
cv2.imshow('Gamma Corrected Image', gamma_corrected)
cv2.imshow('Brightness Adjusted Image', brightness_adjusted)
cv2.imshow('Exposure Adjusted Image', exposure_adjusted)
cv2.imshow('Contrast Adjusted Image', contrast_adjusted)

if option_module == "defog":
    cv2.imshow('Defogged Image', defogged_image)
elif option_module == "watermark":
    cv2.imshow('Watermarked Image', watermark)
elif option_module == "beauty_filter":
    cv2.imshow('Beauty Filtered Image', image)

cv2.waitKey(0)
cv2.destroyAllWindows()
