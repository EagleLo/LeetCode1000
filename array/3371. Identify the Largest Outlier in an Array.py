# LeetCode 3371. Identify the Largest Outlier in an Array
# Difficulty: Medium
# Topic: Array, Hash Table, Counting
"""
Problem Description:
------------------
Given array nums with n elements where:
- n-2 elements are special numbers
- One element is sum of special numbers
- One element is outlier (not special number or sum)
Return largest possible outlier.

Note: Elements can share same value but must have distinct indices.

Example:
Input: nums = [2,3,5,10]
Output: 10
Explanation: Special numbers can be 2,3 with sum 5, making 10 the outlier.

Constraints:
* 3 <= nums.length <= 10^5
* -1000 <= nums[i] <= 1000
* At least one potential outlier exists
"""

from collections import defaultdict

class Solution(object):
   def getLargestOutlier(self, nums):
       """
       Approach: Use formula total_sum = 2 * sum_special + outlier
       Therefore outlier = total_sum - 2 * sum_special
       
       :type nums: List[int]
       :rtype: int
       """
       # Get total sum once - O(n)
       total_sum = sum(nums)
       max_outlier = -float('inf')
       
       # Count frequency of each number - O(n)
       num_count = defaultdict(int)
       for i in range(len(nums)):
           num_count[nums[i]] += 1
           
       # Check each number as potential sum of special numbers
       for i in range(len(nums)):
           sum_special = nums[i]
           # Calculate potential outlier using formula
           p_outlier = total_sum - 2 * sum_special
           
           # Valid outlier if:
           # 1. Exists in array
           # 2. Different from sum_special OR appears multiple times
           if p_outlier in num_count:
               if p_outlier != nums[i] or num_count[p_outlier] > 1:
                   max_outlier = max(p_outlier, max_outlier)
                   
       return max_outlier

def test():
   solution = Solution()
   assert solution.getLargestOutlier([2,3,5,10]) == 10
   assert solution.getLargestOutlier([-2,-1,-3,-6,4]) == 4
   assert solution.getLargestOutlier([1,1,1,1,1,5,5]) == 5
   print("All test cases passed!")

if __name__ == "__main__":
   test()

"""
Solution Analysis:
----------------
Time Complexity: O(n) where n is length of array
- O(n) for sum calculation
- O(n) for frequency counting
- O(n) for checking each number as potential sum

Space Complexity: O(n) for frequency dictionary

Key Takeaways:
1. Look for mathematical relationships:
  total = 2*sum_special + outlier
2. Use frequency counting when dealing with duplicates
3. Consider validity conditions carefully
4. No need to sort - saves O(nlogn) complexity
5. Formula transformation helps simplify solution

How to derive solution:
1. Write equations for what we know:
  - total = sum_special + sum_special + outlier
2. Transform to solve for outlier:
  - outlier = total - 2*sum_special
3. Try each number as sum_special
4. Check validity of resulting outlier
"""