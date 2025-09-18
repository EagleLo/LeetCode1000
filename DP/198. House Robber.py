# LeetCode 198. House Robber
# Difficulty: Medium
# Topic: Dynamic Programming, Array

"""
Problem Description:
------------------
You are a professional robber planning to rob houses along a street. Each house has a 
certain amount of money stashed, the only constraint stopping you from robbing each of 
them is that adjacent houses have security systems connected and it will automatically 
contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the 
maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.

Constraints:
* 1 <= nums.length <= 100
* 0 <= nums[i] <= 400
"""

class Solution(object):
    def rob(self, nums):
        """
        Approach: Dynamic Programming with Memoization
        - Use recursive approach with memoization to avoid recalculating subproblems
        - At each house, we have two choices: rob it or skip it
        - If we rob current house, we can't rob the next house
        - If we skip current house, we can rob the next house
        - Take the maximum of both choices
        
        Time: O(n) - each subproblem is solved once
        Space: O(n) - memoization table + recursion stack
        """
        self.memo = {}
        self.nums = nums
        self.n = len(nums)
        return self.helper(0)
    
    def helper(self, idx):
        """
        Helper function to find maximum money from index idx onwards.
        
        Args:
            idx (int): Current house index
            
        Returns:
            int: Maximum money that can be robbed from house idx onwards
        """
        # Base case: if we've gone past all houses
        if idx >= self.n:
            return 0

        # If we've already calculated this subproblem, return cached result
        if idx in self.memo:
            return self.memo[idx]

        # Two choices:
        # 1. Rob current house: nums[idx] + helper(idx + 2)
        # 2. Skip current house: helper(idx + 1)
        # Take the maximum
        self.memo[idx] = max(
            self.nums[idx] + self.helper(idx + 2),  # Rob current house
            self.helper(idx + 1)                    # Skip current house
        )

        return self.memo[idx]

def test():
    """
    Test function to verify solution with various test cases
    """
    solution = Solution()
    
    # Test case 1: Example from problem
    nums1 = [1, 2, 3, 1]
    result1 = solution.rob(nums1)
    assert result1 == 4, f"Test case 1 failed: expected 4, got {result1}"
    
    # Test case 2: Example from problem
    nums2 = [2, 7, 9, 3, 1]
    result2 = solution.rob(nums2)
    assert result2 == 12, f"Test case 2 failed: expected 12, got {result2}"
    
    # Test case 3: Single house
    nums3 = [5]
    result3 = solution.rob(nums3)
    assert result3 == 5, f"Test case 3 failed: expected 5, got {result3}"
    
    # Test case 4: Two houses
    nums4 = [1, 2]
    result4 = solution.rob(nums4)
    assert result4 == 2, f"Test case 4 failed: expected 2, got {result4}"
    
    # Test case 5: All same values
    nums5 = [3, 3, 3, 3]
    result5 = solution.rob(nums5)
    assert result5 == 6, f"Test case 5 failed: expected 6, got {result5}"
    
    # Test case 6: Alternating pattern
    nums6 = [1, 0, 1, 0, 1]
    result6 = solution.rob(nums6)
    assert result6 == 3, f"Test case 6 failed: expected 3, got {result6}"
    
    print("All test cases passed!")

if __name__ == "__main__":
    test()

"""
What I Learned from This Problem:
================================

1. DYNAMIC PROGRAMMING FUNDAMENTALS:
   - Break down complex problem into simpler subproblems
   - Use memoization to avoid recalculating subproblems
   - Optimal substructure: optimal solution contains optimal solutions to subproblems

2. RECURSIVE THINKING:
   - At each house, make a decision: rob or skip
   - If rob: add current money + optimal solution from 2 houses ahead
   - If skip: take optimal solution from next house
   - Base case: no more houses to consider

3. MEMOIZATION TECHNIQUE:
   - Store results of subproblems in a dictionary
   - Check if result already exists before computing
   - Reduces time complexity from exponential to linear

4. CONSTRAINT HANDLING:
   - Adjacent houses cannot be robbed together
   - This creates a dependency between decisions
   - Must consider the impact of current decision on future decisions

5. OPTIMAL SUBSTRUCTURE:
   - If we know the optimal solution for houses i+1 to n-1,
     we can find optimal solution for houses i to n-1
   - This property allows us to use dynamic programming

6. OVERLAPPING SUBPROBLEMS:
   - Same subproblems are solved multiple times in naive recursion
   - Memoization eliminates redundant calculations
   - Each subproblem is solved exactly once

7. EDGE CASE HANDLING:
   - Empty array: return 0
   - Single house: return its value
   - Two houses: return maximum of the two

8. ALGORITHM PATTERN:
   - Top-down approach with memoization
   - Recursive function with base cases
   - Store and reuse computed results

This problem taught me the fundamentals of dynamic programming and how to
apply memoization to solve optimization problems efficiently!
"""

"""
Solution Analysis:
----------------
1. Approach:
   - Use recursive approach with memoization
   - At each house, decide whether to rob or skip
   - Take maximum of both choices

2. Algorithm:
   - helper(idx) returns maximum money from house idx onwards
   - If rob house idx: nums[idx] + helper(idx + 2)
   - If skip house idx: helper(idx + 1)
   - Base case: idx >= n (no more houses)

3. Time Complexity: O(n)
   - Each subproblem is solved exactly once
   - n subproblems total
   - Each subproblem takes O(1) time

4. Space Complexity: O(n)
   - Memoization table: O(n)
   - Recursion stack: O(n) in worst case
   - Overall: O(n)

5. Key Insights:
   - Adjacent constraint creates dependency between decisions
   - Optimal substructure allows DP approach
   - Memoization eliminates redundant calculations

6. Edge Cases:
   - Empty array: handled by base case
   - Single house: return its value
   - Two houses: return maximum

7. Why This Works:
   - Each decision affects future decisions
   - We can't rob adjacent houses
   - DP finds optimal sequence of decisions
   - Memoization ensures efficiency

8. Alternative Approaches:
   - Bottom-up DP: iterative approach
   - Space-optimized: only store last two values
   - Current approach is clear and intuitive
"""
