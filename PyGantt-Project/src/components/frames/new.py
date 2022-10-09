import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
import lib.global_variable as glv
from tkinter.filedialog import asksaveasfile
import json

FILE_TYPES = [
    ("PyGantt files", "*.pygantt"),
    ("JSON files", "*.json"),
    ("All Files", "*.*"),
]


class New(tk.Frame):
    """This class is used to create the new project frame"""
    def __init__(self, parent=None, controller=None):
        """The constructor"""
        tk.Frame.__init__(self, parent)
        self.root = parent
        self.controller = controller
        self.project_name = tk.StringVar()
        self.project_description = tk.StringVar()
        self.start_date = tk.StringVar()
        self.init_page()

    def init_page(self):
        """This method is used to initialize the page"""
        def save_as():
            """This method is used to save the project in the explorer"""
            if self.project_name.get() == "":
                tk.messagebox.showwarning(
                    title="Input Error", message="No Project name was entered"
                )
                return
            if self.project_description.get() == "":
                tk.messagebox.showwarning(
                    title="Input Error", message="No Project description was entered"
                )
                return
            path = asksaveasfile(
                filetypes=FILE_TYPES,
                defaultextension=FILE_TYPES,
                initialfile=self.project_name.get() + ".pygantt",
            )
            if path is not None:
                with open(path.name, "w", encoding="utf-8") as f:
                    data = {
                        "project_name": self.project_name.get(),
                        "project_description": self.project_description.get(),
                        "start_date": self.start_date.get(),
                        "background_image": "",
                        "tasks": [],
                    }
                    json.dump(data, f, ensure_ascii=False, indent=4)
                    glv.set_variable("PATH", path.name)
                    glv.set_variable("DATA", data)
                    glv.set_variable("STATE", True)
                    self.controller.open_home()

        self.page = tk.Frame(self)

        ttk.Label(
            self.page, text="Enter the name of the project:"
        ).pack(anchor=tk.W, padx=5, pady=5)

        ttk.Entry(
            self.page, textvariable=self.project_name
        ).pack(anchor=tk.W, padx=5, pady=5)

        ttk.Label(
            self.page, text="Enter the description of the project:"
        ).pack(anchor=tk.W, padx=5, pady=5)

        tk.Entry(
            self.page, textvariable=self.project_description
        ).pack(anchor=tk.W, padx=5, pady=5)

        ttk.Label(
            self.page, text="Select the desired start date of the project:"
        ).pack(anchor=tk.W, padx=5, pady=5)

        DateEntry(
            self.page,
            date_pattern="dd/MM/yyyy",
            selectmode="day",
            year=2022,
            month=9,
            day=1,
            textvariable=self.start_date,
        ).pack(anchor=tk.W, padx=5, pady=5)

        ttk.Button(self.page, text="Cancel", command=lambda: self.controller.open_home()).pack(
            anchor=tk.W, side=tk.LEFT, padx=5, pady=5
        )

        ttk.Button(
            self.page, text="Save as...", command=save_as
        ).pack(anchor=tk.S, side=tk.RIGHT, padx=5, pady=5)
        self.page.pack(anchor=tk.CENTER, expand=True)
