"""
LeetCode 198: House Robber
Difficulty: Medium
Pattern: Cluster 11 — Dynamic Programming (Non-Adjacent State Transition)

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        # [rob1, rob2, num, ...]
        for num in nums:
            new_rob = max(rob2, rob1 + num)
            rob1 = rob2
            rob2 = new_rob

        return rob2


if __name__ == "__main__":
    sol = Solution()
    assert sol.rob([1, 2, 3, 1]) == 4, f"Expected 4, got {sol.rob([1, 2, 3, 1])}"
    assert sol.rob([2, 7, 9, 3, 1]) == 12, f"Expected 12, got {sol.rob([2, 7, 9, 3, 1])}"
    print("LC 198 (House Robber): Verified successfully in O(1) space!")
