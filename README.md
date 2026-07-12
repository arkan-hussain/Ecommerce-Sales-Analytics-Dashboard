# Ecommerce Sales Analytics Dashboard

An interactive ecommerce sales analytics dashboard built from the cleaned order
dataset in `data/cleaned/sales_orders.csv`.

## Run the Dashboard

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Open the Tableau Dashboard

Open `tableau/Ecommerce_Sales_Analytics_Dashboard.twbx` in Tableau Desktop. The
packaged workbook includes the Tableau-ready CSV and the requested dashboard
layout.

## Dashboard Layout

- Filters: Date, State, Category, Status
- KPIs: Revenue, Orders, Average Order Value, COD %, Delivered %
- Charts: Revenue trend, category sales, order status, top products, state-wise
  revenue, and top cities by revenue

The SQL folder keeps the database setup, cleaning, and analysis queries used for
the project documentation.
