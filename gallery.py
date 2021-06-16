import tkinter as tk
from tkinter import ttk


class Gallery(ttk.Frame):
    def __init__(self, window, parent):
        super().__init__()
        self.window = window
        self.parent = parent

        mainframe = ttk.Frame(parent, padding="3 3 12 12")
        mainframe.grid(column=1, row=2)

        # place for the photos
        ttk.Frame(mainframe, height=240, width=240, relief="groove").grid(
            column=2, row=1, rowspan=3
        )

        # next and previous buttons
        ttk.Button(mainframe, text="<<").grid(column=1, row=2, sticky=tk.E)
        ttk.Button(mainframe, text=">>").grid(column=3, row=2, sticky=tk.W)
