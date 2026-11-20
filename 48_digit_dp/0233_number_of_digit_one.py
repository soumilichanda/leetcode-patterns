"""
LeetCode 233: Number of Digit One
Difficulty: Hard
Pattern: Digit DP (Tight-Bound Recursive State Memoization)

Time Complexity: O((log10 n)^2)
Space Complexity: O((log10 n)^2)
"""

from functools import lru_cache


class Solution:
    def countDigitOne(self, n: int) -> int:
        if n <= 0:
            return 0

        digits = list(map(int, str(n)))
        length = len(digits)

        @lru_cache(maxsize=None)
        def dfs(pos: int, ones_count: int, tight: bool) -> int:
            if pos == length:
                return ones_count

            limit = digits[pos] if tight else 9
            total = 0

            for digit in range(limit + 1):
                next_tight = tight and (digit == limit)
                next_ones = ones_count + (1 if digit == 1 else 0)
                total += dfs(pos + 1, next_ones, next_tight)

            return total

        return dfs(0, 0, True)
