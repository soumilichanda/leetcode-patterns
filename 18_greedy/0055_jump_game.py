"""
LeetCode 55: Jump Game
Difficulty: Medium
Pattern: Greedy (Reverse Monotonic Reachability)

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == 0
