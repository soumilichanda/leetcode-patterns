"""
LeetCode 78: Subsets
Difficulty: Medium
Pattern: Backtracking (State Space DFS / Power Set)

Invariant:
    At each index, explore two branches:
    1. Include nums[i] in current path
    2. Exclude nums[i] from current path
    Backtrack in-place via path.pop()

Time Complexity: O(n * 2^n)
Space Complexity: O(n) auxiliary recursion stack space
"""

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result: List[List[int]] = []
        path: List[int] = []

        def backtrack(start_idx: int) -> None:
            result.append(list(path))

            for i in range(start_idx, len(nums)):
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()

        backtrack(0)
        return result


if __name__ == "__main__":
    sol = Solution()
    print("Subsets [1, 2, 3]:", sol.subsets([1, 2, 3]))
