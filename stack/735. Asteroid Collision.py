"""
LeetCode: 735. Asteroid Collision
Difficulty: Medium
Topic: Stack, Array, Simulation

Problem Description:
------------------
We are given an array asteroids of integers representing asteroids in a row. 
The indices of the asteroids in the array represent their relative position in space.

For each asteroid, the absolute value represents its size, and the sign represents 
its direction (positive meaning right, negative meaning left). Each asteroid moves 
at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, 
the smaller one will explode. If both are the same size, both will explode. 
Two asteroids moving in the same direction will never meet.

Key Rules:
1. Positive asteroids move right (→)
2. Negative asteroids move left (←)
3. Collision only happens when right-moving asteroid is followed by left-moving asteroid
4. When they collide:
   - Smaller asteroid explodes
   - Same size: both explode
   - Larger asteroid survives

Example 1:
Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.

Example 2:
Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.

Example 3:
Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.

Constraints:
* 2 <= asteroids.length <= 10^4
* -1000 <= asteroids[i] <= 1000
* asteroids[i] != 0
"""

from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        Approach 1: Stack-based Simulation
        Use a stack to simulate the collision process.
        
        Algorithm:
        1. For each asteroid, check if it collides with the top of stack
        2. Collision happens when: current < 0 and stack[-1] > 0
        3. Handle collision based on sizes:
           - If stack asteroid is smaller: remove it and continue checking
           - If same size: remove both
           - If stack asteroid is larger: current asteroid explodes
        4. Add surviving asteroids to stack
        
        Time Complexity: O(n) - each asteroid pushed/popped at most once
        Space Complexity: O(n) - for the stack in worst case
        """
        stack = []
        
        for asteroid in asteroids:
            # Keep processing collisions while current asteroid survives
            while stack and asteroid < 0 and stack[-1] > 0:
                if stack[-1] < abs(asteroid):
                    # Stack asteroid is smaller, remove it
                    stack.pop()
                elif stack[-1] == abs(asteroid):
                    # Same size, both explode
                    stack.pop()
                    break  # Current asteroid also explodes
                else:
                    # Stack asteroid is larger, current explodes
                    break
            else:
                # No collision or current asteroid survived
                stack.append(asteroid)
        
        return stack

    def asteroidCollision_optimized(self, asteroids: List[int]) -> List[int]:
        """
        Approach 2: Optimized Stack Solution
        More efficient version with clearer logic.
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        stack = []
        
        for asteroid in asteroids:
            # Process all possible collisions
            while stack and asteroid < 0 and stack[-1] > 0:
                if stack[-1] < abs(asteroid):
                    stack.pop()
                elif stack[-1] == abs(asteroid):
                    stack.pop()
                    break
                else:
                    break
            else:
                stack.append(asteroid)
        
        return stack

    def asteroidCollision_verbose(self, asteroids: List[int]) -> List[int]:
        """
        Approach 3: Verbose Version for Understanding
        Step-by-step simulation with detailed comments.
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        stack = []
        
        for i, asteroid in enumerate(asteroids):
            print(f"Processing asteroid {asteroid} at position {i}")
            print(f"Current stack: {stack}")
            
            # Check for collisions
            while stack and asteroid < 0 and stack[-1] > 0:
                top = stack[-1]
                print(f"  Collision between {top} and {asteroid}")
                
                if top < abs(asteroid):
                    # Top asteroid is smaller, remove it
                    print(f"  {top} explodes (smaller than {abs(asteroid)})")
                    stack.pop()
                elif top == abs(asteroid):
                    # Same size, both explode
                    print(f"  Both {top} and {abs(asteroid)} explode (same size)")
                    stack.pop()
                    break
                else:
                    # Top asteroid is larger, current explodes
                    print(f"  {asteroid} explodes (smaller than {top})")
                    break
            
            else:
                # No collision or current survived
                print(f"  Adding {asteroid} to stack")
                stack.append(asteroid)
            
            print(f"  Stack after processing: {stack}\n")
        
        return stack


def test_solution():
    """
    Comprehensive test function for asteroid collision.
    """
    solution = Solution()
    
    # Test Case 1: Basic collision
    print("Test Case 1: [5,10,-5]")
    result1 = solution.asteroidCollision([5,10,-5])
    expected1 = [5,10]
    print(f"Result: {result1}, Expected: {expected1}")
    assert result1 == expected1, f"Test 1 failed: got {result1}, expected {expected1}"
    print("✓ Passed\n")
    
    # Test Case 2: Both explode
    print("Test Case 2: [8,-8]")
    result2 = solution.asteroidCollision([8,-8])
    expected2 = []
    print(f"Result: {result2}, Expected: {expected2}")
    assert result2 == expected2, f"Test 2 failed: got {result2}, expected {expected2}"
    print("✓ Passed\n")
    
    # Test Case 3: Chain reaction
    print("Test Case 3: [10,2,-5]")
    result3 = solution.asteroidCollision([10,2,-5])
    expected3 = [10]
    print(f"Result: {result3}, Expected: {expected3}")
    assert result3 == expected3, f"Test 3 failed: got {result3}, expected {expected3}"
    print("✓ Passed\n")
    
    # Test Case 4: No collisions
    print("Test Case 4: [1,2,3,4,5]")
    result4 = solution.asteroidCollision([1,2,3,4,5])
    expected4 = [1,2,3,4,5]
    print(f"Result: {result4}, Expected: {expected4}")
    assert result4 == expected4, f"Test 4 failed: got {result4}, expected {expected4}"
    print("✓ Passed\n")
    
    # Test Case 5: All left-moving
    print("Test Case 5: [-1,-2,-3,-4,-5]")
    result5 = solution.asteroidCollision([-1,-2,-3,-4,-5])
    expected5 = [-1,-2,-3,-4,-5]
    print(f"Result: {result5}, Expected: {expected5}")
    assert result5 == expected5, f"Test 5 failed: got {result5}, expected {expected5}"
    print("✓ Passed\n")
    
    # Test Case 6: Complex chain reaction
    print("Test Case 6: [5,10,-5,8,-8,3,-3]")
    result6 = solution.asteroidCollision([5,10,-5,8,-8,3,-3])
    expected6 = [5,10]
    print(f"Result: {result6}, Expected: {expected6}")
    assert result6 == expected6, f"Test 6 failed: got {result6}, expected {expected6}"
    print("✓ Passed\n")
    
    # Test Case 7: Edge case - single asteroid
    print("Test Case 7: [5]")
    result7 = solution.asteroidCollision([5])
    expected7 = [5]
    print(f"Result: {result7}, Expected: {expected7}")
    assert result7 == expected7, f"Test 7 failed: got {result7}, expected {expected7}"
    print("✓ Passed\n")
    
    print("All test cases passed! 🎉")


def analyze_complexity():
    """
    Complexity Analysis for asteroid collision problem.
    """
    print("Complexity Analysis:")
    print("=" * 50)
    
    print("Time Complexity: O(n)")
    print("- Each asteroid is processed exactly once")
    print("- Each asteroid is pushed to stack at most once")
    print("- Each asteroid is popped from stack at most once")
    print("- Total operations: O(n)")
    
    print("\nSpace Complexity: O(n)")
    print("- Stack can hold at most n asteroids in worst case")
    print("- Worst case: all asteroids survive (no collisions)")
    print("- Best case: all asteroids explode (O(1) space)")
    
    print("\nKey Insights:")
    print("1. Stack is perfect for this problem because:")
    print("   - We need to check collisions with recent asteroids")
    print("   - LIFO order matches the collision sequence")
    print("   - We can efficiently remove exploded asteroids")
    
    print("\n2. Collision Rules:")
    print("   - Only right-moving (positive) followed by left-moving (negative) collide")
    print("   - Same direction asteroids never collide")
    print("   - Size determines survival")
    
    print("\n3. Algorithm Efficiency:")
    print("   - Each asteroid pushed/popped at most once")
    print("   - No redundant operations")
    print("   - Optimal O(n) time complexity")


def simulate_collision_process():
    """
    Simulate the collision process step by step for better understanding.
    """
    print("Step-by-step Simulation:")
    print("=" * 50)
    
    asteroids = [10, 2, -5]
    print(f"Initial asteroids: {asteroids}")
    print("Processing with verbose output:\n")
    
    solution = Solution()
    result = solution.asteroidCollision_verbose(asteroids)
    print(f"Final result: {result}")


if __name__ == "__main__":
    test_solution()
    print("\n" + "=" * 60)
    analyze_complexity()
    print("\n" + "=" * 60)
    simulate_collision_process()
