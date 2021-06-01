from tkinter import *
from tkinter import ttk


class PhotoOrganiser(object):
    def __init__(self, root: Tk) -> None:
        root.title("Photo Organiser")

        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        ttk.Button(mainframe, text="Test button").grid(column=1, row=2, sticky=E)
