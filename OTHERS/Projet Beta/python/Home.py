import tkinter as tk
from Tasks import Tasks


class Home(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.frame = tk.Frame(self, background="red")

        Tasks(self, controller.data)

        self.frame.pack(fill=tk.BOTH, expand=False, side=tk.LEFT)
