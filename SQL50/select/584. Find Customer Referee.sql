# LeetCode 584. Find Customer Referee
# Difficulty: Easy
# Topic: SQL
"""
Problem Description:
------------------
Table: Customer

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| referee_id  | int     |
+-------------+---------+
In SQL, id is the primary key column for this table.
Each row of this table indicates the id of a customer, their name, and the id of the customer who referred them.

Find the names of the customer that are not referred by the customer with id = 2.
Return the result table in any order.

Example:
Input: 
Customer table:
+----+------+------------+
| id | name | referee_id |
+----+------+------------+
| 1  | Will | null       |
| 2  | Jane | null       |
| 3  | Alex | 2          |
| 4  | Bill | null       |
| 5  | Zack | 1          |
| 6  | Mark | 2          |
+----+------+------------+
Output: 
+------+
| name |
+------+
| Will |
| Jane |
| Bill |
| Zack |
+------+
"""

-- Solution
SELECT
    name
FROM 
    Customer
WHERE
    referee_id != 2 OR referee_id IS NULL;

-- Test Cases
/*
Test Case 1: Basic case
Input:
INSERT INTO Customer (id, name, referee_id) VALUES
(1, 'Will', NULL),
(2, 'Jane', NULL),
(3, 'Alex', 2),
(4, 'Bill', NULL),
(5, 'Zack', 1),
(6, 'Mark', 2);

Expected Output:
+------+
| name |
+------+
| Will |
| Jane |
| Bill |
| Zack |
+------+

Test Case 2: All customers referred by id 2
Input:
INSERT INTO Customer (id, name, referee_id) VALUES
(1, 'Will', 2),
(2, 'Jane', 2),
(3, 'Alex', 2);

Expected Output:
+------+
| name |
+------+
(empty result set)

Test Case 3: No customers referred by id 2
Input:
INSERT INTO Customer (id, name, referee_id) VALUES
(1, 'Will', NULL),
(2, 'Jane', 1),
(3, 'Alex', 1);

Expected Output:
+------+
| name |
+------+
| Will |
| Jane |
| Alex |
+------+
*/

"""
Solution Analysis:
----------------
1. Approach:
   - Filter customers using WHERE clause
   - Two conditions:
     * referee_id != 2 (not referred by customer 2)
     * referee_id IS NULL (no referee)
   - Combined with OR operator

2. Time Complexity: O(n)
   - Need to scan all rows in the Customer table
   - WHERE clause filtering is linear

3. Space Complexity: O(k)
   - k is the number of matching customers
   - Only storing names in result

4. Edge Cases Handled:
   - NULL referee_id values
   - All customers referred by id 2
   - No customers referred by id 2

5. Important Note about != vs <>:
   - Both != and <> are valid SQL operators for "not equal"
   - <> is the SQL standard operator
   - != is supported by most DBMS but not part of SQL standard
   - Functionally equivalent, but <> is preferred for:
     * Better portability across different DBMS
     * Following SQL standards
     * More explicit meaning (<> clearly shows "not equal")
   - In this case, both would work, but <> is more standard

6. NULL Handling:
   - NULL values require special handling with IS NULL
   - Cannot use = or != with NULL
   - Must use IS NULL or IS NOT NULL
   - This is why we need the OR referee_id IS NULL condition
"""