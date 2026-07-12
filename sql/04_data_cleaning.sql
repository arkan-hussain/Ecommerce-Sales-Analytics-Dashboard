/*
===========================================================
File: 04_data_cleaning.sql
Project: Ecommerce Sales Analytics Dashboard
Description:
Explore and clean the sales_orders table before analysis.
===========================================================
*/

-- Total records
SELECT COUNT(*) AS total_rows
FROM sales_orders;

-- Preview first 10 rows
SELECT *
FROM sales_orders
LIMIT 10;

SELECT *
FROM sales_orders
LIMIT 1;

SELECT COUNT(*) AS missing_id
FROM sales_orders
WHERE id IS NULL;

SELECT COUNT(*) AS missing_id
FROM sales_orders
WHERE id IS NULL;

SELECT COUNT(*) AS missing_total
FROM sales_orders
WHERE total IS NULL;

SELECT COUNT(*) AS missing_quantity
FROM sales_orders
WHERE quantity IS NULL;

SELECT *
FROM sales_orders
WHERE quantity IS NULL;

SELECT *
FROM sales_orders
WHERE quantity IS NULL;

SELECT DISTINCT status
FROM sales_orders
ORDER BY status;

SELECT DISTINCT category
FROM sales_orders
ORDER BY category;

SELECT DISTINCT iscod
FROM sales_orders
ORDER BY iscod;

SELECT
id,
COUNT(*) AS occurrences
FROM sales_orders
GROUP BY id
HAVING COUNT(*) > 1;