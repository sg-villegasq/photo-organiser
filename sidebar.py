import tkinter as tk
from tkinter import ttk

from options import Options


class Sidebar(object):

    def __init__(self, parent, options):
        self.options = options

        mainframe = ttk.Frame(parent, padding='3 3 12 12')
        mainframe.grid(column=0, row=2, rowspan=2)

        ttk.Button(mainframe, text='add folder',
                   command=self.options.add_new_buttons).grid(column=0, row=1)
