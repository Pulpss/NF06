import tkinter as tk
from tkinter import ttk
import lib.global_variable as glv


class EditTask(tk.Frame):
    """!
    This class is used to edit the different properties of a task
    """
    def __init__(self, parent=None, controller=None):
        """!
        The constructor

        @param parent: The parent of the frame
        @param controller: The controller of the frame used to switch between frames
        """
        tk.Frame.__init__(self, parent)
        self.selected_task_index = int(glv.get_variable("SELECTED_TASK")[0])
        self.task = glv.get_variable("DATA")["tasks"][self.selected_task_index]
        self.root = parent
        self.controller = controller
        self.task_name = tk.StringVar()
        self.duration = tk.IntVar()
        self.state = tk.IntVar()
        self.task_description = tk.StringVar()
        self.init_page()

    def init_page(self):
        """!
        This method is used to initialize the page
        """
        self.page = tk.Frame(self)

        tk.Label(self.page, text="Name").pack(anchor=tk.W, padx=5)
        self.task_name.set(self.task["name"])
        ttk.Entry(self.page, textvariable=self.task_name).pack(
            anchor=tk.W, padx=5, pady=5
        )

        tk.Label(self.page, text="Description").pack(anchor=tk.W, padx=5)
        self.task_description.set(self.task["description"])
        ttk.Entry(self.page, textvariable=self.task_description).pack(
            anchor=tk.W, padx=5, pady=5, fill=tk.X
        )

        tk.Label(self.page, text="Duration").pack(anchor=tk.W, padx=5)
        self.duration.set(self.task["duration"])
        ttk.Entry(self.page, textvariable=self.duration).pack(
            anchor=tk.W, padx=5, pady=5
        )

        tk.Label(self.page, text="State").pack(anchor=tk.W, padx=5)
        self.state.set(1) if self.task["completed"] else self.state.set(0)
        tk.Checkbutton(self.page, text="Completed", variable=self.state).pack(anchor=tk.W, padx=5, pady=5)

        tk.Label(self.page, text="Enter the dependencies of the task").pack(
            anchor=tk.W, padx=5
        )

        self.tasks_select = tk.Frame(
            self.page, highlightbackground="grey", highlightthickness=1
        )

        # Start of the treeview before
        treeview_before_frame = tk.Frame(self.tasks_select)
        self.tasks_table_before = ttk.Treeview(treeview_before_frame, height=5)
        vsb = ttk.Scrollbar(
            treeview_before_frame,
            orient="vertical",
            command=self.tasks_table_before.yview,
        )
        vsb.pack(side=tk.RIGHT, anchor=tk.W, fill=tk.BOTH, padx=5, pady=5)
        self.tasks_table_before.configure(yscrollcommand=vsb.set)
        self.tasks_table_before["columns"] = "task_name"

        self.tasks_table_before.column("#0", width=0, stretch=tk.NO)
        self.tasks_table_before.column("task_name", anchor=tk.CENTER, width=80)

        self.tasks_table_before.heading("#0", text="", anchor=tk.CENTER)
        self.tasks_table_before.heading("task_name", text="Name", anchor=tk.CENTER)

        self.tasks_table_before.pack(
            anchor=tk.W, padx=5, pady=5, expand=True, fill=tk.X
        )
        # End of the treeview before

        # Start of the tasks treeview
        treeview_frame = tk.Frame(self.tasks_select)
        self.tasks_table = ttk.Treeview(treeview_frame, height=5)
        vsb = ttk.Scrollbar(
            treeview_frame, orient="vertical", command=self.tasks_table.yview
        )
        vsb.pack(side=tk.RIGHT, anchor=tk.W, fill=tk.BOTH, padx=5, pady=5)
        self.tasks_table.configure(yscrollcommand=vsb.set)
        self.tasks_table["columns"] = "task_name"

        self.tasks_table.column("#0", width=0, stretch=tk.NO)
        self.tasks_table.column("task_name", anchor=tk.CENTER, width=80)

        self.tasks_table.heading("#0", text="", anchor=tk.CENTER)
        self.tasks_table.heading("task_name", text="Name", anchor=tk.CENTER)

        tasks = [task["name"] for task in glv.get_variable("DATA")["tasks"]]

        if tasks != []:
            for index in range(len(tasks)):
                if index != self.selected_task_index:
                    self.tasks_table.insert(
                        parent="",
                        index="end",
                        iid=index,
                        text="",
                        values=tasks[index],
                    )

        self.tasks_table.pack(anchor=tk.W, padx=5, pady=5, expand=True, fill=tk.X)
        # End of the tasks treeview

        # Start of treeview after
        treeview_after_frame = tk.Frame(self.tasks_select)
        self.tasks_table_after = ttk.Treeview(treeview_after_frame, height=5)
        vsb = ttk.Scrollbar(
            treeview_after_frame,
            orient="vertical",
            command=self.tasks_table_after.yview,
        )
        vsb.pack(side=tk.RIGHT, anchor=tk.W, fill=tk.BOTH, padx=5, pady=5)
        self.tasks_table_after.configure(yscrollcommand=vsb.set)
        self.tasks_table_after["columns"] = "task_name"

        self.tasks_table_after.column("#0", width=0, stretch=tk.NO)
        self.tasks_table_after.column("task_name", anchor=tk.CENTER, width=80)

        self.tasks_table_after.heading("#0", text="", anchor=tk.CENTER)
        self.tasks_table_after.heading("task_name", text="Name", anchor=tk.CENTER)

        self.tasks_table_after.pack(anchor=tk.W, padx=5, pady=5, expand=True, fill=tk.X)
        # End of the treeview after

        for task_name in self.task["tasks_before"]:
            for i in range(len(tasks)):
                if task_name == tasks[i]:
                    self.switch_task_to("to_before", i)
        for task_name in self.task["tasks_after"]:
            for i in range(len(tasks)):
                if task_name == tasks[i]:
                    self.switch_task_to("to_after", i)

        treeview_before_frame.pack(
            anchor=tk.W, side=tk.LEFT, padx=5, pady=5, expand=True, fill=tk.X
        )
        arrows_before_frame = tk.Frame(self.tasks_select)
        ttk.Button(
            arrows_before_frame,
            text="<--",
            command=lambda: self.switch_task_to("to_before"),
        ).pack(anchor=tk.W, padx=5, pady=5)
        ttk.Button(
            arrows_before_frame,
            text="-->",
            command=lambda: self.switch_task_to("from_before"),
        ).pack(anchor=tk.W, padx=5, pady=5)
        arrows_before_frame.pack(anchor=tk.W, side=tk.LEFT)
        treeview_frame.pack(
            anchor=tk.W, side=tk.LEFT, padx=5, pady=5, expand=True, fill=tk.X
        )
        arrows_after_frame = tk.Frame(self.tasks_select)
        ttk.Button(
            arrows_after_frame,
            text="-->",
            command=lambda: self.switch_task_to("to_after"),
        ).pack(anchor=tk.W, padx=5, pady=5)
        ttk.Button(
            arrows_after_frame,
            text="<--",
            command=lambda: self.switch_task_to("from_after"),
        ).pack(anchor=tk.W, padx=5, pady=5)
        arrows_after_frame.pack(anchor=tk.W, side=tk.LEFT)
        treeview_after_frame.pack(
            anchor=tk.W, side=tk.LEFT, padx=5, pady=5, expand=True, fill=tk.X
        )

        self.tasks_select.pack(anchor=tk.W, padx=5, pady=5, expand=True, fill=tk.X)

        ttk.Button(
            self.page, text="Cancel", command=lambda: self.controller.open_home()
        ).pack(anchor=tk.W, side=tk.LEFT, padx=5, pady=5)

        ttk.Button(self.page, text="Update", command=lambda: self.update_task()).pack(
            anchor=tk.W, side=tk.LEFT, padx=5, pady=5
        )

        self.page.pack(anchor=tk.CENTER, expand=True)

    def update_task(self):
        """!
        Update the task in the global variable
        """
        task_from_global_var = glv.get_variable("DATA")["tasks"][self.selected_task_index]
        tasks = glv.get_variable("DATA")["tasks"]
        # Remove the tasks to cleanup
        for task_before_global in task_from_global_var["tasks_before"]:
            for task in tasks:
                if task["name"] == task_before_global:
                    task["tasks_after"].remove(self.task["name"])
        for task_after_global in task_from_global_var["tasks_after"]:
            for task in tasks:
                if task["name"] == task_after_global:
                    task["tasks_before"].remove(self.task["name"])
        tasks_before = []
        tasks_after = []
        if self.task_name.get() == "":
            tk.messagebox.showerror("Error", "Task name cannot be empty")
            return
        elif self.duration.get() == "" or self.duration.get() == 0:
            tk.messagebox.showerror("Error", "Duration cannot be empty nor zero")
            return
        tasks_before_index = self.tasks_table_before.get_children()
        tasks_after_index = self.tasks_table_after.get_children()
        for task in tasks_before_index:
            tasks_before.append(self.tasks_table_before.item(task)["values"][0])
        for task in tasks_after_index:
            tasks_after.append(self.tasks_table_after.item(task)["values"][0])
        for task_before in tasks_before:
            for task in tasks:
                if task["name"] == task_before:
                    if self.task_name.get().replace(" ", "_") not in task["tasks_after"]:
                        task["tasks_after"].append(self.task_name.get().replace(" ", "_"))
        for task_after in tasks_after:
            for task in tasks:
                if task["name"] == task_after:
                    if self.task_name.get().replace(" ", "_") not in task["tasks_before"]:
                        task["tasks_before"].append(self.task_name.get().replace(" ", "_"))
        tasks[self.selected_task_index] = {
            "name": self.task_name.get().replace(" ", "_"),
            "description": self.task_description.get(),
            "duration": self.duration.get(),
            "min_start_date": 0,
            "max_start_date": 0,
            "tasks_before": tasks_before,
            "tasks_after": tasks_after,
            "completed": False if self.state.get() == 0 else True,
        }
        data = glv.get_variable("DATA")
        data["tasks"] = tasks
        glv.set_variable("DATA", data)
        self.controller.open_home()

    def switch_task_to(self, direction, index=None):
        """!
        Switch the task from one table to another

        @param direction The direction of the switch
        @param index The index of the task to switch
        """
        if direction == "to_before":
            if index is None:
                index = self.tasks_table.selection()
                if len(index) <= 0:
                    return
            selected_task = self.tasks_table.item(index)["values"][0]
            self.tasks_table.delete(index)
            self.tasks_table_before.insert(
                parent="",
                index="end",
                iid=selected_task,
                text="",
                values=(selected_task),
            )
        elif direction == "from_before":
            if index is None:
                index = self.tasks_table_before.selection()
                if len(index) <= 0:
                    return
            selected_task = self.tasks_table_before.item(index)["values"][0]
            self.tasks_table_before.delete(index)
            self.tasks_table.insert(
                parent="",
                index="end",
                iid=selected_task,
                text="",
                values=(selected_task),
            )
        elif direction == "to_after":
            if index is None:
                index = self.tasks_table.selection()
                if len(index) <= 0:
                    return
            selected_task = self.tasks_table.item(index)["values"][0]
            self.tasks_table.delete(index)
            self.tasks_table_after.insert(
                parent="",
                index="end",
                iid=selected_task,
                text="",
                values=(selected_task),
            )
        elif direction == "from_after":
            if index is None:
                index = self.tasks_table_after.selection()
                if len(index) <= 0:
                    return
            selected_task = self.tasks_table_after.item(index)["values"][0]
            self.tasks_table_after.delete(index)
            self.tasks_table.insert(
                parent="",
                index="end",
                iid=selected_task,
                text="",
                values=(selected_task),
            )
