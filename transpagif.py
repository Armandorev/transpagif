import glob
import sys
from PIL import Image
import numpy


path = str(sys.argv[1])
print("going to make transparent the gifs under: %s" % path )

folders = [f for f in glob.glob(path + '/**/*.gif',  recursive=True)]

for f in folders:
    im = Image.open(f)
    rgb_image = im.convert('RGBA')
    data = numpy.array(rgb_image)
    red, green, blue, alpha = data.T
    r, g, b = rgb_image.getpixel((1, 1))
    background_areas = (red == r) & (green == g) & (blue == b)
    data[..., :-1][background_areas.T] = (r, g, b, 0)
    image_transparent = Image.fromarray(data)
    print(r,g, b, a , "preparing data for image %s " % f.replace('.gif','.png') )
    # image_transparent.save(f.replace('.gif','.png'), "PNG")