from tkinter import Tk, Scale, Label
from PIL import Image, ImageTk, ImageOps
import colorsys


class ImageEditor:
    def __init__(self, image_path):
        self.root = Tk()
        self.root.title("Image Editor")

        self.image = Image.open(image_path).convert("RGB")
        self.edited_image = self.image.copy()

        self.hue_scale = Scale(self.root, from_=0, to=360, orient="horizontal", command=self.update_image)
        self.hue_scale.set(0)
        self.hue_scale.pack()

        self.saturation_scale = Scale(self.root, from_=0, to=100, orient="horizontal", command=self.update_image)
        self.saturation_scale.set(100)
        self.saturation_scale.pack()

        self.lightness_scale = Scale(self.root, from_=0, to=100, orient="horizontal", command=self.update_image)
        self.lightness_scale.set(100)
        self.lightness_scale.pack()

        self.image_label = Label(self.root)
        self.image_label.pack()

        self.update_image()

    def update_image(self, event=None):
        hue = self.hue_scale.get()
        saturation = self.saturation_scale.get() / 100.0
        lightness = self.lightness_scale.get() / 100.0

        edited_image = self.image.copy()
        edited_pixels = []

        for x in range(edited_image.width):
            for y in range(edited_image.height):
                r, g, b = edited_image.getpixel((x, y))
                h, l, s = colorsys.rgb_to_hls(r / 255.0, g / 255.0, b / 255.0)
                h = hue / 360.0
                l = lightness
                s = saturation
                r, g, b = colorsys.hls_to_rgb(h, l, s)
                edited_pixels.append((int(r * 255), int(g * 255), int(b * 255)))

        edited_image.putdata(edited_pixels)

        self.edited_image = edited_image

        photo = ImageTk.PhotoImage(edited_image)
        self.image_label.configure(image=photo)
        self.image_label.image = photo

    def run(self):
        self.root.mainloop()


image_editor = ImageEditor("../image/miku.jpg")
image_editor.run()
