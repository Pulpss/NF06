import tkinter as tk
from Initial import Initial
from Home import Home


class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.state = "initial"
        self.path = tk.StringVar()
        self.data = {}

        self.title("PyGantt")
        self.geometry("300x400")
        self.minsize(300, 400)
        self.resizable(True, True)
        self.Menu()

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Initial, Home):
            frame = F(container, self)
            frame.grid_columnconfigure(0, weight=1)
            frame.grid_rowconfigure(0, weight=1)

            # the windows class acts as the root window for the frames.
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(Initial)

    def set_state(self, state):
        self.state = state
        if state == "home":
            self.filemenu.entryconfig("Save as...", state=tk.NORMAL)
            self.filemenu.entryconfig("Save", state=tk.NORMAL)
            self.geometry("1000x500")

    def set_data(self, data):
        self.data["name"] = tk.StringVar(value=data["name"])
        self.data["description"] = tk.StringVar(value=data["description"])
        self.data["end_date"] = tk.StringVar(value=data["end_date"])

    def set_path(self, path):
        self.path.set(path)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def Menu(self):
        pass
        self.menubar = tk.Menu(self)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="New")
        self.filemenu.add_command(label="Open")
        self.save = self.filemenu.add_command(label="Save", state=tk.DISABLED)
        self.save_as = self.filemenu.add_command(label="Save as...", state=tk.DISABLED)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.quit)
        self.menubar.add_cascade(label="File", menu=self.filemenu)
        self.config(menu=self.menubar)


if __name__ == "__main__":
    app = Application()
    app.mainloop()
