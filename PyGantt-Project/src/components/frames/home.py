import tkinter as tk
from tkinter import ttk
import lib.global_variable as glv
from components.frames.widgets import gantt, pessimistic_gantt, pert
from lib.c_functions import getTaskLevel, getMinStartDate, findCriticalPath, getMaxStartDate


class Home(tk.Frame):
    """This is the home page of the application. It contains the gantt chart and the pert chart."""
    def __init__(self, parent=None, controller=None):
        """!
        The constructor
        
        @param parent: the parent of the frame
        @param controller: the controller of the frame used to switch between frames
        """
        tk.Frame.__init__(self, parent)
        self.root = parent
        self.controller = controller
        # Displays the right home depending on the state of the app
        if glv.get_variable("STATE") == False:
            self.no_project_init()
        else:
            self.init_page()

    def no_project_init(self):
        """This function is called when there is no project loaded. It displays a message to the user."""
        tk.Label(
            self,
            text="No project is loaded. Please open or create one with the File menu and come back to this page.",
        ).pack(fill="none", expand=True)

    def init_page(self):
        # The next three functions are commented out. If there is a problem
        # with the ctypes functions, uncomment them change the functions used under

        # def find_critical_path(tasks):
        #     path = []
        #     max_dur = max([t["min_start_date"] + t["duration"] for t in tasks])
        #     critcal_last_task = [
        #         t for t in tasks if t["min_start_date"] + t["duration"] == max_dur
        #     ][0]
        #     path.append(critcal_last_task["name"])
        #     while critcal_last_task["tasks_before"] != []:
        #         last_task = [
        #             t for t in tasks if t["name"] in critcal_last_task["tasks_before"]
        #         ]
        #         critcal_last_task = max(
        #             last_task, key=lambda t: t["min_start_date"] + t["duration"]
        #         )
        #         path.append(critcal_last_task["name"])
        #     return list(reversed(path))

        # def get_task_level(task, tasks):
        #     if task["tasks_before"] == []:
        #         return 0
        #     else:
        #         sum = 0
        #         for task_before in [
        #             t for t in tasks if task["name"] in t["tasks_after"]
        #         ]:
        #             sum = max(get_task_level(task_before, tasks))
        #         return sum + 1

        # def get_min_start_date(task, tasks):
        #     tasks_before = [t for t in tasks if task["name"] in t["tasks_after"]]
        #     if tasks_before:
        #         return (
        #             max([get_min_start_date(t, tasks) for t in tasks_before])
        #             + task["duration"]
        #         )
        #     else:
        #         return task["duration"]

        def sort_tasks_by_level(tasks):
            """!
            Sort the tasks by level

            @param tasks: the list of tasks to sort
            """
            for i in range(len(tasks)):
                for j in range(len(tasks) - 1):
                    if tasks[j]["level"] > tasks[j + 1]["level"]:
                        tasks[j], tasks[j + 1] = tasks[j + 1], tasks[j]

        data = glv.get_variable("DATA")

        tasks = [task for task in glv.get_variable("DATA")["tasks"]]

        # Avoid errors by checking if there are tasks
        if tasks != []:
            for task in tasks:
                task["min_start_date"] = getMinStartDate(data, task)
                task["level"] = getTaskLevel(data, task)
                task["max_start_date"] = getMaxStartDate(data, task)
            # We have to sort tasks because it is useful after to have them in order
            sort_tasks_by_level(tasks)

        data["tasks"] = tasks
        glv.set_variable("DATA", data)

        if tasks != []:
            critical_path = [t["name"]for t in findCriticalPath(data)]
        else:
            critical_path = []
        self.page = tk.Frame(self)

        self.tasks_frame = tk.Frame(self.page)

        self.tasks_table = ttk.Treeview(self.tasks_frame)
        vsb = ttk.Scrollbar(
            self.tasks_frame, orient="vertical", command=self.tasks_table.yview
        )
        vsb.pack(side=tk.RIGHT, fill=tk.Y)
        self.tasks_table.configure(yscrollcommand=vsb.set)
        self.tasks_table["columns"] = ("name", "duration", "completed")

        self.tasks_table.column("#0", width=0, stretch=tk.NO)
        self.tasks_table.column("name", anchor=tk.CENTER, width=80)
        self.tasks_table.column("duration", anchor=tk.CENTER, width=60)
        self.tasks_table.column("completed", anchor=tk.CENTER, width=100)

        self.tasks_table.heading("#0", text="", anchor=tk.CENTER)
        self.tasks_table.heading("name", text="Name", anchor=tk.CENTER)
        self.tasks_table.heading("duration", text="Duration", anchor=tk.CENTER)
        self.tasks_table.heading("completed", text="Completed", anchor=tk.CENTER)

        if tasks != []:
            for index in range(len(tasks)):
                self.tasks_table.insert(
                    parent="",
                    index="end",
                    iid=index,
                    text="",
                    values=(
                        tasks[index]["name"],
                        tasks[index]["duration"],
                        tasks[index]["completed"],
                    ),
                )

        self.tasks_table.pack(fill=tk.BOTH, expand=True)
        ttk.Button(
            self.tasks_frame,
            text="Add task",
            command=lambda: self.add_task(),
        ).pack(fill=tk.X)
        ttk.Button(
            self.tasks_frame, text="Remove task", command=lambda: self.remove_task()
        ).pack(fill=tk.X)
        ttk.Button(
            self.tasks_frame, text="Edit Task", command=lambda: self.edit_task()
        ).pack(fill=tk.X)

        self.tasks_frame.pack(fill=tk.Y, expand=False, side=tk.LEFT)


        # Displays the right graph depending on the user choice
        if glv.get_variable("DISPLAY") == "Gantt":
            gantt.Gantt(self.page, tasks, critical_path, data).pack(fill=tk.BOTH, expand=True)
        elif glv.get_variable("DISPLAY") == "PessimisticGantt":
            pessimistic_gantt.PessimisticGantt(self.page, tasks, critical_path, data).pack(fill=tk.BOTH, expand=True)
        elif glv.get_variable("DISPLAY") == "PERT":
            pert.PERT(self.page, tasks, critical_path, data).pack(fill=tk.BOTH, expand=True)

        self.page.pack(fill=tk.BOTH, expand=True)

    def remove_task(self):
        """!
        Remove a task from the list of tasks

        @param self: the object pointer
        """
        index = self.tasks_table.selection()
        if len(index) <= 0:
            return
        selected_task = self.tasks_table.item(index)["values"][0]
        tasks = [task for task in glv.get_variable("DATA")["tasks"]]
        for task in tasks:
            if selected_task in task["tasks_before"]:
                task["tasks_before"].remove(selected_task)
            if selected_task in task["tasks_after"]:
                task["tasks_after"].remove(selected_task)
            if task["name"] == selected_task:
                task_to_remove = task

        tasks.remove(
            task_to_remove
        )  # We do this to avoid changing dict size during iteration
        data = glv.get_variable("DATA")
        data["tasks"] = tasks
        glv.set_variable("DATA", data)
        self.tasks_table.delete(index)
        self.controller.open_home()  # Refresh the page

    def add_task(self):
        """!
        Add a task to the list of tasks
        
        @param self: the object pointer
        """
        glv.set_variable("SELECTED_TASK", -1)
        self.controller.open_page("add_task", "Add a task")

    def edit_task(self):
        """!
        Edit a task from the list of tasks
        
        @param self: the object pointer
        """
        index = self.tasks_table.selection()
        if len(index) <= 0:
            return
        glv.set_variable("SELECTED_TASK", index)
        self.controller.open_page("edit_task", "Edit a task")
