"""
LeetCode 877: Stone Game
Difficulty: Medium
Pattern: Game Theory DP (Zero-Sum Interval Minimax & Parity Invariant)

Time Complexity: O(n^2)
Space Complexity: O(n)
"""

from typing import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp = piles[:]

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                dp[j] = max(piles[i] - dp[j], piles[j] - dp[j - 1])

        return dp[n - 1] > 0


if __name__ == "__main__":
    sol = Solution()
    assert sol.stoneGame([5, 3, 4, 5]) is True
    assert sol.stoneGame([3, 7, 2, 3]) is True
    print("LC 877 verified successfully!")
