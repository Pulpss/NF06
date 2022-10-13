import tkinter as tk
from tkinter import ttk
import lib.global_variable as glv
from tkinter.filedialog import askopenfile

FILE_TYPES = [
    ("JPEG images", "*.jpg"),
    ("PNG images", "*.png"),
    ("All Files", "*.*"),
]

class Background(tk.Frame):
    """!
    This class is used to edit the Background of the diagram
    """
    def __init__(self, parent=None, controller=None):
        """!
        The constructor

        @param parent: The parent of the frame
        @param controller: The controller of the frame used to switch between frames
        """
        tk.Frame.__init__(self, parent)
        self.root = parent
        self.controller = controller
        self.background_image = tk.StringVar()
        self.init_page()

    def init_page(self):
        """!
        This method is used to initialize the page
        """
        def open_file():
            """!
            This method is used to open a file here it's an image
            """
            path = askopenfile(mode="r", filetypes=FILE_TYPES)
            if path:
                with open(path.name, "r", encoding="utf-8") as f:
                    self.background_image.set(path.name)
        self.page = tk.Frame(self)

        ttk.Label(
            self.page, text="Image path:"
        ).pack(anchor=tk.W, padx=5)

        self.entry_frame = tk.Frame(self.page)

        ttk.Button(
            self.entry_frame, text="Browse...", command=lambda: open_file()
        ).pack(anchor=tk.E, side=tk.RIGHT, pady=5)

        self.background_image.set(glv.get_variable("DATA")["background_image"])
        ttk.Entry(
            self.entry_frame, textvariable=self.background_image
        ).pack(anchor=tk.W, padx=5, pady=5)

        self.entry_frame.pack(anchor=tk.W, padx=5, pady=5, expand=True)

        ttk.Button(self.page, text="Cancel", command=lambda: self.controller.open_home()).pack(
            anchor=tk.W, side=tk.LEFT, padx=5, pady=5
        )

        ttk.Button(
            self.page, text="Use this image", command=lambda: self.use_image()
        ).pack(anchor=tk.S, side=tk.RIGHT, padx=5, pady=5)

        self.page.pack(anchor=tk.CENTER, expand=True)
    def use_image(self):
        """!
        This method sets the global variables according to the new background
        """
        data = glv.get_variable("DATA")
        data["background_image"] = self.background_image.get()
        glv.set_variable("DATA", data)
        self.controller.open_home()
