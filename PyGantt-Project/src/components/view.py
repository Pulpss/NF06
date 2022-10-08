from components import menu
from components.frames import new, home, add_task, edit_task, edit, background
import lib.global_variable as glv
import os
import tkinter as tk

class MainPage:
    """!
    This class is the main page of the application.
    It handles the switching between frames.
    It also triggers the main menu.
    """
    def __init__(self, master=None):
        """The constructor"""
        self.root = master
        self.current_frame = None
        self.page_frame = {
            "home": home.Home,
            "new": new.New,
            "add_task": add_task.AddTask,
            "edit_task": edit_task.EditTask,
            "edit": edit.Edit,
            "background": background.Background,
        }
        # set icon for window
        path = os.path.join(
            os.path.abspath(os.path.dirname(__file__)),
            "../../assets/icon.ico",
        )
        self.root.iconbitmap(path)
        self.open_page("home", "PyGantt Home - untitled.pygantt")
        self.root.geometry("1000x550")
    def open_page(self, frame_name, title):
        """!
        This function is used to switch between frames
        
        @param frame_name: the name of the frame to open
        @param title: the title of the window
        """
        self.root.title(title)
        if self.current_frame is not None and (
            hasattr(self.current_frame.destroy, "__call__")
        ):
            self.current_frame.destroy()

        # That's where we set the new frame
        self.current_frame = self.page_frame[frame_name](self.root, self)
        self.current_frame.pack(expand=True, fill=tk.BOTH)
        # Call the menu
        menu.MainMenu(self)

    def open_home(self):
        """!
        This function is used to open the home page or update it

        It sets the title of the window as well
        """
        self.open_page(
            "home",
            "PyGantt Home - "
            + (
                glv.get_variable("DATA")["project_name"]
                if glv.get_variable("STATE")
                else "untitled"
            )
            + ".pygantt",
        )
