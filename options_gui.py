import tkFileDialog, tkMessageBox
import os
from PIL import Image, ImageTk
from Tkinter import Label, Button, LEFT


class OptionsGUI:
    def __init__(self, master, im):
        self.master = master
        self.im = im
        master.title("pJing")
        master.iconbitmap(default=r'images\icon.ico')
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

        self.center(self.master)

    def center(self, win):
        win.update_idletasks()
        width = win.winfo_width()
        height = win.winfo_height()
        x = (win.winfo_screenwidth() // 2) - (width // 2)
        y = (win.winfo_screenheight() // 2) - (height // 2)
        win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    def upload(self):
        tkMessageBox.showerror("Error", "File uploads are not supported yet!")

    def save(self):
        path = tkFileDialog.asksaveasfilename(defaultextension=".png")
        if path is not '':
            self.im.save(path)
        if os.path.isfile('out.png'):
            os.remove('out.png')

    def quit(self):
        if os.path.isfile('out.png'):
            os.remove('out.png')
        self.master.quit()
