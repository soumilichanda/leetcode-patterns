"""
LeetCode 309: Best Time to Buy and Sell Stock with Cooldown
Difficulty: Medium
Pattern: Cluster 31 — Dynamic Programming (Finite State Machine Transitions)

States:
    held:  Holding a share (bought today or carried over)
    sold:  Just sold today (mandates cooldown tomorrow)
    reset: In cooldown or waiting (cash available to buy)

Transitions:
    held  = max(prev_held, prev_reset - price)
    sold  = prev_held + price
    reset = max(prev_reset, prev_sold)

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        held = -float("inf")
        sold = 0
        reset = 0

        for price in prices:
            prev_held = held
            prev_sold = sold
            prev_reset = reset

            held = max(prev_held, prev_reset - price)
            sold = prev_held + price
            reset = max(prev_reset, prev_sold)

        return max(sold, reset)


if __name__ == "__main__":
    sol = Solution()
    assert sol.maxProfit([1, 2, 3, 0, 2]) == 3
    assert sol.maxProfit([1]) == 0
    print("LC 309 verified successfully!")
