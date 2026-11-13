"""
LeetCode 1547: Minimum Cost to Cut a Stick
Difficulty: Hard
Pattern: Cluster 41 — Interval Dynamic Programming (Sorted Cut-Point Partitioning)

Time Complexity: O(m^3) where m = len(cuts) + 2
Space Complexity: O(m^2)
"""

from typing import List


class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        endpoints = [0] + sorted(cuts) + [n]
        m = len(endpoints)

        # dp[i][j] = min cost to perform all cuts strictly between endpoints[i] and endpoints[j]
        dp = [[0] * m for _ in range(m)]

        for length in range(2, m):
            for i in range(0, m - length):
                j = i + length
                segment_length = endpoints[j] - endpoints[i]
                min_subcost = float("inf")

                for k in range(i + 1, j):
                    cost = dp[i][k] + dp[k][j]
                    if cost < min_subcost:
                        min_subcost = cost

                dp[i][j] = segment_length + int(min_subcost)

        return dp[0][m - 1]


if __name__ == "__main__":
    sol = Solution()
    assert sol.minCost(7, [1, 3, 4, 5]) == 16
    assert sol.minCost(9, [5, 6, 1, 4, 2]) == 22
    print("LC 1547 (Minimum Cost to Cut a Stick) verified successfully!")
