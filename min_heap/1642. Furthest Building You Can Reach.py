# LeetCode 1642. Furthest Building You Can Reach
# Difficulty: Medium
# Topic: Array, Greedy, Heap (Priority Queue)
"""
Problem Description:
------------------
Given an integer array 'heights' representing building heights, some 'bricks', 
and some 'ladders', find the furthest building you can reach.

Rules for moving from building i to i+1:
* If current height >= next height: no resources needed
* If current height < next height: need either
  - One ladder OR
  - (heights[i+1] - heights[i]) bricks

Return the furthest building index (0-indexed) reachable with given resources.

Example:
Input: heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1
Output: 4
Explanation: Can reach building 4 using 5 bricks at building 2 and ladder at building 4

Constraints:
* 1 <= heights.length <= 10^5
* 1 <= heights[i] <= 10^6
* 0 <= bricks <= 10^9
* 0 <= ladders <= heights.length
"""
import heapq

class Solution(object):
    def furthestBuilding(self, heights, bricks, ladders):
        """
        Approach: Greedy with Min-Heap
        - Use ladders for largest climbs
        - Use bricks for smaller climbs
        - Min-heap tracks climbs where ladders are used
        
        Time: O(nlogk) where n is buildings and k is ladders
        Space: O(k) for the heap
        
        :type heights: List[int]
        :type bricks: int
        :type ladders: int
        :rtype: int
        """
        ladder_allocations = []  # Min-heap to track climbs using ladders
        
        for i in range(len(heights) - 1):
            climb = heights[i + 1] - heights[i]
            
            # Skip if moving down or staying level
            if climb <= 0:
                continue
                
            # Add current climb to ladder allocations
            heapq.heappush(ladder_allocations, climb)
            
            # If we haven't used all ladders, continue
            if len(ladder_allocations) <= ladders:
                continue
                
            # Otherwise, use bricks for smallest climb
            bricks_needed = heapq.heappop(ladder_allocations)
            bricks -= bricks_needed
            
            # If we run out of bricks, can't proceed further
            if bricks < 0:
                return i
        
        # If we get here, we can reach the last building
        return len(heights) - 1

def test():
    """
    Test function to verify solution
    """
    solution = Solution()
    
    # Test cases
    test_cases = [
        {
            'heights': [4,2,7,6,9,14,12],
            'bricks': 5,
            'ladders': 1,
            'expected': 4
        },
        {
            'heights': [4,12,2,7,3,18,20,3,19],
            'bricks': 10,
            'ladders': 2,
            'expected': 7
        },
        {
            'heights': [14,3,19,3],
            'bricks': 17,
            'ladders': 0,
            'expected': 3
        }
    ]
    
    for i, test in enumerate(test_cases, 1):
        result = solution.furthestBuilding(
            test['heights'], 
            test['bricks'], 
            test['ladders']
        )
        assert result == test['expected'], \
            f"Test case {i} failed: got {result}, expected {test['expected']}"
    
    print("All test cases passed!")

if __name__ == "__main__":
    test()

"""
Solution Analysis:
----------------
Time Complexity: O(nlogk)
- n iterations through buildings
- logk for heap operations where k is number of ladders

Space Complexity: O(k)
- Heap stores at most k elements (ladder allocations)

Key Points:
1. Greedy Approach:
   - Use ladders for largest climbs
   - Use bricks for smaller climbs
   - Min-heap helps track smallest ladder allocation

2. Algorithm Steps:
   - Process buildings left to right
   - For each climb up:
     * Add to ladder allocations heap
     * If exceeded ladders, convert smallest ladder to bricks
     * If run out of bricks, return current position

3. Optimizations:
   - Skip non-positive climbs early
   - Use min-heap for efficient tracking of smallest climb
   - Early return when resources exhausted

4. Edge Cases Handled:
   - Moving down between buildings
   - No ladders available
   - Sufficient resources for all climbs
"""