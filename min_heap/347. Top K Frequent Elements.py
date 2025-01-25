# LeetCode 347. Top K Frequent Elements
# Difficulty: Medium
# Topic: Heap, Hash Table, Counter
"""
Problem Description:
------------------
Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1 
Output: [1]

Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in range [1, number of unique elements]
Answer is guaranteed to be unique
"""

from collections import Counter
import heapq

class Solution(object):
   def topKFrequent(self, nums, k):
       """
       Approach: Use Counter and heap.nlargest
       Time: O(m log k) where m is number of unique elements 
       Space: O(m) for Counter
       
       :type nums: List[int]
       :type k: int
       :rtype: List[int]
       """
       # 1. In heap questions, the complexity of the functions are:
       # (Here n is the number of elements in heap)
       # heappush(heap, item): O(log n)
       # heappop(heap): O(log n) 
       # heapify(list): O(n)
       # heap[0]: O(1) - peek at smallest element
       # Advanced Operations:
       # nlargest(k, iterable): O(n log k)
       # nsmallest(k, iterable): O(n log k)
       # heappushpop(heap, item): O(log n)
       # heapreplace(heap, item): O(log n)

       # Method 1: Time: O(m log k), Method: Counter + Heap nlargest
       count = Counter(nums)
       result = heapq.nlargest(k, count.keys(), key=count.get)
       return result

       # # Method 2: Time: O(n), Method: Counter, Bucket Sort
       # bucket = [[] for _ in range(len(nums) + 1 )]
       # result = []
       # ctr = Counter(nums)
       # for key, v in ctr.items():
           # bucket[v].append(key)
       # count = 0
       # for i in range(len(nums), -1, -1):
           # if bucket[i]:
               # for j in range(len(bucket[i])):
                   # result.append(bucket[i][j])
                   # count += 1
                   # if count == k:
                       # return result
       # # return result

       # # Method 3: Time: O(n * logn), Method: Sort, Counter  
       # counter = Counter(nums)
       # cnt = 0
       # result = []
       # for key, v in sorted(counter.items(), key = lambda x: x[1], reverse=True):
           # cnt += 1
           # result.append(key)
           # if cnt == k:
               # break
       # return result

# Test cases
def test():
   solution = Solution()
   assert set(solution.topKFrequent([1,1,1,2,2,3], 2)) == set([1,2])
   assert solution.topKFrequent([1], 1) == [1] 
   print("All test cases passed!")

if __name__ == "__main__":
   test()

"""
Solution Analysis:
----------------
Method 1 (Current): Using Counter + Heap nlargest
Time: O(m log k) where m is number of unique elements
- Counter creation: O(n)
- nlargest operation: O(m log k) as it maintains heap of size k
Space: O(m) for storing counter dictionary

Method 2 (Commented): Bucket Sort
Time: O(n) 
- Counter creation: O(n)
- Bucket filling: O(m)
- Result collection: O(n)
Space: O(n) for buckets

Method 3 (Commented): Sorting with Counter
Time: O(n log n) 
- Counter: O(n)
- Sorting: O(m log m)
Space: O(m) for counter and sorted list

Key Points:
1. Method 1 is most efficient when k << m
2. Method 2 (bucket sort) has best theoretical complexity
3. Counter is used in all methods for frequency counting
4. nlargest provides clean implementation with good practical performance
"""