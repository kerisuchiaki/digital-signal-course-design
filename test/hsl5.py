from PIL import Image, ImageTk
import colorsys
import tkinter as tk


class ImageEditor:
    def __init__(self, image_path):
        self.root = tk.Tk()
        self.root.title("Image Editor")

        self.image = Image.open(image_path).convert("RGB")
        self.edited_image = self.image.copy()

        self.hue_scale = tk.Scale(self.root, from_=0.0, to=1.0, resolution=0.01, orient="horizontal", )
        self.hue_scale.set(0.5)
        self.hue_scale.pack()

        self.saturation_scale = tk.Scale(self.root, from_=0.0, to=1.0, resolution=0.01, orient="horizontal", )
        self.saturation_scale.set(0.8)
        self.saturation_scale.pack()

        self.lightness_scale = tk.Scale(self.root, from_=0.0, to=10.0, resolution=0.01, orient="horizontal", )
        self.lightness_scale.set(1.2)
        self.lightness_scale.pack()

        self.image_label = tk.Label(self.root)
        self.image_label.pack()

        self.hue_scale.bind("<ButtonRelease>", self.update_image)
        self.saturation_scale.bind("<ButtonRelease>", self.update_image)
        self.lightness_scale.bind("<ButtonRelease>", self.update_image)

        self.update_image()

    def update_image(self, event=None):
        hue_shift = self.hue_scale.get()
        saturation_scale = self.saturation_scale.get()
        lightness_scale = self.lightness_scale.get()

        edited_image = self.image.copy()
        pixels = edited_image.load()

        width, height = edited_image.size
        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]
                h, l, s = colorsys.rgb_to_hls(r / 255.0, g / 255.0, b / 255.0)

                # Adjust HSL values
                h = (h + hue_shift) % 1.0
                s = max(0, min(1, s * saturation_scale))
                l = max(0, min(1, l * lightness_scale))

                r, g, b = colorsys.hls_to_rgb(h, l, s)
                pixels[x, y] = (int(r * 255), int(g * 255), int(b * 255))

        self.edited_image = edited_image

        photo = ImageTk.PhotoImage(edited_image)
        self.image_label.configure(image=photo)
        self.image_label.image = photo

    def run(self):
        self.root.mainloop()


image_editor = ImageEditor("../image/miku.jpg")
image_editor.run()