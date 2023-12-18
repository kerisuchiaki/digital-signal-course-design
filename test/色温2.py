import cv2
import numpy as np

image = cv2.imread("../image/sakura.jpg")
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# 色调调整
hsv_image[:, :, 0] = (hsv_image[:, :, 0] - 10) % 180

# 色温调整
hsv_image[:, :, 1] = np.clip(hsv_image[:, :, 1] * 0.7, 0, 255)
hsv_image[:, :, 2] = np.clip(hsv_image[:, :, 2] * 0.7, 0, 255)

output_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)
cv2.imshow("tar",output_image)
cv2.waitKey(0)
cv2.imwrite("output.jpg", output_image)