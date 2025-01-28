# Binary Search Templates
# Topic: Binary Search
"""
Problem Description:
------------------
Two common templates for binary search problems:
1. Finding exact value: Use when searching for specific match
2. Finding boundary: Use when searching for first/last occurrence or boundary condition

Examples for Template 1:
- Classic binary search
- Square root
- Finding element in sorted array

Examples for Template 2:
- First/last occurrence
- Finding minimum in rotated sorted array
- Finding boundary in boolean array
"""

def binary_search_exact(arr, target):
    """
    Template 1: Finding exact value
    Use when: Looking for exact match
    Pattern: while left <= right
    
    Time: O(log n)
    Space: O(1)
    """
    def condition_met(index):
        return arr[index] == target
        
    def need_larger(index):
        return arr[index] < target
    
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        if condition_met(mid):
            return mid
        elif need_larger(mid):
            left = mid + 1
        else:
            right = mid - 1
            
    return -1  # Not found

def binary_search_boundary(arr):
    """
    Template 2: Finding boundary
    Use when: Looking for first/last occurrence or boundary
    Pattern: while left < right
    
    Time: O(log n)
    Space: O(1)
    """
    def condition_met(index):
        return arr[index] >= 0  # Example condition
    
    left = 0
    right = len(arr)
    
    while left < right:
        mid = left + (right - left) // 2
        if condition_met(mid):
            right = mid
        else:
            left = mid + 1
            
    return left  # Found boundary

def test():
    """
    Test function to demonstrate both templates
    """
    # Test Template 1: Finding exact value
    test_cases_1 = [
        {
            'arr': [1, 2, 3, 4, 5],
            'target': 3,
            'expected': 2,
            'description': "Element exists in middle"
        },
        {
            'arr': [1, 3, 5, 7, 9],
            'target': 7,
            'expected': 3,
            'description': "Element exists"
        },
        {
            'arr': [1, 3, 5, 7, 9],
            'target': 4,
            'expected': -1,
            'description': "Element doesn't exist"
        }
    ]
    
    # Test Template 2: Finding boundary
    test_cases_2 = [
        {
            'arr': [-2, -1, 0, 1, 2],
            'expected': 2,
            'description': "Find first non-negative"
        },
        {
            'arr': [-1, -1, 0, 0, 0],
            'expected': 2,
            'description': "Multiple boundaries"
        }
    ]
    
    # Run Template 1 tests
    for i, test in enumerate(test_cases_1, 1):
        result = binary_search_exact(test['arr'], test['target'])
        assert result == test['expected'], \
            f"""Template 1 Test {i} failed:
            Input: arr={test['arr']}, target={test['target']}
            Expected: {test['expected']}
            Got: {result}
            Description: {test['description']}"""
    
    # Run Template 2 tests
    for i, test in enumerate(test_cases_2, 1):
        result = binary_search_boundary(test['arr'])
        assert result == test['expected'], \
            f"""Template 2 Test {i} failed:
            Input: arr={test['arr']}
            Expected: {test['expected']}
            Got: {result}
            Description: {test['description']}"""
    
    print("All test cases passed!")

if __name__ == "__main__":
    test()

"""
Key Differences Between Templates:
-------------------------------
1. Loop Condition:
   Template 1: while left <= right
   - Used when looking for exact match
   - Checks every element
   - Terminates when left > right
   
   Template 2: while left < right
   - Used when finding boundary
   - Maintains left and right next to each other
   - Terminates when left == right

2. Mid Calculation:
   Template 1: mid = left + (right - left) // 2
   - Standard mid calculation
   
   Template 2: Can use either:
   - mid = left + (right - left) // 2
   - mid = (left + right + 1) // 2  # When bias to right needed

3. Pointer Updates:
   Template 1:
   - left = mid + 1
   - right = mid - 1
   
   Template 2:
   - left = mid + 1
   - right = mid

4. Return Value:
   Template 1: Often returns -1 if not found
   Template 2: Always returns a valid index (boundary position)

Common Use Cases:
1. Template 1:
   - Standard binary search
   - Finding exact value
   - Square root calculation
   
2. Template 2:
   - First/last occurrence
   - Finding minimum in rotated array
   - Finding boundary position
"""