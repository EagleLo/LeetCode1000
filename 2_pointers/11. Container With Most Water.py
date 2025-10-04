"""
LeetCode: 11. Container With Most Water
Difficulty: Medium
Topic: Array, Two Pointers, Greedy

Problem Description:
------------------
You are given an integer array height of length n. There are n vertical lines 
drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the 
container contains the most water.

Return the maximum amount of water a container can store.

Key Rules:
1. Container area = min(height[i], height[j]) * (j - i)
2. Cannot slant the container
3. Find the maximum possible area

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The max area is between lines at indices 1 and 6: min(8,8) * (6-1) = 8 * 5 = 40
Wait, let me recalculate: between indices 1 and 8: min(8,7) * (8-1) = 7 * 7 = 49

Example 2:
Input: height = [1,1]
Output: 1

Constraints:
* 2 <= n <= 10^5
* 0 <= height[i] <= 10^4
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Approach 1: Two Pointers (Optimal)
        Use two pointers from both ends and move the pointer with smaller height.
        
        Key Insight: We can safely move the pointer with smaller height because:
        - The area is limited by the smaller height
        - Moving the larger height pointer can only decrease the area
        - Moving the smaller height pointer might find a better solution
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        left = 0
        right = len(height) - 1
        max_area = 0
        
        while left < right:
            # Calculate current area
            current_area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, current_area)
            
            # Move the pointer with smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area

    def maxArea_brute_force(self, height: List[int]) -> int:
        """
        Approach 2: Brute Force
        Check all possible pairs of lines.
        
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        max_area = 0
        n = len(height)
        
        for i in range(n):
            for j in range(i + 1, n):
                area = min(height[i], height[j]) * (j - i)
                max_area = max(max_area, area)
        
        return max_area

    def maxArea_optimized_brute(self, height: List[int]) -> int:
        """
        Approach 3: Optimized Brute Force
        Skip some unnecessary calculations.
        
        Time Complexity: O(n^2) worst case, but better average case
        Space Complexity: O(1)
        """
        max_area = 0
        n = len(height)
        
        for i in range(n):
            # Skip if current height is 0
            if height[i] == 0:
                continue
                
            for j in range(i + 1, n):
                # Skip if height[j] is 0
                if height[j] == 0:
                    continue
                    
                area = min(height[i], height[j]) * (j - i)
                max_area = max(max_area, area)
        
        return max_area

    def maxArea_verbose(self, height: List[int]) -> int:
        """
        Approach 4: Verbose Two Pointers
        Step-by-step simulation with detailed output.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        left = 0
        right = len(height) - 1
        max_area = 0
        
        print(f"Initial: left={left}, right={right}")
        print(f"Height: {height}")
        print()
        
        while left < right:
            current_area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, current_area)
            
            print(f"Step: left={left} (height={height[left]}), right={right} (height={height[right]})")
            print(f"  Current area: min({height[left]}, {height[right]}) * ({right} - {left}) = {current_area}")
            print(f"  Max area so far: {max_area}")
            
            if height[left] < height[right]:
                print(f"  Moving left pointer: {left} -> {left + 1}")
                left += 1
            else:
                print(f"  Moving right pointer: {right} -> {right - 1}")
                right -= 1
            print()
        
        print(f"Final max area: {max_area}")
        return max_area


def test_solution():
    """
    Comprehensive test function for container with most water.
    """
    solution = Solution()
    
    # Test Case 1: Basic case
    print("Test Case 1: [1,8,6,2,5,4,8,3,7]")
    result1 = solution.maxArea([1,8,6,2,5,4,8,3,7])
    expected1 = 49
    print(f"Result: {result1}, Expected: {expected1}")
    assert result1 == expected1, f"Test 1 failed: got {result1}, expected {expected1}"
    print("✓ Passed\n")
    
    # Test Case 2: Simple case
    print("Test Case 2: [1,1]")
    result2 = solution.maxArea([1,1])
    expected2 = 1
    print(f"Result: {result2}, Expected: {expected2}")
    assert result2 == expected2, f"Test 2 failed: got {result2}, expected {expected2}"
    print("✓ Passed\n")
    
    # Test Case 3: Ascending heights
    print("Test Case 3: [1,2,3,4,5]")
    result3 = solution.maxArea([1,2,3,4,5])
    expected3 = 6  # min(1,5) * 4 = 4, min(2,5) * 3 = 6, min(3,5) * 2 = 6, min(4,5) * 1 = 4
    print(f"Result: {result3}, Expected: {expected3}")
    assert result3 == expected3, f"Test 3 failed: got {result3}, expected {expected3}"
    print("✓ Passed\n")
    
    # Test Case 4: Descending heights
    print("Test Case 4: [5,4,3,2,1]")
    result4 = solution.maxArea([5,4,3,2,1])
    expected4 = 6  # min(5,1) * 4 = 4, min(5,2) * 3 = 6, min(4,2) * 2 = 4, min(4,3) * 1 = 3
    print(f"Result: {result4}, Expected: {expected4}")
    assert result4 == expected4, f"Test 4 failed: got {result4}, expected {expected4}"
    print("✓ Passed\n")
    
    # Test Case 5: All same height
    print("Test Case 5: [3,3,3,3,3]")
    result5 = solution.maxArea([3,3,3,3,3])
    expected5 = 12  # min(3,3) * 4 = 12
    print(f"Result: {result5}, Expected: {expected5}")
    assert result5 == expected5, f"Test 5 failed: got {result5}, expected {expected5}"
    print("✓ Passed\n")
    
    # Test Case 6: Edge case - two elements
    print("Test Case 6: [2,3]")
    result6 = solution.maxArea([2,3])
    expected6 = 2  # min(2,3) * 1 = 2
    print(f"Result: {result6}, Expected: {expected6}")
    assert result6 == expected6, f"Test 6 failed: got {result6}, expected {expected6}"
    print("✓ Passed\n")
    
    # Test Case 7: Complex case
    print("Test Case 7: [4,3,2,1,4]")
    result7 = solution.maxArea([4,3,2,1,4])
    expected7 = 16  # min(4,4) * 4 = 16
    print(f"Result: {result7}, Expected: {expected7}")
    assert result7 == expected7, f"Test 7 failed: got {result7}, expected {expected7}"
    print("✓ Passed\n")
    
    print("All test cases passed! 🎉")


def analyze_complexity():
    """
    Complexity Analysis for container with most water problem.
    """
    print("Complexity Analysis:")
    print("=" * 50)
    
    print("Two Pointers Approach (Optimal):")
    print("Time Complexity: O(n)")
    print("- Each element is visited at most once")
    print("- Two pointers move towards each other")
    print("- Total operations: O(n)")
    
    print("\nSpace Complexity: O(1)")
    print("- Only a few variables needed")
    print("- No additional data structures")
    
    print("\nBrute Force Approach:")
    print("Time Complexity: O(n^2)")
    print("- Check all possible pairs")
    print("- For each i, check all j > i")
    print("- Total pairs: n*(n-1)/2")
    
    print("\nSpace Complexity: O(1)")
    print("- Only a few variables needed")
    
    print("\nKey Insights:")
    print("1. Two pointers approach is optimal")
    print("2. Key insight: move the pointer with smaller height")
    print("3. Why this works:")
    print("   - Area = min(height[left], height[right]) * (right - left)")
    print("   - Moving the larger height pointer can only decrease the area")
    print("   - Moving the smaller height pointer might find a better solution")
    print("4. This is a classic two pointers problem")


def demonstrate_approaches():
    """
    Demonstrate different approaches to the problem.
    """
    print("Comparing Different Approaches:")
    print("=" * 50)
    
    solution = Solution()
    test_cases = [[1,8,6,2,5,4,8,3,7], [1,1], [4,3,2,1,4]]
    
    for heights in test_cases:
        print(f"\nTest: {heights}")
        print("-" * 30)
        
        # Two pointers approach
        result1 = solution.maxArea(heights)
        print(f"Two Pointers: {result1}")
        
        # Brute force approach
        result2 = solution.maxArea_brute_force(heights)
        print(f"Brute Force: {result2}")
        
        # Verify they're the same
        assert result1 == result2, f"Results don't match: {result1} vs {result2}"
        print("✓ Both approaches give same result")


def simulate_step_by_step():
    """
    Simulate the two pointers approach step by step.
    """
    print("Step-by-step Simulation:")
    print("=" * 50)
    
    solution = Solution()
    result = solution.maxArea_verbose([1,8,6,2,5,4,8,3,7])
    print(f"\nFinal result: {result}")


if __name__ == "__main__":
    test_solution()
    print("\n" + "=" * 60)
    analyze_complexity()
    print("\n" + "=" * 60)
    demonstrate_approaches()
    print("\n" + "=" * 60)
    simulate_step_by_step()
