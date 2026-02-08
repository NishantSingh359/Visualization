from plot.deco.plotbase import PlotBase
import seaborn as sns


class ColumnPlot(PlotBase):
    def plot(self, x, y1, y2, y3):
        sns.barplot(x=x, y=y1, color="black")
