# LeetCode 1248. Count Number of Nice Subarrays
# Difficulty: Medium
# Topic: Prefix Sum, Hash Table, Sliding Window

"""
Problem Description:
------------------
Given an array of integers nums and an integer k. A continuous subarray is called nice 
if there are k odd numbers on it.

Return the number of nice sub-arrays.

Example 1:
Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].

Example 2:
Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There are no odd numbers in the array.

Example 3:
Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16

Constraints:
* 1 <= nums.length <= 50000
* 1 <= nums[i] <= 10^5
* 1 <= k <= nums.length
"""

from collections import defaultdict

class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        Approach: Prefix Sum with Hash Table
        - Convert array to binary (odd=1, even=0)
        - Use prefix sum to track cumulative odd counts
        - Use hash table to count subarrays with exactly k odd numbers
        
        Time: O(n) - single pass through array
        Space: O(n) - hash table in worst case
        """
        oddSum = defaultdict(int)
        # Key insight: Initialize with 0 count = 1
        # This handles the case where we start from beginning of array
        oddSum[0] = 1
        oddCnt = 0
        result = 0
        n = len(nums)
        
        for i in range(n):
            if nums[i] % 2 == 1: 
                oddCnt += 1
            oddSum[oddCnt] += 1
            result += oddSum[oddCnt - k]
        
        return result

def test():
    """
    Test function to verify solution with various test cases
    """
    solution = Solution()
    
    # Test case 1: Example from problem
    nums1 = [1, 1, 2, 1, 1]
    k1 = 3
    result1 = solution.numberOfSubarrays(nums1, k1)
    assert result1 == 2, f"Test case 1 failed: expected 2, got {result1}"
    
    # Test case 2: No odd numbers
    nums2 = [2, 4, 6]
    k2 = 1
    result2 = solution.numberOfSubarrays(nums2, k2)
    assert result2 == 0, f"Test case 2 failed: expected 0, got {result2}"
    
    # Test case 3: Complex case
    nums3 = [2, 2, 2, 1, 2, 2, 1, 2, 2, 2]
    k3 = 2
    result3 = solution.numberOfSubarrays(nums3, k3)
    assert result3 == 16, f"Test case 3 failed: expected 16, got {result3}"
    
    # Test case 4: All odd numbers
    nums4 = [1, 1, 1, 1]
    k4 = 2
    result4 = solution.numberOfSubarrays(nums4, k4)
    assert result4 == 3, f"Test case 4 failed: expected 3, got {result4}"
    
    # Test case 5: Single element
    nums5 = [1]
    k5 = 1
    result5 = solution.numberOfSubarrays(nums5, k5)
    assert result5 == 1, f"Test case 5 failed: expected 1, got {result5}"
    
    print("All test cases passed!")

if __name__ == "__main__":
    test()

"""
Solution Analysis:
----------------
1. Algorithm:
   - For each element, if it's odd, increment oddCnt
   - Add current oddCnt to hash table
   - Look up how many previous positions had (oddCnt - k) odd numbers
   - This gives us all subarrays ending at current position with exactly k odd numbers

2. Time Complexity: O(n)
   - Single pass through the array
   - Hash table operations are O(1) on average

3. Space Complexity: O(n)
   - Hash table can store up to n different odd counts
   - In worst case, all elements are odd

4. Edge Cases Handled:
   - No odd numbers in array
   - All numbers are odd
   - Single element arrays
   - k = 1 (minimum value)
   - k = length of array (maximum value)

5. Why oddSum[0] = 1:
   - Represents empty subarray with 0 odd numbers
   - Needed when we find a subarray that starts from beginning
   - Example: [1,1,1], k=3 - we need to count the entire array

6. Alternative Approach:
   - Could use sliding window with two pointers
   - But prefix sum is more elegant and handles edge cases better
"""
