-- Dashboard Overview View
CREATE OR REPLACE VIEW vw_dashboard_overview AS
SELECT
    COUNT(*) AS total_orders,
    COUNT(DISTINCT name) AS total_customers,
    SUM(total) AS total_revenue,
    ROUND(AVG(total),2) AS average_order_value
FROM sales_orders;

--Revenue by Category
CREATE OR REPLACE VIEW vw_category_sales AS
SELECT
    category,
    SUM(total) AS revenue,
    COUNT(*) AS total_orders
FROM sales_orders
GROUP BY category
ORDER BY revenue DESC;

--Revenue by State
CREATE OR REPLACE VIEW vw_state_sales AS
SELECT
    state,
    SUM(total) AS revenue,
    COUNT(*) AS total_orders
FROM sales_orders
GROUP BY state
ORDER BY revenue DESC;

--Monthly Sales Trend
CREATE OR REPLACE VIEW vw_monthly_sales AS
SELECT
    DATE_TRUNC('month', "Date Placed") AS month,
    SUM(total) AS revenue,
    COUNT(*) AS total_orders
FROM sales_orders
GROUP BY DATE_TRUNC('month', "Date Placed")
ORDER BY month;

--Product Performance
CREATE OR REPLACE VIEW vw_product_sales AS
SELECT
    "Product Name",
    category,
    SUM(quantity) AS quantity_sold,
    SUM(total) AS revenue
FROM sales_orders
GROUP BY "Product Name", category
ORDER BY revenue DESC;

--Order Status Summary
CREATE OR REPLACE VIEW vw_order_status AS
SELECT
    status,
    COUNT(*) AS total_orders,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (),2) AS percentage
FROM sales_orders
GROUP BY status;



--Verify the Views
SELECT * FROM vw_dashboard_overview;
SELECT * FROM vw_category_sales;
SELECT * FROM vw_state_sales;
SELECT * FROM vw_monthly_sales;
SELECT * FROM vw_product_sales;
SELECT * FROM vw_order_status;