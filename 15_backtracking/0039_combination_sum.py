"""
LeetCode 39: Combination Sum
Difficulty: Medium
Pattern: Backtracking with State Pruning & Element Reuse

Invariant:
    Prune branch when remain < 0.
    Capture path when remain == 0.
    Allow element reuse by recursing on same index i.

Time Complexity: O(2^t) where t = target / min(candidates)
Space Complexity: O(t) recursion depth
"""

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result: List[List[int]] = []
        path: List[int] = []

        def backtrack(remain: int, start_idx: int) -> None:
            if remain == 0:
                result.append(list(path))
                return
            if remain < 0:
                return

            for i in range(start_idx, len(candidates)):
                path.append(candidates[i])
                backtrack(remain - candidates[i], i)
                path.pop()

        backtrack(target, 0)
        return result


if __name__ == "__main__":
    sol = Solution()
    print("Combination Sum [2, 3, 6, 7] (target 7):", sol.combinationSum([2, 3, 6, 7], 7))
