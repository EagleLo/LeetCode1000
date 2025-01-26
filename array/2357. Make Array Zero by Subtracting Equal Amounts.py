# LeetCode 2357. Make Array Zero by Subtracting Equal Amounts
# Difficulty: Easy
# Topic: Array, Counting
"""
Problem Description:
------------------
Given non-negative array nums. In one operation:
- Choose x ≤ smallest non-zero element
- Subtract x from every positive element
Return minimum operations to make all elements 0.

Example:
Input: nums = [1,5,0,3,5]
Output: 3
Explanation:
1st: x=1 → [0,4,0,2,4]
2nd: x=2 → [0,2,0,0,2]
3rd: x=2 → [0,0,0,0,0]

Constraints:
* 1 <= nums.length <= 100
* 0 <= nums[i] <= 100
"""

from collections import Counter

class Solution(object):
   def minimumOperations(self, nums):
      """
      Approach: Count unique non-zero numbers
      Each unique value needs one operation
      
      :type nums: List[int]
      :rtype: int
      """
      counter = Counter(nums)
      # If 0 exists, exclude it from count
      return len(counter.keys()) - 1 if 0 in counter else len(counter.keys())

def test():
   solution = Solution()
   assert solution.minimumOperations([1,5,0,3,5]) == 3
   assert solution.minimumOperations([0]) == 0
   print("All test cases passed!")

if __name__ == "__main__":
   test()

"""
Solution Analysis:
----------------
Time Complexity: O(n) for counting
Space Complexity: O(k) where k is unique numbers

Key Takeaways:
1. Each unique non-zero number requires one operation
2. Order doesn't matter - can always choose smallest
3. Counter.keys() gives unique elements
4. Need to handle 0 specially
"""