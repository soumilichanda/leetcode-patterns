"""
LeetCode 787: Cheapest Flights Within K Stops
Difficulty: Medium
Pattern: Bellman-Ford / Level-Bounded Edge Relaxation

Time Complexity: O(K * E)
Space Complexity: O(V)
"""

from typing import List


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for _ in range(k + 1):
            temp_prices = list(prices)
            for u, v, w in flights:
                if prices[u] == float("inf"):
                    continue
                if prices[u] + w < temp_prices[v]:
                    temp_prices[v] = prices[u] + w
            prices = temp_prices

        return int(prices[dst]) if prices[dst] != float("inf") else -1


if __name__ == "__main__":
    sol = Solution()
    # Test Case 1: Standard 1-stop path
    flights1 = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
    res1 = sol.findCheapestPrice(4, flights1, 0, 3, 1)
    assert res1 == 700, f"Expected 700, got {res1}"

    # Test Case 2: Direct path cheaper within 0 stops
    flights2 = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
    res2 = sol.findCheapestPrice(3, flights2, 0, 2, 0)
    assert res2 == 500, f"Expected 500, got {res2}"

    print("LC 787 (Cheapest Flights Within K Stops) tests passed successfully!")
