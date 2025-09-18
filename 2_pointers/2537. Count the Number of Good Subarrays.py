# LeetCode 2537. Count the Number of Good Subarrays
# Difficulty: Medium
# Topic: Two Pointers, Sliding Window, Hash Table

"""
Problem Description:
------------------
Given an integer array nums and an integer k, return the number of good subarrays of nums.

A subarray arr is good if there are at least k pairs of indices (i, j) such that i < j and arr[i] == arr[j].

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: nums = [1,1,1,1,1], k = 10
Output: 1
Explanation: The only good subarray is the array nums itself.

Example 2:
Input: nums = [3,1,4,3,2,2,4], k = 2
Output: 4
Explanation: There are 4 different good subarrays:
- [3,1,4,3,2,2] that has 2 pairs.
- [3,1,4,3,2,2,4] that has 3 pairs.
- [1,4,3,2,2,4] that has 2 pairs.
- [4,3,2,2,4] that has 2 pairs.

Constraints:
* 1 <= nums.length <= 10^5
* 1 <= nums[i], k <= 10^9
"""

from collections import Counter

class Solution(object):
    def countGood(self, nums, k):
        """
        Approach: Sliding Window with Two Pointers
        - Use sliding window to find subarrays with at least k pairs
        - When we find a valid subarray, all subarrays extending to the right are also valid
        - Use counter to track frequency of each element
        - Track number of pairs dynamically
        
        Time: O(n) - each element is added and removed at most once
        Space: O(n) - counter to store frequencies
        """
        n = len(nums)
        same, right = 0, -1
        cnt = Counter()
        ans = 0
        
        for left in range(n):
            # Expand window until we have at least k pairs
            while same < k and right + 1 < n:
                right += 1
                same += cnt[nums[right]]  # Add pairs formed with existing elements
                cnt[nums[right]] += 1
            
            # If we found a valid subarray, count all extensions to the right
            if same >= k:
                ans += n - right
            
            # Shrink window from left
            cnt[nums[left]] -= 1
            same -= cnt[nums[left]]  # Remove pairs formed with remaining elements
        
        return ans

def test():
    """
    Test function to verify solution with various test cases
    """
    solution = Solution()
    
    # Test case 1: Example from problem
    nums1 = [1,1,1,1,1]
    k1 = 10
    result1 = solution.countGood(nums1, k1)
    assert result1 == 1, f"Test case 1 failed: expected 1, got {result1}"
    
    # Test case 2: Example from problem
    nums2 = [3,1,4,3,2,2,4]
    k2 = 2
    result2 = solution.countGood(nums2, k2)
    assert result2 == 4, f"Test case 2 failed: expected 4, got {result2}"
    
    # Test case 3: No good subarrays
    nums3 = [1,2,3,4,5]
    k3 = 2
    result3 = solution.countGood(nums3, k3)
    assert result3 == 0, f"Test case 3 failed: expected 0, got {result3}"
    
    # Test case 4: Single element
    nums4 = [1]
    k4 = 1
    result4 = solution.countGood(nums4, k4)
    assert result4 == 0, f"Test case 4 failed: expected 0, got {result4}"
    
    # Test case 5: All same elements
    nums5 = [2,2,2,2]
    k5 = 3
    result5 = solution.countGood(nums5, k5)
    assert result5 == 2, f"Test case 5 failed: expected 2, got {result5}"
    
    # Test case 6: Edge case with k=0
    nums6 = [1,2,3]
    k6 = 0
    result6 = solution.countGood(nums6, k6)
    assert result6 == 6, f"Test case 6 failed: expected 6, got {result6}"
    
    print("All test cases passed!")

if __name__ == "__main__":
    test()

"""
What I Learned from This Problem:
================================

1. SLIDING WINDOW TECHNIQUE:
   - Use two pointers to maintain a window
   - Expand window until condition is met
   - Shrink window from left to find all valid subarrays

2. DYNAMIC PAIR COUNTING:
   - When adding element x: pairs += count[x] (forms pairs with existing x's)
   - When removing element x: pairs -= count[x] (removes pairs with remaining x's)
   - This avoids recalculating pairs from scratch

3. OPTIMIZATION INSIGHT:
   - Once we find a valid subarray [left, right], all subarrays [left, right+1], 
     [left, right+2], ..., [left, n-1] are also valid
   - This gives us O(1) counting for all extensions

4. COUNTER USAGE:
   - Use Counter to track frequency of each element
   - Update frequency when adding/removing elements
   - Use frequency to calculate pair contributions

5. EDGE CASE HANDLING:
   - k=0: all subarrays are valid
   - No valid subarrays: return 0
   - Single element: can't form pairs

6. ALGORITHM PATTERN:
   - For each left position, find minimum right position that makes subarray valid
   - Count all subarrays starting at left that are valid
   - This ensures we count each valid subarray exactly once

7. TIME COMPLEXITY OPTIMIZATION:
   - Each element is added and removed at most once
   - No nested loops, just sliding window
   - O(n) time complexity

8. SPACE COMPLEXITY:
   - Counter stores at most n different elements
   - O(n) space complexity

9. SLIDING WINDOW VARIATIONS:
   - This is a "find minimum window" variation
   - Once condition is met, count all extensions
   - Different from "find all windows" approach

10. MATHEMATICAL INSIGHT:
    - Pairs = sum of C(freq, 2) for all frequencies
    - But we can track pairs incrementally
    - Adding element x contributes count[x] new pairs
    - Removing element x removes count[x] pairs

This problem taught me advanced sliding window techniques and how to
efficiently count subarrays with complex conditions!
"""

"""
Solution Analysis:
----------------
1. Approach:
   - Use sliding window with two pointers
   - For each left position, find minimum right position that makes subarray valid
   - Count all valid subarrays starting at each left position

2. Algorithm:
   - For each left position:
     * Expand window until we have at least k pairs
     * If valid, count all extensions to the right
     * Shrink window from left
   - Use counter to track element frequencies
   - Track pairs dynamically

3. Time Complexity: O(n)
   - Each element is added and removed at most once
   - Sliding window ensures linear time

4. Space Complexity: O(n)
   - Counter stores frequencies of elements
   - At most n different elements

5. Key Insights:
   - Once subarray [left, right] is valid, all [left, right+i] are valid
   - Dynamic pair counting avoids recalculation
   - Sliding window finds minimum valid right for each left

6. Edge Cases:
   - k=0: all subarrays are valid
   - No valid subarrays: return 0
   - Single element: can't form pairs

7. Optimization:
   - Count extensions in O(1) time
   - Avoid recalculating pairs from scratch
   - Use incremental updates

8. Alternative Approaches:
   - Brute force: O(n^3) - check all subarrays
   - This approach: O(n) - sliding window
   - Much more efficient for large inputs
"""
