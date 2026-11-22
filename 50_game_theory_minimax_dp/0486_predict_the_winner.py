"""
LeetCode 486: Predict the Winner
Difficulty: Medium
Pattern: Game Theory DP (Interval Score-Differential Minimax)

Time Complexity: O(n^2)
Space Complexity: O(n)
"""

from typing import List


class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = nums[:]

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                dp[j] = max(nums[i] - dp[j], nums[j] - dp[j - 1])

        return dp[n - 1] >= 0


if __name__ == "__main__":
    sol = Solution()
    assert sol.predictTheWinner([1, 5, 2]) is False
    assert sol.predictTheWinner([1, 5, 233, 7]) is True
    print("LC 486 verified successfully!")
