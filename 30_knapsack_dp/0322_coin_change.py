"""
LeetCode 322: Coin Change
Difficulty: Medium
Pattern: Cluster 30 — Knapsack DP (Unbounded Min-Element DP)

Invariant:
    Subproblem: dp[a] = fewest coins needed to make amount a.
    Base case: dp[0] = 0, dp[1..amount] = inf.
    Transition: dp[a] = min(dp[a], 1 + dp[a - c]) for each c in coins if a >= c.

Time Complexity: O(amount * len(coins))
Space Complexity: O(amount) auxiliary space
"""

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a >= c:
                    dp[a] = min(dp[a], 1 + dp[a - c])

        return int(dp[amount]) if dp[amount] != float("inf") else -1


if __name__ == "__main__":
    sol = Solution()
    assert sol.coinChange([1, 2, 5], 11) == 3, f"Expected 3, got {sol.coinChange([1, 2, 5], 11)}"
    assert sol.coinChange([2], 3) == -1, f"Expected -1, got {sol.coinChange([2], 3)}"
    assert sol.coinChange([1], 0) == 0, f"Expected 0, got {sol.coinChange([1], 0)}"
    print("LC 322 (Coin Change): Verified successfully!")
