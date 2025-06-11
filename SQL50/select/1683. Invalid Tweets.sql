# LeetCode 1683. Invalid Tweets
# Difficulty: Easy
# Topic: SQL

# Key takeaways:
# - Use LENGTH() function to count characters in a string
# - Simple WHERE clause with comparison operator
# - No need for complex string manipulation
# - Primary key (tweet_id) ensures unique results
# - Content consists of alphanumeric, '!', and space characters only

"""
Problem Description:
------------------
Table: Tweets

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| tweet_id       | int     |
| content        | varchar |
+----------------+---------+
tweet_id is the primary key (column with unique values) for this table.
content consists of alphanumeric characters, '!', or ' ' and no other special characters.
This table contains all the tweets in a social media app.

Write a solution to find the IDs of the invalid tweets. The tweet is invalid if the number of characters used in the content of the tweet is strictly greater than 15.

Return the result table in any order.

Example:
Input: 
Tweets table:
+----------+-----------------------------------+
| tweet_id | content                           |
+----------+-----------------------------------+
| 1        | Let us Code                       |
| 2        | More than fifteen chars are here! |
+----------+-----------------------------------+
Output: 
+----------+
| tweet_id |
+----------+
| 2        |
+----------+
Explanation: 
Tweet 1 has length = 11. It is a valid tweet.
Tweet 2 has length = 33. It is an invalid tweet.
"""

-- Solution
SELECT 
    tweet_id
FROM 
    Tweets
WHERE
    LENGTH(content) > 15;

-- Test Cases
/*
Test Case 1: Basic case
Input:
INSERT INTO Tweets (tweet_id, content) VALUES
(1, 'Let us Code'),
(2, 'More than fifteen chars are here!');

Expected Output:
+----------+
| tweet_id |
+----------+
| 2        |
+----------+

Test Case 2: All tweets valid
Input:
INSERT INTO Tweets (tweet_id, content) VALUES
(1, 'Short tweet'),
(2, 'Another short'),
(3, 'Just 15 chars!');

Expected Output:
+----------+
| tweet_id |
+----------+
(empty result set)

Test Case 3: All tweets invalid
Input:
INSERT INTO Tweets (tweet_id, content) VALUES
(1, 'This is a very long tweet that exceeds fifteen characters'),
(2, 'Another very long tweet that should be considered invalid');

Expected Output:
+----------+
| tweet_id |
+----------+
| 1        |
| 2        |
+----------+

Test Case 4: Edge case - exactly 15 characters
Input:
INSERT INTO Tweets (tweet_id, content) VALUES
(1, 'Exactly 15 ch!'),
(2, 'More than 15 ch!');

Expected Output:
+----------+
| tweet_id |
+----------+
| 2        |
+----------+
*/

"""
Solution Analysis:
----------------
1. Approach:
   - Use LENGTH() function to count characters
   - Simple WHERE clause with > operator
   - Select only tweet_id column

2. Time Complexity: O(n)
   - Need to scan all rows in the Tweets table
   - LENGTH() function is O(1) for each row
   - WHERE clause filtering is linear

3. Space Complexity: O(k)
   - k is the number of invalid tweets
   - Only storing tweet_ids in result

4. Edge Cases Handled:
   - All tweets valid
   - All tweets invalid
   - Exactly 15 characters (should be valid)
   - Empty content
   - Very long content

5. Optimizations:
   - Simple and straightforward solution
   - No need for complex string manipulation
   - Index on tweet_id (primary key) helps with performance
   - LENGTH() function is efficient

6. Important Notes:
   - Content consists only of alphanumeric, '!', and space characters
   - tweet_id is primary key (unique)
   - Result can be in any order
   - "Strictly greater than 15" means > 15, not >= 15
"""