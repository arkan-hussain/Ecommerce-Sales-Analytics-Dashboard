/*
===========================================================
03_import_data.sql
Project: Ecommerce Sales Analytics Dashboard
Database: PostgreSQL
===========================================================

Data Import Method:
-------------------
The dataset was imported using DBeaver's "Import Data" wizard.

Source File:
------------
data/raw/E-Commerce Healthcare Dataset.csv

Target Table:
-------------
sales_orders

Steps:
------
1. Right-click sales_orders
2. Select "Import Data"
3. Choose CSV
4. Select the source dataset
5. Map columns automatically
6. Complete the import

Validation:
-----------
SELECT COUNT(*) FROM sales_orders;

Expected Result:
1590 rows imported successfully.
*/