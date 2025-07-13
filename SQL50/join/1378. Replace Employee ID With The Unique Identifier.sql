# LeetCode 1378. Replace Employee ID With The Unique Identifier
# Difficulty: Easy
# Topic: SQL, JOIN
"""
Problem Description:
------------------
Table: Employees

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| name          | varchar |
+---------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table contains the id and the name of an employee in a company.

Table: EmployeeUNI

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| unique_id     | int     |
+---------------+---------+
(id, unique_id) is the primary key (combination of columns with unique values) for this table.
Each row of this table contains the id and the corresponding unique id of an employee in the company.

Write a solution to show the unique ID of each user, If a user does not have a unique ID replace just show null.

Return the result table in any order.

Example 1:
Input: 
Employees table:
+----+----------+
| id | name     |
+----+----------+
| 1  | Alice    |
| 7  | Bob      |
| 11 | Meir     |
| 90 | Winston  |
| 3  | Jonathan |
+----+----------+
EmployeeUNI table:
+----+-----------+
| id | unique_id |
+----+-----------+
| 3  | 1         |
| 11 | 2         |
| 90 | 3         |
+----+-----------+
Output: 
+-----------+----------+
| unique_id | name     |
+-----------+----------+
| null      | Alice    |
| null      | Bob      |
| 2         | Meir     |
| 3         | Winston  |
| 1         | Jonathan |
+-----------+----------+
Explanation: 
Alice and Bob do not have a unique ID, We will show null instead.
The unique ID of Meir is 2.
The unique ID of Winston is 3.
The unique ID of Jonathan is 1.
"""

-- Solution
SELECT 
    euni.unique_id, 
    e.name
FROM 
    Employees e 
LEFT JOIN 
    EmployeeUNI euni 
    ON e.id = euni.id;

-- Test Cases
/*
Test Case 1: Basic case with some employees having unique IDs
Input:
INSERT INTO Employees (id, name) VALUES
(1, 'Alice'),
(7, 'Bob'),
(11, 'Meir'),
(90, 'Winston'),
(3, 'Jonathan');

INSERT INTO EmployeeUNI (id, unique_id) VALUES
(3, 1),
(11, 2),
(90, 3);

Expected Output:
+-----------+----------+
| unique_id | name     |
+-----------+----------+
| null      | Alice    |
| null      | Bob      |
| 2         | Meir     |
| 3         | Winston  |
| 1         | Jonathan |
+-----------+----------+

Test Case 2: All employees have unique IDs
Input:
INSERT INTO Employees (id, name) VALUES
(1, 'Alice'),
(2, 'Bob'),
(3, 'Charlie');

INSERT INTO EmployeeUNI (id, unique_id) VALUES
(1, 101),
(2, 102),
(3, 103);

Expected Output:
+-----------+----------+
| unique_id | name     |
+-----------+----------+
| 101       | Alice    |
| 102       | Bob      |
| 103       | Charlie  |
+-----------+----------+

Test Case 3: No employees have unique IDs
Input:
INSERT INTO Employees (id, name) VALUES
(1, 'Alice'),
(2, 'Bob'),
(3, 'Charlie');

-- EmployeeUNI table is empty

Expected Output:
+-----------+----------+
| unique_id | name     |
+-----------+----------+
| null      | Alice    |
| null      | Bob      |
| null      | Charlie  |
+-----------+----------+

Test Case 4: Empty Employees table
Input:
-- Employees table is empty
-- EmployeeUNI table is empty

Expected Output:
+-----------+----------+
| unique_id | name     |
+-----------+----------+
(empty result set)

Test Case 5: Large dataset
Input:
INSERT INTO Employees (id, name) VALUES
(1, 'Alice'),
(2, 'Bob'),
(3, 'Charlie'),
(4, 'David'),
(5, 'Eve'),
(6, 'Frank'),
(7, 'Grace'),
(8, 'Henry'),
(9, 'Ivy'),
(10, 'Jack');

INSERT INTO EmployeeUNI (id, unique_id) VALUES
(1, 1001),
(3, 1003),
(5, 1005),
(7, 1007),
(9, 1009);

Expected Output:
+-----------+----------+
| unique_id | name     |
+-----------+----------+
| 1001      | Alice    |
| null      | Bob      |
| 1003      | Charlie  |
| null      | David    |
| 1005      | Eve      |
| null      | Frank    |
| 1007      | Grace    |
| null      | Henry    |
| 1009      | Ivy      |
| null      | Jack     |
+-----------+----------+
*/

"""
Solution Analysis:
----------------
1. Approach:
   - Use LEFT JOIN to include all employees from the Employees table
   - Match employees with their unique IDs from EmployeeUNI table
   - If no match found, unique_id will be NULL (which is the desired behavior)
   - Select unique_id and name columns in the specified order

2. Time Complexity: O(n + m)
   - n = number of rows in Employees table
   - m = number of rows in EmployeeUNI table
   - JOIN operation complexity depends on join algorithm used by database

3. Space Complexity: O(n)
   - Result set contains one row per employee
   - Each row has unique_id (int) and name (varchar)

4. Edge Cases Handled:
   - Employees without unique IDs (NULL values)
   - All employees having unique IDs
   - No employees having unique IDs
   - Empty tables
   - Large datasets

5. Optimizations:
   - LEFT JOIN ensures all employees are included
   - Using table aliases (e, euni) for cleaner code
   - No need for additional filtering or sorting
   - Index on id columns would improve JOIN performance

6. Important Notes:
   - LEFT JOIN preserves all rows from the left table (Employees)
   - NULL values are automatically handled for missing matches
   - Result order is not specified, so any order is acceptable
   - The solution handles the case where EmployeeUNI table might be empty
   - Primary key constraints ensure data integrity

7. Alternative Approaches:
   - Could use RIGHT JOIN with table order reversed
   - Could use FULL OUTER JOIN (though unnecessary for this problem)
   - Could use subquery with EXISTS, but JOIN is more efficient
"""
