# LeetCode 322. Coin Change
# Difficulty: Medium
# Topic: BFS, Dynamic Programming
"""
Problem Description:
------------------
Given coins of different denominations and amount,
return fewest coins needed to make up amount.
Return -1 if amount cannot be made up.

Example:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Constraints:
* 1 <= coins.length <= 12
* 1 <= coins[i] <= 2^31 - 1
* 0 <= amount <= 10^4
"""

from collections import deque

class Solution(object):
    def coinChange(self, coins, amount):
        """
        Approach: BFS to find shortest path to target amount
        Each level represents number of coins used
        
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
            
        # Track seen amounts and their steps
        seen = {}
        queue = deque([(0, 0)])  # (current_amount, steps)
        
        while queue:
            curr_amount, steps = queue.popleft()
            
            for coin in coins:
                next_amount = curr_amount + coin
                
                # Found solution
                if next_amount == amount:
                    return steps + 1
                    
                # Valid amount and either unseen or better path
                if next_amount < amount and (
                    next_amount not in seen or 
                    steps + 1 < seen[next_amount]
                ):
                    seen[next_amount] = steps + 1
                    queue.append((next_amount, steps + 1))
                    
        return -1

def test():
    solution = Solution()
    assert solution.coinChange([1,2,5], 11) == 3
    assert solution.coinChange([2], 3) == -1
    assert solution.coinChange([1], 0) == 0
    print("All test cases passed!")

if __name__ == "__main__":
    test()

"""
Solution Analysis:
----------------
Time Complexity: O(amount * len(coins)) (since we have memorization)
Space Complexity: O(amount)

Key Points:
1. Start from 0 and build up amounts
2. Use BFS to ensure minimum number of coins
3. Track seen amounts to avoid cycles
4. Early return when solution found
5. Single dictionary for tracking visited states

Improvements over original:
1. Cleaner state tracking
2. More intuitive starting from 0
3. Better variable names
4. Simpler logic structure
5. Reduced redundant checks
"""