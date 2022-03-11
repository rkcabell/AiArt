from turtle import width
import PIL.Image
import PIL.ImageTk
import tkinter as tk
from tkinter import *
import pdemon as pd
from pdemon import *
from tkinter import filedialog as fd


class Frame:
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
        filepath = "./res/test.jpg"
        self.image_bg = PIL.Image.open(filepath)
        self.tk_image_bg = PIL.ImageTk.PhotoImage(self.image_bg)
        filepath2 = "./res/car.jpg"
        self.user_image = PIL.Image.open(filepath2)
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
        refreshBtn.place(x=50, y=100)

        # Open new picture
        chooseImageBtn = tk.Button(self.root, text="Browse...",
                                   command=self.chooseImage)
        chooseImageBtn.place(x=50, y=150)

        # Remove picture
        # todo: add command to remove picture
        removeImageBtn = tk.Button(self.root, text="Delete",)
        removeImageBtn.place(x=50, y=200)

        # Find color palette
        findPaletteBtn = tk.Button(self.root, text="Find color palette", command=lambda: pd.Edit(
        ).findColorPalette(5, self.user_image))
        findPaletteBtn.place(x=50, y=250)

        # Exit Program
        exitBtn = tk.Button(self.root, text="Exit Program",
                            command=self.root.quit)
        exitBtn.place(x=50, y=300)

        #^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#

        # Canvas with target image
        global user_canvas
        user_canvas = tk.Canvas(
            width=CANVAS_X, height=CANVAS_Y, background='gray85')
        self.image_bg = self.image_bg.resize(
            (CANVAS_X, CANVAS_Y), PIL.Image.ANTIALIAS)
        user_canvas.place(relx=0.5, rely=0.5, anchor=W)
        user_canvas.create_image(self.image_bg.width/2, 0,
                                 image=self.tk_user_image, anchor="center")

    ####################### Button Command Methods #######################

    # Reset the image back to original
    # Todo: relaod image from filepath
    def refreshImage(self):
        return 0
        img2 = tk.PhotoImage(PIL.Image.open("./res/test.jpg"))
        # ERROR __str__ returned non-string (type JpegImageFile)
        self.label1.configure(image=img2)
        #self.label1.image = img2
        self.label1.update()

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
        print(filename)
        self.user_image = PIL.Image.open(filename)
        self.tk_user_image = PIL.ImageTk.PhotoImage(self.user_image)
        user_canvas.create_image(self.image_bg.width/2, 0,
                                 image=self.tk_user_image, anchor="center")
        return 0

#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#

    # Start method
    def main(self):
        self.root.mainloop()


# Run Program
if __name__ == "__main__":
    Frame().main()

######################### TEST CODE #########################
    # create image holder inside Tkinter frame
    # anchor=N      : locks to top of image
    # image.width/2 : probably good to get image in view on canvas
 #   canvas = tk.Canvas(width=500, height=500, background='gray85')
 #   canvas.pack(side="right", fill="none", expand=TRUE)
 #   canvas.create_image(image.width/2, 0, image=tk_image, anchor=N)

 #   user_canvas = tk.Canvas(width=500, height=500, background='gray85')
 #   user_canvas.place(relx=0.5, rely=0.5, anchor=W)
 #   user_canvas.create_image(image.width/2, 0, image=tk_image2, anchor="center")
