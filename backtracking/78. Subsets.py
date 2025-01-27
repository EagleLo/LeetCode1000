# LeetCode 78. Subsets
# Difficulty: Medium
# Topic: Array, Backtracking
"""
Problem Description:
------------------
Given integer array nums of unique elements, return all possible subsets (power set).
Solution set must not contain duplicate subsets. Return in any order.

Example:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Constraints:
* 1 <= nums.length <= 10
* -10 <= nums[i] <= 10
* All numbers in nums are unique
"""

class Solution(object):
   def subsets(self, nums):
      """
      Approach: Backtracking - for each number, decide to include or not
      At each step, add current subset and try adding remaining numbers
      
      :type nums: List[int]
      :rtype: List[List[int]]
      """
      def backtrack(idx, curr):
         # Add current subset to result
         result.append(curr[:])
         
         # Try adding each remaining number
         for i in range(idx + 1, len(nums)):
            curr.append(nums[i])
            backtrack(i, curr)
            curr.pop()
      
      result = []
      backtrack(-1, [])
      return result

def test():
   solution = Solution()
   assert sorted(solution.subsets([1,2,3])) == sorted([[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]])
   assert sorted(solution.subsets([0])) == sorted([[],[0]])
   print("All test cases passed!")

if __name__ == "__main__":
   test()

"""
Solution Analysis:
----------------
Time Complexity: O(2^n)
- Need to generate all possible subsets
- Each element can be either included or not

Space Complexity: O(n)
- Maximum depth of recursion tree is n
- curr array stores at most n elements

Key Points:
1. Use backtracking to try all combinations
2. curr[:] creates copy of current subset
3. pop() after recursion to backtrack
4. Start index prevents duplicate combinations
5. No base case needed as loop handles termination
"""