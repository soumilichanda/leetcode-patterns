"""
LeetCode 121: Best Time to Buy and Sell Stock
Difficulty: Easy
Pattern: Sliding Window / Dynamic Running Minimum

Time Complexity: O(n)
Space Complexity: O(1)
"""


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float("inf")
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)

        return max_profit


if __name__ == "__main__":
    sol = Solution()
    test_prices = [7, 1, 5, 3, 6, 4]
    print(f"Max Profit: {sol.maxProfit(test_prices)}")  # Expected: 5