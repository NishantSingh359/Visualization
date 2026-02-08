import matplotlib.pyplot as plt
from abc import ABC, abstractmethod
import src.common as comm
from matplotlib.ticker import FuncFormatter

formatter = FuncFormatter(comm.chart_format_number)


class PlotBase:
    def __init__(
        self,
        x,
        y1,
        y2=None,
        y3=None,
        title="Plot",
        xlabel="xlabel",
        ylabel="ylabel",
        fsize=(6, 4),
    ):
        self.x = x
        self.y1 = y1
        self.y2 = y2
        self.y3 = y3
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.fsize = fsize

    def base(self):
        plt.figure(figsize=self.fsize)
        ax = plt.gca()
        ax.set_axisbelow(True)
        self.plot(self.x, self.y1, self.y2, self.y3)
        plt.grid(True, axis="y", color="gray", alpha=0.5)
        plt.title(self.title, fontdict=dict(size=22, color="gray"), loc="left", pad=30)
        plt.gca().spines["top"].set_visible(False)
        plt.gca().spines["right"].set_visible(False)
        plt.gca().spines["left"].set_color("gray")
        plt.gca().spines["bottom"].set_color("gray")
        plt.gca().yaxis.set_major_formatter(formatter)
        plt.xlabel(self.xlabel, fontdict=dict(size=15, color="gray"))
        plt.ylabel(self.ylabel, fontdict=dict(size=15, color="gray"))
        plt.tick_params(color="gray")

        plt.xticks(size=12, rotation=90, color="gray")
        plt.yticks(size=12, color="gray")
        plt.savefig(f"output/{self.title}.jpg", dpi=300, bbox_inches="tight")

    @abstractmethod
    def plot(self, x, y1, y2, y3):
        pass
