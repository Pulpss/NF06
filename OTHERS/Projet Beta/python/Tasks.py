import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from datetime import datetime


def Tasks(self, data):
    self.tasks_frame = tk.Frame(self.frame)

    self.tasks_table = ttk.Treeview(self.tasks_frame)
    vsb = ttk.Scrollbar(
        self.tasks_frame, orient="vertical", command=self.tasks_table.yview
    )
    vsb.pack(side=tk.RIGHT, fill=tk.Y)
    self.tasks_table.configure(yscrollcommand=vsb.set)
    self.tasks_table["columns"] = ("task_name", "start_date", "end_date", "duration")

    self.tasks_table.column("#0", width=0, stretch=tk.NO)
    self.tasks_table.column("task_name", anchor=tk.CENTER, width=80)
    self.tasks_table.column("start_date", anchor=tk.CENTER, width=80)
    self.tasks_table.column("end_date", anchor=tk.CENTER, width=80)
    self.tasks_table.column("duration", anchor=tk.CENTER, width=80)

    self.remove_button = ttk.Button(
        self.tasks_frame, text="Remove", command=lambda: remove_task(self)
    ).pack(fill=tk.X)
    self.add_button = ttk.Button(
        self.tasks_frame, text="Add", command=lambda: add_task_window(self)
    ).pack(fill=tk.X)

    self.tasks_table.heading("#0", text="", anchor=tk.CENTER)
    self.tasks_table.heading("task_name", text="Name", anchor=tk.CENTER)
    self.tasks_table.heading("start_date", text="Start Date", anchor=tk.CENTER)
    self.tasks_table.heading("end_date", text="End Date", anchor=tk.CENTER)
    self.tasks_table.heading("duration", text="Duration", anchor=tk.CENTER)

    for values in range(5):
        self.tasks_table.insert(
            parent="",
            index="end",
            iid=values,
            text="",
            values=("Patate" + str(values), "09/10/22", "10/10/22", "2"),
        )

    self.tasks_table.pack(fill=tk.Y, expand=1)

    def add_task_window(self):
        def add_task():
            task_name = self.task_name.get()
            start_date = self.start_date.get()
            end_date = self.end_date.get()
            duration = self.duration.get()
            if checkInput(task_name, start_date, end_date, duration):
                if self.end_or_duration.get() == 1:
                    duration = int((
                        datetime.strptime(end_date, "%d/%m/%Y").timestamp()
                        - datetime.strptime(start_date, "%d/%m/%Y").timestamp()
                    ) / 86400)
                elif self.end_or_duration.get() == 2:
                    end_date = datetime.fromtimestamp(
                        datetime.strptime(start_date, "%d/%m/%Y").timestamp()
                        + duration * 86400
                    )
                self.tasks_table.insert(
                    parent="",
                    index="end",
                    iid=task_name,
                    text="",
                    values=(task_name, start_date, end_date, duration),
                )
                close()
            pass
        def close():
            add_task_window.destroy()
            add_task_window.grab_release()
            return

        def hide_other_mode():
            if self.end_or_duration.get() == 1:
                self.duration_entry.grid_forget()
                self.duration_instruction.grid_forget()
                self.end_date_instruction.grid(row=6, padx=5, pady=5, sticky=tk.W)
                self.end_date_entry.grid(row=7, padx=5, pady=5, sticky=tk.W)
            else:
                self.end_date_instruction.grid_forget()
                self.end_date_entry.grid_forget()
                self.duration_instruction.grid(row=6, padx=5, pady=5, sticky=tk.W)
                self.duration_entry.grid(row=7, padx=5, pady=5, sticky=tk.W)

        add_task_window = tk.Toplevel(self)
        add_task_window.grab_set()
        add_task_window.title("Add Task")
        add_task_window.geometry("320x320")
        add_task_window.resizable(False, False)

        add_task_frame = tk.Frame(add_task_window, background="red")

        tk.Label(add_task_frame, text="Name").grid(row=0, padx=5, pady=5, sticky=tk.W)
        self.task_name = tk.StringVar()
        ttk.Entry(add_task_frame, textvariable=self.task_name).grid(
            row=1, padx=5, pady=5, sticky=tk.W
        )

        tk.Label(add_task_frame, text="Start date").grid(
            row=2, padx=5, pady=5, sticky=tk.W
        )
        self.start_date = tk.StringVar()
        DateEntry(
            add_task_frame,
            date_pattern="dd/MM/yyyy",
            selectmode="day",
            year=2022,
            month=9,
            day=1,
            textvariable=self.start_date,
        ).grid(row=3, padx=5, pady=5, sticky=tk.W)

        self.end_or_duration = tk.IntVar(value=1)  # 1 = end date, 2 = duration

        tk.Radiobutton(
            add_task_frame,
            text="End date",
            variable=self.end_or_duration,
            value=1,
            command=lambda: hide_other_mode(),
        ).grid(row=4, padx=5, pady=5, sticky=tk.W)
        tk.Radiobutton(
            add_task_frame,
            text="Duration",
            variable=self.end_or_duration,
            value=2,
            command=lambda: hide_other_mode(),
        ).grid(row=4, column=1, padx=5, pady=5, sticky=tk.W)

        self.end_date_instruction = tk.Label(add_task_frame, text="End Date")
        self.end_date_instruction.grid(row=6, padx=5, pady=5, sticky=tk.W)
        self.end_date = tk.StringVar()
        self.end_date_entry = DateEntry(
            add_task_frame,
            date_pattern="dd/MM/yyyy",
            selectmode="day",
            year=2022,
            month=9,
            day=1,
            textvariable=self.end_date,
        )
        self.end_date_entry.grid(row=7, padx=5, pady=5, sticky=tk.W)

        self.duration_instruction = tk.Label(add_task_frame, text="Duration")
        self.duration = tk.IntVar()
        self.duration_entry = ttk.Entry(add_task_frame, textvariable=self.duration)

        ttk.Button(add_task_frame, text="Add", command=lambda: add_task()).grid(
            row=8, column=3, padx=5, pady=5, sticky="ew"
        )

        ttk.Button(add_task_frame, text="Cancel", command=close).grid(
            row=8, padx=5, pady=5, sticky=tk.W
        )

        add_task_frame.pack(fill=tk.BOTH, expand=True)
        pass

    def remove_task(self):
        for task in [item[0] for item in self.tasks_table.selection()]:
            self.tasks_table.delete(task)
        pass

    def checkInput(task_name, start_date, end_date, duration):
        if task_name == "":
            tk.messagebox.showwarning(
                title="Input Error", message="No task name was entered"
            )
            return False
        elif start_date == "":
            tk.messagebox.showwarning(
                title="Input Error", message="No task start date was entered"
            )
            return False
        elif end_date == "" and duration == "":
            tk.messagebox.showwarning(
                title="Input Error", message="No task duration or end date was entered"
            )
            return False
        elif (
            datetime.strptime(end_date, "%d/%m/%Y").timestamp()
            <= datetime.strptime(start_date, "%d/%m/%Y").timestamp()
        ):
            tk.messagebox.showwarning(
                title="Input Error", message="End date is before or at the same time as the start date"
            )
            return False
        else:
            return True


