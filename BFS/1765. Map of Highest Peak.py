"""
Map of Highest Peak (LeetCode 1765)

Problem:
Given a matrix representing land and water cells (0=land, 1=water), assign heights to each cell such that:
1. All heights are non-negative
2. Water cells must have height 0
3. Adjacent cells' heights can differ by at most 1
Goal: Maximize the possible heights while following these rules.

Key Insights:
1. This is a BFS problem starting from water cells (height 0)
2. Each step away from water can increase height by 1
3. Use deque for efficient BFS
4. Think about 1D version first to understand pattern

Time Complexity: O(m*n) - visit each cell once
Space Complexity: O(m*n) - for result matrix and queue

Takeaways: 
# 1. When you run BFS, don't use stack pop(0)! It take O(n) time.
# Just use deque and pop left instead.
# 2. Use dirs when you're traversing all the 4 or 8 directions
# 3. If solving a m x n matrix prob is hard, try solving a 1-D 
# version first.

Similar Problems:
- LC 542: 01 Matrix (Finding distance to nearest 0)
"""

from collections import deque

class Solution:
    def highestPeak(self, isWater):
        """
        Args:
            isWater (List[List[int]]): Matrix where 1=water, 0=land
        Returns:
            List[List[int]]: Matrix of assigned heights
        """
        m, n = len(isWater), len(isWater[0])
        result = [[-1 for _ in range(n)] for _ in range(m)]
        queue = deque()
        
        # Initialize water cells with height 0
        for i in range(m):
            for j in range(n):
                if isWater[i][j]:
                    queue.append((i, j, 0))
                    result[i][j] = 0
                    
        # BFS to assign heights
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]  # right, down, left, up
        while queue:
            row, col, h = queue.popleft()
            for dx, dy in dirs:
                newRow, newCol = row + dx, col + dy
                if (0 <= newRow < m and 0 <= newCol < n 
                    and result[newRow][newCol] == -1):
                    result[newRow][newCol] = h + 1
                    queue.append((newRow, newCol, h + 1))
                    
        return result

# Test cases
def test():
    sol = Solution()
    
    test_cases = [
        ([[0,1],[0,0]], [[1,0],[2,1]]),  # Basic case
        ([[0,0,1],[1,0,0],[0,0,0]], [[1,1,0],[0,1,1],[1,2,2]]),  # Multiple water cells
        ([[1]], [[0]]),  # Single cell
        ([[1,1],[1,1]], [[0,0],[0,0]])  # All water
    ]
    
    for i, (input_matrix, expected) in enumerate(test_cases):
        result = sol.highestPeak(input_matrix)
        print(f"Test case {i+1}:")
        print(f"Input: {input_matrix}")
        print(f"Output: {result}")
        print(f"Expected: {expected}")
        print(f"{'Passed' if result == expected else 'Failed'}\n")

if __name__ == "__main__":
    test()