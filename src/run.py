import importlib
import pandas as pd
import src.metrics as m
import plot.chart.lineplot as li
import plot.chart.columnplot as co
import plot.chart.areaplot as ar

importlib.reload(li)
importlib.reload(co)
importlib.reload(ar)
importlib.reload(m)


df = pd.read_csv(
    r"C:\Users\TUF\OneDrive\Documents\Code\Vs Code\Visualization\data\Bike Sales.csv"
)
mt = m.metrics(df)

data = mt.revenue_by_month()
co.ColumnPlot(
    x=data["Month Name"],
    y1=data["Revenue"],
    title="Revenue by Month",
    xlabel="Month",
    ylabel="Revenue",
    fsize=(10, 6),
).base()

data = mt.revenue_by_year()
li.LinePlot(
    x=data["Year"],
    y1=data["Revenue"],
    title="Revenue by Year",
    xlabel="Year",
    ylabel="Revenue",
    fsize=(8, 4),
).base()

data = mt.revenue_by_country()
ar.AreaPlot(
    x=data['Country'],
    y1=data['Revenue'],
    title="Revenue by Country",
    xlabel="Country",
    ylabel="Revenue",
    fsize=(10, 6),    
).base()