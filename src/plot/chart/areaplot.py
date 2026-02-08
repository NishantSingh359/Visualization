from plot.deco.plotbase import PlotBase
import matplotlib.pyplot as plt


class AreaPlot(PlotBase):
    def plot(self, x, y1, y2, y3):
        plt.stackplot(x, y1, color='black', alpha=.8)