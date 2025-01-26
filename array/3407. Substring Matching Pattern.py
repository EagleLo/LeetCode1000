# LeetCode 3407. Substring Matching Pattern
# Difficulty: Easy
# Topic: String, String Matching
"""
Problem Description:
------------------
Given string s and pattern p containing exactly one '*'.
The '*' can be replaced with any sequence of 0+ characters.
Return true if p can be made a substring of s.

Example:
Input: s = "leetcode", p = "ee*e"
Output: true
Explanation: '*' becomes "tcod" to match "eetcode"

Constraints:
* 1 <= s.length <= 50
* 1 <= p.length <= 50
* s contains only lowercase English letters
* p contains only lowercase letters and one '*'
"""

class Solution(object):
   def hasMatch(self, s, p):
       """
       Approach: Split pattern at '*' and check if parts exist in order
       :type s: str
       :type p: str
       :rtype: bool
       """
       # Split pattern into before/after '*'
       sub_p = p.split('*')
       p1, p2 = sub_p[0], sub_p[1]
       
       # Find first part
       start = s.find(p1)
       if start == -1:
           return False
           
       # Find second part after first part
       end = s.find(p2, start + len(p1))
       if end == -1:
           return False
           
       return True

def test():
   solution = Solution()
   assert solution.hasMatch("leetcode", "ee*e") == True
   assert solution.hasMatch("car", "c*v") == False
   assert solution.hasMatch("luck", "u*") == True
   print("All test cases passed!")

if __name__ == "__main__":
   test()

"""
Solution Analysis:
----------------
Time Complexity: O(n) where n is length of s
- split() is O(m) where m is length of p
- find() is O(n)

Space Complexity: O(1)
- Only storing two substrings of constant size

Key Takeaways:
1. str.split() splits string on character
2. str.find() returns -1 if not found
3. str.find(sub, start) searches from index start
4. Pattern matching can often be broken into parts
"""