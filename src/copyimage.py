from PIL import Image
import numpy as np

img = Image.open("../image/red_color.png")
# img.show()
img_array = np.array(img)  # 把图像转成数组格式img = np.asarray(image)
shape = img_array.shape
print(img_array.shape)
for i in range(0, shape[0]):
    for j in range(0, shape[1]):
        value = img_array[i, j]
        # print("",value)
        if value[0] != 0:
            print("", value)
height = shape[0]
width = shape[1]
dst = np.zeros((height, width, 3))
for h in range(0, height):
    for w in range(0, width):
        print(h, w)
        (b, g, r) = img_array[h, w]
        print(b, g, r)
        (b,g,r)=(0,0,0)
        img_array[h,w]=(b,g,r)
        dst[h, w] = img_array[h, w]
img2 = Image.fromarray(np.uint8(dst))
img2.show(img2)
img2.save("3.png", "png")
