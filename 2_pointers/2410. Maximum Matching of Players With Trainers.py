# LeetCode 2410. Maximum Matching of Players With Trainers
# Difficulty: Medium
# Topic: Two Pointers, Greedy, Sorting

"""
Problem Description:
------------------
You are given a 0-indexed integer array players, where players[i] represents the ability 
of the ith player. You are also given a 0-indexed integer array trainers, where 
trainers[j] represents the training capacity of the jth trainer.

The ith player can match with the jth trainer if the player's ability is less than or 
equal to the trainer's training capacity. Additionally, the ith player can be matched 
with at most one trainer, and the jth trainer can be matched with at most one player.

Return the maximum number of matchings between players and trainers that satisfy these conditions.

Example 1:
Input: players = [4,7,9], trainers = [8,2,5,8]
Output: 2
Explanation:
One of the ways we can form two matchings is as follows:
- players[0] can be matched with trainers[0] since 4 <= 8.
- players[1] can be matched with trainers[3] since 7 <= 8.
It can be proven that 2 is the maximum number of matchings that can be formed.

Example 2:
Input: players = [1,1,1], trainers = [10]
Output: 1
Explanation:
The trainer can be matched with any of the 3 players.
Each player can only be matched with one trainer, so the maximum answer is 1.

Constraints:
* 1 <= players.length, trainers.length <= 10^5
* 1 <= players[i], trainers[j] <= 10^9

Note: This question is the same as 445: Assign Cookies.
"""

class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        """
        Approach: Two Pointers with Greedy Strategy
        - Sort both arrays in ascending order
        - Use two pointers to find optimal matches
        - Match each player with the smallest suitable trainer
        
        Time: O(n log n + m log m) - sorting both arrays
        Space: O(1) - only using constant extra space
        """
        players = sorted(players)
        trainers = sorted(trainers)
        match = 0
        i = j = 0

        while i < len(players) and j < len(trainers):
            if players[i] <= trainers[j]:
                match += 1
                i += 1
                j += 1
            else: 
                j += 1
        return match

def test():
    """
    Test function to verify solution with various test cases
    """
    solution = Solution()
    
    # Test case 1: Example from problem
    players1 = [4, 7, 9]
    trainers1 = [8, 2, 5, 8]
    result1 = solution.matchPlayersAndTrainers(players1, trainers1)
    assert result1 == 2, f"Test case 1 failed: expected 2, got {result1}"
    
    # Test case 2: Example from problem
    players2 = [1, 1, 1]
    trainers2 = [10]
    result2 = solution.matchPlayersAndTrainers(players2, trainers2)
    assert result2 == 1, f"Test case 2 failed: expected 1, got {result2}"
    
    # Test case 3: All players can be matched
    players3 = [1, 2, 3]
    trainers3 = [3, 4, 5]
    result3 = solution.matchPlayersAndTrainers(players3, trainers3)
    assert result3 == 3, f"Test case 3 failed: expected 3, got {result3}"
    
    # Test case 4: No matches possible
    players4 = [5, 6, 7]
    trainers4 = [1, 2, 3]
    result4 = solution.matchPlayersAndTrainers(players4, trainers4)
    assert result4 == 0, f"Test case 4 failed: expected 0, got {result4}"
    
    # Test case 5: Single player and trainer
    players5 = [3]
    trainers5 = [5]
    result5 = solution.matchPlayersAndTrainers(players5, trainers5)
    assert result5 == 1, f"Test case 5 failed: expected 1, got {result5}"
    
    # Test case 6: More trainers than players
    players6 = [2, 3]
    trainers6 = [1, 2, 3, 4, 5]
    result6 = solution.matchPlayersAndTrainers(players6, trainers6)
    assert result6 == 2, f"Test case 6 failed: expected 2, got {result6}"
    
    print("All test cases passed!")

if __name__ == "__main__":
    test()

"""
Solution Analysis:
----------------
1. Approach:
   - Sort both arrays in ascending order
   - Use two pointers to find optimal matches
   - Greedy strategy: match each player with smallest suitable trainer

2. Algorithm:
   - Sort players and trainers arrays
   - Initialize two pointers i (players) and j (trainers)
   - If player[i] <= trainer[j], match them and move both pointers
   - If player[i] > trainer[j], move trainer pointer to find better match
   - Continue until one array is exhausted

3. Time Complexity: O(n log n + m log m)
   - Sorting players: O(n log n)
   - Sorting trainers: O(m log m)
   - Two pointer traversal: O(min(n, m))
   - Overall: O(n log n + m log m)

4. Space Complexity: O(1)
   - Only using constant extra space for variables
   - Sorting is done in-place (Python's sort modifies original array)

5. Key Insights:
   - Greedy approach works because we want maximum matches
   - Sorting ensures we always match with smallest suitable trainer
   - This maximizes remaining trainers for future players

6. Edge Cases Handled:
   - No matches possible
   - All players can be matched
   - More players than trainers
   - More trainers than players
   - Single player/trainer
   - Empty arrays

7. Why Greedy Works:
   - If we match a player with a larger trainer than necessary,
     we might miss a match for a later player
   - Always choosing smallest suitable trainer maximizes future opportunities
   - This is optimal because we want maximum total matches

8. Similar Problems:
   - 445: Assign Cookies (same problem, different context)
   - 881: Boats to Save People
   - 1353: Maximum Number of Events That Can Be Attended
"""
