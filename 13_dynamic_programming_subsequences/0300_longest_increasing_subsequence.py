"""
LeetCode 300: Longest Increasing Subsequence
Pattern: Dynamic Programming / Patience Sorting (Binary Search)
Time Complexity: O(n log n)
Space Complexity: O(n)
"""

from bisect import bisect_left
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        tails: List[int] = []

        for x in nums:
            idx = bisect_left(tails, x)
            if idx == len(tails):
                tails.append(x)
            else:
                tails[idx] = x

        return len(tails)


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ([10, 9, 2, 5, 3, 7, 101, 18], 4),
        ([0, 1, 0, 3, 2, 3], 4),
        ([7, 7, 7, 7, 7, 7, 7], 1),
    ]

    for nums, expected in test_cases:
        res = sol.lengthOfLIS(nums)
        assert res == expected, f"Failed for {nums}: expected {expected}, got {res}"
        print(f"nums={nums} -> LIS Length: {res} (Passed)")
