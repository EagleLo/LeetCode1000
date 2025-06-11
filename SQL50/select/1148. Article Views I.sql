# LeetCode 1148. Article Views I
# Difficulty: Easy
# Topic: SQL

# Key takeaways:
# - Use DISTINCT to remove duplicates
# - Use column alias (AS) to rename output column
# - Use ORDER BY for sorting results
# - Simple self-comparison (author_id = viewer_id) to find self-views
# - No need for complex joins or subqueries

"""
Problem Description:
------------------
Table: Views

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| article_id    | int     |
| author_id     | int     |
| viewer_id     | int     |
| view_date     | date    |
+---------------+---------+
There is no primary key (column with unique values) for this table, the table may have duplicate rows.
Each row of this table indicates that some viewer viewed an article (written by some author) on some date. 
Note that equal author_id and viewer_id indicate the same person.

Write a solution to find all the authors that viewed at least one of their own articles.
Return the result table sorted by id in ascending order.

Example:
Input: 
Views table:
+------------+-----------+-----------+------------+
| article_id | author_id | viewer_id | view_date  |
+------------+-----------+-----------+------------+
| 1          | 3         | 5         | 2019-08-01 |
| 1          | 3         | 6         | 2019-08-02 |
| 2          | 7         | 7         | 2019-08-01 |
| 2          | 7         | 6         | 2019-08-02 |
| 4          | 7         | 1         | 2019-07-22 |
| 3          | 4         | 4         | 2019-07-21 |
| 3          | 4         | 4         | 2019-07-21 |
+------------+-----------+-----------+------------+
Output: 
+------+
| id   |
+------+
| 4    |
| 7    |
+------+
"""

-- Solution
SELECT DISTINCT 
    author_id AS id 
FROM 
    Views 
WHERE 
    author_id = viewer_id 
ORDER BY 
    id;

-- Test Cases
/*
Test Case 1: Basic case
Input:
INSERT INTO Views (article_id, author_id, viewer_id, view_date) VALUES
(1, 3, 5, '2019-08-01'),
(1, 3, 6, '2019-08-02'),
(2, 7, 7, '2019-08-01'),
(2, 7, 6, '2019-08-02'),
(4, 7, 1, '2019-07-22'),
(3, 4, 4, '2019-07-21'),
(3, 4, 4, '2019-07-21');

Expected Output:
+------+
| id   |
+------+
| 4    |
| 7    |
+------+

Test Case 2: No self-views
Input:
INSERT INTO Views (article_id, author_id, viewer_id, view_date) VALUES
(1, 1, 2, '2019-08-01'),
(2, 2, 3, '2019-08-02'),
(3, 3, 1, '2019-08-03');

Expected Output:
+------+
| id   |
+------+
(empty result set)

Test Case 3: Multiple self-views
Input:
INSERT INTO Views (article_id, author_id, viewer_id, view_date) VALUES
(1, 1, 1, '2019-08-01'),
(2, 1, 1, '2019-08-02'),
(3, 2, 2, '2019-08-03'),
(4, 2, 2, '2019-08-04');

Expected Output:
+------+
| id   |
+------+
| 1    |
| 2    |
+------+
*/

"""
Solution Analysis:
----------------
1. Approach:
   - Simple filtering using WHERE clause
   - Compare author_id with viewer_id to find self-views
   - Use DISTINCT to remove duplicates
   - Sort results by id

2. Time Complexity: O(n log n)
   - O(n) for scanning the table
   - O(n log n) for sorting the results
   - O(n) for removing duplicates

3. Space Complexity: O(k)
   - k is the number of unique authors who viewed their own articles
   - Only storing author_ids in result

4. Edge Cases Handled:
   - No self-views
   - Multiple self-views by same author
   - Duplicate rows in input
   - Single self-view
   - Multiple authors with self-views

5. Optimizations:
   - DISTINCT removes duplicates efficiently
   - Simple comparison without joins
   - Index on author_id and viewer_id would help performance

6. Important Notes:
   - Table has no primary key
   - Duplicate rows are possible
   - author_id = viewer_id indicates same person
   - Results must be sorted by id
   - Using column alias (AS) to match expected output format
"""