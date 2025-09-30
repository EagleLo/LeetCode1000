#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    """
    Calculate and print the ratios of positive, negative, and zero elements.
    
    Args:
        arr: List of integers
    """
    n = len(arr)
    n_pos = n_neg = n_zero = 0
    
    # Count positive, negative, and zero elements
    for num in arr:
        if num > 0: 
            n_pos += 1
        elif num == 0:
            n_zero += 1
        else:  # num < 0
            n_neg += 1
    
    # Print ratios with 6 decimal places
    print(f"{n_pos/n:.6f}")  # Positive ratio
    print(f"{n_neg/n:.6f}")  # Negative ratio  
    print(f"{n_zero/n:.6f}") # Zero ratio
    
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)


# Test function to verify the solution
def test_plusMinus():
    """Test the plusMinus function with the provided example."""
    print("Testing with example: [-4, 3, -9, 0, 4, 1]")
    print("Expected output:")
    print("0.500000  # 3 positive out of 6")
    print("0.333333  # 2 negative out of 6") 
    print("0.166667  # 1 zero out of 6")
    print("\nActual output:")
    plusMinus([-4, 3, -9, 0, 4, 1])
    
    print("\n" + "="*50)
    print("Testing with another example: [1, -2, -7, 9, 1, -8, -5]")
    print("Expected: 3 positive, 4 negative, 0 zero")
    plusMinus([1, -2, -7, 9, 1, -8, -5])

if __name__ == '__main__' and len(sys.argv) > 1 and sys.argv[1] == 'test':
    test_plusMinus()
