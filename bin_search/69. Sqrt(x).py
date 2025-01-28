# LeetCode 69. Sqrt(x)
# Difficulty: Easy
# Topic: Binary Search, Math
"""
Problem Description:
------------------
Given a non-negative integer x, compute and return the square root of x.
Since the return type is an integer, the decimal digits are truncated,
and only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator.

Example:
Input: x = 8
Output: 2
Explanation: sqrt(8) = 2.82842..., and since we truncate the decimal part, 2 is returned.

Constraints:
* 0 <= x <= 2^31 - 1
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        """
        Approach: Binary Search
        - Search space: 1 to x
        - For each mid, compare mid * mid with x
        - Return right pointer for floor value
        
        Time: O(log x)
        Space: O(1)
        """
        # Handle base cases
        if x < 2:
            return x
            
        # Initialize binary search boundaries
        left = 1
        right = x
        
        # Binary search for square root
        while left <= right:
            # Calculate midpoint safely
            mid = left + (right - left) // 2
            square = mid * mid
            
            # Check if we found exact square root
            if square == x:
                return mid
            # If square too large, search lower half
            elif square > x:
                right = mid - 1
            # If square too small, search upper half
            else:
                left = mid + 1
                
        # Return floor value of square root
        return right

def test():
    """
    Test function to verify solution with various test cases
    """
    solution = Solution()
    
    # Test cases
    test_cases = [
        {
            'input': 4,
            'expected': 2,
            'explanation': "Perfect square"
        },
        {
            'input': 8,
            'expected': 2,
            'explanation': "Floor value (sqrt(8) = 2.82842...)"
        },
        {
            'input': 0,
            'expected': 0,
            'explanation': "Edge case: zero"
        },
        {
            'input': 1,
            'expected': 1,
            'explanation': "Edge case: one"
        },
        {
            'input': 16,
            'expected': 4,
            'explanation': "Perfect square"
        },
        {
            'input': 2147395599,
            'expected': 46339,
            'explanation': "Large number"
        }
    ]
    
    # Run test cases
    for i, test in enumerate(test_cases, 1):
        result = solution.mySqrt(test['input'])
        assert result == test['expected'], \
            f"""Test case {i} failed:
            Input: {test['input']}
            Expected: {test['expected']}
            Got: {result}
            Explanation: {test['explanation']}"""
    
    print("All test cases passed!")

if __name__ == "__main__":
    test()

"""
Solution Analysis:
----------------
1. Binary Search Details:
   - Why use 'while left <= right':
     * Looking for exact value or floor
     * Need to check midpoint for equality
     * Last value needs to be checked
   
   - Why return 'right':
     * When loop ends, right points to floor value
     * left has moved past actual square root
     Example: for x = 8
     * Final state: right = 2, left = 3
     * 2 is correct floor value of sqrt(8)

2. Time Complexity: O(log x)
   - Binary search reduces search space by half each time
   - Number of steps proportional to log of input

3. Space Complexity: O(1)
   - Only using constant extra space
   - No additional data structures

4. Edge Cases Handled:
   - x = 0: Direct return
   - x = 1: Direct return
   - Perfect squares: Exact match found
   - Large numbers: No overflow due to safe mid calculation

5. Optimizations:
   - Safe midpoint calculation to avoid overflow
   - Early return for values < 2
   - Direct comparison without floating point
   
6. Common Pitfalls Avoided:
   - Integer overflow in multiplication
   - Missing floor value for non-perfect squares
   - Edge cases of 0 and 1
"""