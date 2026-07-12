# Ecommerce Sales Analytics Dashboard

An interactive ecommerce sales analytics dashboard built from cleaned order
data, with parallel implementations in Streamlit (Python) and Tableau.

## Project Structure
├── app.py                          # Streamlit dashboard app
├── requirements.txt                # Python dependencies
├── data/
│   ├── raw/                        # Original, unprocessed order data
│   └── cleaned/                    # Cleaned dataset used by the app
├── sql/
│   ├── 01_create_database.sql
│   ├── 02_create_tables.sql
│   ├── 03_import_data.sql
│   ├── 04_data_cleaning.sql
│   ├── 05_analysis_queries.sql
│   └── 06_views.sql                # Reporting views (overview, category,
│                                    # state, monthly trend, products, status)
├── google_sheets/
│   └── Ecommerce_KPI_Calculation... # KPI calculations reference sheet
└── tableau/
├── Sales_Orders_Dashboard.twb   # Tableau workbook
├── Data/
│   └── sales_orders_tableau.csv # Data source used by the workbook
└── Tableau_Dashboard_Build_G...  # Build notes / guide

## Run the Streamlit Dashboard

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Open the Tableau Dashboard

Open `tableau/Sales_Orders_Dashboard.twb` in Tableau Desktop.

The workbook connects to `tableau/Data/sales_orders_tableau.csv` using a
relative path, so keep the `Data/` folder in place alongside the `.twb` file
— if you move one, move both together.

## Dashboard Layout

**KPIs:** Total Orders, Total Customers, Total Revenue, Average Order Value

**Charts:**
- Monthly sales trend (revenue over time)
- Revenue by category
- Revenue by state
- Top products (revenue + quantity sold)
- Order status summary (with % of total per status)

## Database & Analysis

The `sql/` folder contains the full pipeline used to build and analyze the
dataset:
1. Database and table creation
2. Data import and cleaning
3. Analysis queries (category, state, monthly trend, product performance,
   order status breakdown)
4. Reporting views consumed by the dashboards above

## License

See [LICENSE](./LICENSE).
A couple of things worth double-checking on your end before you commit this:

I truncated Ecommerce_KPI_Calculation... and Tableau_Dashboard_Build_G... in the tree since I can't see their full filenames from the screenshot — fill those in.
Confirm whether app.py actually reads from data/cleaned/ — if it reads a different file, update that line in Project Structure to match.
i use tableau not streamlit so give me perfect readme file according to my folder structure that i shared earlierResolved to deliver straightforward README tailored for TableauResolved to deliver straightforward README tailored for TableauGot it — here's a README rebuilt around your actual structure and Tableau-only workflow:
markdown# Ecommerce Sales Analytics Dashboard

A sales analytics dashboard for ecommerce order data, built in Tableau on top
of a cleaned dataset produced by a SQL data pipeline.

## Project Structure
├── data/
│   ├── raw/                          # Original, unprocessed order data
│   └── cleaned/                      # Cleaned dataset output by the SQL pipeline
├── sql/
│   ├── 01_create_database.sql
│   ├── 02_create_tables.sql
│   ├── 03_import_data.sql
│   ├── 04_data_cleaning.sql
│   ├── 05_analysis_queries.sql
│   └── 06_views.sql                  # Reporting views (overview, category,
│                                      # state, monthly trend, products, status)
├── google_sheets/
│   └── Ecommerce_KPI_Calculation...  # KPI calculations reference sheet
└── tableau/
├── Sales_Orders_Dashboard.twb    # Tableau workbook
├── Data/
│   └── sales_orders_tableau.csv  # Data source the workbook connects to
├── Tableau_Dashboard_Build_G...   # Build notes / guide
└── README.md                     # Tableau-specific notes

## Open the Dashboard

Open `tableau/Sales_Orders_Dashboard.twb` in Tableau Desktop.

The workbook connects to `tableau/Data/sales_orders_tableau.csv` using a
relative path, so the `Data/` folder must stay in the same directory as the
`.twb` file — if you move one, move both together.

## Dashboard Layout

**KPIs:** Total Orders, Total Customers, Total Revenue, Average Order Value

**Charts:**
- Monthly sales trend (revenue over time)
- Revenue by category
- Revenue by state
- Top products (revenue + quantity sold)
- Order status summary (with % of total per status)

## Data Pipeline

The `sql/` folder contains the full pipeline behind the cleaned dataset:

1. **Database & table setup** — `01_create_database.sql`, `02_create_tables.sql`
2. **Import & cleaning** — `03_import_data.sql`, `04_data_cleaning.sql`
3. **Analysis** — `05_analysis_queries.sql` (category, state, monthly trend,
   product performance, order status breakdown)
4. **Reporting views** — `06_views.sql`, consumed directly by the dashboard
