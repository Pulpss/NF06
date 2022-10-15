import tkinter as tk
import lib.global_variable as glv
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.patches import Patch
from PIL import Image, ImageOps


class Gantt(tk.Frame):
    """!
    This class is used to display the Gantt chart
    """
    def __init__(self, parent, tasks=[], critical_path=[], data=None):
        """!
        The constructor
        
        @param parent: The parent of the frame
        @param tasks: The list of tasks
        @param critical_path: The list of tasks in the critical path
        @param data: The data of the project
        """
        tk.Frame.__init__(self, parent)
        self.tasks = tasks
        self.root = parent
        self.data = data
        self.critical_path = critical_path
        self.init_page()

    def init_page(self):
        """!
        This method is used to initialize the page
        """
        self.gantt_frame = tk.Frame(self)

        plt.rcParams["figure.autolayout"] = True
        background_path = glv.get_variable("DATA")["background_image"]
        fig, ax = plt.subplots(1, figsize=(16, 6))

        ax.barh(
            [task["name"] for task in self.tasks],
            [task["duration"] for task in self.tasks],
            left=[task["min_start_date"] for task in self.tasks],
            color=["#34D05C" if task["completed"] else "#3475D0" for task in self.tasks],
            edgecolor=[
                "red" if task["name"] in self.critical_path else "white"
                for task in self.tasks
            ],
        )
        legends_dict = {"Completed": "#34D05C", "Not completed": "#3475D0"}
        legend_elements = [
            Patch(facecolor=legends_dict[i], label=i) for i in legends_dict
        ]
        legend_elements.append(
            Patch(edgecolor="red", facecolor="white", label="Critical path")
        )
        plt.legend(handles=legend_elements)
        try:
            end_duration = max(
                [task["min_start_date"] + task["duration"] for task in self.tasks]
            )
        except:
            end_duration = 0
        if background_path != "":
            try:
                im = ImageOps.flip(Image.open(background_path, mode="r"))
                im = ax.imshow(
                    im,
                    extent=[
                        0,
                        end_duration + 1,
                        -1,
                        len(glv.get_variable("DATA")["tasks"]),
                    ],
                    aspect="auto",
                )
            except:
                tk.messagebox.showerror(
                    "Error",
                    "The background image is not valid. Please select a valid image.",
                )
        ax.invert_yaxis()
        xticks = np.arange(
            0,
            end_duration + 1,
            3,
        )
        xticks_labels = pd.date_range(
            datetime.strptime(self.data["start_date"], "%d/%m/%Y"),
            end=(
                datetime.strptime(self.data["start_date"], "%d/%m/%Y")
                + timedelta(days=end_duration)
            ),
        ).strftime("%d/%m")
        xticks_minor = np.arange(
            0,
            end_duration + 1,
            1,
        )
        ax.set_xticks(xticks)
        ax.set_xticks(xticks_minor, minor=True)
        ax.set_xticklabels(xticks_labels[::3])

        plt.title("Gantt Diagram")

        chart_type = FigureCanvasTkAgg(fig, self.gantt_frame)
        chart_type.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        self.gantt_frame.pack(fill=tk.BOTH, expand=True)