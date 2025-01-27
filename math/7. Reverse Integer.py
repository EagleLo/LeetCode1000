# LeetCode 7. Reverse Integer
# Difficulty: Medium
# Topic: Math
"""
Problem Description:
------------------
Given a signed 32-bit integer x, return x with its digits reversed.
Return 0 if result exceeds 32-bit integer range [-2^31, 2^31 - 1].
Environment does not allow 64-bit integers.

Example:
Input: x = 123
Output: 321

Input: x = -123
Output: -321

Constraints:
* -2^31 <= x <= 2^31 - 1
"""

class Solution(object):
   def reverse(self, x):
      """
      Approach: Iteratively build reversed number with overflow checks
      :type x: int
      :rtype: int
      """
      # Constants for 32-bit integer limits
      MAX_INT = 2**31 - 1  # 2147483647
      MIN_INT = -2**31     # -2147483648
      
      # Handle negative numbers
      is_negative = x < 0
      x = abs(x)
      
      # Reverse digits
      reversed_num = 0
      while x > 0:
         digit = x % 10
         
         # Check overflow for negative numbers
         if is_negative:
            if (reversed_num > abs(MIN_INT)//10) or \
               (reversed_num == abs(MIN_INT)//10 and digit > abs(MIN_INT)%10):
                  return 0
         # Check overflow for positive numbers
         else:
            if (reversed_num > MAX_INT//10) or \
               (reversed_num == MAX_INT//10 and digit > MAX_INT%10):
                  return 0
                  
         reversed_num = reversed_num * 10 + digit
         x //= 10
         
      return -reversed_num if is_negative else reversed_num

def test():
   solution = Solution()
   assert solution.reverse(123) == 321
   assert solution.reverse(-123) == -321
   assert solution.reverse(120) == 21
   assert solution.reverse(1534236469) == 0  # Overflow test
   print("All test cases passed!")

if __name__ == "__main__":
   test()

"""
Solution Analysis:
----------------
Time Complexity: O(log x) - number of digits in x
Space Complexity: O(1) - only using constants

Key Points:
1. Handle negative numbers separately
2. Check overflow before adding each digit
3. Use integer division // and modulo % for digit extraction
4. Return 0 for any overflow case
5. Can't use 64-bit integers per problem constraints

Overflow Check Logic:
1. For positive numbers:
  - Check if current > MAX_INT/10
  - Or if current == MAX_INT/10 and digit > MAX_INT%10
2. For negative numbers:
  - Similar check against MIN_INT
  - Use abs() since we're working with positive numbers
"""