# LeetCode 2021. Brightest Position on Street
# Difficulty: Medium
# Topic: Prefix Sum, Line Sweep, Hash Table

"""
Problem Description:
------------------
A perfectly straight street is represented by a number line. The street has street lamp(s) 
on it and is represented by a 2D integer array lights. Each lights[i] = [positioni, rangei] 
indicates that there is a street lamp at position positioni that lights up the area from 
[positioni - rangei, positioni + rangei] (inclusive).

The brightness of a position p is defined as the number of street lamp that light up the position p.

Given lights, return the brightest position on the street. If there are multiple brightest 
positions, return the smallest one.

Example 1:
Input: lights = [[-3,2],[1,2],[3,3]]
Output: -1
Explanation:
The first street lamp lights up the area from [(-3) - 2, (-3) + 2] = [-5, -1].
The second street lamp lights up the area from [1 - 2, 1 + 2] = [-1, 3].
The third street lamp lights up the area from [3 - 3, 3 + 3] = [0, 6].

Position -1 has a brightness of 2, illuminated by the first and second street light.
Positions 0, 1, 2, and 3 have a brightness of 2, illuminated by the second and third street light.
Out of all these positions, -1 is the smallest, so return it.

Example 2:
Input: lights = [[1,0],[0,1]]
Output: 1
Explanation:
The first street lamp lights up the area from [1 - 0, 1 + 0] = [1, 1].
The second street lamp lights up the area from [0 - 1, 0 + 1] = [-1, 1].

Position 1 has a brightness of 2, illuminated by the first and second street light.
Return 1 because it is the brightest position on the street.

Example 3:
Input: lights = [[1,2]]
Output: -1
Explanation:
The first street lamp lights up the area from [1 - 2, 1 + 2] = [-1, 3].

Positions -1, 0, 1, 2, and 3 have a brightness of 1, illuminated by the first street light.
Out of all these positions, -1 is the smallest, so return it.

Constraints:
* 1 <= lights.length <= 10^5
* lights[i].length == 2
* -10^8 <= positioni <= 10^8
* 0 <= rangei <= 10^8
"""

from collections import defaultdict

class Solution(object):
    def brightestPosition(self, lights):
        """
        Approach: Line Sweep Algorithm with Prefix Sum
        - Use events to mark start and end of each light's range
        - Sort events and sweep through to find maximum brightness
        - This avoids iterating through every position individually
        
        Time: O(n log n) - sorting the events
        Space: O(n) - storing events for each light
        """
        # 2nd method - OPTIMIZED: Line Sweep Algorithm
        lights = sorted(lights)
        count = defaultdict(int)
        
        # Create events: +1 at start, -1 at end+1
        for (pos, r) in lights:
            count[pos - r] += 1      # Light starts here
            count[pos + r + 1] -= 1  # Light ends here (exclusive)
        
        brightest = -1
        bestPlace = 0
        cur = 0
        
        # Sweep through sorted positions
        for pos in sorted(count):
            cur += count[pos]
            if cur > brightest: 
                brightest = cur
                bestPlace = pos
        return bestPlace

        # First method - NAIVE: Memory limit exceeded
        # This approach iterates through every position in the range
        # which can be very large (up to 10^8 positions)
        # lights = sorted(lights)
        # count = defaultdict(int)
        # min_val = float('inf') 
        # max_val = -float('inf')
        # for (pos, r) in lights:
        #     for i in range(pos - r, pos + r + 1):
        #         if i < min_val: min_val = i
        #         if i > max_val: max_val = i
        #         count[i] += 1
        # 
        # brightest = -1
        # bestPlace = 0
        # for pos in sorted(count):
        #     if count[pos] > brightest: 
        #         brightest = count[pos]
        #         bestPlace = pos
        # return bestPlace

def test():
    """
    Test function to verify solution with various test cases
    """
    solution = Solution()
    
    # Test case 1: Example from problem
    lights1 = [[-3,2],[1,2],[3,3]]
    result1 = solution.brightestPosition(lights1)
    assert result1 == -1, f"Test case 1 failed: expected -1, got {result1}"
    
    # Test case 2: Example from problem
    lights2 = [[1,0],[0,1]]
    result2 = solution.brightestPosition(lights2)
    assert result2 == 1, f"Test case 2 failed: expected 1, got {result2}"
    
    # Test case 3: Example from problem
    lights3 = [[1,2]]
    result3 = solution.brightestPosition(lights3)
    assert result3 == -1, f"Test case 3 failed: expected -1, got {result3}"
    
    # Test case 4: Single light
    lights4 = [[0,1]]
    result4 = solution.brightestPosition(lights4)
    assert result4 == -1, f"Test case 4 failed: expected -1, got {result4}"
    
    # Test case 5: Overlapping lights
    lights5 = [[0,2],[1,2],[2,2]]
    result5 = solution.brightestPosition(lights5)
    assert result5 == 1, f"Test case 5 failed: expected 1, got {result5}"
    
    print("All test cases passed!")

if __name__ == "__main__":
    test()

"""
What I Learned from This Problem:
================================

1. LINE SWEEP ALGORITHM:
   - Instead of checking every position individually, use events
   - Mark start (+1) and end (-1) of each interval
   - Sweep through sorted events to find maximum overlap
   - This reduces time complexity from O(n * range) to O(n log n)

2. PREFIX SUM CONCEPT:
   - The line sweep is essentially a prefix sum on events
   - Each event changes the current count by a delta
   - We track the running sum to find maximum

3. MEMORY OPTIMIZATION:
   - First approach: O(range) memory - can be huge (10^8)
   - Second approach: O(n) memory - only store events
   - This is crucial for large ranges

4. EVENT-BASED THINKING:
   - Instead of "what happens at each position"
   - Think "what events change the state"
   - This is a powerful pattern for interval problems

5. SORTING STRATEGY:
   - Sort events by position to process in order
   - This ensures we handle all changes at each position together

6. EDGE CASE HANDLING:
   - Multiple positions with same brightness → return smallest
   - Empty ranges (range = 0) → single position
   - Large ranges → need efficient algorithm

7. ALGORITHM PATTERNS:
   - Line sweep for interval overlap problems
   - Event-based processing for range updates
   - Prefix sum for cumulative counting

8. OPTIMIZATION THINKING:
   - When naive approach has memory issues
   - Look for ways to avoid storing every position
   - Use mathematical properties (events) instead

9. CODING TECHNIQUES:
   - Use defaultdict for sparse data
   - Sort events before processing
   - Track running state during sweep

10. PROBLEM RECOGNITION:
    - Interval overlap problems often use line sweep
    - Range update problems often use prefix sum
    - When ranges are large, avoid naive iteration

This problem taught me the power of event-based algorithms and how to
optimize space usage when dealing with large ranges!
"""

"""
Solution Analysis:
----------------
1. Approach:
   - Use line sweep algorithm with events
   - Mark start (+1) and end (-1) of each light's range
   - Sweep through sorted events to find maximum brightness

2. Algorithm:
   - For each light [pos, range], create two events:
     * +1 at position (pos - range)
     * -1 at position (pos + range + 1)
   - Sort all events by position
   - Sweep through events, maintaining running count
   - Track position with maximum count

3. Time Complexity: O(n log n)
   - Sorting n events: O(n log n)
   - Sweeping through events: O(n)
   - Overall: O(n log n)

4. Space Complexity: O(n)
   - Store 2 events per light: O(n)
   - Much better than O(range) in naive approach

5. Key Insights:
   - Line sweep avoids checking every position
   - Events capture all state changes
   - Sorting ensures correct order of processing

6. Why This Works:
   - Each light contributes +1 to all positions in its range
   - Events mark where this contribution starts and ends
   - Sweeping through events gives us the count at each position

7. Edge Cases:
   - Multiple positions with same brightness → return smallest
   - Empty ranges (range = 0) → single position
   - Large ranges → efficient with events

8. Alternative Approaches:
   - Naive: O(n * range) time and space
   - Segment tree: O(n log n) but more complex
   - Line sweep: O(n log n) and simple
"""
