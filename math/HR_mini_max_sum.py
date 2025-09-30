#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    """
    Find the minimum and maximum values that can be calculated by summing 
    exactly four of the five integers.
    
    Key insight: 
    - Minimum sum = total sum - maximum element (exclude the largest)
    - Maximum sum = total sum - minimum element (exclude the smallest)
    
    Args:
        arr: List of 5 positive integers
    """
    # Calculate total sum of all elements
    total_sum = sum(arr)
    
    # Minimum sum: exclude the largest element
    min_sum = total_sum - max(arr)
    
    # Maximum sum: exclude the smallest element  
    max_sum = total_sum - min(arr)
    
    # Print the results as space-separated integers
    print(f"{min_sum} {max_sum}")


def test_miniMaxSum():
    """Test the miniMaxSum function with provided examples."""
    print("Testing miniMaxSum function:")
    print("=" * 40)
    
    # Test case 1: [1, 2, 3, 4, 5]
    print("Test 1: [1, 2, 3, 4, 5]")
    print("Expected: 10 14")
    print("Explanation:")
    print("  Sum without 1: 2+3+4+5 = 14 (max)")
    print("  Sum without 2: 1+3+4+5 = 13")
    print("  Sum without 3: 1+2+4+5 = 12") 
    print("  Sum without 4: 1+2+3+5 = 11")
    print("  Sum without 5: 1+2+3+4 = 10 (min)")
    print("Actual result:")
    miniMaxSum([1, 2, 3, 4, 5])
    print()
    
    # Test case 2: [7, 69, 2, 221, 8974]
    print("Test 2: [7, 69, 2, 221, 8974]")
    print("Expected: 299 9271")
    print("Actual result:")
    miniMaxSum([7, 69, 2, 221, 8974])
    print()
    
    # Test case 3: Edge case with same numbers
    print("Test 3: [5, 5, 5, 5, 5]")
    print("Expected: 20 20 (all sums are equal)")
    print("Actual result:")
    miniMaxSum([5, 5, 5, 5, 5])
    print()
    
    # Test case 4: Large numbers (testing 64-bit integer handling)
    print("Test 4: [1000000000, 2000000000, 3000000000, 4000000000, 5000000000]")
    print("Expected: 10000000000 14000000000")
    print("Actual result:")
    miniMaxSum([1000000000, 2000000000, 3000000000, 4000000000, 5000000000])


if __name__ == '__main__':
    # Check if running in test mode
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        test_miniMaxSum()
    else:
        # Normal execution for HackerRank
        arr = list(map(int, input().rstrip().split()))
        miniMaxSum(arr)
