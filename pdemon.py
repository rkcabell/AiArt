from turtle import width
import PIL.Image
import PIL.ImageTk
import tkinter as tk
from tkinter import *
from collections import defaultdict


class Edit:
    # Generate 1-X most common colors in the image\
    # Todo: decide on range of labels
    @staticmethod
    def findColorPalette(self, num, image):
        # using recursion to bug-check
        # Pros: looks cool, Cons: impacts performance
        if (num < 1):
            self.findColorPalette(num+1, image)
            return

        pallete = defaultdict(int)
        for pixel in image.getdata():
            pallete[pixel] += 1
        pallete = sorted(pallete, key=pallete.get, reverse=True)[:num]
        print(pallete)

        return(pallete)
