import cv2 as cv
import matplotlib.pyplot as plt

# 1.以灰度图的形式读取图片
img = cv.imread("./image/miku.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# 2.实例化OpenCV人脸和眼睛识别的分类器
face_cas = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
face_cas.load('haarcascade_frontalface_default.xml')

eyes_cas = cv.CascadeClassifier("haarcascade_eye.xml")
eyes_cas.load("haarcascade_eye.xml")

# 3.调用识别人脸
faceRects = face_cas.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=3, minSize=(32, 32))
for faceRect in faceRects:
    x, y, w, h = faceRect
    # 框出人脸
    cv.rectangle(img, (x, y), (x + h, y + w), (0, 255, 0), 3)
    # 4.在识别出的人脸中进行眼睛的检测
    roi_color = img[y:y + h, x:x + w]
    roi_gray = gray[y:y + h, x:x + w]
    eyes = eyes_cas.detectMultiScale(roi_gray)
    for (ex, ey, ew, eh) in eyes:
        cv.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
# 5. 检测结果的绘制
plt.figure(figsize=(8, 6), dpi=100)
plt.imshow(img[:, :, ::-1]), plt.title('检测结果')
plt.xticks([]), plt.yticks([])
plt.show()
