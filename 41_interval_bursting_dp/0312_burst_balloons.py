"""
LeetCode 312: Burst Balloons
Difficulty: Hard
Pattern: Cluster 41 — Interval Dynamic Programming (Reverse Last-Element Partitioning)

Time Complexity: O(n^3)
Space Complexity: O(n^2)
"""

from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Filter zero-value balloons early as they contribute 0 coins when burst
        padded = [1] + [x for x in nums if x > 0] + [1]
        n = len(padded)

        # dp[left][right] = max coins obtained by bursting all balloons strictly inside (left, right)
        dp = [[0] * n for _ in range(n)]

        # Iterate over increasing interval lengths (distance between left and right)
        for length in range(2, n):
            for left in range(0, n - length):
                right = left + length
                boundary_product = padded[left] * padded[right]
                best = 0

                # k is the LAST balloon to be burst in open interval (left, right)
                for k in range(left + 1, right):
                    coins = boundary_product * padded[k] + dp[left][k] + dp[k][right]
                    if coins > best:
                        best = coins

                dp[left][right] = best

        return dp[0][n - 1]


if __name__ == "__main__":
    sol = Solution()
    assert sol.maxCoins([3, 1, 5, 8]) == 167
    assert sol.maxCoins([1, 5]) == 10
    print("LC 312 (Burst Balloons) verified successfully!")
