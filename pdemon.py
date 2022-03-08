from turtle import width
import PIL.Image
import PIL.ImageTk
import tkinter as tk
from tkinter import *


class Edit:
    # Generate 5 most common colors in the image
    @staticmethod
    def findColorPalette(num, image):
        from collections import defaultdict
        pallete = defaultdict(int)
        for pixel in image.getdata():
            pallete[pixel] += 1
        pallete = sorted(pallete, key=pallete.get, reverse=True)[:num]
        print(pallete)

        return(pallete)
