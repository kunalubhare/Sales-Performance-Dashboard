-- Sales Performance Dashboard SQL Queries

SELECT SUM(Sales) AS Total_Sales
FROM orders;

-- Sales by Category

SELECT
    Category,
    ROUND(SUM(Sales), 2) AS Total_Sales
FROM orders
GROUP BY Category
ORDER BY Total_Sales DESC;

-- Profit by Category

SELECT
    Category,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM orders
GROUP BY Category
ORDER BY Total_Profit DESC;

-- Top 10 Products by Sales

SELECT
    "Product Name",
    ROUND(SUM(Sales), 2) AS Total_Sales
FROM orders
GROUP BY "Product Name"
ORDER BY Total_Sales DESC
LIMIT 10;

-- Sales by Region

SELECT
    Region,
    ROUND(SUM(Sales), 2) AS Total_Sales
FROM orders
GROUP BY Region
ORDER BY Total_Sales DESC;

-- Sales by Customer Segment

SELECT
    Segment,
    ROUND(SUM(Sales), 2) AS Total_Sales
FROM orders
GROUP BY Segment
ORDER BY Total_Sales DESC;


-- Profit by Customer Segment

SELECT
    Segment,
    ROUND(SUM(Profit), 2) AS Total_Profit
FROM orders
GROUP BY Segment
ORDER BY Total_Profit DESC;


-- Top 10 Customers by Sales

SELECT
    "Customer Name",
    ROUND(SUM(Sales), 2) AS Total_Sales
FROM orders
GROUP BY "Customer Name"
ORDER BY Total_Sales DESC
LIMIT 10;


-- Average Order Value

SELECT
    ROUND(
        SUM(Sales) / COUNT(DISTINCT "Order ID"),
        2
    ) AS Average_Order_Value
FROM orders;


-- Sales by Market

SELECT
    Market,
    ROUND(SUM(Sales), 2) AS Total_Sales
FROM orders
GROUP BY Market
ORDER BY Total_Sales DESC;