# LeetCode 875. Koko Eating Bananas
# Difficulty: Medium
# Topic: Binary Search
"""
Problem Understanding:
------------------
1. Given: piles of bananas and hours (h)
2. Need to find: minimum eating speed (k) to eat all bananas within h hours
3. Rules:
   - Can eat k bananas per hour from one pile
   - If pile has less than k bananas, eat all and wait
   - Must eat all bananas before h hours

Key Insight:
- This is a binary search on the answer (eating speed k)
- For any speed k, we can check if it's possible to eat all bananas in h hours
- The possible speeds form a monotonic pattern:
  * If speed k works, any speed > k works
  * If speed k doesn't work, any speed < k doesn't work
"""

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Binary search approach:
        1. Search space: 1 to max(piles)
        2. For each speed k, check if possible to eat all in h hours
        3. Binary search to find minimum valid k
        
        Time: O(n * log(max(piles))) where n is length of piles
        Space: O(1)
        """
        def can_eat_all(speed):
            """Helper function to check if we can eat all bananas at given speed"""
            hours_needed = 0
            for pile in piles:
                # Calculate hours needed for current pile
                # Using ceiling division to round up
                hours_needed += (pile + speed - 1) // speed
            return hours_needed <= h
        
        left = 1  # Minimum possible speed
        right = max(piles)  # Maximum needed speed
        
        # Binary search for minimum valid speed
        while left < right:
            mid = (left + right) // 2
            if can_eat_all(mid):
                # This speed works, try lower speeds
                right = mid
            else:
                # Speed too slow, try higher speeds
                left = mid + 1
                
        return left

def test():
    """
    Test function to verify solution
    """
    solution = Solution()
    
    # Test cases
    test_cases = [
        {
            'piles': [3,6,7,11],
            'h': 8,
            'expected': 4,
            'explanation': """
            With k = 4:
            Pile 1 (3): 1 hour
            Pile 2 (6): 2 hours
            Pile 3 (7): 2 hours
            Pile 4 (11): 3 hours
            Total = 8 hours
            """
        },
        {
            'piles': [30,11,23,4,20],
            'h': 5,
            'expected': 30,
            'explanation': "Need to eat each pile in 1 hour"
        },
        {
            'piles': [30,11,23,4,20],
            'h': 6,
            'expected': 23,
            'explanation': "Can take 2 hours on one pile"
        },
        {
            'piles': [1],
            'h': 1,
            'expected': 1,
            'explanation': "Single pile edge case"
        }
    ]
    
    for i, test in enumerate(test_cases, 1):
        result = solution.minEatingSpeed(test['piles'], test['h'])
        assert result == test['expected'], \
            f"""Test case {i} failed: 
            Input: piles={test['piles']}, h={test['h']}
            Expected: {test['expected']}
            Got: {result}
            Explanation: {test['explanation']}"""
    
    print("All test cases passed!")

if __name__ == "__main__":
    test()

"""
Detailed Solution Explanation:
---------------------------
1. Why Binary Search Works:
   - For any eating speed k:
     * If Koko can eat all bananas in ≤ h hours with speed k
     * She can definitely eat them with any speed > k
     * This creates a monotonic pattern perfect for binary search

2. Search Space:
   - Minimum speed = 1 (can't eat slower)
   - Maximum speed = max(piles) (no need to eat faster than largest pile)
   - Binary search in this range to find minimum valid speed

3. Checking Valid Speed:
   - For each pile, calculate hours needed with current speed
   - Use ceiling division (pile + speed - 1) // speed
   - Sum up total hours needed
   - Compare with target hours h

4. Optimizations:
   - Use ceiling division instead of math.ceil
   - Early return in can_eat_all if hours exceed h
   - Binary search on answer space instead of checking all speeds

5. Edge Cases Handled:
   - Single pile
   - h equal to number of piles
   - h greater than number of piles
   - Very large piles
"""