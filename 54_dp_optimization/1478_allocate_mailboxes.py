"""
LeetCode 1478: Allocate Mailboxes
Difficulty: Hard
Pattern: Cluster 54 — DP Optimization (Precomputed Median-Cost Interval DP)

Time Complexity: O(k * n^2)
Space Complexity: O(n^2)
"""

from typing import List


class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        n = len(houses)
        if k >= n:
            return 0

        houses.sort()

        # Precompute cost[i][j]: minimum distance sum for 1 mailbox covering houses[i..j]
        cost = [[0] * n for _ in range(n)]
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                cost[i][j] = cost[i + 1][j - 1] + houses[j] - houses[i]

        # dp[p][j]: min distance covering houses[0..j] using p mailboxes
        inf = float("inf")
        dp = [[inf] * n for _ in range(k + 1)]
        for j in range(n):
            dp[1][j] = cost[0][j]

        for p in range(2, k + 1):
            for j in range(p - 1, n):
                for i in range(p - 2, j):
                    candidate = dp[p - 1][i] + cost[i + 1][j]
                    if candidate < dp[p][j]:
                        dp[p][j] = candidate

        return int(dp[k][n - 1])


if __name__ == "__main__":
    sol = Solution()
    assert sol.minDistance([1, 4, 8, 10, 20], 3) == 5
    assert sol.minDistance([2, 3, 5, 12, 18], 2) == 9
    assert sol.minDistance([7, 4, 6, 1], 1) == 8
    print("LC 1478 verified successfully!")
