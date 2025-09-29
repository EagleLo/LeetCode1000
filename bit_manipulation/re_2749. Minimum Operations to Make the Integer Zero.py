"""
2749. Minimum Operations to Make the Integer Zero

You are given two integers num1 and num2.
In one operation, you can choose integer i in the range [0, 60] and subtract 2^i + num2 from num1.
Return the integer denoting the minimum number of operations needed to make num1 equal to 0.
If it is impossible to make num1 equal to 0, return -1.

Key insights:
1. We need to find the minimum number of operations k such that we can make num1 = 0
2. Each operation subtracts (2^i + num2) from num1
3. After k operations, we need: num1 - k*num2 - sum of k powers of 2 = 0
4. This means: num1 - k*num2 = sum of k powers of 2
5. The sum of k powers of 2 can be represented as a binary number with k set bits
6. We need to check if (num1 - k*num2) can be represented as a sum of k powers of 2
"""

class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        """
        Find minimum operations to make num1 zero.
        
        Args:
            num1: The target number to make zero
            num2: The constant added to each power of 2
            
        Returns:
            Minimum number of operations, or -1 if impossible
        """
        # Try different numbers of operations from 1 to 60
        for k in range(1, 61):
            # Calculate what remains after subtracting k*num2
            x = num1 - num2 * k
            
            # If x is negative, we can't make it zero with k operations
            if x < k:
                return -1
            
            # Check if x can be represented as sum of k powers of 2
            # This means x must have at most k set bits in binary representation
            if k >= x.bit_count():
                return k
        
        return -1


# Test cases
def test_solution():
    solution = Solution()
    
    # Example 1: num1 = 3, num2 = -2, expected output = 3
    result1 = solution.makeTheIntegerZero(3, -2)
    print(f"Test 1: num1=3, num2=-2, result={result1}, expected=3")
    assert result1 == 3, f"Expected 3, got {result1}"
    
    # Example 2: num1 = 5, num2 = 7, expected output = -1
    result2 = solution.makeTheIntegerZero(5, 7)
    print(f"Test 2: num1=5, num2=7, result={result2}, expected=-1")
    assert result2 == -1, f"Expected -1, got {result2}"
    
    # Additional test cases
    result3 = solution.makeTheIntegerZero(1, 1)
    print(f"Test 3: num1=1, num2=1, result={result3}")
    
    result4 = solution.makeTheIntegerZero(0, 0)
    print(f"Test 4: num1=0, num2=0, result={result4}")
    
    print("All tests passed!")


if __name__ == "__main__":
    test_solution()
