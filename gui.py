import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


class ImageProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("图像处理程序")

        self.load_button = tk.Button(self.root, text="加载图片", command=self.load_image)
        self.load_button.pack()

        self.canvas = tk.Canvas(self.root, width=400, height=400)
        self.canvas.pack()

        self.process_button = tk.Button(self.root, text="处理图片", command=self.process_image)
        self.process_button.pack()

    def load_image(self):
        file_path = filedialog.askopenfilename()
        self.image = Image.open(file_path)
        self.display_image()

    def process_image(self):
        if hasattr(self, 'image'):
            # Example: Cropping (crop the image to a square)
            width, height = self.image.size
            min_dim = min(width, height)
            cropped_image = self.image.crop((0, 0, min_dim, min_dim))

            # Example: Adjusting brightness
            brightness_factor = 1.5
            brightness_adjusted = cropped_image.point(lambda p: p * brightness_factor)

            # Example: Adjusting contrast
            contrast_factor = 1.5
            contrast_adjusted = brightness_adjusted.point(lambda p: (p - 128) * contrast_factor + 128)

            # Display the processed image
            self.image = contrast_adjusted
            self.display_image()

    def display_image(self):
        # Resize image to fit in the canvas
        resized_image = self.image.resize((400, 400), Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(resized_image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)


if __name__ == "__main__":
    root = tk.Tk()
    app = ImageProcessorApp(root)
    root.mainloop()
