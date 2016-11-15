# encoding: cp1252
import pygame, os
import pyautogui
from image_handler import ImageHandler
from Tkinter import Tk
from PIL import Image
from options_gui import OptionsGUI

pygame.init()


if __name__ == "__main__":
    im_handle = ImageHandler()
    pyautogui.screenshot('foo.png')
    input_loc = 'foo.png'
    output_loc = 'out.png'
    screen, px = im_handle.setup(input_loc)
    left, upper, right, lower = im_handle.mainLoop(screen, px)

    # ensure output rect always has positive width, height
    if right < left:
        left, right = right, left
    if lower < upper:
        lower, upper = upper, lower
    im = Image.open(input_loc)
    im = im.crop((left, upper, right, lower))
    pygame.display.quit()
    im.save(output_loc)
    os.remove(input_loc)

    # File options
    root = Tk()
    my_gui = OptionsGUI(root, im)
    root.mainloop()