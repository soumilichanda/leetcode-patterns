"""
LeetCode 518: Coin Change II
Difficulty: Medium
Pattern: Cluster 30 — Knapsack DP (Combinatorial Unbounded DP)

Invariant:
    Subproblem: dp[a] = total unique combinations that sum up to amount a.
    Base case: dp[0] = 1 (1 way to make 0: empty set).
    Outer Loop on Coins: Iterating coins externally prevents permutation duplicates
    (e.g., [1, 2] vs [2, 1] counted once).
    Transition: dp[a] += dp[a - c] for each coin c and amount a in [c, amount].

Time Complexity: O(amount * len(coins))
Space Complexity: O(amount) auxiliary space
"""

from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for c in coins:
            for a in range(c, amount + 1):
                dp[a] += dp[a - c]

        return dp[amount]


if __name__ == "__main__":
    sol = Solution()
    assert sol.change(5, [1, 2, 5]) == 4, f"Expected 4, got {sol.change(5, [1, 2, 5])}"
    assert sol.change(3, [2]) == 0, f"Expected 0, got {sol.change(3, [2])}"
    assert sol.change(10, [10]) == 1, f"Expected 1, got {sol.change(10, [10])}"
    print("LC 518 (Coin Change II): Verified successfully!")
