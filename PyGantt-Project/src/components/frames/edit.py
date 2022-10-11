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


class Edit(tk.Frame):
    """!
    This class is used to edit the different parameters of the project
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
        self.project_name = tk.StringVar()
        self.project_description = tk.StringVar()
        self.start_date = tk.StringVar()
        self.init_page()

    def init_page(self):
        """!
        This method is used to initialize the page
        """
        def update():
            """!
            This method is used to update the project
            It also validates that the fields don't have a problem
            """
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
            path = glv.get_variable("PATH")
            data = glv.get_variable("DATA")
            data["project_name"] = self.project_name.get()
            data["project_description"] = self.project_description.get()
            data["start_date"] = self.start_date.get()
            with open(path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
                glv.set_variable("DATA", data)
            self.controller.open_home()

        self.page = tk.Frame(self)

        ttk.Label(
            self.page, text="Enter the name of the project:"
        ).pack(anchor=tk.W, padx=5, pady=5)

        self.project_name.set(glv.get_variable("DATA")["project_name"])
        ttk.Entry(
            self.page, textvariable=self.project_name
        ).pack(anchor=tk.W, padx=5, pady=5)

        ttk.Label(
            self.page, text="Enter the description of the project:"
        ).pack(anchor=tk.W, padx=5, pady=5)

        self.project_description.set(glv.get_variable("DATA")["project_description"])
        tk.Entry(
            self.page, textvariable=self.project_description
        ).pack(anchor=tk.W, padx=5, pady=5)

        ttk.Label(
            self.page, text="Select the desired start date of the project:"
        ).pack(anchor=tk.W, padx=5, pady=5)

        self.start_date.set(glv.get_variable("DATA")["start_date"])
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
            self.page, text="Update", command=update
        ).pack(anchor=tk.S, side=tk.RIGHT, padx=5, pady=5)
        self.page.pack(anchor=tk.CENTER, expand=True)
