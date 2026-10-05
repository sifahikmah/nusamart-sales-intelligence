
import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# =========================================================
# 1. Membaca Dataset
# =========================================================

df = pd.read_csv("nusamart_sales.csv")
df["date"] = pd.to_datetime(df["date"])


# =========================================================
# 2. KPI
# =========================================================

total_revenue = df["revenue"].sum()
total_transactions = df.shape[0]
total_quantity = df["quantity"].sum()
average_transaction = df["revenue"].mean()


# =========================================================
# 3. Monthly Revenue
# =========================================================

df["month"] = df["date"].dt.to_period("M")

monthly_revenue = df.groupby("month")["revenue"].sum()


# =========================================================
# 4. Category Performance
# =========================================================

category_revenue = (
    df.groupby("category")["revenue"]
    .sum()
    .sort_values(ascending=False)
)


# =========================================================
# 5. Product Performance
# =========================================================

product_revenue = (
    df.groupby("product")["revenue"]
    .sum()
    .sort_values(ascending=False)
)


# =========================================================
# 6. Geographic Analysis
# =========================================================

city_revenue = (
    df.groupby("city")["revenue"]
    .sum()
    .sort_values(ascending=False)
)


# =========================================================
# 7. Sales Forecast
# =========================================================

monthly_sales = monthly_revenue.reset_index()

# Lag features
monthly_sales["lag_1"] = monthly_sales["revenue"].shift(1)
monthly_sales["lag_2"] = monthly_sales["revenue"].shift(2)
monthly_sales["lag_3"] = monthly_sales["revenue"].shift(3)

# Fitur waktu
monthly_sales["month_num"] = monthly_sales["month"].dt.month
monthly_sales["year"] = monthly_sales["month"].dt.year

# Data untuk training
model_data = monthly_sales.dropna().copy()

final_features = [
    "lag_1",
    "lag_2",
    "lag_3",
    "month_num",
    "year"
]

X_train = model_data[final_features]
y_train = model_data["revenue"]

# Model final
final_model = RandomForestRegressor(
    n_estimators=200,
    max_depth=5,
    random_state=42
)

final_model.fit(X_train, y_train)


# =========================================================
# 8. Forecast September 2025
# =========================================================

future_data = pd.DataFrame({
    "lag_1": [monthly_revenue.loc["2025-08"]],
    "lag_2": [monthly_revenue.loc["2025-07"]],
    "lag_3": [monthly_revenue.loc["2025-06"]],
    "month_num": [9],
    "year": [2025]
})

predicted_september = final_model.predict(
    future_data[final_features]
)[0]

august_revenue = monthly_revenue.loc["2025-08"]

increase = predicted_september - august_revenue
increase_percentage = (increase / august_revenue) * 100


# =========================================================
# 9. Dashboard
# =========================================================

st.title("NusaMart Sales Intelligence")

st.write(
    "Dashboard analitik penjualan untuk memantau performa "
    "bisnis dan memproyeksikan revenue."
)


# =========================================================
# 10. KPI
# =========================================================

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Revenue",
    f"Rp {total_revenue:,.0f}"
)

col2.metric(
    "Transactions",
    f"{total_transactions:,}"
)

col3.metric(
    "Quantity",
    f"{total_quantity:,}"
)

col4.metric(
    "Avg Transaction",
    f"Rp {average_transaction:,.0f}"
)


# =========================================================
# 11. Monthly Revenue
# =========================================================

st.subheader("Monthly Revenue")

monthly_chart = monthly_revenue.copy()
monthly_chart.index = monthly_chart.index.astype(str)

st.line_chart(monthly_chart)


# =========================================================
# 12. Category Performance
# =========================================================

st.subheader("Revenue by Category")

st.bar_chart(category_revenue)


# =========================================================
# 13. Product Performance
# =========================================================

st.subheader("Top Products by Revenue")

st.bar_chart(product_revenue)


# =========================================================
# 14. Geographic Analysis
# =========================================================

st.subheader("Revenue by City")

st.bar_chart(city_revenue)


# =========================================================
# 15. Sales Forecast
# =========================================================

st.subheader("Sales Forecast")

forecast_col1, forecast_col2 = st.columns(2)

forecast_col1.metric(
    "Predicted Revenue — Sep 2025",
    f"Rp {predicted_september:,.0f}"
)

forecast_col2.metric(
    "Predicted Growth",
    f"{increase_percentage:.2f}%"
)

st.caption(
    "Forecast generated using Random Forest based on "
    "the previous three months' revenue and time features."
)
