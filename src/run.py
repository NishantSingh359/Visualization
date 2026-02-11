import importlib
import pandas as pd
import src.metrics as m
import src.plot.chart.lineplot as li
import src.plot.chart.columnplot as co
import src.plot.chart.areaplot as ar
import src.plot.chart.stepplot as st
import src.plot.chart.scatterplot as sc

importlib.reload(li)
importlib.reload(co)
importlib.reload(ar)
importlib.reload(m)
importlib.reload(st)
importlib.reload(sc)

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
    x=data["Country"],
    y1=data["Revenue"],
    title="Revenue by Country",
    xlabel="Country",
    ylabel="Revenue",
    fsize=(10, 6),
).base()

data = mt.mountain_bikes_avg_price()
st.StepPlot(
    x=data["Year"],
    y1=data["Avg Price"],
    title="Mountain Bike's Avg Price",
    xlabel="Year",
    ylabel="Avg Price",
    fsize=(10, 6),
).base()


data = mt.product_by_revenue_and_profit()
sc.ScatterPlot(
    x=data["Revenue"],
    y1=data["Profit"],
    title="Product by Revenue & Profit",
    xlabel="Revenue",
    ylabel="Profit",
    xvlinevalue=data["Revenue"].mean(),
    xhlinevalue=data["Profit"].mean(),
    xaxisformatter=True,
    fsize=(10, 6),
).base()


data = mt.revenue_by_sub_category()
sc.ScatterPlot(
    x=data["Sub_Category"],
    y1=data["Revenue"],
    title="Revenue by Sub-Category",
    xlabel="Sub-Category",
    ylabel="Revenue",
    fsize=(10, 6),
).base()
