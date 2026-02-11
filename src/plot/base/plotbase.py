import yaml
import numpy as np
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod
import plot.common.common as comm
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
        xvlinevalue=np.nan,
        xhlinevalue=np.nan,
        yaxisformatter=True,
        xaxisformatter=False,
        fsize=(6, 4),
    ):
        self.x = x
        self.y1 = y1
        self.y2 = y2
        self.y3 = y3
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.xvlinevalue = xvlinevalue
        self.xhlinevalue = xhlinevalue
        self.xaxisformatter = xaxisformatter
        self.yaxisformatter = yaxisformatter
        self.fsize = fsize

    def base(self):

        font = self.config()
        title = self.config()["title"]
        xaxis = self.config()["axis"]["xaxis"]
        yaxis = self.config()["axis"]["yaxis"]
        tick = self.config()["axis"]["tick"]
        vline = self.config()["line"]["vline"]
        hline = self.config()["line"]["hline"]

        plt.figure(figsize=self.fsize)
        ax = plt.gca()
        ax.set_axisbelow(True)

        self.plot(self.x, self.y1, self.y2, self.y3)
        plt.grid(True, axis="y", color="gray", alpha=0.5)

        plt.title(
            self.title,
            loc=title["loc"],
            pad=title["pad"],
            fontdict=dict(
                size=title["size"],
                color=title["color"],
                weight=title["weight"],
                style=title["style"],
                fontname=font["fontname"],
            ),
        )

        plt.gca().spines["top"].set_visible(False)
        plt.gca().spines["right"].set_visible(False)
        plt.gca().spines["left"].set_color("gray")
        plt.gca().spines["bottom"].set_color("gray")

        if self.yaxisformatter:
            plt.gca().yaxis.set_major_formatter(formatter)

        if self.xaxisformatter:
            plt.gca().xaxis.set_major_formatter(formatter)

        plt.xlabel(
            self.xlabel,
            fontdict=dict(
                size=xaxis["label"]["size"],
                color=xaxis["label"]["color"],
                weight=xaxis["label"]["weight"],
                style=xaxis["label"]["style"],
                fontname=font["fontname"]
            )
        )
        plt.ylabel(
            self.ylabel,
            fontdict=dict(
                size=xaxis["label"]["size"],
                color=xaxis["label"]["color"],
                weight=xaxis["label"]["weight"],
                style=xaxis["label"]["style"],
                fontname=font["fontname"]
            )
        )

        plt.xticks(
            size=xaxis["ticks"]["size"],
            color=xaxis["ticks"]["color"],
            weight=xaxis['ticks']['weight'],
            style=xaxis['ticks']['style'],
            fontname=font["fontname"],
            rotation=xaxis["ticks"]["rotation"],
        )
        plt.yticks(
            size=yaxis["ticks"]["size"],
            color=yaxis["ticks"]["color"],
            weight=yaxis['ticks']['weight'],
            style=yaxis['ticks']['style'],
            fontname=font["fontname"],
            rotation=yaxis["ticks"]["rotation"],
        )

        plt.tick_params(size=tick["size"], color=tick["color"])

        plt.axvline(
            self.xvlinevalue,
            color=vline["color"],
            alpha=vline["alpha"],
            linestyle=vline["style"],
            linewidth=vline["width"],
        )
        plt.axhline(
            self.xhlinevalue,
            color=hline["color"],
            alpha=hline["alpha"],
            linestyle=hline["style"],
            linewidth=hline["width"],
        )

        plt.savefig(f"output/{self.title}.jpg", dpi=300, bbox_inches="tight")

    def config(self):
        with open("src\\plot\\config\\decorator.yaml") as f:
            cfg = yaml.full_load(f)["common"]
        return cfg

    @abstractmethod
    def plot(self, x, y1, y2, y3):
        pass
