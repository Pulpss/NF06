import tkinter as tk
import networkx as nx
import matplotlib.pyplot as plt
import lib.global_variable as glv
from PIL import Image
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class PERT(tk.Frame):
    """!
    The PERT frame
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
        self.pert_frame = tk.Frame(self)

        plt.rcParams["figure.autolayout"] = True
        background_path = glv.get_variable("DATA")["background_image"]
        fig, ax = plt.subplots(1, figsize=(16, 6))

        G = nx.DiGraph()

        # start
        G.add_node(0, node_color="red")
        for i in range(len(self.tasks)):
            if self.tasks[i]["tasks_before"] == []:
                if self.tasks[i]["name"] in self.critical_path:
                    G.add_edge(0, i + 1, edge_color="red")
                else:
                    G.add_edge(0, i + 1, edge_color="black")

        # end
        G.add_node(len(self.tasks) + 1, node_color="red")
        for i in range(len(self.tasks)):
            if self.tasks[i]["tasks_after"] == []:
                if self.tasks[i]["name"] in self.critical_path:
                    G.add_edge(i + 1, len(self.tasks) + 1, edge_color="red")
                else:
                    G.add_edge(i + 1, len(self.tasks) + 1, edge_color="black")

        for i in range(len(self.tasks)):
            for task_before in self.tasks[i]["tasks_before"]:
                for j in range(len(self.tasks)):
                    if task_before == self.tasks[j]["name"]:
                        break
                if (
                    self.tasks[i]["name"] in self.critical_path
                    and self.tasks[j]["name"] in self.critical_path
                ):
                    G.add_edge(j + 1, i + 1, edge_color="red")
                else:
                    G.add_edge(j + 1, i + 1, edge_color="black")

        for i in range(len(self.tasks)):
            if self.tasks[i]["completed"]:
                G.add_node(i + 1, node_color="#34D05C")
            else:
                G.add_node(i + 1, node_color="#3475D0")
        node_size = 2500
        nx.draw_networkx_nodes(
            G,
            pos=nx.spectral_layout(G),
            nodelist=G.nodes,
            node_color=[G.nodes[i]["node_color"] for i in G.nodes],
            node_size=node_size,
        )
        nx.draw_networkx_edges(
            G,
            pos=nx.spectral_layout(G),
            edgelist=G.edges,
            edge_color=[G[u][v]["edge_color"] for u, v in G.edges],
            node_size=node_size,
        )
        nx.draw_networkx_labels(
            G,
            pos=nx.spectral_layout(G),
            labels={
                i
                + 1: str(i + 1)
                + " | "
                + str(self.tasks[i]["min_start_date"])
                + " | "
                + str(self.tasks[i]["max_start_date"])
                for i in range(len(self.tasks))
            },
            font_size=10,
            font_color="white",
        )
        try:
            end_date = max([t["min_start_date"] + t["duration"] for t in self.tasks])
        except:
            end_date = 0
        nx.draw_networkx_labels(
            G,
            pos=nx.spectral_layout(G),
            labels={
                0: "S | 0 | 0",
                len(self.tasks)
                + 1: "E | "
                + str(end_date)
                + " | "
                + str(end_date),
            },
            font_size=10,
            font_color="white",
        )
        if background_path != "":
            try:
                im = Image.open(background_path, mode="r")
                im = ax.imshow(
                    im,
                    extent=[
                        ax.get_xlim()[0],
                        ax.get_xlim()[1],
                        ax.get_ylim()[0],
                        ax.get_ylim()[1],
                    ],
                    aspect="auto",
                )
            except:
                tk.messagebox.showerror(
                    "Error",
                    "The background image is not valid. Please select a valid image.",
                )

        ax.margins(0.05)
        ax.set_title("PERT Chart")

        chart_type = FigureCanvasTkAgg(fig, self.pert_frame)
        chart_type.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        self.pert_frame.pack(fill=tk.BOTH, expand=True)
