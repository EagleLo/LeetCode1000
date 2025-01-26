# LeetCode 1152. Analyze User Website Visit Pattern
# Difficulty: Medium
# Topic: Hash Table, Array, Sorting
"""
Problem Description:
------------------
Given arrays username, website, and timestamp of same length where:
[username[i], website[i], timestamp[i]] indicates user visited website at time.
Find the most common 3-website pattern (sequence) across users.
- Pattern must be visited in order but not necessarily consecutively
- Count pattern only once per user even if they repeat it
- Return lexicographically smallest pattern if multiple have same count

1152. Analyze User Website Visit Pattern
Solved
Medium

Topics

Companies

Hint
You are given two string arrays username and website and an integer array timestamp. All the given arrays are of the same length and the tuple [username[i], website[i], timestamp[i]] indicates that the user username[i] visited the website website[i] at time timestamp[i].

A pattern is a list of three websites (not necessarily distinct).

For example, ["home", "away", "love"], ["leetcode", "love", "leetcode"], and ["luffy", "luffy", "luffy"] are all patterns.
The score of a pattern is the number of users that visited all the websites in the pattern in the same order they appeared in the pattern.

For example, if the pattern is ["home", "away", "love"], the score is the number of users x such that x visited "home" then visited "away" and visited "love" after that.
Similarly, if the pattern is ["leetcode", "love", "leetcode"], the score is the number of users x such that x visited "leetcode" then visited "love" and visited "leetcode" one more time after that.
Also, if the pattern is ["luffy", "luffy", "luffy"], the score is the number of users x such that x visited "luffy" three different times at different timestamps.
Return the pattern with the largest score. If there is more than one pattern with the same largest score, return the lexicographically smallest such pattern.

Note that the websites in a pattern do not need to be visited contiguously, they only need to be visited in the order they appeared in the pattern.

Example 1:

Input: username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"], timestamp = [1,2,3,4,5,6,7,8,9,10], website = ["home","about","career","home","cart","maps","home","home","about","career"]
Output: ["home","about","career"]
Explanation: The tuples in this example are:
["joe","home",1],["joe","about",2],["joe","career",3],["james","home",4],["james","cart",5],["james","maps",6],["james","home",7],["mary","home",8],["mary","about",9], and ["mary","career",10].
The pattern ("home", "about", "career") has score 2 (joe and mary).
The pattern ("home", "cart", "maps") has score 1 (james).
The pattern ("home", "cart", "home") has score 1 (james).
The pattern ("home", "maps", "home") has score 1 (james).
The pattern ("cart", "maps", "home") has score 1 (james).
The pattern ("home", "home", "home") has score 0 (no user visited home 3 times).

Example 2:

Input: username = ["ua","ua","ua","ub","ub","ub"], timestamp = [1,2,3,4,5,6], website = ["a","b","a","a","b","c"]
Output: ["a","b","a"]

Constraints:
* 3 <= username.length <= 50
* 1 <= username[i].length <= 10
* timestamp.length == username.length
* 1 <= timestamp[i] <= 10^9
* website.length == username.length 
* 1 <= website[i].length <= 10
* username[i] and website[i] consist of lowercase English letters
* At least one user visited at least three websites
* All tuples [username[i], timestamp[i], website[i]] are unique
"""

from collections import defaultdict

class Solution(object):
    def mostVisitedPattern(self, username, timestamp, website):
        """
        Approach:
        1. Sort visits by timestamp
        2. Group websites by user
        3. Find all 3-website patterns per user (only count once per user)
        4. Return most common pattern (lexicographically smallest if tie)
        
        :type username: List[str]
        :type timestamp: List[int]
        :type website: List[str]
        :rtype: List[str]
        """
        # Sort visits by timestamp
        visits = sorted((time, name, site) 
                       for (time, name, site) in zip(timestamp, username, website))
        
        # Group websites by user
        user_history = defaultdict(list)
        for (time, name, site) in visits:
            user_history[name].append(site)
            
        # Count patterns (only once per user)
        pattern_count = defaultdict(int)
        for user, sites in user_history.items():
            n = len(sites)
            # Generate all possible 3-website patterns for this user
            patterns = set((sites[i], sites[j], sites[k])
                         for i in range(n - 2)
                         for j in range(i + 1, n - 1)
                         for k in range(j + 1, n))
            # Count each pattern once per user
            for pattern in patterns:
                pattern_count[pattern] += 1
                
        # Find pattern with highest count
        result = []
        max_count = 0
        for pattern, count in pattern_count.items():
            if count > max_count:
                max_count = count
                result = list(pattern)
            elif count == max_count:
                # If tie, take lexicographically smaller
                if list(pattern) < result:
                    result = list(pattern)
                    
        return result

# Test cases
def test():
    solution = Solution()
    # Test case 1
    assert solution.mostVisitedPattern(
        ["joe","joe","joe","james","james","james","james","mary","mary","mary"],
        [1,2,3,4,5,6,7,8,9,10],
        ["home","about","career","home","cart","maps","home","home","about","career"]
    ) == ["home","about","career"]
    
    # Test case 2
    assert solution.mostVisitedPattern(
        ["ua","ua","ua","ub","ub","ub"],
        [1,2,3,4,5,6],
        ["a","b","a","a","b","c"]
    ) == ["a","b","a"]
    print("All test cases passed!")

if __name__ == "__main__":
    test()

"""
Solution Analysis:
----------------
Time Complexity: O(n log n + u * w^3) where:
- n: total number of visits (for sorting)
- u: number of users
- w: max websites per user
- w^3 for generating all 3-website patterns per user

Space Complexity: O(n)
- O(n) for user_history dictionary
- O(w^3) for patterns set per user
- O(p) for pattern_count where p is total unique patterns

Key Points:
1. Sort by timestamp to maintain visit order
2. Use set() to count patterns only once per user
3. Group by user first to handle pattern ordering
4. Handle ties by comparing lexicographically
"""