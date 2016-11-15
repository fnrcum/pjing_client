# encoding: cp1252
import pygame, os
from PIL import Image, ImageTk
import pyautogui
import tkFileDialog
from Tkinter import Tk, Label, Button, LEFT


class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("pJing")
        master.iconbitmap(r'icon.ico')

        pilImage = Image.open('out.png')
        image = ImageTk.PhotoImage(pilImage)

        label = Label(image=image)
        label.image = image  # keep a reference!
        label.pack()

        self.greet_button = Button(master, text="Upload", command=self.upload)
        self.greet_button.pack(side=LEFT)

        self.greet_button = Button(master, text="Save", command=self.save)
        self.greet_button.pack(side=LEFT)

        self.close_button = Button(master, text="Quit", command=self.quit)
        self.close_button.pack(side=LEFT)

    def upload(self):
        print("Not Supported yet!")

    def save(self):
        path = tkFileDialog.asksaveasfilename(defaultextension=".png")
        im.save(path)
        os.remove('out.png')

    def quit(self):
        os.remove('out.png')
        self.master.quit()

pygame.init()


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
    pygame.font.SysFont("Arial", 16)
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