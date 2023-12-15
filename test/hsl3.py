import numpy as np
from PIL import Image
from scipy.optimize import differential_evolution

def rgb_difference(image_rgb, target_rgb):
    return np.sum((image_rgb - target_rgb) ** 2)

def adjust_rgb(image_path, target_rgb):
    image = Image.open(image_path)
    width, height = image.size
    image_rgb = np.array(image).reshape(-1, 3)

    def objective(rgb):
        return rgb_difference(image_rgb, target_rgb * 255)

    bounds = [(0, 1), (0, 1), (0, 1)]
    result = differential_evolution(objective, bounds, tol=1e-3)

    adjusted_image = Image.new("RGB", (width, height))
    adjusted_rgb = np.clip(result.x * 255, 0, 255).astype(int)

    adjusted_image.putdata(list(map(tuple, adjusted_rgb.reshape(-1, 3))))
    adjusted_image.save("adjusted_image.jpg")

# 调整图像到 RGB(51, 204, 255)
adjust_rgb("../image/red.png", np.array([51, 204, 255]) / 255)