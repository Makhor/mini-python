import sys, os
from PIL import Image

#   Spritesheet/Tilesheet builder
#   Uses: Python 3.6
#   Made by: Jorge Sánchez (@jorge_makhor)
#   Description: Takes a bunch of pictures of the same size and bundles them up into a single spritesheet image.
#   ALL THE PICTURES THAT YOU PASS IN NEED TO BE THE SAME SIZE

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
            line2 = input("input the name of the final file (without the extension):")
            file_name = line2
            break
        else:
            line = input("input the output directory:")
            root = line
            line2 = input("input the name of the final file (without the extension):")
            file_name = line2

            break

    if os.path.exists(root):
        options()
        return
    else:
        print("ERROR: bad output directory.")
        return


def options():
    global width
    global height
    global frames
    global rows
    global im_frame

    while True:
        width = input("input the width of the frames (px):")
        height = input("input the height of the frames (px):")
        frames = input("input the amount of frames (horizontal) :")
        rows = input("input the amount of rows (vertical) :")

        if frames.isnumeric() and rows.isnumeric() and width.isnumeric() and height.isnumeric():
            break
        else:
            print("ERROR: all values must be numbers!")

    width = int(width)
    height = int(height)
    frames = int(frames)
    rows = int(rows)
    final_size = (width * frames, height * rows)
    im_frame = Image.new("RGBA", final_size)
    setup()
    return


def setup():
    x = 0
    y = 0
    new_frames = max(0, frames)
    new_rows = max(0, rows)
    com = ""
    new_im = 0
    dire = ""
    region = 0
    root_dir = ""
    has_root_dir = False
    global im_frame

    option = input("type 'S' if all your image files are in the same folder, else, don't type anything and press Enter: ")

    if option.lower() == "s":
        has_root_dir = True
        while True:
            root_dir = input("input the directory where your image files are located: ")

            if os.path.exists(root_dir):
                break
            else:
                print("ERROR: invalid directory!")


    for x in range(new_frames):
        for y in range(new_rows):
            print("frame: %s, row: %s" % (x,y))
            com = input("input 'S' to skip this frame, else, press enter to continue: ")

            if com.lower() != "s":

                if has_root_dir == False:
                    dire = input("Input image directory (with file name): ")
                else:
                    dire = input("Input the name of your file in the directory you entered (with file extension): ")

                try:
                    if has_root_dir == False:
                        new_im = Image.open(dire)
                    else:
                        new_im = Image.open(root_dir + "/" + dire)
                    if new_im.size == (width, height):
                        region = (x * width, y * height, x * width + width, y * height + height)
                        im_frame.paste(new_im, region)
                        new_im.close()
                    else:
                        print("ERROR: wrong image size!")
                        new_im.close()
                except IOError:
                    print("ERROR: invalid directory!")
    save()
    return


def save():
    im_frame.save(root + "/" + file_name + ".png", "PNG")
    im_frame.close()
    print("saved!")
    return


main()
