# LeetCode 2214. Minimum Health to Beat Game
# Difficulty: Medium
# Topic: Array, Greedy
"""
Problem Description:
------------------
You are playing a game with n levels (0 to n-1). Each level i causes damage[i] health loss.
You have one armor ability that can be used once to block up to 'armor' amount of damage
on any single level.

Return the minimum initial health needed to complete the game while keeping health > 0.

Example:
Input: damage = [2,7,4,3], armor = 4
Output: 13
Explanation: Use armor on level 2 to reduce 7 damage to 3 damage.
Total damage taken: 2 + 3 + 4 + 3 = 12
Need 13 health to have 1 health remaining.

Constraints:
* n == damage.length
* 1 <= n <= 10^5
* 0 <= damage[i] <= 10^5
* 0 <= armor <= 10^5
"""

class Solution:
    def minimumHealth(self, damage, armor):
        """
        Approach: Greedy
        - Find the maximum damage level to apply armor
        - Calculate total damage needed after armor application
        
        Time: O(n) where n is number of levels
        Space: O(1)
        
        :type damage: List[int]
        :type armor: int
        :rtype: int
        """
        # Find total damage and maximum single damage
        total_damage = sum(damage)
        max_damage = max(damage)
        
        # Calculate armor benefit (minimum of armor and max damage)
        armor_benefit = min(armor, max_damage)
        
        # Need enough health to survive total damage minus armor benefit
        # Plus 1 to keep health > 0
        return total_damage - armor_benefit + 1

def test():
    """
    Test function to verify solution
    """
    solution = Solution()
    
    # Test cases
    test_cases = [
        {
            'damage': [2,7,4,3],
            'armor': 4,
            'expected': 13,
            'explanation': "Use armor on 7 damage level"
        },
        {
            'damage': [2,5,3,4],
            'armor': 7,
            'expected': 10,
            'explanation': "Use armor on 5 damage level"
        },
        {
            'damage': [3,3,3],
            'armor': 0,
            'expected': 10,
            'explanation': "No armor available"
        },
        {
            'damage': [10],
            'armor': 5,
            'expected': 6,
            'explanation': "Single level with armor"
        },
        {
            'damage': [1,1,1,1],
            'armor': 100,
            'expected': 4,
            'explanation': "Armor greater than any damage"
        }
    ]
    
    for i, test in enumerate(test_cases, 1):
        result = solution.minimumHealth(test['damage'], test['armor'])
        assert result == test['expected'], \
            f"""Test case {i} failed: 
            Input: damage={test['damage']}, armor={test['armor']}
            Expected: {test['expected']} ({test['explanation']})
            Got: {result}"""
    
    print("All test cases passed!")

if __name__ == "__main__":
    test()

"""
Solution Analysis:
----------------
Time Complexity: O(n)
- One pass to calculate sum and find maximum
- All other operations are O(1)

Space Complexity: O(1)
- Only using constant extra space
- No additional data structures needed

Key Points:
1. Greedy Strategy:
   - Best use of armor is on maximum damage level
   - Only need to track total damage and maximum damage
   - No need to track position of maximum damage

2. Optimization Insights:
   - Don't need to simulate the game
   - Can calculate minimum health directly
   - Armor benefit is min(armor, max_damage)

3. Important Details:
   - Need +1 health at the end
   - Armor can only be used once
   - Health must stay > 0 at all times

4. Edge Cases Handled:
   - Armor = 0
   - Single level
   - Armor greater than any damage
   - All damage values equal
   - Armor greater than maximum damage
"""