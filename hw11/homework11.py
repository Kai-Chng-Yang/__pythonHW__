import tkinter as tk
from tkinter import Button,Frame

class Window(tk.Tk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

top_frame = Frame(self, bg='#ffffff')


mid_frame = Frame(self, bg='#ffffff')


buttom_frame = Frame(self, bg='#ffffff')