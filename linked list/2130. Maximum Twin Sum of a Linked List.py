# LeetCode 2130: Maximum Twin Sum of a Linked List
# Difficulty: Medium
# Topic: Linked List, Two Pointers
"""
Problem Description:
------------------
Given linked list of even length n, find maximum twin sum.
Twin nodes are (i)th and (n-1-i)th nodes where 0 <= i <= (n/2)-1.
Twin sum is sum of a node and its twin.

Example:
Input: head = [5,4,2,1]
Output: 6
Explanation: Node 0 (5) and 3 (1) are twins, Node 1 (4) and 2 (2) are twins
Maximum twin sum is max(5+1, 4+2) = 6

Constraints:
* Number of nodes is even and in range [2, 10^5]
* 1 <= Node.val <= 10^5
"""

class Solution(object):
   def pairSum(self, head):
       """
       Approach: Use slow-fast pointers to find middle while reversing first half
       Then compare reversed first half with second half
       
       :type head: Optional[ListNode]
       :rtype: int
       """
       # Takeaway:
       # 1. For finding middle/detecting cycles, use slow-fast pointers
       # 2. When length is even, while fast.next is enough
       #    When length could be odd, need while fast and fast.next
       #    - Even length: fast reaches None
       #    - Odd length: fast reaches last node

       # Initialize pointers
       slow = head
       fast = head
       prev = None

       # Find middle while reversing first half
       while fast and fast.next:
           fast = fast.next.next
           
           # Save next node before breaking link
           next_slow = slow.next
           # Reverse current node
           slow.next = prev
           # Move prev and slow forward
           prev = slow
           slow = next_slow

       # Now:
       # - prev points to last node of reversed first half
       # - slow points to first node of second half
       # - Original: 5->4->2->1
       # - After: 5<-4  2->1
       #          ^     ^
       #         prev  slow

       # Find maximum twin sum
       max_sum = 0
       while slow:
           max_sum = max(max_sum, slow.val + prev.val)
           slow = slow.next
           prev = prev.next

       return max_sum

def test():
   # Helper function to create linked list
   def create_linked_list(arr):
       if not arr: return None
       head = ListNode(arr[0])
       curr = head
       for val in arr[1:]:
           curr.next = ListNode(val)
           curr = curr.next
       return head

   solution = Solution()
   assert solution.pairSum(create_linked_list([5,4,2,1])) == 6
   assert solution.pairSum(create_linked_list([4,2,2,3])) == 7
   assert solution.pairSum(create_linked_list([1,100000])) == 100001
   print("All test cases passed!")

"""
Solution Analysis:
----------------
Time Complexity: O(n) - single pass through list
Space Complexity: O(1) - in-place reversal

Key Points:
1. Use slow-fast pointers to find middle
2. Reverse first half in-place while finding middle
3. Compare reversed first half with second half
4. For even length lists, while fast.next works
5. For lists that could be odd, need while fast and fast.next
"""