# LeetCode 362. Design Hit Counter
# Difficulty: Medium
# Topic: Object-Oriented Programming, Queue, Design

"""
Problem Description:
------------------
Design a hit counter which counts the number of hits received in the past 5 minutes 
(i.e., the past 300 seconds).

Your system should accept a timestamp parameter (in seconds granularity), and you may 
assume that calls are being made to the system in chronological order (i.e., timestamp 
is monotonically increasing). Several hits may arrive roughly at the same time.

Implement the HitCounter class:
- HitCounter(): Initializes the object of the hit counter system.
- void hit(int timestamp): Records a hit that happened at timestamp (in seconds). 
  Several hits may happen at the same timestamp.
- int getHits(int timestamp): Returns the number of hits in the past 5 minutes from 
  timestamp (i.e., the past 300 seconds).

Example 1:
Input:
["HitCounter", "hit", "hit", "hit", "getHits", "hit", "getHits", "getHits"]
[[], [1], [2], [3], [4], [300], [300], [301]]

Output: [null, null, null, null, 3, null, 4, 3]

Explanation:
HitCounter hitCounter = new HitCounter();
hitCounter.hit(1);       // hit at timestamp 1.
hitCounter.hit(2);       // hit at timestamp 2.
hitCounter.hit(3);       // hit at timestamp 3.
hitCounter.getHits(4);   // get hits at timestamp 4, return 3.
hitCounter.hit(300);     // hit at timestamp 300.
hitCounter.getHits(300); // get hits at timestamp 300, return 4.
hitCounter.getHits(301); // get hits at timestamp 301, return 3.

Constraints:
* 1 <= timestamp <= 2 * 10^9
* All the calls are being made to the system in chronological order (i.e., timestamp 
  is monotonically increasing).
* At most 300 calls will be made to hit and getHits.

Follow up: What if the number of hits per second could be huge? Does your design scale?
"""

from collections import deque

class HitCounter(object):
    def __init__(self):
        """
        Initialize the hit counter system.
        
        Data Structure Choice:
        - Use deque (double-ended queue) for efficient operations
        - Deque functions: append(x), appendleft(x), pop(), popleft()
        - Use len(deque) to check the length
        - Use d[0] or d[-1] to peek at first/last elements
        """
        self.mem = deque()

    def hit(self, timestamp):
        """
        Record a hit that happened at the given timestamp.
        
        Args:
            timestamp (int): The timestamp when the hit occurred
        """
        self.mem.append(timestamp)
        
    def getHits(self, timestamp):
        """
        Get the number of hits in the past 5 minutes (300 seconds) from the given timestamp.
        
        Algorithm:
        1. Remove all hits that are older than 300 seconds
        2. Return the count of remaining hits
        
        Args:
            timestamp (int): The current timestamp
            
        Returns:
            int: Number of hits in the past 5 minutes
        """
        # Remove all hits older than 300 seconds
        while self.mem and self.mem[0] <= timestamp - 300:
            self.mem.popleft()
        
        # Return count of remaining hits
        return len(self.mem)

def test():
    """
    Test function to verify solution with various test cases
    """
    # Test case 1: Example from problem
    hitCounter = HitCounter()
    
    hitCounter.hit(1)
    hitCounter.hit(2)
    hitCounter.hit(3)
    result1 = hitCounter.getHits(4)
    assert result1 == 3, f"Test case 1 failed: expected 3, got {result1}"
    
    hitCounter.hit(300)
    result2 = hitCounter.getHits(300)
    assert result2 == 4, f"Test case 2 failed: expected 4, got {result2}"
    
    result3 = hitCounter.getHits(301)
    assert result3 == 3, f"Test case 3 failed: expected 3, got {result3}"
    
    # Test case 4: Edge case - exactly 300 seconds ago
    hitCounter2 = HitCounter()
    hitCounter2.hit(1)
    result4 = hitCounter2.getHits(301)  # 301 - 300 = 1, so hit at 1 should be removed
    assert result4 == 0, f"Test case 4 failed: expected 0, got {result4}"
    
    # Test case 5: Multiple hits at same timestamp
    hitCounter3 = HitCounter()
    hitCounter3.hit(100)
    hitCounter3.hit(100)
    hitCounter3.hit(100)
    result5 = hitCounter3.getHits(200)
    assert result5 == 3, f"Test case 5 failed: expected 3, got {result5}"
    
    # Test case 6: No hits
    hitCounter4 = HitCounter()
    result6 = hitCounter4.getHits(100)
    assert result6 == 0, f"Test case 6 failed: expected 0, got {result6}"
    
    print("All test cases passed!")

if __name__ == "__main__":
    test()

"""
What I Learned from This Problem:
================================

1. DEQUE DATA STRUCTURE:
   - Use deque (double-ended queue) for efficient operations
   - append(x): add to right end
   - popleft(): remove from left end
   - O(1) operations for both ends
   - Perfect for sliding window problems

2. SLIDING WINDOW CONCEPT:
   - Maintain a window of the last 300 seconds
   - Remove old elements that fall outside the window
   - Keep only relevant data in memory

3. CHRONOLOGICAL ORDER ASSUMPTION:
   - Timestamps are monotonically increasing
   - This allows us to remove elements from the left
   - No need to search through the entire data structure

4. EFFICIENT CLEANUP:
   - Remove old hits during getHits() call
   - This keeps memory usage bounded
   - O(k) time where k is number of old hits to remove

5. EDGE CASE HANDLING:
   - Exactly 300 seconds ago: should be removed
   - Multiple hits at same timestamp: all should be counted
   - No hits: return 0

6. MEMORY MANAGEMENT:
   - Old hits are automatically removed
   - Memory usage is bounded by 300 seconds of data
   - Scales well for long-running systems

7. ALGORITHM EFFICIENCY:
   - hit(): O(1) - append to deque
   - getHits(): O(k) - remove k old hits
   - Space: O(n) where n is hits in last 300 seconds

8. FOLLOW-UP CONSIDERATIONS:
   - What if hits per second could be huge?
   - Current design: O(k) cleanup time
   - Could optimize with circular buffer or other techniques

This problem taught me about sliding window algorithms and how to design
efficient time-based data structures with automatic cleanup!
"""

"""
Solution Analysis:
----------------
1. Approach:
   - Use deque to store timestamps of hits
   - Remove old hits (older than 300 seconds) during getHits()
   - Return count of remaining hits

2. Data Structure:
   - deque: efficient append and popleft operations
   - Stores timestamps in chronological order
   - Automatically maintains sliding window

3. Time Complexity:
   - hit(): O(1) - append to deque
   - getHits(): O(k) - remove k old hits
   - k is number of hits older than 300 seconds

4. Space Complexity: O(n)
   - Store timestamps for hits in last 300 seconds
   - n is number of hits in the window

5. Key Insights:
   - Chronological order enables efficient cleanup
   - Sliding window keeps memory bounded
   - Deque provides O(1) operations on both ends

6. Edge Cases:
   - Exactly 300 seconds ago: removed
   - Multiple hits at same timestamp: all counted
   - No hits: return 0

7. Follow-up Considerations:
   - For huge hits per second: O(k) cleanup might be slow
   - Could use circular buffer or other optimizations
   - Current design is simple and efficient for given constraints

8. Why This Works:
   - Timestamps are monotonically increasing
   - Old hits can be removed from left end
   - Remaining hits are all within 300 seconds
   - Count is simply length of deque
"""
