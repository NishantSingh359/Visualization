import pandas as pd


class metrics:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def revenue_by_month(self):
        return (
            self.df.groupby(["Month", "Month Name"], as_index=False)["Revenue"]
            .sum()
            .sort_values("Month", ascending=True)
        )  # type: ignore

    def revenue_by_year(self):
        return (
            self.df.groupby("Year", as_index=False)["Revenue"]
            .sum()
            .sort_values("Year", ascending=True)
        )  # type: ignore

    def revenue_by_country(self):
        return (
            self.df.groupby("Country", as_index=False)["Revenue"]
            .sum()
            .sort_values("Revenue", ascending=False)
        )  # type:ignore

    def orders_by_country(self):
        return (
            self.df.groupby("Country", as_index=False)["Revenue"]
            .count()
            .rename(columns={"Revenue": "Orders"})  # type:ignore
            .sort_values("Orders", ascending=False)
        )

    def mountain_bikes_avg_price(self):
        return (
            self.df.groupby("Year", as_index=False)["Unit_Price"]
            .mean()
            .rename(columns={"Unit_Price": "Avg Price"})  # type:ignore
            .sort_values("Year", ascending=True)
        )

    def product_by_revenue_and_profit(self):
        return (
            self.df.groupby("Product", as_index=False)[["Revenue", "Profit"]]
            .sum()
            .sort_values("Revenue", ascending=True)
        )

    def revenue_by_sub_category(self):
        return self.df.groupby("Sub_Category", as_index=False)["Revenue"].sum()
