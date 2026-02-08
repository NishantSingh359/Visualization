from plot.deco.plotbase import PlotBase
import seaborn as sns


class LinePlot(PlotBase):
    def plot(self, x, y1, y2, y3):
        sns.lineplot(
            x=x,
            y=y1,
            color="black",
            marker="o",
            ms=9,
            markeredgecolor="black",
            markerfacecolor="white",
            markeredgewidth=2,
            linewidth=2,
        )
