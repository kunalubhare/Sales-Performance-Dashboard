import pandas as pd
import matplotlib.pyplot as plt

# ==========================
# LOAD DATASET
# ==========================

df = pd.read_excel(
    r"C:\Users\lenov\Desktop\Projects\Sales Performance Dashboard\data\Superstore Dataset.xlsx",
    sheet_name="Orders"
)

# ==========================
# DATASET OVERVIEW
# ==========================

print("Shape:", df.shape)

print("\nColumns:")
print(df.columns)

print("\nDataset Info:")
df.info()

# ==========================
# KPI ANALYSIS
# ==========================

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_quantity = df["Quantity"].sum()

print("\n========== KPI SUMMARY ==========")
print(f"Total Sales: ${total_sales:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Total Quantity Sold: {total_quantity:,}")

# ==========================
# CATEGORY ANALYSIS
# ==========================

print("\n========== SALES BY CATEGORY ==========")
print(df.groupby("Category")["Sales"].sum())

print("\n========== PROFIT BY CATEGORY ==========")
print(df.groupby("Category")["Profit"].sum())

# ==========================
# TOP 10 PRODUCTS BY SALES
# ==========================

top_products = (
    df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\n========== TOP 10 PRODUCTS BY SALES ==========")
print(top_products)

# ==========================
# CHART 1: SALES BY CATEGORY
# ==========================

category_sales = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(8, 5))
category_sales.plot(kind="bar")

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")

plt.tight_layout()

plt.savefig(
    r"C:\Users\lenov\Desktop\Projects\Sales Performance Dashboard\images\sales_by_category.png"
)

plt.show()


# ==========================
# CHART 2: TOP 10 PRODUCTS
# ==========================

plt.figure(figsize=(12, 6))

top_products.plot(kind="bar")

plt.title("Top 10 Products by Sales")
plt.xlabel("Product Name")
plt.ylabel("Sales")

plt.xticks(rotation=45, ha="right")

plt.tight_layout()

plt.savefig(
    r"C:\Users\lenov\Desktop\Projects\Sales Performance Dashboard\images\top_10_products.png"
)

plt.show()


# ==========================
# SALES BY REGION
# ==========================

region_sales = (
    df.groupby("Region")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print("\n========== SALES BY REGION ==========")
print(region_sales)


# ==========================
# CHART 3: SALES BY REGION
# ==========================

import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))

region_sales.head(10).plot(kind="bar")

plt.title("Top 10 Regions by Sales")
plt.xlabel("Region")
plt.ylabel("Sales")

plt.tight_layout()

plt.savefig(
    r"C:\Users\lenov\Desktop\Projects\Sales Performance Dashboard\images\sales_by_region.png"
)

plt.show()


# ==========================
# MONTHLY SALES TREND
# ==========================

df["Month"] = df["Order Date"].dt.to_period("M")

monthly_sales = (
    df.groupby("Month")["Sales"]
    .sum()
)

print("\n========== MONTHLY SALES TREND ==========")
print(monthly_sales)


# ==========================
# CHART 4: MONTHLY SALES TREND
# ==========================

plt.figure(figsize=(14, 6))

monthly_sales.plot(kind="line")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.tight_layout()

plt.savefig(
    r"C:\Users\lenov\Desktop\Projects\Sales Performance Dashboard\images\monthly_sales_trend.png"
)

plt.show()