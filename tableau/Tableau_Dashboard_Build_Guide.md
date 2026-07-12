# Tableau Dashboard Build Guide

Open `Ecommerce_Sales_Analytics_Dashboard.twbx` in Tableau Desktop. The package
contains `Data/sales_orders_tableau.csv`, already cleaned and renamed for
Tableau.

## Dashboard Size

- Fixed size: `1366 x 900`
- Dashboard title: `Ecommerce Sales Analytics Dashboard`
- Layout order:
  - Filters: Date, State, Category, Status
  - KPI row: Revenue, Orders, AOV, COD %, Delivered %
  - Row 1: Revenue Trend, Sales by Category
  - Row 2: Order Status, Top Products
  - Row 3: State-wise Revenue, Top Cities by Revenue

## Calculated Fields

Create these if Tableau does not preserve the generated workbook fields exactly:

```text
Revenue
SUM([Revenue])

Orders
COUNTD([Order ID])

AOV
SUM([Revenue]) / COUNTD([Order ID])

COD %
AVG([COD Flag])

Delivered %
AVG([Delivered Flag])
```

Format `Revenue` and `AOV` as currency with 0 decimals. Format `COD %` and
`Delivered %` as percentages with 1 decimal.

## Worksheets

### KPI Sheets

Create one text sheet each for:

- `KPI - Revenue`: Text = `SUM([Revenue])`
- `KPI - Orders`: Text = `COUNTD([Order ID])`
- `KPI - AOV`: Text = `AOV`
- `KPI - COD Percent`: Text = `COD %`
- `KPI - Delivered Percent`: Text = `Delivered %`

### Revenue Trend

- Columns: `Order Date`
- Rows: `SUM([Revenue])`
- Marks: Line
- Tooltip: `Order Date`, `Revenue`, `Orders`

### Sales by Category

- Rows: `Category`
- Columns: `SUM([Revenue])`
- Marks: Bar
- Sort: Descending by `SUM([Revenue])`

### Order Status Donut

- Create calculated field `One` with value `1`
- Columns: `MIN([One])`, then duplicate it once
- First Marks card:
  - Mark type: Pie
  - Color: `Status`
  - Angle: `COUNTD([Order ID])`
  - Label: `Status` and percent of total
- Second Marks card:
  - Mark type: Pie
  - Color: White or dashboard background
  - Size: Smaller than the first pie
- Right-click the second axis and choose Dual Axis
- Synchronize axis, hide headers, and remove gridlines

### Top Products

- Rows: `Product Name`
- Columns: `SUM([Revenue])`
- Marks: Bar
- Filter: Top 10 by `SUM([Revenue])`
- Sort: Descending

### State-wise Revenue

- Rows: `State`
- Columns: `SUM([Revenue])`
- Marks: Bar
- Sort: Descending

### Top Cities by Revenue

- Rows: `City`
- Columns: `SUM([Revenue])`
- Marks: Bar
- Filter: Top 15 by `SUM([Revenue])`
- Sort: Descending

## Dashboard Filters

Add these dashboard filters and apply them to all worksheets using this data
source:

- `Order Date`: Range of dates
- `State`: Multiple values dropdown
- `Category`: Multiple values dropdown
- `Status`: Multiple values dropdown

