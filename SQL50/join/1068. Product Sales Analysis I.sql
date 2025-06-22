# LeetCode 1068. Product Sales Analysis I
# Difficulty: Easy
# Topic: SQL, JOIN
"""
Problem Description:
------------------
Table: Sales

+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| sale_id     | int   |
| product_id  | int   |
| year        | int   |
| quantity    | int   |
| price       | int   |
+-------------+-------+
(sale_id, year) is the primary key (combination of columns with unique values) of this table.
product_id is a foreign key (reference column) to Product table.
Each row of this table shows a sale on the product product_id in a certain year.
Note that the price is per unit.

Table: Product

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| product_id   | int     |
| product_name | varchar |
+--------------+---------+
product_id is the primary key (column with unique values) of this table.
Each row of this table indicates the product name of each product.

Write a solution to report the product_name, year, and price for each sale_id in the Sales table.

Return the resulting table in any order.

Example 1:
Input: 
Sales table:
+---------+------------+------+----------+-------+
| sale_id | product_id | year | quantity | price |
+---------+------------+------+----------+-------+ 
| 1       | 100        | 2008 | 10       | 5000  |
| 2       | 100        | 2009 | 12       | 5000  |
| 7       | 200        | 2011 | 15       | 9000  |
+---------+------------+------+----------+-------+
Product table:
+------------+--------------+
| product_id | product_name |
+------------+--------------+
| 100        | Nokia        |
| 200        | Apple        |
| 300        | Samsung      |
+------------+--------------+
Output: 
+--------------+-------+-------+
| product_name | year  | price |
+--------------+-------+-------+
| Nokia        | 2008  | 5000  |
| Nokia        | 2009  | 5000  |
| Apple        | 2011  | 9000  |
+--------------+-------+-------+
Explanation: 
From sale_id = 1, we can conclude that Nokia was sold for 5000 in the year 2008.
From sale_id = 2, we can conclude that Nokia was sold for 5000 in the year 2009.
From sale_id = 7, we can conclude that Apple was sold for 9000 in the year 2011.
"""

-- Solution
SELECT 
    p.product_name, 
    s.year, 
    s.price
FROM 
    Sales s
JOIN 
    Product p 
    ON s.product_id = p.product_id;

-- Test Cases
/*
Test Case 1: Basic case with multiple sales
Input:
INSERT INTO Sales (sale_id, product_id, year, quantity, price) VALUES
(1, 100, 2008, 10, 5000),
(2, 100, 2009, 12, 5000),
(7, 200, 2011, 15, 9000);

INSERT INTO Product (product_id, product_name) VALUES
(100, 'Nokia'),
(200, 'Apple'),
(300, 'Samsung');

Expected Output:
+--------------+-------+-------+
| product_name | year  | price |
+--------------+-------+-------+
| Nokia        | 2008  | 5000  |
| Nokia        | 2009  | 5000  |
| Apple        | 2011  | 9000  |
+--------------+-------+-------+

Test Case 2: Single product with multiple years
Input:
INSERT INTO Sales (sale_id, product_id, year, quantity, price) VALUES
(1, 100, 2020, 5, 1000),
(2, 100, 2021, 8, 1200),
(3, 100, 2022, 10, 1500);

INSERT INTO Product (product_id, product_name) VALUES
(100, 'iPhone');

Expected Output:
+--------------+-------+-------+
| product_name | year  | price |
+--------------+-------+-------+
| iPhone       | 2020  | 1000  |
| iPhone       | 2021  | 1200  |
| iPhone       | 2022  | 1500  |
+--------------+-------+-------+

Test Case 3: Multiple products with same year
Input:
INSERT INTO Sales (sale_id, product_id, year, quantity, price) VALUES
(1, 100, 2023, 20, 500),
(2, 200, 2023, 15, 800),
(3, 300, 2023, 25, 300);

INSERT INTO Product (product_id, product_name) VALUES
(100, 'Laptop'),
(200, 'Tablet'),
(300, 'Phone');

Expected Output:
+--------------+-------+-------+
| product_name | year  | price |
+--------------+-------+-------+
| Laptop       | 2023  | 500   |
| Tablet       | 2023  | 800   |
| Phone        | 2023  | 300   |
+--------------+-------+-------+

Test Case 4: Products with no sales
Input:
INSERT INTO Sales (sale_id, product_id, year, quantity, price) VALUES
(1, 100, 2023, 10, 1000);

INSERT INTO Product (product_id, product_name) VALUES
(100, 'Product A'),
(200, 'Product B');  -- No sales for this product

Expected Output:
+--------------+-------+-------+
| product_name | year  | price |
+--------------+-------+-------+
| Product A    | 2023  | 1000  |
+--------------+-------+-------+

Test Case 5: Large dataset with various scenarios
Input:
INSERT INTO Sales (sale_id, product_id, year, quantity, price) VALUES
(1, 100, 2020, 10, 1000),
(2, 100, 2021, 15, 1100),
(3, 200, 2020, 5, 2000),
(4, 200, 2022, 8, 2200),
(5, 300, 2021, 12, 1500),
(6, 400, 2023, 20, 800),
(7, 500, 2020, 3, 5000);

INSERT INTO Product (product_id, product_name) VALUES
(100, 'Smartphone'),
(200, 'Laptop'),
(300, 'Tablet'),
(400, 'Headphones'),
(500, 'Gaming Console'),
(600, 'Camera');  -- No sales for this product

Expected Output:
+--------------+-------+-------+
| product_name | year  | price |
+--------------+-------+-------+
| Smartphone   | 2020  | 1000  |
| Smartphone   | 2021  | 1100  |
| Laptop       | 2020  | 2000  |
| Laptop       | 2022  | 2200  |
| Tablet       | 2021  | 1500  |
| Headphones   | 2023  | 800   |
| Gaming Console| 2020 | 5000  |
+--------------+-------+-------+
*/

"""
Solution Analysis:
----------------
1. Approach:
   - Use INNER JOIN to combine Sales and Product tables
   - Match records based on product_id (foreign key relationship)
   - Select product_name, year, and price columns
   - No filtering or sorting required as per problem statement

2. Time Complexity: O(n + m)
   - n = number of rows in Sales table
   - m = number of rows in Product table
   - JOIN operation complexity depends on join algorithm used by database
   - With proper indexing on product_id, complexity can be optimized

3. Space Complexity: O(n)
   - Result set contains one row per sale
   - Each row has product_name (varchar), year (int), and price (int)
   - Only sales with valid product_id will be included

4. Edge Cases Handled:
   - Multiple sales for the same product in different years
   - Multiple products sold in the same year
   - Products with no sales (automatically excluded by INNER JOIN)
   - Large datasets with various scenarios
   - Different price points for same product across years

5. Optimizations:
   - INNER JOIN ensures only valid product relationships are included
   - Using table aliases (s, p) for cleaner code
   - No need for additional filtering or sorting
   - Index on product_id columns would significantly improve JOIN performance
   - Foreign key constraint ensures referential integrity

6. Important Notes:
   - INNER JOIN automatically excludes products with no sales
   - Result order is not specified, so any order is acceptable
   - Foreign key relationship ensures data integrity
   - Price is per unit as specified in the problem
   - The solution handles the case where some products might not have sales

7. Alternative Approaches:
   - Could use LEFT JOIN with WHERE clause to filter out NULLs
   - Could use subquery with EXISTS, but JOIN is more efficient
   - Could use WHERE clause instead of ON clause, but ON is more explicit for JOINs
   - Could use NATURAL JOIN if column names were identical

8. Database Considerations:
   - Foreign key constraint on Sales.product_id referencing Product.product_id
   - Composite primary key (sale_id, year) in Sales table
   - Simple primary key (product_id) in Product table
   - Proper indexing on join columns improves performance
"""
