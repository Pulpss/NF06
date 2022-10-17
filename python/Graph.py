import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry


class Graph(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.frame = tk.Frame(self)

        self.Tasks()

        self.frame.pack(fill=tk.Y, side=tk.LEFT)

    def Tasks(self):
        self.tasks_frame = tk.Frame(self.frame)

        tk.Label(self.tasks_frame, text='Tasks').pack(anchor=tk.W, padx=5)
        self.tasks_table = ttk.Treeview(self.tasks_frame)
        vsb = ttk.Scrollbar(self.tasks_frame, orient="vertical",
                            command=self.tasks_table.yview)
        vsb.pack(side=tk.RIGHT, fill=tk.Y)
        self.tasks_table.configure(yscrollcommand=vsb.set)
        self.tasks_table['columns'] = ('task_name', 'start_date',
                                       'end_date', 'duration')

        self.tasks_table.column("#0", width=0,  stretch=tk.NO)
        self.tasks_table.column("task_name", anchor=tk.CENTER, width=80)
        self.tasks_table.column("start_date", anchor=tk.CENTER, width=80)
        self.tasks_table.column("end_date", anchor=tk.CENTER, width=80)
        self.tasks_table.column("duration", anchor=tk.CENTER, width=80)

        self.remove_button = ttk.Button(
            self.tasks_frame, text='Remove', command=lambda: self.remove_task()).pack(fill=tk.X)
        self.add_button = ttk.Button(
            self.tasks_frame, text='Add', command=lambda: self.add_task_window()).pack(fill=tk.X)

        self.tasks_table.heading("#0", text="", anchor=tk.CENTER)
        self.tasks_table.heading("task_name", text="Name", anchor=tk.CENTER)
        self.tasks_table.heading(
            "start_date", text="Start Date", anchor=tk.CENTER)
        self.tasks_table.heading("end_date", text="End Date", anchor=tk.CENTER)
        self.tasks_table.heading("duration", text="Duration", anchor=tk.CENTER)

        for values in range(5):
            self.tasks_table.insert(parent='', index='end', iid=values, text='',
                                    values=('Patate'+str(values), '09/10/22', '10/10/22', '2'))

        self.tasks_table.pack(fill=tk.Y, expand=1)

        self.tasks_frame.pack(side=tk.LEFT, fill=tk.Y)
        pass

    def add_task_window(self):
        def close():
            add_task_window.destroy()
            add_task_window.grab_release()
            return

        def hide_other_mode():
            if (self.end_or_duration.get() == 1):
                self.duration_entry.pack_forget()
                self.duration_instruction.pack_forget()
                self.end_date_instruction.pack()
                self.end_date_entry.pack()
            else:
                self.end_date_instruction.pack_forget()
                self.end_date_entry.pack_forget()
                self.duration_instruction.pack()
                self.duration_entry.pack()

        add_task_window = tk.Toplevel(self)
        add_task_window.grab_set()
        add_task_window.title('Add Task')
        add_task_window.geometry('300x300')
        add_task_window.resizable(False, False)

        add_task_frame = tk.Frame(add_task_window)

        tk.Label(add_task_frame, text='Name').pack(anchor=tk.W, padx=5)
        self.task_name = tk.StringVar()
        ttk.Entry(
            add_task_frame, textvariable=self.task_name).pack(anchor=tk.W, padx=5, pady=5)

        tk.Label(add_task_frame, text='Start date').pack(
            anchor=tk.W, padx=5)
        self.start_date = tk.StringVar()
        DateEntry(
            add_task_frame, selectmode="day", year=2022, month=9, day=1, textvariable=self.start_date).pack(anchor=tk.W, padx=5, pady=5)

        self.end_or_duration = tk.IntVar(value=1)  # 1 = end date, 2 = duration

        tk.Radiobutton(add_task_frame, text="End date", variable=self.end_or_duration,
                       value=1, command=lambda: hide_other_mode()).pack(anchor=tk.W)
        tk.Radiobutton(add_task_frame, text="Duration", variable=self.end_or_duration,
                       value=2, command=lambda: hide_other_mode()).pack(anchor=tk.W)

        self.end_date_instruction = tk.Label(
            add_task_frame, text='End Date')
        self.end_date_instruction.pack(anchor=tk.W, padx=5)
        self.end_date = tk.StringVar()
        self.end_date_entry = DateEntry(
            add_task_frame, selectmode="day", year=2022, month=9, day=1, textvariable=self.end_date)
        self.end_date_entry.pack(anchor=tk.W, padx=5, pady=5)

        self.duration_instruction = tk.Label(add_task_frame, text='Name')
        self.duration_instruction.pack(anchor=tk.W, padx=5)
        self.duration = tk.IntVar()
        self.duration_entry = ttk.Entry(
            add_task_frame, textvariable=self.duration)
        self.duration_entry.pack(anchor=tk.W, padx=5, pady=5)

        ttk.Button(
            add_task_frame, text='Ok').pack(anchor=tk.S, side=tk.RIGHT, padx=5 , pady=5)

        ttk.Button(
            add_task_frame, text='Cancel', command=close).pack(anchor=tk.S, side=tk.LEFT, padx=5, pady=5)

        add_task_frame.pack(fill=tk.Y)
        pass

    def remove_task(self):
        for task in [item[0] for item in self.tasks_table.selection()]:
            print(task)
            self.tasks_table.delete(task)
        pass
