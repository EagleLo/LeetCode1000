# LeetCode 1757. Recyclable and Low Fat Products
# Difficulty: Easy
# Topic: SQL

# Key takeaways:
# - Use WHERE clause to filter rows
# - Use AND operator to combine multiple conditions
# - Use enum type for columns
# - IS is for specific values, = is for range

"""
Problem Description:
------------------
Table: Products

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_id  | int     |
| low_fats    | enum    |
| recyclable  | enum    |
+-------------+---------+
product_id is the primary key (column with unique values) for this table.
low_fats is an ENUM (category) of type ('Y', 'N') where 'Y' means this product is low fat and 'N' means it is not.
recyclable is an ENUM (category) of types ('Y', 'N') where 'Y' means this product is recyclable and 'N' means it is not.

Write a solution to find the ids of products that are both low fat and recyclable.
Return the result table in any order.

Example:
Input: 
Products table:
+-------------+----------+------------+
| product_id  | low_fats | recyclable |
+-------------+----------+------------+
| 0           | Y        | N          |
| 1           | Y        | Y          |
| 2           | N        | Y          |
| 3           | Y        | Y          |
| 4           | N        | N          |
+-------------+----------+------------+
Output: 
+-------------+
| product_id  |
+-------------+
| 1           |
| 3           |
+-------------+
Explanation: Only products 1 and 3 are both low fat and recyclable.
"""

-- Solution
SELECT 
    product_id 
FROM 
    Products 
WHERE 
    low_fats = 'Y' 
    AND recyclable = 'Y';

-- Test Cases
/*
Test Case 1: Basic case
Input:
INSERT INTO Products (product_id, low_fats, recyclable) VALUES
(0, 'Y', 'N'),
(1, 'Y', 'Y'),
(2, 'N', 'Y'),
(3, 'Y', 'Y'),
(4, 'N', 'N');

Expected Output:
+-------------+
| product_id  |
+-------------+
| 1           |
| 3           |
+-------------+

Test Case 2: No matching products
Input:
INSERT INTO Products (product_id, low_fats, recyclable) VALUES
(0, 'Y', 'N'),
(1, 'N', 'Y'),
(2, 'N', 'N');

Expected Output:
+-------------+
| product_id  |
+-------------+
(empty result set)

Test Case 3: All products match
Input:
INSERT INTO Products (product_id, low_fats, recyclable) VALUES
(0, 'Y', 'Y'),
(1, 'Y', 'Y'),
(2, 'Y', 'Y');

Expected Output:
+-------------+
| product_id  |
+-------------+
| 0           |
| 1           |
| 2           |
+-------------+
*/

"""
Solution Analysis:
----------------
1. Approach:
   - Simple filtering using WHERE clause
   - Two conditions combined with AND operator
   - No need for ORDER BY as result can be in any order

2. Time Complexity: O(n)
   - Need to scan all rows in the Products table
   - WHERE clause filtering is linear

3. Space Complexity: O(k)
   - k is the number of matching products
   - Only storing product_ids in result

4. Edge Cases Handled:
   - Empty table
   - No matching products
   - All products match
   - Mixed cases

5. Optimizations:
   - Simple and straightforward solution
   - No need for complex joins or subqueries
   - Index on product_id (primary key) helps with performance
"""