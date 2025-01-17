# 2425. Bitwise XOR of All Pairings
# Problem Description:
# You are given two 0-indexed arrays, nums1 and nums2, consisting of non-negative integers.
# There exists another array, nums3, which contains the bitwise XOR of all pairings of integers
# between nums1 and nums2 (every integer in nums1 is paired with every integer in nums2 exactly once).
# Return the bitwise XOR of all integers in nums3.

# Example 1:
# Input: nums1 = [2,1,3], nums2 = [10,2,5,0]
# Output: 13
# Explanation: A possible nums3 array is [8,0,7,2,11,3,4,1,9,1,6,3].
# The bitwise XOR of all these numbers is 13, so we return 13.

# Example 2:
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 0
# Explanation: All possible pairs of bitwise XORs are nums1[0] ^ nums2[0], nums1[0] ^ nums2[1],
# nums1[1] ^ nums2[0], and nums1[1] ^ nums2[1]. Thus, one possible nums3 array is [2,5,1,6].
# 2 ^ 5 ^ 1 ^ 6 = 0, so we return 0.

# Constraints:
# 1 <= nums1.length, nums2.length <= 10^5
# 0 <= nums1[i], nums2[j] <= 10^9

from collections import defaultdict

class Solution(object):
    def xorAllNums(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        # Only when the other array has odd num of elements should we ^ this array

        # Initialize XOR results for both arrays
        xor1, xor2 = 0, 0

        # Get lengths of both arrays
        len1, len2 = len(nums1), len(nums2)

        # If nums2 length is odd, each element in nums1 appears odd times in final result
        if len2 % 2:
            for num in nums1:
                xor1 ^= num

        # If nums1 length is odd, each element in nums2 appears odd times in final result
        if len1 % 2:
            for num in nums2:
                xor2 ^= num

        # Return XOR of both results
        return xor1 ^ xor2

# Complexity Analysis
# Let n and m be the lengths of the arrays nums1 and nums2 respectively.
# Time complexity: O(n+m)
# The algorithm performs two conditional iterations. If len2 is odd, it iterates through nums1 taking O(n) time.
# If len1 is odd, it iterates through nums2 taking O(m) time. In the worst case, both conditions are true,
# leading to a total time complexity of O(n+m).

# Space complexity: O(1)
# The algorithm only uses four variables (xor1, xor2, len1, len2) regardless of the input size.
# These variables consume constant space and do not grow with the input size. Therefore, the space complexity is O(1).


# Testing the Solution
if __name__ == "__main__":
    solution = Solution()

    # Example 1
    nums1_example1 = [2, 1, 3]
    nums2_example1 = [10, 2, 5, 0]
    expected_output_example1 = 13
    result_example1 = solution.xorAllNums(nums1_example1, nums2_example1)
    print(f"Example 1: Expected Output = {expected_output_example1}, Actual Output = {result_example1}")

    # Example 2
    nums1_example2 = [1, 2]
    nums2_example2 = [3, 4]
    expected_output_example2 = 0
    result_example2 = solution.xorAllNums(nums1_example2, nums2_example2)
    print(f"Example 2: Expected Output = {expected_output_example2}, Actual Output = {result_example2}")