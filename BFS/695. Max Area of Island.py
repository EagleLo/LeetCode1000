# LeetCode 695. Max Area of Island
# Difficulty: Medium
# Topic: BFS, DFS, Matrix

"""
Problem Description:
------------------
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) 
connected 4-directionally (horizontal or vertical.) You may assume all four edges of the 
grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.

Example 1:
Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
               [0,0,0,0,0,0,0,1,1,1,0,0,0],
               [0,1,1,0,1,0,0,0,0,0,0,0,0],
               [0,1,0,0,1,1,0,0,1,0,1,0,0],
               [0,1,0,0,1,1,0,0,1,1,1,0,0],
               [0,0,0,0,0,0,0,0,0,0,1,0,0],
               [0,0,0,0,0,0,0,1,1,1,0,0,0],
               [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Output: 6
Explanation: The answer is not 11, because the island must be connected 4-directionally.

Example 2:
Input: grid = [[0,0,0,0,0,0,0,0]]
Output: 0

Constraints:
* m == grid.length
* n == grid[i].length
* 1 <= m, n <= 50
* grid[i][j] is either 0 or 1.
"""

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        Approach: DFS/BFS to find connected components
        - For each cell that is land (1), explore all connected land cells
        - Mark visited cells as 0 to avoid revisiting
        - Keep track of maximum area found
        
        Time: O(m * n) - visit each cell at most once
        Space: O(m * n) - recursion stack in worst case
        """
        self.m = len(grid)
        self.n = len(grid[0])
        maxArea = 0
        
        for i in range(self.m):
            for j in range(self.n): 
                maxArea = max(maxArea, self.bfs(grid, i, j))
        return maxArea

    def bfs(self, grid, curY, curX):
        """
        DFS function to explore connected land cells
        Returns the area of the island starting from (curY, curX)
        """
        # Base cases: out of bounds or water
        if not (0 <= curY < self.m) or not(0 <= curX < self.n) or grid[curY][curX] == 0:
            return 0
        
        # Mark current cell as visited
        area = 1
        grid[curY][curX] = 0
        
        # Explore all 4 directions
        area += self.bfs(grid, curY + 1, curX)  # down
        area += self.bfs(grid, curY - 1, curX)  # up
        area += self.bfs(grid, curY, curX + 1)  # right
        area += self.bfs(grid, curY, curX - 1)  # left
        
        return area

def test():
    """
    Test function to verify solution with various test cases
    """
    solution = Solution()
    
    # Test case 1: Example from problem
    grid1 = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
              [0,0,0,0,0,0,0,1,1,1,0,0,0],
              [0,1,1,0,1,0,0,0,0,0,0,0,0],
              [0,1,0,0,1,1,0,0,1,0,1,0,0],
              [0,1,0,0,1,1,0,0,1,1,1,0,0],
              [0,0,0,0,0,0,0,0,0,0,1,0,0],
              [0,0,0,0,0,0,0,1,1,1,0,0,0],
              [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    
    result1 = solution.maxAreaOfIsland(grid1)
    assert result1 == 6, f"Test case 1 failed: expected 6, got {result1}"
    
    # Test case 2: No islands
    grid2 = [[0,0,0,0,0,0,0,0]]
    result2 = solution.maxAreaOfIsland(grid2)
    assert result2 == 0, f"Test case 2 failed: expected 0, got {result2}"
    
    # Test case 3: Single island
    grid3 = [[1,1,1],
              [1,0,1],
              [1,1,1]]
    result3 = solution.maxAreaOfIsland(grid3)
    assert result3 == 8, f"Test case 3 failed: expected 8, got {result3}"
    
    # Test case 4: Multiple islands
    grid4 = [[1,0,0,0],
              [1,0,0,0],
              [0,0,1,1],
              [0,0,1,1]]
    result4 = solution.maxAreaOfIsland(grid4)
    assert result4 == 4, f"Test case 4 failed: expected 4, got {result4}"
    
    print("All test cases passed!")

if __name__ == "__main__":
    test()

"""
Solution Analysis:
----------------
1. Approach:
   - Use DFS/BFS to explore connected land cells
   - Mark visited cells as 0 to avoid revisiting
   - Keep track of maximum area found across all islands

2. Time Complexity: O(m * n)
   - Visit each cell at most once
   - Each cell is marked as visited after processing

3. Space Complexity: O(m * n)
   - Recursion stack in worst case (when entire grid is one island)
   - In practice, much less due to early termination

4. Key Insights:
   - Use DFS for cleaner recursive implementation
   - Mark cells as visited by setting to 0
   - Explore all 4 directions: up, down, left, right
   - Return 0 for out-of-bounds or water cells

5. Edge Cases Handled:
   - Empty grid
   - No islands (all water)
   - Single cell islands
   - Large connected islands
   - Multiple disconnected islands

6. Optimizations:
   - Early termination for out-of-bounds and water cells
   - In-place modification to avoid extra space
   - Simple recursive structure for readability
"""
