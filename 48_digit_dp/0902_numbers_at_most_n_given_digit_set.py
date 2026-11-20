"""
LeetCode 902: Numbers At Most N Given Digit Set
Difficulty: Hard
Pattern: Digit DP (Leading-Zero & Tight-Bound State Counting)

Time Complexity: O(log10(n) * len(digits))
Space Complexity: O(log10(n))
"""

from functools import lru_cache
from typing import List


class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        bound_digits = list(map(int, str(n)))
        allowed = [int(d) for d in digits]
        length = len(bound_digits)

        @lru_cache(maxsize=None)
        def dfs(pos: int, tight: bool, started: bool) -> int:
            if pos == length:
                return 1 if started else 0

            limit = bound_digits[pos] if tight else 9
            total = 0

            if not started:
                total += dfs(pos + 1, False, False)

            for d in allowed:
                if d > limit:
                    break
                next_tight = tight and (d == limit)
                total += dfs(pos + 1, next_tight, True)

            return total

        return dfs(0, True, False)
