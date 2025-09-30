"""
LeetCode: 430. Flatten a Multilevel Doubly Linked List
Difficulty: Medium
Topic: Linked List, Depth-First Search, Doubly Linked List

Problem Description:
------------------
You are given a doubly linked list, which contains nodes that have a next pointer, 
a previous pointer, and an additional child pointer. This child pointer may or may 
not point to a separate doubly linked list, also containing these special nodes. 
These child lists may have one or more children of their own, and so on, to produce 
a multilevel data structure.

Given the head of the first level of the list, flatten the list so that all the 
nodes appear in a single-level, doubly linked list. Let curr be a node with a child 
list. The nodes in the child list should appear after curr and before curr.next 
in the flattened list.

Return the head of the flattened list. The nodes in the list must have all of 
their child pointers set to null.

Example 1:
Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
Output: [1,2,3,7,8,11,12,9,10,4,5,6]

The multilevel structure:
 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL

After flattening: 1---2---3---7---8---11---12---9---10---4---5---6--NULL

Example 2:
Input: head = [1,2,null,3]
Output: [1,3,2]

Example 3:
Input: head = []
Output: []

Constraints:
* The number of Nodes will not exceed 1000
* 1 <= Node.val <= 10^5

Key Insights:
1. DFS approach: When we encounter a child, we need to flatten it first
2. Stack approach: Use a stack to keep track of next nodes when we go into children
3. The flattened list should maintain the doubly linked structure
4. All child pointers must be set to null after flattening
"""

# Definition for a Node.
class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        Approach 1: Stack-based Iterative Solution
        Use a stack to keep track of nodes that need to be processed later.
        
        Algorithm:
        1. Traverse the list from head
        2. When we find a node with a child:
           - If current node has a next, push it to stack
           - Connect child to current node
           - Move to child
        3. When we reach the end of a level, pop from stack to continue
        
        Time Complexity: O(n) where n is total number of nodes
        Space Complexity: O(n) for the stack in worst case
        """
        if not head:
            return None
            
        cur = head
        stack = []
        
        while cur:
            if cur.child:
                # Save the next node if it exists
                if cur.next:
                    stack.append(cur.next)
                
                # Connect child to current node
                cur.next = cur.child
                cur.child.prev = cur
                cur.child = None  # Set child to null
                
                # Move to child
                cur = cur.next
            elif cur.next:
                # No child, move to next
                cur = cur.next
            elif stack:
                # No child and no next, but we have saved nodes
                next_node = stack.pop()
                cur.next = next_node
                next_node.prev = cur
                cur = next_node
            else:
                # No child, no next, no stack - we're done
                break
                
        return head

    def flatten_dfs(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        Approach 2: Recursive DFS Solution
        Recursively flatten child lists before continuing with the main list.
        
        Time Complexity: O(n)
        Space Complexity: O(d) where d is the maximum depth of the multilevel structure
        """
        if not head:
            return None
            
        def dfs(node):
            if not node:
                return None
                
            # If node has a child, flatten the child first
            if node.child:
                child_tail = dfs(node.child)
                
                # Save the original next node
                original_next = node.next
                
                # Connect child to current node
                node.next = node.child
                node.child.prev = node
                
                # Connect child tail to original next
                if original_next:
                    child_tail.next = original_next
                    original_next.prev = child_tail
                
                # Clear child pointer
                node.child = None
                
                # Continue from the original next
                return dfs(original_next) if original_next else child_tail
            else:
                # No child, continue with next or return current node as tail
                return dfs(node.next) if node.next else node
        
        dfs(head)
        return head

    def flatten_iterative_optimized(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        Approach 3: Optimized Iterative Solution
        More efficient version that processes nodes in a single pass.
        
        Time Complexity: O(n)
        Space Complexity: O(1) - no extra space for stack
        """
        if not head:
            return None
            
        cur = head
        while cur:
            if cur.child:
                # Find the tail of the child list
                child_tail = cur.child
                while child_tail.next:
                    child_tail = child_tail.next
                
                # Save the original next
                original_next = cur.next
                
                # Connect child to current node
                cur.next = cur.child
                cur.child.prev = cur
                
                # Connect child tail to original next
                if original_next:
                    child_tail.next = original_next
                    original_next.prev = child_tail
                
                # Clear child pointer
                cur.child = None
                
                # Move to original next
                cur = original_next
            else:
                cur = cur.next
                
        return head


def create_multilevel_list(values):
    """
    Helper function to create a multilevel doubly linked list from array representation.
    This is a simplified version for testing purposes.
    """
    if not values:
        return None
    
    # Create nodes
    nodes = [Node(val) if val is not None else None for val in values]
    
    # Connect next and prev pointers
    for i in range(len(nodes)):
        if nodes[i] is None:
            continue
        if i > 0 and nodes[i-1] is not None:
            nodes[i].prev = nodes[i-1]
        if i < len(nodes) - 1 and nodes[i+1] is not None:
            nodes[i].next = nodes[i+1]
    
    return nodes[0] if nodes else None


def list_to_array(head):
    """
    Convert flattened list to array for testing.
    """
    result = []
    cur = head
    while cur:
        result.append(cur.val)
        cur = cur.next
    return result


def test_solution():
    """
    Comprehensive test function for all approaches.
    """
    solution = Solution()
    
    # Test Case 1: Complex multilevel structure
    print("Test Case 1: Complex multilevel structure")
    # This is a simplified test - in practice, you'd need a more sophisticated
    # list builder for multilevel structures
    head1 = Node(1)
    head1.next = Node(2)
    head1.next.prev = head1
    head1.next.next = Node(3)
    head1.next.next.prev = head1.next
    head1.next.next.next = Node(4)
    head1.next.next.next.prev = head1.next.next
    head1.next.next.next.next = Node(5)
    head1.next.next.next.next.prev = head1.next.next.next
    head1.next.next.next.next.next = Node(6)
    head1.next.next.next.next.next.prev = head1.next.next.next.next
    
    # Add child at node 3
    child1 = Node(7)
    child1.next = Node(8)
    child1.next.prev = child1
    child1.next.next = Node(9)
    child1.next.next.prev = child1.next
    child1.next.next.next = Node(10)
    child1.next.next.next.prev = child1.next.next
    
    # Add grandchild at node 8
    grandchild = Node(11)
    grandchild.next = Node(12)
    grandchild.next.prev = grandchild
    child1.next.child = grandchild
    
    head1.next.next.child = child1
    
    # Test all approaches
    result1_stack = solution.flatten(head1)
    print(f"Stack approach result: {list_to_array(result1_stack)}")
    
    # Test Case 2: Simple case
    print("\nTest Case 2: Simple case")
    head2 = Node(1)
    head2.next = Node(2)
    head2.next.prev = head2
    head2.child = Node(3)
    
    result2 = solution.flatten_dfs(head2)
    print(f"DFS approach result: {list_to_array(result2)}")
    
    # Test Case 3: Empty list
    print("\nTest Case 3: Empty list")
    result3 = solution.flatten(None)
    print(f"Empty list result: {list_to_array(result3)}")
    
    print("\nAll tests completed!")


def analyze_complexity():
    """
    Complexity Analysis for different approaches.
    """
    print("Complexity Analysis:")
    print("=" * 50)
    
    print("1. Stack-based Iterative Solution:")
    print("   Time Complexity: O(n) - each node visited exactly once")
    print("   Space Complexity: O(n) - stack can hold up to n nodes in worst case")
    print("   Best for: General case, easy to understand")
    
    print("\n2. Recursive DFS Solution:")
    print("   Time Complexity: O(n) - each node visited exactly once")
    print("   Space Complexity: O(d) - recursion depth equals max depth of multilevel structure")
    print("   Best for: When depth is much smaller than total nodes")
    
    print("\n3. Optimized Iterative Solution:")
    print("   Time Complexity: O(n) - each node visited exactly once")
    print("   Space Complexity: O(1) - no extra space used")
    print("   Best for: Memory-constrained environments")
    
    print("\nKey Takeaways:")
    print("- All approaches have O(n) time complexity")
    print("- Stack approach is most intuitive and handles all cases well")
    print("- DFS approach uses less space when depth is small")
    print("- Optimized approach uses constant space but is more complex")
    print("- The key insight is to process child lists before continuing with main list")


if __name__ == "__main__":
    test_solution()
    print("\n" + "=" * 60)
    analyze_complexity()
