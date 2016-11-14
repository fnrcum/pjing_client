# encoding: cp1252
import pygame, sys, os
from PIL import Image
import pygbutton
import pyautogui
from tkinter import Tk, Label, Button, LEFT, RIGHT


class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("pJing")

        self.label = Label(master, text="This is our first GUI!")
        self.label.pack()

        self.greet_button = Button(master, text="Upload", command=self.upload)
        self.greet_button.pack(side=LEFT)

        self.greet_button = Button(master, text="Remove", command=self.remove)
        self.greet_button.pack(side=LEFT)

        self.close_button = Button(master, text="Quit", command=master.quit)
        self.close_button.pack(side=RIGHT)

    def upload(self):
        print("Not Supported yet!")

    def remove(self):
        os.remove('out.png')

pygame.init()

buttonObj = pygbutton.PygButton((50, 50, 60, 30), 'Button Caption')


def displayImage(screen, px, topleft, prior):
    # ensure that the rect always has positive width, height
    x, y = topleft
    width =  pygame.mouse.get_pos()[0] - topleft[0]
    height = pygame.mouse.get_pos()[1] - topleft[1]
    if width < 0:
        x += width
        width = abs(width)
    if height < 0:
        y += height
        height = abs(height)

    # eliminate redundant drawing cycles (when mouse isn't moving)
    current = x, y, width, height
    if not (width and height):
        return current
    if current == prior:
        return current

    # draw transparent box and blit it onto canvas
    screen.blit(px, px.get_rect())
    im = pygame.Surface((width, height))
    im.fill((128, 128, 128))
    pygame.draw.rect(im, (32, 32, 32), im.get_rect(), 1)
    im.set_alpha(128)
    screen.blit(im, (x, y))
    pygame.display.flip()

    # return current box extents
    return x, y, width, height


def setup(path):
    px = pygame.image.load(path)
    rect = px.get_rect()
    wg = rect[2]
    hg = rect[3]
    screen = pygame.display.set_mode([wg, hg], pygame.FULLSCREEN)
    screen.blit(px, px.get_rect())
    pygame.display.flip()
    return screen, px


def mainLoop(screen, px):
    topleft = bottomright = prior = None
    end = False
    while not end:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                if not topleft:
                    topleft = event.pos
                else:
                    bottomright = event.pos
                    end = True
        if topleft:
            prior = displayImage(screen, px, topleft, prior)
    return topleft + bottomright

if __name__ == "__main__":
    pyautogui.screenshot('foo.png')
    input_loc = 'foo.png'
    output_loc = 'out.png'
    screen, px = setup(input_loc)
    left, upper, right, lower = mainLoop(screen, px)

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
    my_gui = MyFirstGUI(root)
    root.mainloop()