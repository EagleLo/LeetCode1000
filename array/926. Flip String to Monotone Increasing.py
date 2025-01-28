# LeetCode 926. Flip String to Monotone Increasing
# Difficulty: Medium
# Topic: String, Dynamic Programming
"""
Problem Description:
------------------
A binary string is monotone increasing if it consists of some number of 0's 
(possibly none), followed by some number of 1's (also possibly none).

Given a binary string s, you can flip s[i] changing it from 0 to 1 or from 1 to 0.
Return the minimum number of flips needed to make s monotone increasing.

Example:
Input: s = "00110"
Output: 1
Explanation: We flip the last digit to get 00111.

Constraints:
* 1 <= s.length <= 10^5
* s[i] is either '0' or '1'
"""

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        """
        Approach: Two-Pass Counter
        - First pass: Count total zeros (potential flips to ones)
        - Second pass: Try each position as transition point
        
        Time Complexity: O(n) where n is length of string
        Space Complexity: O(1)
        
        :type s: str
        :rtype: int
        """
        # First pass: count total zeros
        m = 0  # Count of flips needed
        for c in s:
            if c == '0':
                m += 1
        
        ans = m  # Initial answer if we flip all to 1s
        
        # Second pass: try each position as transition point
        for c in s:
            if c == '0':
                # Don't need to flip this 0 (it's before transition)
                m -= 1
                ans = min(ans, m)
            else:
                # Need to flip this 1 to 0 (it's before transition)
                m += 1
        
        return ans

def test():
    """
    Test function to verify solution
    """
    solution = Solution()
    
    # Test cases
    test_cases = [
        {
            'input': "00110",
            'expected': 1,
            'explanation': "Flip last 0 to get 00111"
        },
        {
            'input': "010110",
            'expected': 2,
            'explanation': "Flip to get 011111 or 000111"
        },
        {
            'input': "00011000",
            'expected': 2,
            'explanation': "Flip to get 00000000"
        },
        {
            'input': "11111",
            'expected': 0,
            'explanation': "Already monotone increasing"
        },
        {
            'input': "00000",
            'expected': 0,
            'explanation': "Already monotone increasing"
        }
    ]
    
    for i, test in enumerate(test_cases, 1):
        result = solution.minFlipsMonoIncr(test['input'])
        assert result == test['expected'], \
            f"""Test case {i} failed: 
            Input: {test['input']}
            Expected: {test['expected']} ({test['explanation']})
            Got: {result}"""
    
    print("All test cases passed!")

if __name__ == "__main__":
    test()

"""
Solution Analysis:
----------------
Time Complexity: O(n)
- Two passes through the string
- Each operation within the loops is O(1)

Space Complexity: O(1)
- Only using a constant amount of extra space
- No additional data structures needed

Key Points:
1. Algorithm Insight:
   - For monotone increasing string, all 0s must come before all 1s
   - At some point, we transition from 0s to 1s
   - Need to find optimal transition point

2. Two-Pass Approach:
   First Pass:
   - Count total zeros (potential flips to ones)
   - This gives maximum flips needed
   
   Second Pass:
   - For each position, consider it as transition point
   - Before position: should be all zeros
   - After position: should be all ones
   - Track minimum flips needed across all positions

3. Optimization:
   - No need for additional arrays/storage
   - Single variable tracks current flip count
   - Continuously update minimum flips needed

4. Edge Cases Handled:
   - All zeros or all ones
   - Alternating zeros and ones
   - String starts/ends with different values
"""