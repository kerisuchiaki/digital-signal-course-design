import PIL.Image
import scipy.misc

if _name_ == 'main':
    im = scipy.misc.imread('/image/shuiyin.jpg', mode='RGBA')
    im_water = scipy.misc.imread('./image/miku.jpg', mode='RGBA')

for x in range(im_water.shape[0]):
    for y in range(im_water.shape[1]):
        a = 0.3 * im_water[x][y][-1] / 255
        im[x][y][0:3] = (1 - a) * im[x][y][0:3] + a * im_water[x][y][0:3]

PIL.Image.fromarray(im).show()
