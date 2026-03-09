-- Total Sales
SELECT SUM(Sales) AS Total_Sales
FROM sales_data;

-- Sales by Region
SELECT Region, SUM(Sales) AS Total_Sales
FROM sales_data
GROUP BY Region;

-- Top Selling Products
SELECT Product, SUM(Sales) AS Total_Sales
FROM sales_data
GROUP BY Product
ORDER BY Total_Sales DESC;

-- Sales by Category
SELECT Category, SUM(Sales) AS Total_Sales
FROM sales_data
GROUP BY Category;

-- Total Quantity Sold by Product
SELECT Product, SUM(Quantity) AS Total_Quantity
FROM sales_data
GROUP BY Product
ORDER BY Total_Quantity DESC;
