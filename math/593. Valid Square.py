# LeetCode 593. Valid Square
# Difficulty: Medium
# Topic: Math, Geometry

"""
Problem Description:
------------------
Given the coordinates of four points in 2D space p1, p2, p3 and p4, return true if 
the four points construct a square.

The coordinate of a point pi is represented as [xi, yi]. The input is not given in any order.

A valid square has four equal sides with positive length and four equal angles (90-degree angles).

Example 1:
Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: true

Example 2:
Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,12]
Output: false

Example 3:
Input: p1 = [1,0], p2 = [-1,0], p3 = [0,1], p4 = [0,-1]
Output: true

Constraints:
* p1.length == p2.length == p3.length == p4.length == 2
* -10^4 <= xi, yi <= 10^4
"""

from collections import Counter 

class Solution(object):
    def validSquare(self, p1, p2, p3, p4):
        """
        Approach: Distance-based validation
        - Calculate all pairwise distances between the 4 points
        - A square has exactly 2 types of distances:
          * 4 equal side lengths
          * 2 equal diagonal lengths
        - Check if we have exactly 2 unique distances with correct counts
        
        Time: O(1) - constant time operations
        Space: O(1) - constant space for distance calculations
        """
        pts = [p1, p2, p3, p4]
        pts.sort(key=lambda p:(p[0], p[1]))
        l1 = self.dist(pts[0], pts[1])
        l2 = self.dist(pts[1], pts[2])
        l3 = self.dist(pts[2], pts[3])
        l4 = self.dist(pts[3], pts[0])
        l5 = self.dist(pts[0], pts[2])
        l6 = self.dist(pts[1], pts[3])
        count = Counter([l1, l2, l3, l4, l5, l6])
        if len(count) == 2 and 0 not in count and sorted(count.values()) == [2, 4]:
            return True
        return False

    def dist(self, p1, p2):
        """
        Calculate squared distance between two points
        Using squared distance to avoid floating point precision issues
        """
        return pow(p2[0]-p1[0], 2) + pow(p2[1]-p1[1], 2)

def test():
    """
    Test function to verify solution with various test cases
    """
    solution = Solution()
    
    # Test case 1: Valid square
    p1, p2, p3, p4 = [0,0], [1,1], [1,0], [0,1]
    result1 = solution.validSquare(p1, p2, p3, p4)
    assert result1 == True, f"Test case 1 failed: expected True, got {result1}"
    
    # Test case 2: Invalid square (rectangle)
    p1, p2, p3, p4 = [0,0], [1,1], [1,0], [0,12]
    result2 = solution.validSquare(p1, p2, p3, p4)
    assert result2 == False, f"Test case 2 failed: expected False, got {result2}"
    
    # Test case 3: Valid square (diamond shape)
    p1, p2, p3, p4 = [1,0], [-1,0], [0,1], [0,-1]
    result3 = solution.validSquare(p1, p2, p3, p4)
    assert result3 == True, f"Test case 3 failed: expected True, got {result3}"
    
    # Test case 4: Invalid (not a square)
    p1, p2, p3, p4 = [0,0], [1,0], [1,1], [0,2]
    result4 = solution.validSquare(p1, p2, p3, p4)
    assert result4 == False, f"Test case 4 failed: expected False, got {result4}"
    
    # Test case 5: Invalid (degenerate case - all same point)
    p1, p2, p3, p4 = [0,0], [0,0], [0,0], [0,0]
    result5 = solution.validSquare(p1, p2, p3, p4)
    assert result5 == False, f"Test case 5 failed: expected False, got {result5}"
    
    # Test case 6: Valid square (rotated)
    p1, p2, p3, p4 = [1,1], [2,2], [2,1], [1,2]
    result6 = solution.validSquare(p1, p2, p3, p4)
    assert result6 == True, f"Test case 6 failed: expected True, got {result6}"
    
    print("All test cases passed!")

if __name__ == "__main__":
    test()

"""
Solution Analysis:
----------------
1. Key Insight:
   - A square has exactly 2 types of distances:
     * 4 equal side lengths (smaller distance)
     * 2 equal diagonal lengths (larger distance)
   - Total of 6 distances: 4 sides + 2 diagonals

2. Algorithm:
   - Calculate all pairwise distances between the 4 points
   - Count the frequency of each distance
   - Check if we have exactly 2 unique distances with counts [2, 4]

3. Distance Calculation:
   - Use squared distance to avoid floating point precision issues
   - Distance = (x2-x1)² + (y2-y1)²
   - No need to take square root since we're comparing distances

4. Validation Logic:
   - len(count) == 2: exactly 2 unique distances
   - 0 not in count: no degenerate cases (all points same)
   - sorted(count.values()) == [2, 4]: 2 diagonals and 4 sides

5. Time Complexity: O(1)
   - Constant number of distance calculations
   - Constant time sorting and counting

6. Space Complexity: O(1)
   - Only storing constant number of distances
   - Counter with at most 6 entries

7. Edge Cases Handled:
   - All points are the same (degenerate case)
   - Points form a rectangle but not square
   - Points form other quadrilaterals
   - Valid squares in different orientations

8. Why This Works:
   - Geometric property: square has equal sides and equal diagonals
   - No other quadrilateral has this exact distance pattern
   - Sorting helps with consistent ordering but not strictly necessary

9. Alternative Approaches:
   - Could check angles (90 degrees)
   - Could check side lengths and slopes
   - Distance-based approach is most robust
"""
