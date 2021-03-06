from turtle import width
import PIL.Image
import PIL.ImageTk
import tkinter as tk
from tkinter import *
import pdemon as pd
from pdemon import *
from tkinter import filedialog as fd
from collections import defaultdict


class Frame:
    # class variables for the last image used
    filepath_image = "./res/car.jpg"
    filepath_bg = "./res/test.jpg"

    def __init__(self):
        # Create an instance of Tkinter frame
        self.root = Tk()
        self.root.title("Image app project")
        window_width = 1200
        window_height = 800
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)
        self.root.geometry(
            f'{window_width}x{window_height}+{center_x}+{center_y}')
        self.root.resizable(False, False)
        self.root.attributes('-topmost', 1)
        self.root.iconbitmap('./res/A_logo.ico')

        # Canvas dimensions
        CANVAS_X = 500
        CANVAS_Y = 500

        # Create a photoimage object of the image in the path
        self.image_bg = PIL.Image.open(self.filepath_bg)
        self.tk_image_bg = PIL.ImageTk.PhotoImage(self.image_bg)
        self.user_image = PIL.Image.open(self.filepath_image)
        self.tk_user_image = PIL.ImageTk.PhotoImage(self.user_image)

        # Position image on label
        self.image_bg_label = tk.Label(image=self.tk_image_bg)
        self.image_bg_label.place(x=0, y=0)

        # Center text label
        Label(self.root, text='AiArt', font=(
            'Helvetica', 18)).pack(side=TOP, padx=20, pady=30)

        ####################### Functionality buttons #######################
        # Refresh
        refreshBtn = tk.Button(self.root, text="Refresh",
                               command=self.refreshImage)

        # Open new picture
        chooseImageBtn = tk.Button(self.root, text="Browse...",
                                   command=self.chooseImage)

        # Remove picture
        removeImageBtn = tk.Button(
            self.root, text="Delete", command=self.removeImage)

        # Find color palette
        findPaletteBtn = tk.Button(self.root, text="Find color palette",
                                   command=self.findColorPalette)

        # Exit Program
        exitBtn = tk.Button(self.root, text="Exit Program",
                            command=self.root.quit)
        # Button Placements
        buttonList = []
        buttonList.append(refreshBtn)
        buttonList.append(chooseImageBtn)
        buttonList.append(removeImageBtn)
        buttonList.append(findPaletteBtn)
        buttonList.append(exitBtn)
        for i in range(len(buttonList)):
            buttonList[i].place(x=i*50, y=(i*50)+100)

        #refreshBtn.place(x=50, y=100)
        #chooseImageBtn.place(x=50, y=150)
        #removeImageBtn.place(x=50, y=200)
        #findPaletteBtn.place(x=50, y=250)
        #exitBtn.place(x=50, y=300)

        # Todo: undo FIFO

        # Todo: redo FIFO

        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#

        # Canvas with target image
        # Todo: image resize to canvas not working
        global user_canvas
        user_canvas = tk.Canvas(
            width=CANVAS_X, height=CANVAS_Y, background='gray85')
        self.image_bg = self.image_bg.resize(
            (CANVAS_X, CANVAS_Y), PIL.Image.ANTIALIAS)
        user_canvas.place(relx=0.5, rely=0.5, anchor=W)
        self.setNewImage()

    ####################### Button Command Methods #######################

    # Reset the image back to original
    def refreshImage(self):
        self.setNewImage()
        return 0

    # Choose a new image from computer
    def chooseImage(self):
        filetypes = (
            ('PNG files', '*.png'),
            ('JPG files', '*.jpg, *.jpeg'),
            ('All files', '*'))
        filename = fd.askopenfilename(
            title='Select an image',
            initialdir='./res',
            filetypes=filetypes)
        self.filepath_image = filename
        self.setNewImage()
        return 0

    # Clear Canvas
    def removeImage(self):
        user_canvas.delete("all")
        return 0

    # Place selected image in canvas
    def setNewImage(self):
        self.user_image = PIL.Image.open(self.filepath_image)
        self.tk_user_image = PIL.ImageTk.PhotoImage(self.user_image)
        user_canvas.create_image(self.image_bg.width/2, 0,
                                 image=self.tk_user_image, anchor="center")

    # Find top common colors and display them
    # on labels below the canvas
    # TODO: define range for NUM_COLORS
    def findColorPalette(self):
        # between 5 and X
        NUM_COLORS = 5
        labelList = []
        # Convert palette colors to hex values
        palette_rgb = pd.Edit().findColorPalette(self, NUM_COLORS, self.user_image)
        palette_hex = self.ConvertPaletteToHex(palette_rgb)
        # add labels to list then display
        print(palette_hex)
        for color in range(len(palette_hex)):
            labelList.append(
                tk.Label(self.root, height=7, width=5, padx=4, bg=palette_hex[color]))
        print(labelList)
        for i in range(len(labelList)):
            labelList[i].place(
                x=(i*50)+600,
                y=656)

    def rgbToHex(self, r, g, b):
        return ('{:X}{:X}{:X}').format(r, g, b)

    # Method to clean findColorPalette by reducing clutter
    # @palette : default dict where elements are int[2], and ints are 0-255
    # @palette : example element: [255, 255, 255]
    def ConvertPaletteToHex(self, palette):
        for i in range(len(palette)):
            palette[i] = "#" + ('{:X}{:X}{:X}').format(
                palette[i][0],
                palette[i][1],
                palette[i][2])
        return palette


#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#

    # Start method

    def main(self):
        self.root.mainloop()


# Run Program
if __name__ == "__main__":
    Frame().main()

######################### TEST CODE #########################
