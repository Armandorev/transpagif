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
    r_pixelMask, g_pixelMask, b_pixelMask, a_pixelMask  = rgb_image.getpixel((0, 0))
    r_transparent, g_transparent, b_transparent, a_transparent  = r_pixelMask, g_pixelMask, b_pixelMask, 0
    data = np.array(rgb_image)

    red, green, blue, alpha = data[:,:,0], data[:,:,1], data[:,:,2], data[:,:,3]
    mask = (red == r_pixelMask) & (green == g_pixelMask) & (blue == b_pixelMask)

    data[:,:,:4][mask] = [r_transparent, g_transparent, b_transparent, a_transparent]

    image_transparent = Image.fromarray(data)

    # mask = data[:,:,:,0] = 0
    coords = np.argwhere(mask)
    x0, y0 = coords.min(axis=0)
    x1, y1 = coords.max(axis=0) + 1
    cropped = data[x0:x1, y0:y1]

    image_transparent_cropped = Image.fromarray(data)

    print("Creating new transparent image: %s " % f.replace('.gif','.png') )
    image_transparent_cropped.save(f.replace('.gif','.png'), "PNG")