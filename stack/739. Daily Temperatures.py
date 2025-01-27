# LeetCode: 739. Daily Temperatures
# Difficulty: Medium
# Topic: Stack, Array, Monotonic Stack
"""
Problem Description:
------------------
Given an array of integers 'temperatures' represents daily temperatures, 
return an array 'answer' such that answer[i] is the number of days you have 
to wait after the ith day to get a warmer temperature.
If there is no future day for which this is possible, keep answer[i] == 0.

Example:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Constraints:
* 1 <= temperatures.length <= 10^5
* 30 <= temperatures[i] <= 100
"""

class Solution:
    def dailyTemperatures(self, temperatures):
        """
        Approach 1: Monotonic Stack
        - Use stack to track indices of temperatures
        - When finding warmer temp, calculate waiting days for all colder temps
        
        Time: O(n) - each element pushed/popped at most once
        Space: O(n) - for stack in worst case
        """
        n = len(temperatures)
        result = [0] * n
        stack = []  # stores indices of temperatures
        
        for i in range(n):
            curr_temp = temperatures[i]
            
            # Process stack while current temp is warmer than stack temps
            while stack and curr_temp > temperatures[stack[-1]]:
                prev_day = stack.pop()
                result[prev_day] = i - prev_day
            
            stack.append(i)
            
        return result

    def dailyTemperaturesBackward(self, temperatures):
        """
        Approach 2: Backward Traversal with Optimization
        - Traverse array from right to left
        - Track hottest temperature to skip unnecessary comparisons
        - Use previously calculated results to skip days
        
        Time: O(n) - with potentially fewer operations
        Space: O(1) - only output array used
        """
        n = len(temperatures)
        result = [0] * n
        hottest = 0  # track highest temperature seen
        
        for curr_day in range(n - 1, -1, -1):
            curr_temp = temperatures[curr_day]
            
            # If current temp is hottest so far, no warmer days ahead
            if curr_temp >= hottest:
                hottest = curr_temp
                continue
            
            # Search for next warmer day, using previous results to skip days
            days = 1
            while (days + curr_day < n and 
                   temperatures[curr_day + days] <= curr_temp):
                if result[curr_day + days] > 0:
                    days += result[curr_day + days]
                else:
                    days += 1
            
            if curr_day + days < n:
                result[curr_day] = days
        
        return result

def test():
    """
    Test function to verify both solutions
    """
    solution = Solution()
    
    # Test cases
    test_cases = [
        ([73,74,75,71,69,72,76,73], [1,1,4,2,1,1,0,0]),
        ([30,40,50,60], [1,1,1,0]),
        ([30,60,90], [1,1,0]),
        ([30], [0]),
        ([30,30,30], [0,0,0])
    ]
    
    for temps, expected in test_cases:
        # Test stack-based solution
        assert solution.dailyTemperatures(temps) == expected, \
            f"Stack solution failed for input {temps}"
        # Test backward solution
        assert solution.dailyTemperaturesBackward(temps) == expected, \
            f"Backward solution failed for input {temps}"
    
    print("All test cases passed!")

if __name__ == "__main__":
    test()

"""
Solution Analysis:
----------------
1. Stack-based Solution (Approach 1):
   - Advantages:
     * More intuitive to understand
     * Consistent performance
     * Good for frequently changing temperatures
   - Disadvantages:
     * Uses O(n) extra space
     * May do more operations for ascending sequences

2. Backward Solution (Approach 2):
   - Advantages:
     * O(1) extra space
     * Efficient for ascending sequences
     * Can skip days using previous results
   - Disadvantages:
     * More complex logic
     * Performance varies with input pattern

Key Implementation Details:
1. Stack solution uses indices instead of temperatures for memory efficiency
2. Backward solution tracks hottest temperature to skip unnecessary work
3. Both solutions handle edge cases (single temperature, same temperatures)
4. Comprehensive test cases verify both approaches
5. Clear variable naming improves code readability
"""