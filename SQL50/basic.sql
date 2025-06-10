-- This file contains the basic SQL commands.

-- 1. Basic SELECT Statement
SELECT column1, column2 FROM table_name;
SELECT * FROM table_name;  -- Select all columns

-- 2. WHERE Clause
SELECT * FROM table_name WHERE condition;
-- Examples:
SELECT * FROM employees WHERE salary > 50000;
SELECT * FROM products WHERE category = 'Electronics';

-- 3. ORDER BY
SELECT * FROM table_name ORDER BY column_name ASC;  -- Ascending
SELECT * FROM table_name ORDER BY column_name DESC; -- Descending

-- 4. LIMIT
SELECT * FROM table_name LIMIT 10;  -- Get first 10 rows

-- 5. DISTINCT
SELECT DISTINCT column_name FROM table_name;  -- Remove duplicates

-- 6. Basic Aggregation Functions
SELECT 
    COUNT(*),      -- Count rows
    SUM(column),   -- Sum of values
    AVG(column),   -- Average
    MAX(column),   -- Maximum value
    MIN(column)    -- Minimum value
FROM table_name;

-- 7. GROUP BY
SELECT column1, COUNT(*) 
FROM table_name 
GROUP BY column1;

-- 8. HAVING
SELECT column1, COUNT(*) 
FROM table_name 
GROUP BY column1 
HAVING COUNT(*) > 5;

-- 9. JOIN Basics
-- INNER JOIN
SELECT * 
FROM table1 
INNER JOIN table2 
ON table1.id = table2.id;

-- LEFT JOIN
SELECT * 
FROM table1 
LEFT JOIN table2 
ON table1.id = table2.id;

-- 10. Common Operators
-- Comparison
=, <>, <, >, <=, >=
-- Logical
AND, OR, NOT
-- LIKE
SELECT * FROM table_name WHERE column LIKE 'A%';  -- Starts with A
SELECT * FROM table_name WHERE column LIKE '%A';  -- Ends with A
SELECT * FROM table_name WHERE column LIKE '%A%'; -- Contains A

-- 11. NULL Handling
SELECT * FROM table_name WHERE column IS NULL;
SELECT * FROM table_name WHERE column IS NOT NULL;

-- 12. CASE Statement
SELECT 
    column1,
    CASE 
        WHEN condition1 THEN result1
        WHEN condition2 THEN result2
        ELSE result3
    END as new_column
FROM table_name;

-- 13. Common String Functions
SELECT 
    LENGTH(column),    -- Length of string
    UPPER(column),     -- Convert to uppercase
    LOWER(column),     -- Convert to lowercase
    SUBSTRING(column, start, length),  -- Extract substring
    CONCAT(str1, str2) -- Concatenate strings
FROM table_name;

-- 14. Date Functions
SELECT 
    CURRENT_DATE,      -- Current date
    CURRENT_TIMESTAMP, -- Current timestamp
    DATE_ADD(date, INTERVAL 1 DAY),    -- Add days
    DATE_SUB(date, INTERVAL 1 DAY)     -- Subtract days
FROM table_name;

-- 15. Common LeetCode Patterns
-- Find duplicates
SELECT column, COUNT(*) as count
FROM table_name
GROUP BY column
HAVING COUNT(*) > 1;

-- Find second highest
SELECT MAX(column) 
FROM table_name 
WHERE column < (SELECT MAX(column) FROM table_name);

-- Find employees earning more than their managers
SELECT e1.name as Employee
FROM Employee e1
JOIN Employee e2 ON e1.managerId = e2.id
WHERE e1.salary > e2.salary;
