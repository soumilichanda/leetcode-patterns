"""
LeetCode 813: Largest Sum of Averages
Difficulty: Medium
Pattern: Cluster 54 — DP Optimization (k-Partition Prefix-Average DP)

Time Complexity: O(k * n^2)
Space Complexity: O(n)
"""

from typing import List


class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        n = len(nums)
        prefix = [0.0] * (n + 1)
        for i, val in enumerate(nums):
            prefix[i + 1] = prefix[i] + val

        # Base case: 1 partition covering prefix [0..i)
        dp = [0.0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = prefix[i] / i

        for p in range(2, k + 1):
            for i in range(n, p - 1, -1):
                best = dp[i]
                for j in range(p - 1, i):
                    candidate = dp[j] + (prefix[i] - prefix[j]) / (i - j)
                    if candidate > best:
                        best = candidate
                dp[i] = best

        return dp[n]


if __name__ == "__main__":
    sol = Solution()
    assert abs(sol.largestSumOfAverages([9, 1, 2, 3, 9], 3) - 20.0) < 1e-6
    assert abs(sol.largestSumOfAverages([1, 2, 3, 4, 5, 6, 7], 4) - 20.5) < 1e-6
    print("LC 813 verified successfully!")
