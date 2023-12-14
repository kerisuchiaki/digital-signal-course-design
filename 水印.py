from PIL import Image, ImageFilter


def add_visible_watermark(background_path, watermark_path, output_path, alpha=0.9):
    # 打开背景图和水印图
    background = Image.open(background_path).convert('RGBA')
    watermark = Image.open(watermark_path).convert('RGBA')

    # 调整水印大小以适应背景图
    watermark = watermark.resize(background.size, Image.LANCZOS)

    # 将水印叠加到背景图上
    result = Image.blend(background, watermark, alpha)

    # 保存结果
    result.save(output_path, format='PNG')


# 使用示例
background_image_path = './image/img2.jpg'
watermark_image_path = './image/miku.jpg'
output_image_path = 'C:/Users/minamichiaki/Desktop/output.png'

add_visible_watermark(background_image_path, watermark_image_path, output_image_path)
