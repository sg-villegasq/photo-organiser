import tkinter as tk
from tkinter import ttk
from collections import namedtuple
import math


class Options(ttk.Frame):
    def __init__(self, window, parent, n):
        self.window = window
        self.parent = parent
        self.n_buttons = n

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

    def add_new_buttons(self):
        ButtonLocation = namedtuple('button', ['row', 'column'])
        last_button = ButtonLocation(
            math.ceil(self.n_buttons / 2), self.n_buttons % 2)
