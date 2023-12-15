from tkinter import *
from time import *
import tkinter.filedialog
import io
import cv2
from PIL import Image, ImageTk

root = Tk()
w_box = 1280
h_box = 640
root.title('RectOnPic Tool')
root.geometry('1280x640')
e = StringVar()
# print(e)
e_entry = Entry(root, textvariable=e)
e_entry.grid(row=6, column=1, padx=10, pady=5)
# print(e_entry.get())
# root.resizable(0,0)
Label1 = Label(root, text='X:').grid(row=0, column=0)
Label2 = Label(root, text='Y:').grid(row=1, column=0)
v1 = StringVar()
p1 = StringVar()
v1.set(0)
p1.set(0)
submit_button = Button(root, text="选择文件", command=root.quit)
Label3 = Label(root, text='W:').grid(row=3, column=0)
Label4 = Label(root, text='H').grid(row=4, column=0)
v2 = StringVar()
p2 = StringVar()
v2.set(0)
p2.set(0)
e1 = Entry(root, textvariable=v1)
e2 = Entry(root, textvariable=p1)
e1.grid(row=0, column=1, padx=10, pady=5)
e2.grid(row=1, column=1, padx=10, pady=5)
e3 = Entry(root, textvariable=v2)
e4 = Entry(root, textvariable=p2)
e3.grid(row=3, column=1, padx=10, pady=5)
e4.grid(row=4, column=1, padx=10, pady=5)
global imgGl
imgGl = Label(root, image=None)
imgGl.place(x=300, y=0)


def resize(w_box, h_box, pil_image):
    w, h = pil_image.size
    f1 = 1.0 * w_box / w
    f2 = 1.0 * h_box / h
    factor = min([f1, f2])
    width = int(w * factor)
    height = int(h * factor)
    return pil_image.resize((width, height), Image.ANTIALIAS)


def choose_file():
    selectFileName = tkinter.filedialog.askopenfilename(title='选择文件')
    # print(selectFileName)
    e.set(selectFileName)


def showImg(img1):
    imgGl.config(image='')
    load = Image.open(img1)
    pil_image_resized = resize(w_box, h_box, load)
    render = ImageTk.PhotoImage(pil_image_resized)
    imgGl.image = render
    imgGl.config(image=render)


def showImgAgain(img2):
    img = cv2.imread(img2)
    x = float(e1.get())
    y = float(e2.get())
    w = float(e3.get())
    h = float(e4.get())
    size = img.shape
    sz0 = size[0]
    sz1 = size[1]
    cv2.rectangle(img, (int(x * sz1), int(y * sz0)), (int((x + w) * sz1), int((y + h) * sz0)), (0, 255, 0), 4)
    cv2.imwrite('completed.jpg', img)
    showImg('completed.jpg')


Button(root, text='退出', width=10, command=root.quit) \
    .grid(row=9, column=0, sticky=W, padx=10, pady=5)
Button(root, text="选择文件", width=10, command=choose_file) \
    .grid(row=6, column=0, sticky=W, padx=10, pady=5)
Button(root, text="显示图片", width=10, command=lambda: showImg(e_entry.get())) \
    .grid(row=7, column=0, sticky=W, padx=10, pady=5)
Button(root, text="画坐标框", width=10, command=lambda: showImgAgain(e_entry.get())) \
    .grid(row=8, column=0, sticky=W, padx=10, pady=5)

mainloop()
