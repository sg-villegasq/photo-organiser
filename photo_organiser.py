import tkinter as tk
from tkinter import ttk

from gallery import Gallery
from options import Options
from sidebar import Sidebar


class PhotoOrganiser(tk.Tk):
    def __init__(self, root: tk.Tk) -> None:
        super().__init__()
        self.root = root
        root.title("Photo Organiser")

        mainframe = ttk.Frame(root, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        ttk.Label(mainframe, text='<title>').grid(column=1, row=1)

        Gallery(root, mainframe)

        op = Options(root, mainframe, 7)

        Sidebar(root, mainframe, op)
