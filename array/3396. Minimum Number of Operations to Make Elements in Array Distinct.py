# LeetCode 3396. Minimum Number of Operations to Make Elements in Array Distinct
# Difficulty: Easy
# Topic: Array, Hash Table
"""
Problem Description:
------------------
Given integer array nums. Make elements distinct by operations:
- Remove 3 elements from start (or all if < 3 elements)
Return minimum operations needed.

Example:
Input: nums = [1,2,3,4,2,3,3,5,7]
Output: 2
Explanation: 
1st op: [4,2,3,3,5,7]
2nd op: [3,5,7] (distinct)

Constraints:
* 1 <= nums.length <= 100
* 1 <= nums[i] <= 100
"""

from collections import Counter

class Solution(object):
    def minimumOperations(self, nums):
        """
        Approach: Keep removing 3 elements until array becomes distinct
        Check distinctness using set comparison

        :type nums: List[int]
        :rtype: int
        """
        count = {}
        length = len(nums)
        ans = 0

        for i in range(length - 1, -1, -1):
            count[nums[i]] = count.get(nums[i], 0) + 1
            if count[nums[i]] > 1:
                return (i//3) + 1

        return 0 

def test():
   solution = Solution()
   assert solution.minimumOperations([1,2,3,4,2,3,3,5,7]) == 2
   assert solution.minimumOperations([4,5,6,4,4]) == 2
   assert solution.minimumOperations([6,7,8,9]) == 0
   print("All test cases passed!")

if __name__ == "__main__":
   test()

"""
Solution Analysis:
----------------
Time Complexity: O(n^2) 
- Each set() operation is O(n)
- May need to do this n/3 times

Space Complexity: O(n) for set creation

Key Takeaways:
1. del list[:k] removes first k elements
2. set() gives unique elements
3. Compare len(set) vs len(list) for distinctness
4. Modify input list directly saves space
"""