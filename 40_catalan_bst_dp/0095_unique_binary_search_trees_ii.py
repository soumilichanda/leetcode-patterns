"""
LeetCode 95: Unique Binary Search Trees II
Difficulty: Medium
Pattern: Catalan Dynamic Programming / Memoized Sub-Interval Tree Synthesis

Invariant:
    Every value root in [start, end] forms valid BSTs by taking the
    Cartesian product of all unique left subtrees over [start, root - 1]
    and all unique right subtrees over [root + 1, end].

Time Complexity: O(4^n / n^(1/2)) (Catalan output bound)
Space Complexity: O(4^n / n^(1/2))
"""

from functools import lru_cache
from typing import List, Optional


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []

        @lru_cache(maxsize=None)
        def build(start: int, end: int) -> tuple[Optional[TreeNode], ...]:
            if start > end:
                return (None,)

            trees: list[TreeNode] = []
            for root_val in range(start, end + 1):
                left_subtrees = build(start, root_val - 1)
                right_subtrees = build(root_val + 1, end)

                for left_node in left_subtrees:
                    for right_node in right_subtrees:
                        trees.append(TreeNode(root_val, left_node, right_node))

            return tuple(trees)

        return list(build(1, n))


if __name__ == "__main__":
    sol = Solution()
    trees_3 = sol.generateTrees(3)
    assert len(trees_3) == 5, f"Expected 5 trees for n=3, got {len(trees_3)}"
    print("LC 95 (Unique Binary Search Trees II) verified successfully!")
