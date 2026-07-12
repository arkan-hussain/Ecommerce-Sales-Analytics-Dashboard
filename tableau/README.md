# Tableau Files

- `Sales_Orders_Dashboard.twb`: Tableau workbook containing the dashboard
  sheets, KPIs, and layout.
- `Data/sales_orders_tableau.csv`: Tableau-friendly cleaned dataset the
  workbook connects to via a relative path.
- `Tableau_Dashboard_Build_Guide.md`: exact field, sheet, filter, and layout
  instructions for final polish inside Tableau Desktop.

Open `Sales_Orders_Dashboard.twb` in Tableau Desktop 2026.2 or newer. Keep the
`Data/` folder in the same directory as the `.twb` file — the workbook
references the CSV by relative path, so moving one without the other will
break the connection.
