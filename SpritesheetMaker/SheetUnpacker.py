import sys, os
from PIL import Image

#   Spritesheet/Tilesheet unpacker
#   Uses: Python 3.6
#   Made by: Jorge Sánchez (@jorge_makhor)
#   Description: Takes a bunch of spritesheet and saves all the frames as individual files
#   (This is supposed to go hand in hand with the spritesheetMaker)

#   Dependencies: Pillow (pip install Pillow)


frames = 0
rows = 0
width = 0
height = 0
im_frame = 0
root = ""
file_name = ""


def main():
    global im_frame
    global root
    global file_name

    print("Tip: whenever you're asked to enter/input a value, type it and press enter to continue")

    while True:
        if len(sys.argv) > 1:
            root = sys.argv[1:1]
            line2 = input("input the name of the tile sheet (with extension):")
            file_name = line2
        else:
            line = input("input the output directory:")
            root = line
            line2 = input("input the name of the tile sheet (with extension): ")
            file_name = line2

        try:
            im_frame = Image.open(root + "/" + file_name)
            options()
            break
        except IOError:
            print("ERROR: invalid file name or directory, input again.")


def options():
    global width
    global height
    global frames
    global rows
    global im_frame

    size = im_frame.size

    width = input("input the width of the frames (px):")
    height = input("input the height of the frames (px):")

    frames = int(size[0] / int(width))
    rows = int(size[1] / int(height))

    width = int(width)
    height = int(height)
    setup()
    return


def setup():
    x = 0
    y = 0
    new_frames = max(0, frames)
    new_rows = max(0, rows)
    new_im = 0
    region = 0
    str = ""
    name = file_name
    global im_frame

    if name.endswith(".png") or name.endswith(".jpg"):
        name =  name[:-4]



    for x in range(new_frames):
        for y in range(new_rows):
            print("frame: %s, row: %s" % (x,y))
            region = (x * width, y * height, x * width + width, y * height + height)
            new_im = im_frame.crop(region)
            str = "%s_%s" % (x,y)
            new_im.save(root + "/" + name + str + ".png", "PNG")
            new_im.close()

    return


main()