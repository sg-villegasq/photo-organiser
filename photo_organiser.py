from tkinter import *
from tkinter import ttk

from gallery import Gallery
from options import Options


class PhotoOrganiser(object):
    def __init__(self, root: Tk) -> None:
        root.title("Photo Organiser")

        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        Gallery(mainframe)

        Options(mainframe, 7)
