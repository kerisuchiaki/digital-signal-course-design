from tkinter import Tk, Canvas
from PIL import ImageTk, Image

class MyApp:
    def __init__(self):
        self.root = Tk()
        self.canvas = Canvas(self.root, width=960, height=960)
        self.canvas.pack()
        self.canvas.bind("<ButtonRelease-1>", self.on_mouse_release)
        self.image = Image.open("../image/miku.jpg")
        self.photo = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, anchor="nw", image=self.photo)
        self.start_x = None
        self.start_y = None

    def on_mouse_release(self, event):
        if self.start_x is not None and self.start_y is not None:
            self.crop(event.x, event.y)

    def crop(self, end_x, end_y):
        cropped_image = self.image.crop((self.start_x, self.start_y, end_x, end_y))
        cropped_photo = ImageTk.PhotoImage(cropped_image)
        self.canvas.create_image(0, 0, anchor="nw", image=cropped_photo)
        self.canvas.image = cropped_photo  # 保持对图片的引用

    def run(self):
        self.root.mainloop()

app = MyApp()
app.run()