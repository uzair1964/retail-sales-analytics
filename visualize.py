import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine
from pathlib import Path

sns.set(style="whitegrid")
Path("reports/figures").mkdir(parents=True, exist_ok=True)

engine = create_engine("sqlite:///database/sales.db")
df = pd.read_sql("SELECT * FROM transactions", engine, parse_dates=["order_datetime"])

# Monthly revenue
monthly = (df[df["status"]=="Completed"]
           .groupby(df["order_datetime"].dt.to_period("M"))
           .agg(revenue=("net_revenue","sum"), profit=("profit","sum"))
           .reset_index())
monthly["ym"] = monthly["order_datetime"].astype(str)

plt.figure(figsize=(10,5))
sns.lineplot(data=monthly, x="ym", y="revenue", marker="o")
plt.xticks(rotation=45, ha="right")
plt.title("Monthly Revenue")
plt.tight_layout()
plt.savefig("reports/figures/monthly_revenue.png", dpi=150)

# Category mix
cat = df.groupby("category", as_index=False).agg(revenue=("net_revenue","sum"))
cat = cat.sort_values("revenue", ascending=False)

plt.figure(figsize=(8,5))
sns.barplot(data=cat, x="revenue", y="category")
plt.title("Revenue by Category")
plt.tight_layout()
plt.savefig("reports/figures/revenue_by_category.png", dpi=150)

# City x Channel top combos
cc = (df.groupby(["city","channel"], as_index=False)
        .agg(revenue=("net_revenue","sum"), margin=("margin_pct","mean"))
        .sort_values("revenue", ascending=False)
        .head(12))

plt.figure(figsize=(10,6))
sns.barplot(data=cc, x="revenue", y="city", hue="channel")
plt.title("Top City-Channel Pairs by Revenue")
plt.tight_layout()
plt.savefig("reports/figures/top_city_channel.png", dpi=150)

# Margin distribution (Completed)
comp = df[df["status"]=="Completed"].copy()
plt.figure(figsize=(8,5))
sns.histplot(comp["margin_pct"], bins=40, kde=True)
plt.title("Margin Distribution (Completed Orders)")
plt.tight_layout()
plt.savefig("reports/figures/margin_distribution.png", dpi=150)

print("Saved charts into reports/figures/")
