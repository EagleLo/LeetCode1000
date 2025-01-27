# LeetCode 75. Sort Colors
# Difficulty: Medium
# Topic: Array, Two Pointers, Sorting
"""
Problem Description:
------------------
Given array nums with n objects colored red(0), white(1), and blue(2), 
sort them in-place so same colors are adjacent in order red, white, blue.
Must solve without library sort function.

Example:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Constraints:
* n == nums.length
* 1 <= n <= 300
* nums[i] is 0, 1, or 2
"""

class Solution(object):
   def sortColors(self, nums):
      """
      Approach: Dutch National Flag algorithm with 3 pointers
      left: boundary of 0s
      right: boundary of 2s
      curr: current element being examined
      
      :type nums: List[int]
      :rtype: None Do not return anything, modify nums in-place instead.
      """
      left = curr = 0
      right = len(nums) - 1
      
      # Use <= because right pointer points to unprocessed element
      while curr <= right:
          if nums[curr] == 0:
              # Swap with left boundary and expand 0s section
              nums[left], nums[curr] = nums[curr], nums[left]
              left += 1
              curr += 1
          elif nums[curr] == 2:
              # Swap with right boundary and shrink unprocessed section
              nums[right], nums[curr] = nums[curr], nums[right]
              right -= 1
          else:  # nums[curr] == 1
              # 1s stay in middle
              curr += 1

def test():
   solution = Solution()
   
   # Test case 1
   nums1 = [2,0,2,1,1,0]
   solution.sortColors(nums1)
   assert nums1 == [0,0,1,1,2,2]
   
   # Test case 2
   nums2 = [2,0,1]
   solution.sortColors(nums2)
   assert nums2 == [0,1,2]
   
   print("All test cases passed!")

if __name__ == "__main__":
   test()

"""
Solution Analysis:
----------------
Time Complexity: O(n) - single pass through array
Space Complexity: O(1) - in-place sorting with constant extra space

Key Points:
1. Dutch National Flag algorithm uses 3 pointers:
  - left: rightmost boundary of 0s
  - right: leftmost boundary of 2s
  - curr: current element being processed
2. Important to use <= in while condition because:
  - right pointer points to unprocessed elements
  - need to process element at right pointer
3. When swapping with right, don't increment curr because:
  - new element from right is unprocessed
  - need to check it in next iteration
4. Alternative counting sort approach possible but requires two passes

Note: This is optimal one-pass solution using constant space
"""