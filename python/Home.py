import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from Graph import Graph

from tkinter.filedialog import asksaveasfile, askopenfile

import json


FILE_TYPES = [('All Files', '*.*'),
              ('PyGantt files', '*.pygantt'),
              ('JSON files', '*.json'), ]


class Home(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.frame = tk.Frame(self)

        self.instruction = ttk.Label(
            self.frame, text='Create a new project:').pack(anchor=tk.W, padx=5, pady=5)

        self.instruction_name = ttk.Label(
            self.frame, text='Enter the name of the project:').pack(anchor=tk.W, padx=5, pady=5)

        self.project_name = tk.StringVar()
        self.project_name_entry = ttk.Entry(
            self.frame, textvariable=self.project_name).pack(anchor=tk.W, padx=5, pady=5)

        self.instruction_description = ttk.Label(
            self.frame, text='Enter the description of the project:').pack(anchor=tk.W, padx=5, pady=5)

        self.project_description = tk.StringVar()
        self.project_description_entry = tk.Entry(
            self.frame, textvariable=self.project_description).pack(anchor=tk.W, padx=5, pady=5)

        self.instruction_date = ttk.Label(
            self.frame, text='Select the desired end date of the project:').pack(anchor=tk.W, padx=5, pady=5)

        self.end_date = tk.StringVar()
        self.end_date_entry = DateEntry(
            self.frame, selectmode="day", year=2022, month=9, day=1, textvariable=self.end_date).pack(anchor=tk.W, padx=5, pady=5)

        self.create_button = ttk.Button(
            self.frame, text='Save as...', command=lambda: self.save_as(controller)).pack(anchor=tk.S, side=tk.RIGHT, padx=5, pady=5)

        self.open_button = ttk.Button(
            self.frame, text='Open a project', command=lambda: self.open(controller)).pack(anchor=tk.S, side=tk.RIGHT, padx=5, pady=5)

        self.exit_button = ttk.Button(
            self.frame, text='Exit', command=self.quit).pack(anchor=tk.S, side=tk.LEFT, padx=5, pady=5)

        self.frame.pack(expand=True, fill=tk.BOTH)

    def checkInput(self):
        pass
        if self.project_name.get() == '':
            tk.messagebox.showwarning(
                title="Input Error", message="No Project name was entered")
            return False
        if self.project_description.get() == '':
            tk.messagebox.showwarning(
                title="Input Error", message="No Project description was entered")
            return False
        return True

    def open(self, controller):
        pass
        path = askopenfile(mode='r', filetypes=FILE_TYPES).name
        if path is not None:
            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                controller.set_data(data)
                controller.set_state("graph")
                controller.show_frame(Graph)

    def save_as(self, controller):
        pass
        if (self.checkInput() == False):
            return
        path = asksaveasfile(
            filetypes=FILE_TYPES, defaultextension=FILE_TYPES, initialfile=self.project_name.get()+".pygantt").name
        if path is not None:
            with open(path, 'w', encoding='utf-8') as f:
                data = {
                    "name": self.project_name.get(),
                    "description": self.project_description.get(),
                    "end_date": self.end_date.get()
                }
                json.dump(data, f, ensure_ascii=False, indent=4)
                controller.set_data(data)
                controller.set_state("graph")
                controller.show_frame(Graph)
