# LeetCode 2502. Design Memory Allocator
# Difficulty: Medium
# Topic: Object-Oriented Programming, Simulation, Array

"""
Problem Description:
------------------
You are given an integer n representing the size of a 0-indexed memory array. 
All memory units are initially free.

You have a memory allocator with the following functionalities:
1. Allocate a block of size consecutive free memory units and assign it the id mID.
2. Free all memory units with the given id mID.

Note that:
- Multiple blocks can be allocated to the same mID.
- You should free all the memory units with mID, even if they were allocated in different blocks.

Implement the Allocator class:
- Allocator(int n): Initializes an Allocator object with a memory array of size n.
- int allocate(int size, int mID): Find the leftmost block of size consecutive free memory 
  units and allocate it with the id mID. Return the block's first index. If such a block 
  does not exist, return -1.
- int freeMemory(int mID): Free all memory units with the id mID. Return the number of 
  memory units you have freed.

Example 1:
Input:
["Allocator", "allocate", "allocate", "allocate", "freeMemory", "allocate", "allocate", "allocate", "freeMemory", "allocate", "freeMemory"]
[[10], [1, 1], [1, 2], [1, 3], [2], [3, 4], [1, 1], [1, 1], [1], [10, 2], [7]]

Output: [null, 0, 1, 2, 1, 3, 1, 6, 3, -1, 0]

Explanation:
Allocator loc = new Allocator(10); // Initialize a memory array of size 10. All memory units are initially free.
loc.allocate(1, 1); // The leftmost block's first index is 0. The memory array becomes [1,_,_,_,_,_,_,_,_,_]. We return 0.
loc.allocate(1, 2); // The leftmost block's first index is 1. The memory array becomes [1,2,_,_,_,_,_,_,_,_]. We return 1.
loc.allocate(1, 3); // The leftmost block's first index is 2. The memory array becomes [1,2,3,_,_,_,_,_,_,_]. We return 2.
loc.freeMemory(2); // Free all memory units with mID 2. The memory array becomes [1,_, 3,_,_,_,_,_,_,_]. We return 1 since there is only 1 unit with mID 2.
loc.allocate(3, 4); // The leftmost block's first index is 3. The memory array becomes [1,_,3,4,4,4,_,_,_,_]. We return 3.
loc.allocate(1, 1); // The leftmost block's first index is 1. The memory array becomes [1,1,3,4,4,4,_,_,_,_]. We return 1.
loc.allocate(1, 1); // The leftmost block's first index is 6. The memory array becomes [1,1,3,4,4,4,1,_,_,_]. We return 6.
loc.freeMemory(1); // Free all memory units with mID 1. The memory array becomes [_,_,3,4,4,4,_,_,_,_]. We return 3 since there are 3 units with mID 1.
loc.allocate(10, 2); // We can not find any free block with 10 consecutive free memory units, so we return -1.
loc.freeMemory(7); // Free all memory units with mID 7. The memory array remains the same since there is no memory unit with mID 7. We return 0.

Constraints:
* 1 <= n, size, mID <= 1000
* At most 1000 calls will be made to allocate and freeMemory.
"""

class Allocator(object):
    def __init__(self, n):
        """
        Initialize the memory allocator with size n.
        
        Args:
            n (int): Size of the memory array
        """
        self.mem = [0] * n          # Memory array: 0 = free, mID = allocated
        self.memSize = n            # Total memory size
        self.IDs = set()            # Set of allocated IDs for quick lookup

    def allocate(self, size, mID):
        """
        Allocate a block of size consecutive free memory units.
        
        Args:
            size (int): Number of consecutive memory units needed
            mID (int): ID to assign to the allocated block
            
        Returns:
            int: Starting index of allocated block, or -1 if not possible
        """
        i = 0
        init = -1
        
        # Find leftmost block of size consecutive free units
        while (i + size - 1) < self.memSize:
            if self.mem[i] == 0:  # Found potential starting position
                init = i
                # Check if all positions in range are free
                for offset in range(size):
                    if self.mem[i + offset] != 0:
                        init = -1
                        i = i + offset + 1  # Skip to after occupied position
                        break
                
                if init != -1:  # Found valid block
                    # Allocate the block
                    for j in range(init, init + size):
                        self.mem[j] = mID
                    self.IDs.add(mID)
                    return init
            else:
                i += 1
        
        return -1  # No suitable block found
        
    def freeMemory(self, mID):
        """
        Free all memory units with the given mID.
        
        Args:
            mID (int): ID of memory units to free
            
        Returns:
            int: Number of memory units freed
        """
        if mID not in self.IDs:
            return 0

        count = 0
        # Find and free all memory units with this mID
        for i in range(self.memSize):
            if self.mem[i] == mID:
                count += 1
                self.mem[i] = 0  # Mark as free
        
        self.IDs.remove(mID)
        return count

def test():
    """
    Test function to verify solution with various test cases
    """
    # Test case 1: Example from problem
    allocator = Allocator(10)
    
    # Test allocate operations
    assert allocator.allocate(1, 1) == 0, "First allocation should return 0"
    assert allocator.allocate(1, 2) == 1, "Second allocation should return 1"
    assert allocator.allocate(1, 3) == 2, "Third allocation should return 2"
    
    # Test free operation
    assert allocator.freeMemory(2) == 1, "Freeing mID 2 should return 1"
    
    # Test more allocations
    assert allocator.allocate(3, 4) == 3, "Allocating 3 units should return 3"
    assert allocator.allocate(1, 1) == 1, "Allocating 1 unit should return 1"
    assert allocator.allocate(1, 1) == 6, "Allocating 1 unit should return 6"
    
    # Test free operation
    assert allocator.freeMemory(1) == 3, "Freeing mID 1 should return 3"
    
    # Test impossible allocation
    assert allocator.allocate(10, 2) == -1, "Allocating 10 units should return -1"
    
    # Test freeing non-existent ID
    assert allocator.freeMemory(7) == 0, "Freeing non-existent mID should return 0"
    
    print("All test cases passed!")

if __name__ == "__main__":
    test()

"""
What I Learned from This Problem:
================================

1. OBJECT-ORIENTED DESIGN:
   - Design a class with clear responsibilities
   - Maintain state (memory array, allocated IDs)
   - Implement methods that modify and query state

2. MEMORY MANAGEMENT CONCEPTS:
   - Simulate real memory allocation
   - Track allocated blocks by ID
   - Handle fragmentation and free space

3. ALGORITHM DESIGN:
   - Find leftmost consecutive free block
   - Efficiently scan memory for free space
   - Handle edge cases (no space, invalid IDs)

4. DATA STRUCTURE CHOICES:
   - Array for memory representation (simple and efficient)
   - Set for tracking allocated IDs (O(1) lookup)
   - Simple data structures for this problem size

5. EDGE CASE HANDLING:
   - No space available for allocation
   - Freeing non-existent memory ID
   - Multiple blocks with same ID
   - Fragmented memory layout

6. SIMULATION APPROACH:
   - Model real-world memory allocator
   - Track state changes over time
   - Handle complex allocation patterns

7. OPTIMIZATION CONSIDERATIONS:
   - For larger scales, might need more sophisticated data structures
   - Current approach is O(n) for allocation and freeing
   - Could use segment trees or other advanced structures for better performance

8. TESTING STRATEGY:
   - Test normal allocation and freeing
   - Test edge cases (no space, invalid IDs)
   - Test complex scenarios with multiple operations

This problem taught me how to design a simple but functional memory allocator
and think about the trade-offs between simplicity and performance!
"""

"""
Solution Analysis:
----------------
1. Approach:
   - Use array to represent memory (0 = free, mID = allocated)
   - Use set to track allocated IDs for quick lookup
   - Linear scan to find leftmost consecutive free block

2. Algorithm:
   - allocate(): Scan memory left to right, find first block of size consecutive 0s
   - freeMemory(): Scan entire memory, set all positions with mID to 0

3. Time Complexity:
   - allocate(): O(n) in worst case (scan entire memory)
   - freeMemory(): O(n) (scan entire memory)
   - Overall: O(n) per operation

4. Space Complexity: O(n)
   - Memory array: O(n)
   - Set of IDs: O(k) where k is number of unique IDs

5. Key Insights:
   - Simple array representation is sufficient for this problem size
   - Leftmost allocation strategy (first-fit)
   - Track IDs to handle freeing correctly

6. Edge Cases:
   - No space available → return -1
   - Freeing non-existent ID → return 0
   - Multiple blocks with same ID → free all

7. Optimizations:
   - Could use more sophisticated data structures for better performance
   - Current approach is simple and correct for given constraints
   - For larger scales, consider segment trees or other advanced structures

8. Design Decisions:
   - Array representation: simple and intuitive
   - Set for ID tracking: efficient lookup
   - Linear scan: simple but not optimal for large scales
"""
