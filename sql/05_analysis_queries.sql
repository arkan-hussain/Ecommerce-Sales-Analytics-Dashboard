-- Total Revenue
SELECT
    SUM(total) AS total_revenue
FROM sales_orders;


-- Total Orders
SELECT
    COUNT(*) AS total_orders
FROM sales_orders;

-- Unique Customers
SELECT
    COUNT(DISTINCT name) AS total_customers
FROM sales_orders;

-- Average Order Value
SELECT
    ROUND(AVG(total),2) AS average_order_value
FROM sales_orders;

--Revenue by Category
SELECT
    category,
    SUM(total) AS revenue
FROM sales_orders
GROUP BY category
ORDER BY revenue DESC;

-- Orders by Category
SELECT
    category,
    COUNT(*) AS total_orders
FROM sales_orders
GROUP BY category
ORDER BY total_orders DESC;

--Revenue by Product
SELECT
    "Product Name",
    SUM(total) AS revenue
FROM sales_orders
GROUP BY "Product Name"
ORDER BY revenue DESC;

--Top 10 Products
SELECT
    "Product Name",
    SUM(total) AS revenue
FROM sales_orders
GROUP BY "Product Name"
ORDER BY revenue DESC
LIMIT 10;

--Order Status Distribution
SELECT
    status,
    COUNT(*) AS orders
FROM sales_orders
GROUP BY status
ORDER BY orders DESC;

--Revenue by State
SELECT
    state,
    SUM(total) AS revenue
FROM sales_orders
GROUP BY state
ORDER BY revenue DESC;

--Revenue by City
SELECT
    city,
    SUM(total) AS revenue
FROM sales_orders
GROUP BY city
ORDER BY revenue DESC
LIMIT 20;

--Monthly Revenue
SELECT
    DATE_TRUNC('month', "Date Placed") AS month,
    SUM(total) AS revenue
FROM sales_orders
GROUP BY month
ORDER BY month;

--Monthly Orders
SELECT
    DATE_TRUNC('month', "Date Placed") AS month,
    COUNT(*) AS orders
FROM sales_orders
GROUP BY month
ORDER BY month;

--Delivered vs Returned vs RTO
SELECT
    status,
    COUNT(*) AS total_orders,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (),2) AS percentage
FROM sales_orders
GROUP BY status;


--COD vs Prepaid Orders
SELECT
    iscod,
    COUNT(*) AS orders
FROM sales_orders
GROUP BY iscod;

--Average Revenue per Category
SELECT
    category,
    ROUND(AVG(total),2) AS avg_revenue
FROM sales_orders
GROUP BY category
ORDER BY avg_revenue DESC;

--Top States by Orders
SELECT
    state,
    COUNT(*) AS total_orders
FROM sales_orders
GROUP BY state
ORDER BY total_orders DESC
LIMIT 10;

--Top Cities by Orders
SELECT
    city,
    COUNT(*) AS total_orders
FROM sales_orders
GROUP BY city
ORDER BY total_orders DESC
LIMIT 10;

--Highest Value Orders
SELECT
    id,
    name,
    city,
    total
FROM sales_orders
ORDER BY total DESC
LIMIT 20;

--Product Performance
SELECT
    "Product Name",
    category,
    SUM(quantity) AS quantity_sold,
    SUM(total) AS revenue
FROM sales_orders
GROUP BY "Product Name", category
ORDER BY revenue DESC;