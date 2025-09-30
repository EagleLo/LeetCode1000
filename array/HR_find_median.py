"""
HackerRank-style: Find Median Without Full Sorting

Problem
Given an integer array `arr` of odd length, return its median.
- The median is the element at index n//2 in the array's sorted order (0-based).
- You should provide an implementation that does NOT fully sort the array (QuickSelect),
  and also include a simple sorting baseline for comparison/testing.

Input format (when run normally):
- One line with integer n (odd)
- One line with n space-separated integers
Output:
- A single integer: the median (lower median for odd length)

Notes
- For even length arrays (not expected by the problem), we return the lower median
  (i.e., element at index n//2 in sorted order), matching common HR problems.

Usage
- Run normally to read from stdin and print the median
- Run with: `python HR_find_median.py test` to execute built-in tests
"""

import random
import sys
from typing import List


def findMedian_quickselect(arr: List[int]) -> int:
    """Return the lower median using QuickSelect in O(n) average time.

    This does not fully sort the array. Works for both odd and even n, returning
    the element at index n//2 in the sorted order (lower median for even n).
    """
    if not arr:
        raise ValueError("Array must be non-empty")

    target_index = len(arr) // 2

    def quickselect(nums: List[int], k: int) -> int:
        # Recursive QuickSelect using random pivot; average O(n)
        if len(nums) == 1:
            return nums[0]

        pivot = random.choice(nums)
        left = [x for x in nums if x < pivot]
        mid = [x for x in nums if x == pivot]
        right = [x for x in nums if x > pivot]

        if k < len(left):
            return quickselect(left, k)
        if k < len(left) + len(mid):
            return pivot
        return quickselect(right, k - len(left) - len(mid))

    return quickselect(arr, target_index)


def findMedian_sorting(arr: List[int]) -> int:
    """Baseline: sort the array and return the lower median in O(n log n)."""
    if not arr:
        raise ValueError("Array must be non-empty")
    nums = sorted(arr)
    return nums[len(nums) // 2]


def _run_tests() -> None:
    """Lightweight self-tests for both implementations."""
    test_cases = [
        ([1], 1),
        ([1, 2, 3], 2),
        ([3, 1, 2], 2),
        ([5, 4, 3, 2, 1], 3),
        ([7, 7, 7, 7, 7], 7),
        ([2, 2, 1, 3, 4], 2),
        ([9, -1, 0, 5, 2], 2),
        # Even length: return lower median
        ([1, 2, 3, 4], 3 // 1 and 2),  # evaluates to 2; comment keeps readability
        ([4, 1, 2, 3], 2),
    ]

    def assert_eq(a, b, msg: str) -> None:
        if a != b:
            raise AssertionError(f"{msg}: expected {b}, got {a}")

    print("Running tests for findMedian_quickselect and findMedian_sorting ...")
    for arr, expected in test_cases:
        got_qs = findMedian_quickselect(arr.copy())
        got_sort = findMedian_sorting(arr.copy())
        assert_eq(got_qs, expected, f"QuickSelect failed for {arr}")
        assert_eq(got_sort, expected, f"Sorting failed for {arr}")
        print(f"✓ {arr} -> {expected}")
    print("All tests passed!")


def _run_cli() -> None:
    n_line = sys.stdin.readline().strip()
    if not n_line:
        raise SystemExit(0)
    try:
        n = int(n_line)
    except ValueError:
        raise SystemExit("First line must be an integer n")

    arr_line = sys.stdin.readline().strip()
    if not arr_line:
        raise SystemExit("Second line with array elements is required")

    try:
        arr = list(map(int, arr_line.split()))
    except ValueError:
        raise SystemExit("Array elements must be integers")

    if len(arr) != n:
        # If input size mismatches, still compute based on provided elements
        # to be robust in local runs.
        pass

    print(findMedian_quickselect(arr))


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        _run_tests()
    else:
        _run_cli()
