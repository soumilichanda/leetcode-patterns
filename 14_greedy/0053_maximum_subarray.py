"""
LeetCode 53: Maximum Subarray
Difficulty: Medium
Pattern: Kadane's Algorithm (Greedy Dynamic Programming)

Invariant:
    At each element x, the optimal subarray ending at index i either:
    1. Extends the running contiguous subarray: curr_sum + x
    2. Drops negative accumulated baggage and starts fresh at: x
    curr_sum = max(x, curr_sum + x)
    max_sum = max(max_sum, curr_sum)

Time Complexity: O(n) ? Single linear scan
Space Complexity: O(1) ? Constant memory
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        curr_sum = nums[0]
        max_sum = nums[0]

        for x in nums[1:]:
            curr_sum = max(x, curr_sum + x)
            max_sum = max(max_sum, curr_sum)

        return max_sum
