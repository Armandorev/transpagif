import glob
import sys
from PIL import Image


path = str(sys.argv[1])
print("going to make transparent the gifs under: %s" % path )

folders = [f for f in glob.glob(path + '/**/*.gif',  recursive=True)]

for f in folders:
    im = Image.open(f)
    rgb_image = im.convert('RGB')
    r, g, b = rgb_image.getpixel((1, 1))
    print(r, g, b)