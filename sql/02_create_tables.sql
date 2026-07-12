CREATE TABLE sales_orders (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    city VARCHAR(100),
    state VARCHAR(100),
    address TEXT,
    iscod BOOLEAN,
    "Date Placed" TIMESTAMP,
    status VARCHAR(30),
    ivr VARCHAR(50),
    remarks TEXT,
    total NUMERIC(10,2),
    "Date Delivered" TIMESTAMP,
    "Date Returned" TIMESTAMP,
    pid TEXT,                -- Changed from INT to TEXT
    category VARCHAR(20),
    quantity INT,
    "Product Name" VARCHAR(255)
);