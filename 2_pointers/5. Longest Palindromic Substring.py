# LeetCode 5. Longest Palindromic Substring
# Difficulty: Medium
# Topic: String, Dynamic Programming
"""
Problem Description:
------------------
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters.
"""

class Solution(object):
   def checkPalindrome(self, s, l, r, res, res_len):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if r - l + 1 > res_len:
                res_len = r - l + 1
                res = s[l:r+1]
            r += 1
            l -= 1
        return res, res_len
   def longestPalindrome(self, s):
       """
       Approach: Expand Around Center
       For each character, treat it as center and expand in both directions
       Check both odd and even length palindromes
       
       :type s: str
       :rtype: str
       """
       res = ""
       res_len = 0
       
       for i in range(len(s)):
           # odd palindromes
           res, res_len = self.checkPalindrome(s, i, i, res, res_len)
           # even palindromes
           res, res_len = self.checkPalindrome(s, i, i + 1, res, res_len)
               
       return res

# Test cases
def test():
   solution = Solution()
   assert solution.longestPalindrome("babad") in ["bab", "aba"]
   assert solution.longestPalindrome("cbbd") == "bb"
   assert solution.longestPalindrome("a") == "a"
   print("All test cases passed!")

if __name__ == "__main__":
   test()

"""
Solution Analysis:
----------------
Time Complexity: O(n²)
- For each character (n), we might expand up to length of string (n)

Space Complexity: O(1)
- Only storing result string
- No extra space needed that grows with input

Key Points:
1. Two pointers technique useful for palindrome problems
2. Need to check both odd and even length palindromes
3. Expanding around center is intuitive approach
4. While Manacher's algorithm exists for O(n), this solution is more practical
  for most cases due to simplicity

Note: More optimal O(n) solution exists using Manacher's Algorithm but is more
complex to implement.
"""