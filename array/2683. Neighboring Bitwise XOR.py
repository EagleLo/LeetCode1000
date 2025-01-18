# LeetCode 2683: Neighboring Bitwise XOR
# Difficulty: Medium
# Topic: Array, Bit Manipulation

"""
Problem Description:
------------------
Given a 0-indexed array 'derived' of length n that is derived by computing the bitwise XOR (⊕)
of adjacent values in a binary array 'original' of length n.

For each index i in the range [0, n - 1]:
- If i = n - 1, then derived[i] = original[i] ⊕ original[0]
- Otherwise, derived[i] = original[i] ⊕ original[i + 1]

Task: Determine if there exists a valid binary array 'original' that could have formed 'derived'.
Return true if such an array exists, or false otherwise.

Note: A binary array contains only 0's and 1's.
"""

class Solution:
    def doesValidArrayExist(self, derived):
        """
        Approach:
        1. We can construct the original array by starting with 0 as the first element
        2. Then for each element in derived, we can XOR it with the current element 
           to get the next element in original
        3. Finally, check if the last XOR operation matches the first element we assumed
        
        Key insight: If we start with 0, we can determine all other elements uniquely.
        The solution exists if and only if the XOR chain forms a valid cycle.
        
        Time Complexity: O(n) where n is the length of derived array
        Space Complexity: O(1) as we only use constant extra space
        
        :type derived: List[int]
        :rtype: bool
        """
        # Start with assuming first element is 0
        cur = 0
        n = len(derived)
        
        # Calculate XOR chain for all elements
        for i in range(n):
            cur ^= derived[i]
            
        # Check if the result is 0 (valid cycle)
        return cur == 0


# Test cases
def test_solution():
    solution = Solution()
    
    # Test Case 1
    assert solution.doesValidArrayExist([1, 1, 0]) == True, "Test case 1 failed"
    # Original array can be [0,1,0]
    
    # Test Case 2
    assert solution.doesValidArrayExist([1, 1]) == True, "Test case 2 failed"
    # Original array can be [0,1]
    
    # Test Case 3
    assert solution.doesValidArrayExist([1, 0]) == False, "Test case 3 failed"
    # No valid original array exists
    
    # Additional Test Case 4
    assert solution.doesValidArrayExist([0, 0, 0]) == True, "Test case 4 failed"
    # Original array can be [0,0,0]
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_solution()

"""
Solution Analysis:
----------------
Time Complexity: O(n)
- We traverse the derived array once, performing constant time operations at each step

Space Complexity: O(1)
- We only use a constant amount of extra space regardless of input size

Key Points:
1. The problem can be solved by focusing on the XOR properties:
   - a ⊕ b = c implies b = a ⊕ c
   - XOR is associative and commutative
2. If a solution exists, we can find it by assuming the first element is 0
3. The solution exists if and only if the XOR chain forms a valid cycle back to our initial assumption

Note: While we could try to construct the entire original array, it's not necessary
for determining if a solution exists. We only need to track the running XOR value.
"""