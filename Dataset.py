# import pandas as pd
# import numpy as np

# np.random.seed(42)

# rows = 500000

# countries = {
#     "USA": ("North America", 1.2),
#     "India": ("Asia", 0.6),
#     "Germany": ("Europe", 1.0),
#     "UK": ("Europe", 1.1),
#     "UAE": ("Middle East", 1.3),
#     "Brazil": ("South America", 0.7),
#     "China": ("Asia", 1.1),
#     "Australia": ("Oceania", 1.0)
# }

# channels = ["Online", "Retail", "Wholesale"]
# categories = ["Shoes", "Apparel", "Accessories"]

# data = []

# # 📅 Date Range
# start_date = pd.to_datetime("2018-01-01")
# end_date = pd.to_datetime("2026-04-25")
# date_range_days = (end_date - start_date).days

# for _ in range(rows):
#     country = np.random.choice(list(countries.keys()))
#     region, multiplier = countries[country]

#     # 📅 Random Date
#     date = start_date + pd.to_timedelta(
#         np.random.randint(0, date_range_days), unit="D"
#     )

#     channel = np.random.choice(channels, p=[0.5, 0.3, 0.2])
#     category = np.random.choice(categories, p=[0.5, 0.3, 0.2])

#     base_units = np.random.randint(1, 20)
#     units = int(base_units * multiplier)

#     base_price = {
#         "Shoes": 100,
#         "Apparel": 60,
#         "Accessories": 30
#     }[category]

#     price = base_price * multiplier

#     discount = np.random.uniform(0.05, 0.4 if country in ["India", "Brazil"] else 0.25)

#     revenue = units * price * (1 - discount)
#     cost = revenue * np.random.uniform(0.5, 0.75)
#     profit = revenue - cost

#     marketing_spend = revenue * np.random.uniform(0.05, 0.15)
#     roi = revenue / marketing_spend if marketing_spend > 0 else 0

#     data.append([
#         date, country, region, channel, category,
#         units, round(revenue,2), round(cost,2), round(profit,2),
#         round(discount,2), round(marketing_spend,2), round(roi,2)
#     ])

# df = pd.DataFrame(data, columns=[
#     "Date","Country","Region","Channel","Category",
#     "Units Sold","Revenue","Cost","Profit",
#     "Discount","Marketing Spend","ROI"
# ])

# df.to_csv("adidas_global_sales.csv", index=False)
# print("Dataset generated!")



# import pandas as pd
# import numpy as np

# np.random.seed(42)

# rows = 500000

# countries = {
#     "USA": ("North America", 1.2),
#     "India": ("Asia", 0.6),
#     "Germany": ("Europe", 1.0),
#     "UK": ("Europe", 1.1),
#     "UAE": ("Middle East", 1.3),
#     "Brazil": ("South America", 0.7),
#     "China": ("Asia", 1.1),
#     "Australia": ("Oceania", 1.0)
# }

# channels = ["Online", "Retail", "Wholesale"]
# categories = ["Shoes", "Apparel", "Accessories"]

# data = []

# # 📅 Date Range
# start_date = pd.to_datetime("2018-01-01")
# end_date = pd.to_datetime("2026-04-25")
# date_range_days = (end_date - start_date).days

# for _ in range(rows):
#     country = np.random.choice(list(countries.keys()))
#     region, multiplier = countries[country]

#     # 📅 Random Date
#     date = start_date + pd.to_timedelta(
#         np.random.randint(0, date_range_days), unit="D"
#     )

#     channel = np.random.choice(channels, p=[0.5, 0.3, 0.2])
#     category = np.random.choice(categories, p=[0.5, 0.3, 0.2])

#     # 🧠 Units variation
#     base_units = np.random.randint(1, 20)
#     units = int(base_units * multiplier)

#     # 💰 Base Price
#     base_price = {
#         "Shoes": 100,
#         "Apparel": 60,
#         "Accessories": 30
#     }[category]

#     price = base_price * multiplier

#     # 🎯 Discount variation (emerging markets higher discount)
#     discount = np.random.uniform(0.05, 0.4 if country in ["India", "Brazil"] else 0.25)

#     # 📈 Base Revenue
#     revenue = units * price * (1 - discount)

#     # ============================
#     # 🔥 REALISM STARTS HERE
#     # ============================

#     # 📈 1. Growth Trend (yearly)
#     year_factor = 1 + (date.year - 2018) * 0.08
#     revenue *= year_factor

#     # 🎄 2. Seasonality
#     month = date.month
#     if month in [10, 11, 12]:       # festive / holidays
#         season_factor = 1.3
#     elif month in [6, 7]:           # slow season
#         season_factor = 0.85
#     else:
#         season_factor = 1

#     revenue *= season_factor

#     # 🦠 3. Special Event (COVID dip)
#     if date.year == 2020:
#         revenue *= 0.8

#     # 📊 4. Random noise (real fluctuation)
#     noise = np.random.normal(1, 0.1)
#     revenue *= noise

#     # 📢 5. Marketing Spend
#     marketing_spend = revenue * np.random.uniform(0.05, 0.15)

#     # 🚀 Marketing boost effect
#     if marketing_spend > revenue * 0.12:
#         revenue *= 1.2

#     # 💸 6. Cost
#     base_cost = price * np.random.uniform(0.4, 0.7)
#      cost = units * base_cost

#     # 💰 7. FINAL Profit (correct formula)
#     profit = revenue - cost - marketing_spend

#     # 📊 8. ROI
#     roi = revenue / marketing_spend if marketing_spend > 0 else 0

#     data.append([
#         date, country, region, channel, category,
#         units,
#         round(revenue, 2),
#         round(cost, 2),
#         round(profit, 2),
#         round(discount, 2),
#         round(marketing_spend, 2),
#         round(roi, 2)
#     ])

# df = pd.DataFrame(data, columns=[
#     "Date", "Country", "Region", "Channel", "Category",
#     "Units Sold", "Revenue", "Cost", "Profit",
#     "Discount", "Marketing Spend", "ROI"
# ])

# df.to_csv("adidas_global_sales.csv", index=False)

# print("✅ Realistic dataset generated!")


import pandas as pd
import numpy as np

np.random.seed(42)

rows = 500000

countries = {
    "USA": ("North America", 1.2),
    "India": ("Asia", 0.6),
    "Germany": ("Europe", 1.0),
    "UK": ("Europe", 1.1),
    "UAE": ("Middle East", 1.3),
    "Brazil": ("South America", 0.7),
    "China": ("Asia", 1.1),
    "Australia": ("Oceania", 1.0)
}

channels = ["Online", "Retail", "Wholesale"]
categories = ["Shoes", "Apparel", "Accessories"]

data = []

# 📅 Date Range
start_date = pd.to_datetime("2018-01-01")
end_date = pd.to_datetime("2026-04-25")
date_range_days = (end_date - start_date).days

for _ in range(rows):
    # 🌍 Country & Region
    country = np.random.choice(list(countries.keys()))
    region, multiplier = countries[country]

    # 📅 Random Date
    date = start_date + pd.to_timedelta(
        np.random.randint(0, date_range_days), unit="D"
    )

    # 🛒 Channel & Category
    channel = np.random.choice(channels, p=[0.5, 0.3, 0.2])
    category = np.random.choice(categories, p=[0.5, 0.3, 0.2])

    # 📦 Units (demand variation by country)
    base_units = np.random.randint(1, 20)
    units = int(base_units * multiplier)

    # 💰 Base Price
    base_price = {
        "Shoes": 100,
        "Apparel": 60,
        "Accessories": 30
    }[category]

    price = base_price * multiplier * np.random.uniform(0.9, 1.2)

    # 🎯 Discount behavior
    discount = np.random.uniform(
        0.05,
        0.4 if country in ["India", "Brazil"] else 0.25
    )

    # 📈 Demand reaction to discount
    if discount > 0.25:
        units *= np.random.uniform(1.2, 1.5)
    elif discount < 0.1:
        units *= np.random.uniform(0.8, 1.0)

    units = int(units)

    # =========================
    # 📊 REVENUE CALCULATION
    # =========================
    revenue = units * price * (1 - discount)

    # 📈 Growth Trend (yearly)
    year_factor = 1 + (date.year - 2018) * 0.08
    revenue *= year_factor

    # 🎄 Seasonality
    if date.month in [10, 11, 12]:
        revenue *= 1.3
    elif date.month in [6, 7]:
        revenue *= 0.85

    # 🦠 COVID dip
    if date.year == 2020:
        revenue *= 0.8

    # 📊 Random fluctuation
    revenue *= np.random.normal(1, 0.1)

    # =========================
    # 📢 MARKETING
    # =========================
    marketing_spend = revenue * np.random.uniform(0.05, 0.15)

    # Marketing boost effect
    if marketing_spend > revenue * 0.12:
        revenue *= 1.2

    # =========================
    # 💸 COST
    # =========================
    base_cost = price * np.random.uniform(0.4, 0.7)
    cost = units * base_cost

    # Cost inflation over time
    cost *= (1 + (date.year - 2018) * 0.05)

    # =========================
    # 💰 PROFIT
    # =========================
    profit = revenue - cost - marketing_spend

    # 📊 ROI
    roi = revenue / marketing_spend if marketing_spend > 0 else 0

    # Store row
    data.append([
        date, country, region, channel, category,
        units,
        round(revenue, 2),
        round(cost, 2),
        round(profit, 2),
        round(discount, 2),
        round(marketing_spend, 2),
        round(roi, 2)
    ])

# =========================
# 📄 CREATE DATAFRAME
# =========================
df = pd.DataFrame(data, columns=[
    "Date", "Country", "Region", "Channel", "Category",
    "Units Sold", "Revenue", "Cost",
    "Profit",
    "Discount", "Marketing Spend", "ROI"
])

# Save file
df.to_csv("adidas_global_sales.csv", index=False)

print("✅ Realistic dataset generated successfully!")