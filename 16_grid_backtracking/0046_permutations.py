"""
LeetCode 46: Permutations
Difficulty: Medium
Pattern: Backtracking (In-Place Element Swapping)

Invariant:
    Branch by swapping elements at index `first` with `i` (first <= i < n).
    Recurse down to depth first + 1.
    Backtrack by swapping back to preserve state-space integrity.

Time Complexity: O(n * n!)
Space Complexity: O(n) auxiliary recursion stack space
"""

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res: List[List[int]] = []
        n = len(nums)

        def backtrack(first: int) -> None:
            if first == n:
                res.append(nums[:])
                return

            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]

        backtrack(0)
        return res


if __name__ == "__main__":
    sol = Solution()
    print("LC 46 Permutations [1, 2, 3]:", sol.permute([1, 2, 3]))
