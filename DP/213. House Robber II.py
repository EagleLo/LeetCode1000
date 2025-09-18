# LeetCode 213. House Robber II
# Difficulty: Medium
# Topic: Dynamic Programming, Array

"""
Problem Description:
------------------
You are a professional robber planning to rob houses along a street. Each house has a 
certain amount of money stashed. All houses at this place are arranged in a circle. 
That means the first house is the neighbor of the last one. Meanwhile, adjacent houses 
have a security system connected, and it will automatically contact the police if two 
adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the 
maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), 
because they are adjacent houses.

Example 2:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 3:
Input: nums = [1,2,3]
Output: 3

Constraints:
* 1 <= nums.length <= 100
* 0 <= nums[i] <= 1000

Key Insight:
Since House[1] and House[n] are adjacent, they cannot be robbed together. Therefore, 
the problem becomes to rob either House[1]-House[n-1] or House[2]-House[n], depending 
on which choice offers more money. Now the problem has degenerated to the House Robber, 
which is already been solved.
"""

class Solution(object):
    def rob(self, nums):
        """
        Approach: Dynamic Programming with Circular Constraint
        - Since houses are in a circle, we can't rob both first and last house
        - Break the problem into two cases:
          1. Rob houses 0 to n-2 (exclude last house)
          2. Rob houses 1 to n-1 (exclude first house)
        - Take the maximum of both cases
        
        Time: O(n) - two passes through the array
        Space: O(n) - memoization table
        """
        if len(nums) == 1:
            return nums[0]

        return max(self._rob(nums, 0, len(nums) - 2),
                   self._rob(nums, 1, len(nums) - 1))

    def _rob(self, nums, lo, hi):
        """
        Rob houses from index lo to hi (inclusive) using dynamic programming.
        
        Args:
            nums (List[int]): Array of money in each house
            lo (int): Starting index
            hi (int): Ending index
            
        Returns:
            int: Maximum money that can be robbed
        """
        memo = {}

        def dp(i):
            """
            Dynamic programming function to find maximum money from index i onwards.
            
            Args:
                i (int): Current house index
                
            Returns:
                int: Maximum money from house i onwards
            """
            if i > hi:
                return 0
            
            if i in memo:
                return memo[i]

            # Two choices: rob current house or skip it
            # If rob current: nums[i] + dp(i+2)
            # If skip current: dp(i+1)
            memo[i] = max(nums[i] + dp(i + 2), dp(i + 1))
            return memo[i]

        return dp(lo)

def test():
    """
    Test function to verify solution with various test cases
    """
    solution = Solution()
    
    # Test case 1: Example from problem
    nums1 = [2, 3, 2]
    result1 = solution.rob(nums1)
    assert result1 == 3, f"Test case 1 failed: expected 3, got {result1}"
    
    # Test case 2: Example from problem
    nums2 = [1, 2, 3, 1]
    result2 = solution.rob(nums2)
    assert result2 == 4, f"Test case 2 failed: expected 4, got {result2}"
    
    # Test case 3: Example from problem
    nums3 = [1, 2, 3]
    result3 = solution.rob(nums3)
    assert result3 == 3, f"Test case 3 failed: expected 3, got {result3}"
    
    # Test case 4: Single house
    nums4 = [5]
    result4 = solution.rob(nums4)
    assert result4 == 5, f"Test case 4 failed: expected 5, got {result4}"
    
    # Test case 5: Two houses
    nums5 = [1, 2]
    result5 = solution.rob(nums5)
    assert result5 == 2, f"Test case 5 failed: expected 2, got {result5}"
    
    # Test case 6: All same values
    nums6 = [2, 2, 2, 2]
    result6 = solution.rob(nums6)
    assert result6 == 4, f"Test case 6 failed: expected 4, got {result6}"
    
    print("All test cases passed!")

if __name__ == "__main__":
    test()

"""
What I Learned from This Problem:
================================

1. CIRCULAR CONSTRAINT HANDLING:
   - When houses are in a circle, first and last are adjacent
   - Can't rob both first and last house together
   - Break into two separate linear problems

2. PROBLEM REDUCTION:
   - Reduce circular problem to linear problems
   - Case 1: Rob houses 0 to n-2 (exclude last)
   - Case 2: Rob houses 1 to n-1 (exclude first)
   - Take maximum of both cases

3. DYNAMIC PROGRAMMING PATTERN:
   - Use memoization to avoid recalculating subproblems
   - Two choices at each house: rob or skip
   - Optimal substructure: optimal solution contains optimal solutions to subproblems

4. EDGE CASE HANDLING:
   - Single house: return that house's value
   - Two houses: return maximum of the two
   - Empty array: handled by constraints

5. MEMOIZATION TECHNIQUE:
   - Store results of subproblems in a dictionary
   - Check if result already exists before computing
   - Reduces time complexity from exponential to linear

6. RECURSIVE THINKING:
   - At each house, decide whether to rob or skip
   - If rob: add current money + optimal solution from 2 houses ahead
   - If skip: take optimal solution from next house

7. OPTIMIZATION INSIGHT:
   - Circular constraint reduces to two linear problems
   - Each linear problem can be solved with standard DP
   - No need for complex circular DP algorithms

8. ALGORITHM DESIGN:
   - Identify the constraint (circular adjacency)
   - Break constraint into manageable cases
   - Apply known solution to each case
   - Combine results optimally

This problem taught me how to handle circular constraints by breaking them
into linear subproblems and applying standard DP techniques!
"""

"""
Solution Analysis:
----------------
1. Approach:
   - Break circular problem into two linear problems
   - Use dynamic programming with memoization
   - Take maximum of both cases

2. Algorithm:
   - Case 1: Rob houses 0 to n-2
   - Case 2: Rob houses 1 to n-1
   - For each case, use DP to find maximum money
   - Return maximum of both cases

3. Time Complexity: O(n)
   - Two passes through the array
   - Each pass takes O(n) time
   - Overall: O(n)

4. Space Complexity: O(n)
   - Memoization table stores at most n results
   - Recursion stack depth is at most n

5. Key Insights:
   - Circular constraint can be broken into linear cases
   - Standard House Robber DP applies to each case
   - No need for complex circular DP algorithms

6. Edge Cases:
   - Single house: return its value
   - Two houses: return maximum
   - All houses have same value

7. Why This Works:
   - First and last houses can't both be robbed
   - One of them must be excluded
   - Two cases cover all possibilities
   - Each case is a standard linear DP problem

8. Alternative Approaches:
   - Could use iterative DP instead of recursive
   - Could use space-optimized version
   - Current approach is clear and efficient
"""
