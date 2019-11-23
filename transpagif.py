import glob
import sys

path = str(sys.argv[1])
print("going to make transparent the gifs under: %s" % path )

folders = [f for f in glob.glob(path + '/**/*.gif',  recursive=True)]

for f in folders:
    print(f)