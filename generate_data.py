import numpy as np
import pandas as pd
from pathlib import Path

np.random.seed(42)
N = 100_000

# Date range (2 years)
dates = pd.date_range("2024-01-01", "2025-09-01", freq="H")
order_dates = np.random.choice(dates, size=N)

# Dimensions
states = ["Maharashtra","Karnataka","Delhi","Gujarat","Tamil Nadu","West Bengal","Rajasthan","Telangana","Kerala"]
cities_by_state = {
    "Maharashtra":["Mumbai","Pune","Nashik","Nagpur"],
    "Karnataka":["Bengaluru","Mysuru","Mangalore"],
    "Delhi":["Delhi"],
    "Gujarat":["Ahmedabad","Surat","Vadodara"],
    "Tamil Nadu":["Chennai","Coimbatore","Madurai"],
    "West Bengal":["Kolkata","Siliguri"],
    "Rajasthan":["Jaipur","Udaipur"],
    "Telangana":["Hyderabad","Warangal"],
    "Kerala":["Kochi","Thiruvananthapuram","Kozhikode"],
}
state = np.random.choice(states, size=N, p=[.18,.1,.08,.1,.1,.08,.08,.12,.16])

def pick_city(s):
    return np.random.choice(cities_by_state[s])

city = np.array([pick_city(s) for s in state])

channels = ["Online","Store"]
channel = np.random.choice(channels, size=N, p=[0.65, 0.35])
payment = np.random.choice(["UPI","Card","COD","NetBanking"], size=N, p=[0.45,0.35,0.15,0.05])

cats = ["Jeans","Tops","Dresses","Accessories","Footwear","Outerwear"]
subcats = {
    "Jeans":["Slim","Straight","Wide","Cargo"],
    "Tops":["Shirt","Tee","Crop","Blouse"],
    "Dresses":["Skater","Bodycon","A-Line","Maxi"],
    "Accessories":["Cap","Belt","Bag","Socks"],
    "Footwear":["Sneaker","Boot","Sandal","Loafer"],
    "Outerwear":["Jacket","Hoodie","Coat","Blazer"]
}
category = np.random.choice(cats, size=N, p=[.28,.22,.16,.1,.14,.1])

def pick_subcat(c):
    return np.random.choice(subcats[c])

subcategory = np.array([pick_subcat(c) for c in category])

product_id = np.array([f"P{hash((category[i],subcategory[i]))%9999:04d}" for i in range(N)])
unit_price = np.round(np.random.lognormal(mean=3.2, sigma=0.45, size=N), 2)  # ~Rs 10-200
quantity = np.random.choice([1,2,3,4,5], size=N, p=[.65,.2,.1,.04,.01])
discount_pct = np.round(np.clip(np.random.normal(0.12, 0.10, size=N), 0, 0.6), 2)

# Costs & revenue
cost_per_unit = np.round(unit_price * np.random.uniform(0.45, 0.8, size=N), 2)
gross = unit_price * quantity
discount_amount = gross * discount_pct
net_revenue = gross - discount_amount
cogs = cost_per_unit * quantity
profit = np.round(net_revenue - cogs, 2)
margin_pct = np.round(np.where(net_revenue>0, profit / net_revenue, 0), 4)

customer_id = np.random.randint(10000, 99999, size=N)
order_id = np.arange(1, N+1)

status = np.random.choice(["Completed","Returned","Cancelled"], size=N, p=[0.92,0.04,0.04])
# If returned/cancelled, revenue & profit ~0
mask_bad = status != "Completed"
net_revenue[mask_bad] = 0
profit[mask_bad] = 0
margin_pct[mask_bad] = 0

df = pd.DataFrame({
    "order_id": order_id,
    "order_datetime": pd.to_datetime(order_dates),
    "customer_id": customer_id,
    "state": state,
    "city": city,
    "channel": channel,
    "payment_method": payment,
    "product_id": product_id,
    "category": category,
    "subcategory": subcategory,
    "unit_price": unit_price,
    "quantity": quantity,
    "discount_pct": discount_pct,
    "net_revenue": np.round(net_revenue,2),
    "cogs": np.round(cogs,2),
    "profit": profit,
    "margin_pct": margin_pct,
    "status": status
})

# Save
Path("data/raw").mkdir(parents=True, exist_ok=True)
df.to_csv("data/raw/transactions.csv", index=False)
print("Saved data/raw/transactions.csv with", len(df), "rows")
