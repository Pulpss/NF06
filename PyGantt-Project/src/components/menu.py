import tkinter as tk
import lib.global_variable as glv
from tkinter.filedialog import askopenfile
import json

FILE_TYPES = [
    ("PyGantt files", "*.pygantt"),
    ("JSON files", "*.json"),
    ("All Files", "*.*"),
]

class MainMenu:
    """This class is used to create the main menu"""
    def __init__(self, master):
        """!
        The constructor
        
        @param master: the main page used to switch between frames
        """
        self.master = master
        self.root = master.root
        self.init_menu()

    def init_menu(self):
        """This method is used to initialize the menu"""
        def open_file():
            """This method is used to open a file"""
            path = askopenfile(mode="r", filetypes=FILE_TYPES)
            if path:
                with open(path.name, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    glv.set_variable("PATH", path.name)
                    glv.set_variable("DATA", data)
                    glv.set_variable("STATE", True)
                    self.master.open_home()

        self.menubar = tk.Menu(self.root)

        filemenu = tk.Menu(self.menubar, tearoff=0)
        filemenu.add_command(
            label="New",
            command=lambda: self.master.open_page("new", "Create a new project"),
        )
        filemenu.add_command(
            label="Open",
            command=lambda: open_file(),
        )
        filemenu.add_command(
            label="Save",
            command=lambda: self.save(),
            state=tk.ACTIVE if glv.get_variable("STATE") == True else tk.DISABLED,
        )
        filemenu.add_command(
            label="Edit project",
            command=lambda: self.master.open_page("edit", "Edit project"),
            state=tk.ACTIVE if glv.get_variable("STATE") == True else tk.DISABLED,
        )
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.root.quit)

        homemenu = tk.Menu(self.menubar, tearoff=0)
        homemenu.add_command(
            label="Home",
            command=lambda: self.master.open_home(),
        )
        homemenu.add_separator()
        homemenu.add_command(
            label="Background image",
            command=lambda: self.master.open_page("background", "Change background image"),
            state=tk.ACTIVE if glv.get_variable("STATE") == True else tk.DISABLED,
        )

        displaymenu = tk.Menu(self.menubar, tearoff=0)
        displaymenu.add_command(
            label="Diplay Gantt Diagram",
            command=lambda: self.gantt_diagram(),
            state=tk.ACTIVE if glv.get_variable("STATE") == True else tk.DISABLED,
        )
        displaymenu.add_command(
            label="Display Pessimistic Gantt Diagram",
            command=lambda: self.pessimistic_gantt_diagram(),
            state=tk.ACTIVE if glv.get_variable("STATE") == True else tk.DISABLED,
        )
        displaymenu.add_command(
            label="Display PERT Diagram",
            command=lambda: self.pert_diagram(),
            state=tk.ACTIVE if glv.get_variable("STATE") == True else tk.DISABLED,
        )

        self.menubar.add_cascade(label="File", menu=filemenu)
        self.menubar.add_cascade(label="Home", menu=homemenu)
        self.menubar.add_cascade(label="Display", menu=displaymenu)
        self.root.config(menu=self.menubar)

    # These function need to be here because they don't stand in one line
    def gantt_diagram(self):
        """This method is used to display the gantt diagram"""
        glv.set_variable("DISPLAY", "Gantt")
        self.master.open_home()
    def pessimistic_gantt_diagram(self):
        """This method is used to display the pessimistic gantt diagram"""
        glv.set_variable("DISPLAY", "PessimisticGantt")
        self.master.open_home()
    def pert_diagram(self):
        """This method is used to display the pert diagram"""
        glv.set_variable("DISPLAY", "PERT")
        self.master.open_home()
    def save(self):
        """This method is used to save the project"""
        path = glv.get_variable("PATH")
        data = glv.get_variable("DATA")
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

