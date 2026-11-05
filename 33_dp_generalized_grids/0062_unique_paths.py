"""
LeetCode 62: Unique Paths
Difficulty: Medium
Pattern: Cluster 33 — Coordinate Grid DP / Rolling 1D Array

Time Complexity: O(m * n)
Space Complexity: O(n)
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for _ in range(1, m):
            for c in range(1, n):
                dp[c] += dp[c - 1]
        return dp[-1]


if __name__ == "__main__":
    sol = Solution()
    assert sol.uniquePaths(3, 7) == 28
    assert sol.uniquePaths(3, 2) == 3
    print("LC 62 verified successfully!")
