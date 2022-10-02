import os
import tkinter as tk
import lib.global_variable as glv
from components import view


class App(tk.Tk):
    """!
    Application Class
    """

    def __init__(self):
        """!
        Constructor
        
        It initializes the main app with new global variables.
        It displays the MainPage and toggles the loop.
        """
        glv.init_global_variable()
        glv.set_variable("PATH", os.path.dirname(__file__))
        glv.set_variable("STATE", False)
        glv.set_variable("DISPLAY", "Gantt")

        tk.Tk.__init__(self)

        view.MainPage(self)

        self.mainloop()


if __name__ == "__main__":
    App()
