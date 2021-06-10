import tkinter as tk
from tkinter import ttk


class Options(object):
    def __init__(self, parent, n):

        mainframe = ttk.Frame(parent, padding="3 3 12 12")
        mainframe.grid(column=1, row=3)

        self.add_option_buttons(mainframe, n)

    def add_option_buttons(self, mainframe, n):
        i = 0
        r = 1

        # TODO: refactor this omg it looks awful
        while i < n:
            c = 1
            while c <= 2 and i < n:
                ttk.Button(mainframe, text=f"option{i}").grid(column=c, row=r)
                c += 1
                i += 1
            r += 1
