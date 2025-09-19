# LeetCode 981. Time Based Key Value Store
# Difficulty: Medium
# Topic: Object-Oriented Programming, Binary Search, Hash Table

"""
Problem Description:
------------------
Design a time-based key-value data structure that can store multiple values for the same 
key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:
- TimeMap(): Initializes the object of the data structure.
- void set(String key, String value, int timestamp): Stores the key key with the value 
  value at the given time timestamp.
- String get(String key, int timestamp): Returns a value such that set was called 
  previously, with timestamp_prev <= timestamp. If there are multiple such values, it 
  returns the value associated with the largest timestamp_prev. If there are no values, 
  it returns "".

Example 1:
Input:
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]

Output: [null, null, "bar", "bar", null, "bar2", "bar2"]

Explanation:
TimeMap timeMap = new TimeMap();
timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
timeMap.get("foo", 1);         // return "bar"
timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
timeMap.get("foo", 4);         // return "bar2"
timeMap.get("foo", 5);         // return "bar2"

Constraints:
* 1 <= key.length, value.length <= 100
* key and value consist of lowercase English letters and digits.
* 1 <= timestamp <= 10^7
* All the timestamps timestamp of set are strictly increasing.
* At most 2 * 10^5 calls will be made to set and get.
"""

from collections import defaultdict

class TimeMap(object):
    def __init__(self):
        """
        Initialize the TimeMap data structure.
        
        Key Design Decisions:
        1. Need to assume dict.keys() doesn't keep the order of insertion
        2. If you need the values saved to be sorted:
           - 1st: use list append (maintains insertion order)
           - 2nd: Use Binary Search to minimize search time
        3. When using Binary Search like this, at the end if mid is not found:
           - The right will be the largest smaller than target
           - And left will be the smallest larger than target
        """
        # key: str -> list of (value, timestamp)
        # Using list to maintain insertion order (timestamps are strictly increasing)
        self.store = defaultdict(list) 

    def set(self, key, value, timestamp):
        """
        Store the key with value at the given timestamp.
        
        Args:
            key (str): The key to store
            value (str): The value to store
            timestamp (int): The timestamp (strictly increasing)
        """
        self.store[key].append((value, timestamp))

    def get(self, key, timestamp):
        """
        Get the value for key at or before the given timestamp.
        
        Args:
            key (str): The key to look up
            timestamp (int): The timestamp to search for
            
        Returns:
            str: The value at the largest timestamp <= given timestamp, or "" if not found
        """
        if key not in self.store: 
            return ""

        # Use binary search to find the targeted item
        entries = self.store[key]
        return self.search(entries, timestamp)
    
    def search(self, entries, timestamp):
        """
        Binary search to find the largest timestamp <= target timestamp.
        
        Key Binary Search Concepts:
        1. lo <= hi: This is the correct condition for binary search
        2. mid = (lo + hi) // 2: Calculate middle index
        3. hi = mid - 1: When target is smaller, search left half
        4. lo = mid + 1: When target is larger or equal, search right half
        
        At the end of binary search:
        - If target found: mid points to the target
        - If target not found: 
          * right (hi) will be the largest smaller than target
          * left (lo) will be the smallest larger than target
        
        Args:
            entries (List[Tuple]): List of (value, timestamp) pairs
            timestamp (int): Target timestamp
            
        Returns:
            str: The value at the largest timestamp <= target timestamp
        """
        lo = 0
        hi = len(entries) - 1
        res = ""
        
        while lo <= hi:  # Key: lo <= hi (not lo < hi)
            mid = (lo + hi) // 2  # Key: mid = (lo + hi) // 2
            v, t = entries[mid]
            
            if t > timestamp:
                # Current timestamp is too large, search left half
                hi = mid - 1  # Key: hi = mid - 1
            elif t <= timestamp:
                # Current timestamp is valid, but keep searching for larger valid timestamp
                res = v  # Update result with current valid value
                lo = mid + 1  # Key: lo = mid + 1
        
        return res

def test():
    """
    Test function to verify solution with various test cases
    """
    timeMap = TimeMap()
    
    # Test case 1: Example from problem
    timeMap.set("foo", "bar", 1)
    result1 = timeMap.get("foo", 1)
    assert result1 == "bar", f"Test case 1 failed: expected 'bar', got '{result1}'"
    
    result2 = timeMap.get("foo", 3)
    assert result2 == "bar", f"Test case 2 failed: expected 'bar', got '{result2}'"
    
    timeMap.set("foo", "bar2", 4)
    result3 = timeMap.get("foo", 4)
    assert result3 == "bar2", f"Test case 3 failed: expected 'bar2', got '{result3}'"
    
    result4 = timeMap.get("foo", 5)
    assert result4 == "bar2", f"Test case 4 failed: expected 'bar2', got '{result4}'"
    
    # Test case 5: Non-existent key
    result5 = timeMap.get("nonexistent", 1)
    assert result5 == "", f"Test case 5 failed: expected '', got '{result5}'"
    
    # Test case 6: Timestamp before any set
    result6 = timeMap.get("foo", 0)
    assert result6 == "", f"Test case 6 failed: expected '', got '{result6}'"
    
    # Test case 7: Multiple values for same key
    timeMap.set("test", "value1", 10)
    timeMap.set("test", "value2", 20)
    timeMap.set("test", "value3", 30)
    
    result7 = timeMap.get("test", 15)
    assert result7 == "value1", f"Test case 7 failed: expected 'value1', got '{result7}'"
    
    result8 = timeMap.get("test", 25)
    assert result8 == "value2", f"Test case 8 failed: expected 'value2', got '{result8}'"
    
    result9 = timeMap.get("test", 35)
    assert result9 == "value3", f"Test case 9 failed: expected 'value3', got '{result9}'"
    
    print("All test cases passed!")

if __name__ == "__main__":
    test()

"""
What I Learned from This Problem:
================================

1. BINARY SEARCH FUNDAMENTALS:
   - lo <= hi: This is the correct condition for binary search
   - mid = (lo + hi) // 2: Calculate middle index
   - hi = mid - 1: When target is smaller, search left half
   - lo = mid + 1: When target is larger or equal, search right half

2. BINARY SEARCH FOR "LARGEST <= TARGET":
   - When searching for largest element <= target
   - Update result when we find a valid element (t <= timestamp)
   - Continue searching right to find potentially larger valid element
   - At end: result contains the largest valid element

3. DATA STRUCTURE DESIGN:
   - Use defaultdict(list) to store multiple values per key
   - List maintains insertion order (timestamps are strictly increasing)
   - Each entry is (value, timestamp) tuple

4. TIMESTAMP ORDERING:
   - Problem states timestamps are strictly increasing
   - This means we can use binary search efficiently
   - No need to sort the list

5. EDGE CASE HANDLING:
   - Non-existent key: return ""
   - Timestamp before any set: return ""
   - Empty list: handled by binary search logic

6. BINARY SEARCH TERMINATION:
   - When lo > hi, search terminates
   - At this point, we have the largest valid element
   - Result is updated during the search process

7. ALGORITHM EFFICIENCY:
   - set: O(1) - append to list
   - get: O(log n) - binary search
   - Space: O(n) - store all values

8. WHY THIS APPROACH WORKS:
   - Timestamps are strictly increasing (no sorting needed)
   - Binary search finds largest timestamp <= target
   - List append maintains order efficiently
   - Modular design with separate search function

This problem taught me advanced binary search techniques and how to design
efficient time-based data structures!
"""

"""
Solution Analysis:
----------------
1. Approach:
   - Use defaultdict(list) to store multiple values per key
   - Each entry is (value, timestamp) tuple
   - Use binary search to find largest timestamp <= target

2. Data Structure:
   - store: key -> list of (value, timestamp)
   - List maintains insertion order
   - Timestamps are strictly increasing

3. Time Complexity:
   - set: O(1) - append to list
   - get: O(log n) - binary search
   - n is number of entries for the key

4. Space Complexity: O(n)
   - Store all (value, timestamp) pairs
   - n is total number of set operations

5. Key Binary Search Details:
   - lo <= hi: correct termination condition
   - mid = (lo + hi) // 2: middle calculation
   - hi = mid - 1: search left half
   - lo = mid + 1: search right half

6. Search Strategy:
   - When t > timestamp: search left (hi = mid - 1)
   - When t <= timestamp: update result, search right (lo = mid + 1)
   - Result contains largest valid timestamp

7. Edge Cases:
   - Non-existent key: return ""
   - Timestamp before any set: return ""
   - Empty list: handled by binary search

8. Why This Works:
   - Strictly increasing timestamps enable binary search
   - Binary search finds largest element <= target
   - List append maintains order efficiently
   - Modular design improves readability
"""
