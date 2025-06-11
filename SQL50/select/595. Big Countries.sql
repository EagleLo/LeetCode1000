# LeetCode 595. Big Countries
# Difficulty: Easy
# Topic: SQL
"""
Problem Description:
------------------
Table: World

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| name        | varchar |
| continent   | varchar |
| area        | int     |
| population  | int     |
| gdp         | bigint  |
+-------------+---------+
name is the primary key (column with unique values) for this table.
Each row of this table gives information about the name of a country, the continent to which it belongs, its area, the population, and its GDP value.

A country is big if:
- it has an area of at least three million (i.e., 3000000 km2), or
- it has a population of at least twenty-five million (i.e., 25000000).

Write a solution to find the name, population, and area of the big countries.
Return the result table in any order.

Example:
Input: 
World table:
+-------------+-----------+---------+------------+--------------+
| name        | continent | area    | population | gdp          |
+-------------+-----------+---------+------------+--------------+
| Afghanistan | Asia      | 652230  | 25500100   | 20343000000  |
| Albania     | Europe    | 28748   | 2831741    | 12960000000  |
| Algeria     | Africa    | 2381741 | 37100000   | 188681000000 |
| Andorra     | Europe    | 468     | 78115      | 3712000000   |
| Angola      | Africa    | 1246700 | 20609294   | 100990000000 |
+-------------+-----------+---------+------------+--------------+
Output: 
+-------------+------------+---------+
| name        | population | area    |
+-------------+------------+---------+
| Afghanistan | 25500100   | 652230  |
| Algeria     | 37100000   | 2381741 |
+-------------+------------+---------+
"""

-- Solution
SELECT 
    name,
    population,
    area
FROM 
    World
WHERE 
    area >= 3000000 
    OR population >= 25000000;

-- Test Cases
/*
Test Case 1: Basic case
Input:
INSERT INTO World (name, continent, area, population, gdp) VALUES
('Afghanistan', 'Asia', 652230, 25500100, 20343000000),
('Albania', 'Europe', 28748, 2831741, 12960000000),
('Algeria', 'Africa', 2381741, 37100000, 188681000000),
('Andorra', 'Europe', 468, 78115, 3712000000),
('Angola', 'Africa', 1246700, 20609294, 100990000000);

Expected Output:
+-------------+------------+---------+
| name        | population | area    |
+-------------+------------+---------+
| Afghanistan | 25500100   | 652230  |
| Algeria     | 37100000   | 2381741 |
+-------------+------------+---------+

Test Case 2: Country meets both criteria
Input:
INSERT INTO World (name, continent, area, population, gdp) VALUES
('China', 'Asia', 9596961, 1400000000, 17734000000000),
('Monaco', 'Europe', 2, 39242, 7071000000);

Expected Output:
+-------------+------------+---------+
| name        | population | area    |
+-------------+------------+---------+
| China       | 1400000000 | 9596961 |
+-------------+------------+---------+

Test Case 3: No big countries
Input:
INSERT INTO World (name, continent, area, population, gdp) VALUES
('Monaco', 'Europe', 2, 39242, 7071000000),
('Vatican City', 'Europe', 0, 825, 12000000);

Expected Output:
+-------------+------------+---------+
| name        | population | area    |
+-------------+------------+---------+
(empty result set)
*/

"""
Solution Analysis:
----------------
1. Approach:
   - Simple filtering using WHERE clause
   - Two conditions combined with OR operator:
     * area >= 3000000
     * population >= 25000000
   - Select only required columns: name, population, area

2. Time Complexity: O(n)
   - Need to scan all rows in the World table
   - WHERE clause filtering is linear

3. Space Complexity: O(k)
   - k is the number of big countries
   - Only storing name, population, and area in result

4. Edge Cases Handled:
   - Countries meeting both criteria
   - Countries meeting only area criterion
   - Countries meeting only population criterion
   - No big countries in dataset
   - Countries with very large numbers

5. Optimizations:
   - Simple and straightforward solution
   - No need for complex joins or subqueries
   - Index on name (primary key) helps with performance
   - Using OR operator efficiently combines both conditions

6. Important Notes:
   - Numbers are large, but within int/bigint range
   - No need to handle NULL values as per problem constraints
   - Result can be in any order as specified
"""