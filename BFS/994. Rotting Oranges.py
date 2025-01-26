# LeetCode 994. Rotting Oranges
# Difficulty: Medium
# Topic: BFS, Matrix
"""
Problem Description:
------------------
Given an m x n grid where each cell can have:
- 0: empty cell
- 1: fresh orange
- 2: rotten orange
Every minute, fresh oranges 4-directionally adjacent to rotten ones become rotten.
Return minimum minutes until no fresh oranges remain, or -1 if impossible.

Example 1:
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
"""

from collections import deque

class Solution(object):
   def orangesRotting(self, grid):
       """
       Approach: BFS to simulate rotting process
       Track fresh count for termination check
       
       :type grid: List[List[int]]
       :rtype: int
       """
       dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
       m = len(grid)
       n = len(grid[0])
       max_time = 0
       q = deque()
       fresh = 0

       for i in range(m):
           for j in range(n):
               if grid[i][j] == 2:
                   q.append((i, j, 0))
               elif grid[i][j] == 1:
                   fresh += 1

       while q and fresh > 0:
           row, col, time = q.popleft()
           for dir in dirs:
               new_y = row + dir[0]
               new_x = col + dir[1]
               if 0 <= new_y < m and 0 <= new_x < n and grid[new_y][new_x] == 1:
                   grid[new_y][new_x] = 2
                   q.append((new_y, new_x, time + 1))
                   fresh -= 1
                   max_time = max(time + 1, max_time)
         
       if fresh > 0:
           return -1
    
       return max_time

# Test cases
def test():
   solution = Solution()
   assert solution.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]) == 4
   assert solution.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]) == -1
   assert solution.orangesRotting([[0,2]]) == 0
   print("All test cases passed!")

if __name__ == "__main__":
   test()

"""
Solution Analysis:
----------------
Time Complexity: O(m*n)
- Visit each cell at most once
- Each cell processed at most once in queue

Space Complexity: O(m*n)
- Queue can store at most all cells
- Direction array is constant space

Key Points:
1. BFS for level-by-level rotting simulation
2. Fresh counter avoids need for set
3. Grid modification eliminates visited set
4. Early check for unreachable oranges
5. Direction array for clean 4-way traversal
"""