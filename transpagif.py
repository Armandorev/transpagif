import glob
import sys
from PIL import Image
import numpy as np


path = str(sys.argv[1])
print("going to make transparent the gifs under: %s" % path )

folders = [f for f in glob.glob(path + '/**/*.gif',  recursive=True)]

for f in folders:
    im = Image.open(f)
    rgb_image = im.convert('RGBA')
    r_pixelMask, g_pixelMask, b_pixelMask, a_pixelMask  = rgb_image.getpixel((1, 1))
    r_transparent, g_transparent, b_transparent, a_transparent  = r_pixelMask, g_pixelMask, b_pixelMask, 0
    data = np.array(rgb_image)

    red, green, blue, alpha = data[:,:,0], data[:,:,1], data[:,:,2], data[:,:,3]
    mask = (red == r_pixelMask) & (green == g_pixelMask) & (blue == b_pixelMask)

    data[:,:,:4][mask] = [r_transparent, g_transparent, b_transparent, a_transparent]

    image_transparent = Image.fromarray(data)
    print("preparing data for image %s " % f.replace('.gif','.png') )
    image_transparent.save(f.replace('.gif','.png'), "PNG")