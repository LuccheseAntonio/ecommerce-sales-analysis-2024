# ============================================================
# E-Commerce Sales Analysis 2024
# Author: Antonio Lucchese | Data Analyst
# Tools: Python, Pandas, Plotly
# Dataset: Simulated Italian e-commerce sales data (500 orders)
# ============================================================

import pandas as pd
import plotly.graph_objects as go

# --- 1. LOAD DATA ---
df = pd.read_csv("ecommerce_sales_2024.csv", parse_dates=["order_date"])
df["month"] = df["order_date"].dt.to_period("M")

# --- 2. KEY METRICS ---
total_revenue   = df["revenue"].sum()
total_orders    = len(df)
unique_customers = df["customer_id"].nunique()
avg_order_value = total_revenue / total_orders

print(f"Total Revenue:        €{total_revenue:,.2f}")
print(f"Total Orders:         {total_orders}")
print(f"Unique Customers:     {unique_customers}")
print(f"Avg Order Value:      €{avg_order_value:.2f}")

# --- 3. REVENUE BY MONTH ---
monthly_revenue = df.groupby("month")["revenue"].sum()
print("\nTop 3 months by revenue:")
print(monthly_revenue.sort_values(ascending=False).head(3))

# --- 4. REVENUE BY CATEGORY ---
cat_revenue = df.groupby("category")["revenue"].sum().sort_values(ascending=False)
print("\nRevenue by category:")
print(cat_revenue)

# --- 5. DISCOUNT IMPACT ---
discount_analysis = df.groupby("discount").agg(
    orders=("order_id", "count"),
    avg_revenue=("revenue", "mean")
).round(2)
print("\nDiscount impact on avg order value:")
print(discount_analysis)

# --- 6. TOP 10 CUSTOMERS ---
top_customers = df.groupby("customer_id")["revenue"].sum().sort_values(ascending=False).head(10)
print("\nTop 10 customers by revenue:")
print(top_customers)

# --- INSIGHTS ---
print("\n=== KEY BUSINESS INSIGHTS ===")
print(f"1. Electronics drives {cat_revenue['Electronics']/total_revenue*100:.1f}% of total revenue")
print(f"2. Avg discount: {df['discount'].mean()*100:.1f}% — relatively low, margin-healthy")
print(f"3. Top 10 customers = {top_customers.sum()/total_revenue*100:.1f}% of revenue (concentration risk)")
