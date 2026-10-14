"""
LeetCode 55: Jump Game
Difficulty: Medium
Pattern: Greedy Reachability Horizon

Invariant:
    Maintain the furthest reachable index `max_reachable`.
    For each index i:
    1. If i > max_reachable, current index is unreachable -> return False.
    2. Update max_reachable = max(max_reachable, i + nums[i]).
    3. If max_reachable >= len(nums) - 1, destination is reachable -> early exit True.

Time Complexity: O(n) ? Single linear scan
Space Complexity: O(1) ? In-place frontier tracking
"""

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reachable = 0
        n = len(nums)

        for i, jump in enumerate(nums):
            if i > max_reachable:
                return False

            max_reachable = max(max_reachable, i + jump)
            if max_reachable >= n - 1:
                return True

        return True
