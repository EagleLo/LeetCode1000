# LeetCode 1800: Maximum Ascending Subarray Sum
# Difficulty: Easy
# Topic: Array
"""
Problem Description:
------------------
Find maximum sum of ascending subarray in array of positive integers.
Ascending subarray: Each element greater than previous element.
Single element counts as ascending subarray.
 
Example:
Input: nums = [10,20,30,5,10,50]
Output: 65
Explanation: [5,10,50] is ascending subarray with max sum

Constraints:
* 1 <= nums.length <= 100
* 1 <= nums[i] <= 100
"""

class Solution(object):
   def maxAscendingSum(self, nums):
       """
       Approach: Track current sum and reset when sequence breaks
       :type nums: List[int]
       :rtype: int
       """
       max_sum = temp_sum = nums[0]
       
       for i in range(len(nums) - 1):
           # If sequence breaks, reset temp_sum
           if nums[i + 1] <= nums[i]:
               temp_sum = 0
           # Add next number to current sum    
           temp_sum += nums[i + 1]
           # Update max_sum if needed
           max_sum = max(max_sum, temp_sum)
               
       return max_sum

def test():
   solution = Solution()
   assert solution.maxAscendingSum([10,20,30,5,10,50]) == 65
   assert solution.maxAscendingSum([10,20,30,40,50]) == 150
   assert solution.maxAscendingSum([12,17,15,13,10,11,12]) == 33
   print("All test cases passed!")

if __name__ == "__main__":
   test()

"""
Solution Analysis:
----------------
Time Complexity: O(n) - single pass through array
Space Complexity: O(1) - only using two variables

Key Points:
1. Track both current sum and max sum
2. Reset current sum when ascending sequence breaks
3. Update max_sum after each addition
4. Single element can be max sum if no ascending sequences
5. No need to store the sequence, only need sum
"""